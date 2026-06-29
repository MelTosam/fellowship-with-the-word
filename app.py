from flask import Flask, render_template, request, send_from_directory, session, redirect, url_for
import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key')

WORD_OF_THE_DAY = [
    {"verse": "John 3:16", "text": "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."},
    {"verse": "Romans 8:28", "text": "And we know that in all things God works for the good of those who love him, who have been called according to his purpose."},
    {"verse": "Philippians 4:13", "text": "I can do all this through him who gives me strength."},
    {"verse": "Jeremiah 29:11", "text": "For I know the plans I have for you, declares the Lord, plans to prosper you and not to harm you, plans to give you hope and a future."},
    {"verse": "Psalm 23:1", "text": "The Lord is my shepherd, I lack nothing."},
    {"verse": "Isaiah 40:31", "text": "But those who hope in the Lord will renew their strength. They will soar on wings like eagles; they will run and not grow weary, they will walk and not be faint."},
    {"verse": "Proverbs 3:5-6", "text": "Trust in the Lord with all your heart and lean not on your own understanding; in all your ways submit to him, and he will make your paths straight."},
    {"verse": "Matthew 6:33", "text": "But seek first his kingdom and his righteousness, and all these things will be given to you as well."},
    {"verse": "Romans 5:8", "text": "But God demonstrates his own love for us in this: While we were still sinners, Christ died for us."},
    {"verse": "2 Corinthians 5:17", "text": "Therefore, if anyone is in Christ, the new creation has come: The old has gone, the new is here!"},
    {"verse": "Ephesians 2:8-9", "text": "For it is by grace you have been saved, through faith and this is not from yourselves, it is the gift of God, not by works, so that no one can boast."},
    {"verse": "Galatians 2:20", "text": "I have been crucified with Christ and I no longer live, but Christ lives in me."},
    {"verse": "Romans 8:1", "text": "Therefore, there is now no condemnation for those who are in Christ Jesus."},
    {"verse": "John 1:12", "text": "Yet to all who did receive him, to those who believed in his name, he gave the right to become children of God."},
    {"verse": "1 John 4:8", "text": "Whoever does not love does not know God, because God is love."},
    {"verse": "Psalm 119:105", "text": "Your word is a lamp for my feet, a light on my path."},
    {"verse": "John 14:6", "text": "Jesus answered, I am the way and the truth and the life. No one comes to the Father except through me."},
    {"verse": "Romans 10:9", "text": "If you declare with your mouth, Jesus is Lord, and believe in your heart that God raised him from the dead, you will be saved."},
    {"verse": "1 Corinthians 13:4-5", "text": "Love is patient, love is kind. It does not envy, it does not boast, it is not proud. It does not dishonor others, it is not self-seeking."},
    {"verse": "Hebrews 11:1", "text": "Now faith is confidence in what we hope for and assurance about what we do not see."},
    {"verse": "James 1:17", "text": "Every good and perfect gift is from above, coming down from the Father of the heavenly lights, who does not change like shifting shadows."},
    {"verse": "Colossians 3:23", "text": "Whatever you do, work at it with all your heart, as working for the Lord, not for human masters."},
    {"verse": "Joshua 1:9", "text": "Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go."},
    {"verse": "Psalm 46:1", "text": "God is our refuge and strength, an ever-present help in trouble."},
    {"verse": "Isaiah 41:10", "text": "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you."},
    {"verse": "Matthew 11:28", "text": "Come to me, all you who are weary and burdened, and I will give you rest."},
    {"verse": "John 10:10", "text": "The thief comes only to steal and kill and destroy; I have come that they may have life, and have it to the full."},
    {"verse": "Romans 12:2", "text": "Do not conform to the pattern of this world, but be transformed by the renewing of your mind."},
    {"verse": "Philippians 4:7", "text": "And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus."},
    {"verse": "1 Peter 5:7", "text": "Cast all your anxiety on him because he cares for you."},
    {"verse": "Lamentations 3:22-23", "text": "Because of the Lords great love we are not consumed, for his compassions never fail. They are new every morning; great is your faithfulness."},
]

