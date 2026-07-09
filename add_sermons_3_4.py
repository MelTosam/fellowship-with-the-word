import psycopg2

NEON_URL = "postgresql://neondb_owner:npg_X4Ihzl2tAdpO@ep-raspy-king-atkm989g.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

conn = psycopg2.connect(NEON_URL)
cursor = conn.cursor()

cursor.execute(
    'INSERT INTO sermons (title, date, description, video_url) VALUES (%s, %s, %s, %s)',
    (
        'Life and Immortality (Part 3)',
        '26-12-2024',
        'A continuation of the study on 2 Timothy 1:10 — going deeper into the life and immortality brought to light through the gospel, and what walking in that reality looks like for the believer daily.',
        'https://www.youtube.com/embed/MewpVwcVRsU'
    )
)

cursor.execute(
    'INSERT INTO sermons (title, date, description, video_url) VALUES (%s, %s, %s, %s)',
    (
        'Life and Immortality (Part 4)',
        '30-12-2024',
        'The concluding part of the Life and Immortality series — bringing together the full revelation of 2 Timothy 1:10 and its practical implications for every believer in Christ Jesus.',
        'https://www.youtube.com/embed/mWxBU3LIHXQ'
    )
)

conn.commit()
cursor.close()
conn.close()
print('Parts 3 and 4 added successfully')
