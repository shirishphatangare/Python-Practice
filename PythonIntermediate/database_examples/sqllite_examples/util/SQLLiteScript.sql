CREATE TABLE IF NOT EXISTS customers(
id integer PRIMARY KEY,
first_name text NOT NULL,
last_name text NOT NULL);

CREATE TABLE IF NOT EXISTS products (
id integer PRIMARY KEY,
name text NOT NULL,
price real NOT NULL);

CREATE TABLE IF NOT EXISTS orders  (
id integer PRIMARY KEY,
date text NOT NULL,
customer_id integer,
FOREIGN KEY (customer_id) REFERENCES customers (id));

CREATE TABLE IF NOT EXISTS lineitems  (
id integer PRIMARY KEY,
quantity integer NOT NULL,
total real NOT NULL,
product_id integer,
order_id integer,
FOREIGN KEY (product_id) REFERENCES products (id),
FOREIGN KEY (order_id) REFERENCES orders (id));

CREATE TABLE IF NOT EXISTS hardware  (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS software  (
 id INTEGER PRIMARY KEY,
 name TEXT NOT NULL,
 price REAL NOT NULL
);