OLD_TESTAMENT = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
    "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra",
    "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
    "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah", "Lamentations",
    "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
    "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk",
    "Zephaniah", "Haggai", "Zechariah", "Malachi"
]

NEW_TESTAMENT = [
    "Matthew", "Mark", "Luke", "John", "Acts",
    "Romans", "1 Corinthians", "2 Corinthians", "Galatians", "Ephesians",
    "Philippians", "Colossians", "1 Thessalonians", "2 Thessalonians", "1 Timothy",
    "2 Timothy", "Titus", "Philemon", "Hebrews", "James",
    "1 Peter", "2 Peter", "1 John", "2 John", "3 John",
    "Jude", "Revelation"
]

BOOK_CHAPTERS = {
    "Genesis": 50, "Exodus": 40, "Leviticus": 27, "Numbers": 36, "Deuteronomy": 34,
    "Joshua": 24, "Judges": 21, "Ruth": 4, "1 Samuel": 31, "2 Samuel": 24,
    "1 Kings": 22, "2 Kings": 25, "1 Chronicles": 29, "2 Chronicles": 36, "Ezra": 10,
    "Nehemiah": 13, "Esther": 10, "Job": 42, "Psalms": 150, "Proverbs": 31,
    "Ecclesiastes": 12, "Song of Solomon": 8, "Isaiah": 66, "Jeremiah": 52, "Lamentations": 5,
    "Ezekiel": 48, "Daniel": 12, "Hosea": 14, "Joel": 3, "Amos": 9,
    "Obadiah": 1, "Jonah": 4, "Micah": 7, "Nahum": 3, "Habakkuk": 3,
    "Zephaniah": 3, "Haggai": 2, "Zechariah": 14, "Malachi": 4,
    "Matthew": 28, "Mark": 16, "Luke": 24, "John": 21, "Acts": 28,
    "Romans": 16, "1 Corinthians": 16, "2 Corinthians": 13, "Galatians": 6, "Ephesians": 6,
    "Philippians": 4, "Colossians": 4, "1 Thessalonians": 5, "2 Thessalonians": 3, "1 Timothy": 6,
    "2 Timothy": 4, "Titus": 3, "Philemon": 1, "Hebrews": 13, "James": 5,
    "1 Peter": 5, "2 Peter": 3, "1 John": 5, "2 John": 1, "3 John": 1,
    "Jude": 1, "Revelation": 22
}

def get_word_of_the_day():
    day_of_year = datetime.date.today().timetuple().tm_yday
    index = day_of_year % len(WORD_OF_THE_DAY)
    return WORD_OF_THE_DAY[index]

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
    conn, db_type = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, date, description, video_url FROM sermons')
    rows = cursor.fetchall()
    conn.close()
    sermons = []
    for row in rows:
        sermon = {
            'id': row[0],
            'title': row[1],
            'date': row[2],
            'description': row[3],
            'video_url': row[4]
        }
        sermons.append(sermon)
    return sermons

def get_todays_devotional(devotionals):
    today = datetime.date.today().strftime('%d-%m-%Y')
    for devotional in devotionals:
        if devotional['date'] == today:
            return devotional
    return None

def get_yesterdays_devotional(devotionals):
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%d-%m-%Y')
    for devotional in devotionals:
        if devotional['date'] == yesterday:
            return devotional
    return None

def get_latest_sermon(sermons):
    if sermons:
        return sermons[-1]
    return None

def get_placeholder(db_type):
    return '%s' if db_type == 'postgresql' else '?'

