CREATE TABLE task(
id INTEGER PRIMARY KEY,
task_name TEXT,
due_date TEXT,
due_time TEXT
);
.save "todo.db"
.exit