import psycopg2

NEON_URL = "postgresql://neondb_owner:npg_X4Ihzl2tAdpO@ep-raspy-king-atkm989g.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

conn = psycopg2.connect(NEON_URL)
cursor = conn.cursor()

# Delete old test sermons
cursor.execute('DELETE FROM sermons WHERE id IN (1, 2, 3)')

# Add real sermons
cursor.execute(
    'INSERT INTO sermons (title, date, description, video_url) VALUES (%s, %s, %s, %s)',
    (
        'Life and Immortality (Part 1)',
        '19-12-2024',
        'An expository teaching on 2 Timothy 1:10, exploring the life and immortality that has been brought to light through the gospel of Jesus Christ — and what it means for every believer today.',
        'https://www.youtube.com/embed/0unWl3ur51o'
    )
)

cursor.execute(
    'INSERT INTO sermons (title, date, description, video_url) VALUES (%s, %s, %s, %s)',
    (
        'Life and Immortality (Part 2)',
        '23-12-2024',
        'A continuation of the study on 2 Timothy 1:10 — going deeper into the life that God has made available to every believer through Christ Jesus, and how to walk in the reality of it daily.',
        'https://www.youtube.com/embed/51RuiK7gsBQ'
    )
)

conn.commit()
cursor.close()
conn.close()
print('Done — old sermons deleted, real sermons added')
