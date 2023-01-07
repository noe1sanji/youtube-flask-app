drop table if exists search;

create table search(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    search_text TEXT,
    published_at DATETIME,
    channel_id TEXT,
    title TEXT,
    description TEXT,
    thumbnails_url TEXT,
    channel_title TEXT,
    video_id TEXT
)