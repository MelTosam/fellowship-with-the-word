from flask import Flask, render_template, request, send_from_directory, session, redirect, url_for
import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key')

def get_db_connection():
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL and DATABASE_URL.startswith('postgresql'):
        import psycopg2
        conn = psycopg2.connect(DATABASE_URL)
        return conn, 'postgresql'
    else:
        import sqlite3
        conn = sqlite3.connect('fellowship.db')
        return conn, 'sqlite'

def load_devotionals():
    conn, db_type = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, verse, explanation, date FROM devotionals')
    rows = cursor.fetchall()
    conn.close()

    devotionals = []
    for row in rows:
        devotional = {
            'id': row[0],
            'title': row[1],
            'verse': row[2],
            'explanation': row[3],
            'date': row[4]
        }
        devotionals.append(devotional)
    return devotionals

def load_sermons():
    sermons = []
    with open('sermons.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split('|')
                sermon = {
                    'title': parts[0],
                    'date': parts[1],
                    'description': parts[2],
                    'video_url': parts[3]
                }
                sermons.append(sermon)
    return sermons

def get_todays_devotional(devotionals):
    today = datetime.date.today().strftime('%d-%m-%Y')
    for devotional in devotionals:
        if devotional['date'] == today:
            return devotional
    return None

def get_placeholder(db_type):
    return '%s' if db_type == 'postgresql' else '?'

@app.route('/')
def home():
    devotionals = load_devotionals()
    todays_devotional = get_todays_devotional(devotionals)
    return render_template('home.html', devotional=todays_devotional)

@app.route('/devotionals')
def devotionals_page():
    devotionals = load_devotionals()
    keyword = request.args.get('search', '')
    if keyword:
        devotionals = [d for d in devotionals if
                      keyword.lower() in d['title'].lower() or
                      keyword.lower() in d['explanation'].lower()]
    return render_template('devotionals.html', devotionals=devotionals, keyword=keyword)

@app.route('/devotionals/<int:devotional_id>')
def devotional_detail(devotional_id):
    conn, db_type = get_db_connection()
    cursor = conn.cursor()
    ph = get_placeholder(db_type)
    cursor.execute(f'SELECT id, title, verse, explanation, date FROM devotionals WHERE id = {ph}', (devotional_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        devotional = {
            'id': row[0],
            'title': row[1],
            'verse': row[2],
            'explanation': row[3],
            'date': row[4]
        }
        return render_template('devotional_detail.html', devotional=devotional)
    else:
        return 'Devotional not found', 404

@app.route('/sermons')
def sermons_page():
    sermons = load_sermons()
    return render_template('sermons.html', sermons=sermons)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/give')
def give():
    return render_template('give.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/bible', methods=['GET', 'POST'])
def bible():
    verse_text = None
    verse_reference = None
    error = None

    if request.method == 'POST':
        reference = request.form.get('reference')
        if reference:
            try:
                response = requests.get(f'https://bible-api.com/{reference}')
                data = response.json()
                if 'error' in data:
                    error = 'Verse not found. Please check your reference and try again.'
                else:
                    verse_text = data['text']
                    verse_reference = data['reference']
            except:
                error = 'Something went wrong. Please try again.'

    return render_template('bible.html', verse_text=verse_text, verse_reference=verse_reference, error=error)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')
        if password == os.environ.get('ADMIN_PASSWORD'):
            session['admin'] = True
            return redirect(url_for('add_devotional'))
        else:
            error = 'Incorrect password. Please try again.'
    return render_template('admin_login.html', error=error)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('home'))

@app.route('/add-devotional', methods=['GET', 'POST'])
def add_devotional():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))

    message = None

    if request.method == 'POST':
        title = request.form.get('title')
        verse = request.form.get('verse')
        explanation = request.form.get('explanation')
        date = request.form.get('date')

        conn, db_type = get_db_connection()
        cursor = conn.cursor()
        ph = get_placeholder(db_type)
        cursor.execute(
            f'INSERT INTO devotionals (title, verse, explanation, date) VALUES ({ph}, {ph}, {ph}, {ph})',
            (title, verse, explanation, date)
        )
        conn.commit()
        conn.close()

        message = 'Devotional saved successfully.'

    return render_template('add_devotional.html', message=message)

@app.route('/static/sw.js')
def service_worker():
    return send_from_directory('static', 'sw.js', mimetype='application/javascript')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
