Run:
    pip install flask
    pip install psycopg2-binary
------------------------
create a new database called myduka_db;

\c myduka_db
Create tables; products,users,sales,stock
insert into products values(0,'Laptop',120000,150000);

myduka_db=# \dt     - to list tables
myduka_db=# \d products     - to list products tables
myduka_db=# select * from products; - display whats in products

---------------
Prerequisites:-
SQL - sql queries(crud), pk & fk, joins , where
PYTHON - data types, type conversion, data structures(lists and tuples), loops, if , functions

----------------------
**Internet**-> Global network of connected devices or computers
**www**-> a service running on the internet tha connects users to the internet via the browser
**server** -> a computer device used for receiving / sending data from a clien
**hosting** -> uploading application files to a server to make the application available or visible online

1.build your application
2.send your files to a server
3.ip address is assigned to your application

**ip address** -> a number used to uniquely identify a device on a network eg 178.100.82.80
**domain name** -> a user friendly name attached to an ip address to enable users access applications e.g www.google.com

developer uploads app files to a server
that server has an assigned ip address
now to access the app hosed on the server, we use the server ip address -> 170.100.82.80

**DNS** -> domain name system - the internets phonebook used to translate domain names into ip address

User Applications/Hardware <---->    . Drivers.     <-----> OS (KERNEL)
                                 (Keyboard driver)
                                 (Bluetooth driver)

Python code <-----> DB-API Interface <------> Drivers (psycopg2) <------> DB (postgres)

----------------
PSYCOPG2
- A PostgresQL adapter (driver) used to connect Python to a Postgres database
- Connects Postgres to your Python code

server, database, port, username, password

** psycopg2.connect() - a function used to establish a connecion btn python and Postgres
- it has the following arguments:
**host** - where is my Postgres database located?
    host='localhost'
    localhos - own device
**port** - where exactly in my device is the Postgres service running?
    - default port of Postgres = 5432
**user** - username of the Postgres user   - default user is => postgres
**password** - password attached to username to authentic Postgres login
**dbname** - the database you want to connect to


