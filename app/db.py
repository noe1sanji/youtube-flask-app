import sqlite3

conn = sqlite3.connect("app/database.db")

with open("app/schema.sql", "r") as f:
    conn.executescript(f.read())

cur = conn.cursor()

# cur.execute("""insert into search (
#     search_text,
#     published_at,
#     channel_id,
#     title,
#     description,
#     thumbnails_url,
#     channel_title
#     ) values (
#         "google",
#         "2022-12-16 15:33:45",
#         "fj41",
#         "google",
#         "test",
#         "https://google.com",
#         "Google"
#     )
# """)

conn.commit()
conn.close()
print("Base de datos inicializada")