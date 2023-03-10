DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS inventory;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE inventory (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
desc TEXT NOT NULL,
price MONEY NOT NULL, 
qis INTEGER,
invtvalue as (price * qis),
reorderlevel INTEGER NOT NULL,
rtd INTEGER NOT NULL,
qir INTEGER,
inreorder TEXT,
discont TEXT
);