@app.route('/')
def home():
    devotionals = load_devotionals()
    sermons = load_sermons()
    todays_devotional = get_todays_devotional(devotionals)
    yesterdays_devotional = get_yesterdays_devotional(devotionals)
    latest_sermon = get_latest_sermon(sermons)
    word_of_the_day = get_word_of_the_day()
    return render_template('home.html',
        devotional=todays_devotional,
        yesterday=yesterdays_devotional,
        latest_sermon=latest_sermon,
        word_of_the_day=word_of_the_day)

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
    keyword = request.args.get('search', '')
    if keyword:
        sermons = [s for s in sermons if
                  keyword.lower() in s['title'].lower() or
                  keyword.lower() in s['description'].lower()]
    return render_template('sermons.html', sermons=sermons, keyword=keyword)

@app.route('/sermons/<int:sermon_id>')
def sermon_detail(sermon_id):
    conn, db_type = get_db_connection()
    cursor = conn.cursor()
    ph = get_placeholder(db_type)
    cursor.execute(f'SELECT id, title, date, description, video_url FROM sermons WHERE id = {ph}', (sermon_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        sermon = {
            'id': row[0],
            'title': row[1],
            'date': row[2],
            'description': row[3],
            'video_url': row[4]
        }
        return render_template('sermon_detail.html', sermon=sermon)
    else:
        return 'Sermon not found', 404

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

@app.route('/bible')
def bible():
    selected_book = request.args.get('book', '')
    selected_chapter = request.args.get('chapter', '')
    verses = []
    verse_reference = None
    error = None
    chapters = []

    if selected_book:
        chapter_count = BOOK_CHAPTERS.get(selected_book, 0)
        chapters = list(range(1, chapter_count + 1))

    if selected_book and selected_chapter:
        try:
            reference = f'{selected_book}+{selected_chapter}'
            response = requests.get(f'https://bible-api.com/{reference}')
            data = response.json()
            if 'error' in data:
                error = 'Chapter not found. Please try again.'
            else:
                verses = data.get('verses', [])
                verse_reference = data.get('reference', '')
        except:
            error = 'Something went wrong. Please try again.'

    return render_template('bible.html',
        verses=verses,
        verse_reference=verse_reference,
        error=error,
        selected_book=selected_book,
        selected_chapter=selected_chapter,
        chapters=chapters,
        old_testament=OLD_TESTAMENT,
        new_testament=NEW_TESTAMENT)

@app.route('/bible/search')
def bible_search():
    reference = request.args.get('reference', '')
    verses = []
    verse_reference = None
    error = None

    if reference:
        try:
            response = requests.get(f'https://bible-api.com/{reference}')
            data = response.json()
            if 'error' in data:
                error = 'Verse not found. Try a format like John 3:16 or Romans 8.'
            else:
                verses = data.get('verses', [])
                verse_reference = data.get('reference', '')
        except:
            error = 'Something went wrong. Please try again.'

    return render_template('bible_search.html',
        verses=verses,
        verse_reference=verse_reference,
        error=error,
        reference=reference,
        old_testament=OLD_TESTAMENT,
        new_testament=NEW_TESTAMENT)

@app.route('/admin/login'), methods=['GET', 'POST'])
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

@app.route('/add-sermon', methods=['GET', 'POST'])
def add_sermon():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    message = None
    if request.method == 'POST':
        title = request.form.get('title')
        date = request.form.get('date')
        description = request.form.get('description')
        video_url = request.form.get('video_url')
        conn, db_type = get_db_connection()
        cursor = conn.cursor()
        ph = get_placeholder(db_type)
        cursor.execute(
            f'INSERT INTO sermons (title, date, description, video_url) VALUES ({ph}, {ph}, {ph}, {ph})',
            (title, date, description, video_url)
        )
        conn.commit()
        conn.close()
        message = 'Sermon saved successfully.'
    return render_template('add_sermon.html', message=message)

@app.route('/static/sw.js')
def service_worker():
    return send_from_directory('static', 'sw.js', mimetype='application/javascript')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
