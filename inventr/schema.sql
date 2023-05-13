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
price INTEGER NOT NULL, 
qis INTEGER,
invtvalue as (price * qis),
reorderlevel INTEGER NOT NULL,
rtd INTEGER NOT NULL,
qir INTEGER,
discont TEXT
);

INSERT INTO inventory (name, desc, price, qis, reorderlevel, rtd, qir, discont)
VALUES ('Item 1', 'Desc 1', 51.00, 25, 29, 13, 50, '');

INSERT INTO inventory (name, desc, price, qis, reorderlevel, rtd, qir, discont)
VALUES ('Item 2', 'Desc 2', 93.00, 132, 231, 4, 50, '');

INSERT INTO inventory (name, desc, price, qis, reorderlevel, rtd, qir, discont)
VALUES ('Item 3', 'Desc 3', 57.00, 151, 114, 11, 150, '');

INSERT INTO inventory (name, desc, price, qis, reorderlevel, rtd, qir, discont)
VALUES ('Item 4', 'Desc 4', 19.00, 186, 158, 6, 50, 'yes');
