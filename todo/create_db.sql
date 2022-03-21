CREATE TABLE task(
id INTEGER PRIMARY KEY,
owner_id INTEGER,
task_name TEXT,
due_date TEXT,
due_time TEXT
);

CREATE TABLE users(
id INTEGER PRIMARY KEY,
username TEXT,
password TEXT
);


.save "todo.db"
.exit
