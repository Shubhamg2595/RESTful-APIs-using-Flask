import sqlite3

# creating a connection

connection=sqlite3.connect('data.db')
#we are cimple creating a file called data.db that we will connect all the required  data to connect to our sqlite DB.

cursor=connection.cursor()

#creating a new table in sqlite

# create_table="create table users(id int,username text,password text)"
# cursor.execute(create_table)


"once you run this script, a data.db file will be created. ignore it for now"
'comment the create table part,once you have created the table'

'lets create a new user'

# user=(1,'shubham',70422) #simple tuple containing user data
# insert_query="insert into users values (? ,? ,? )"
# cursor.execute(insert_query,user)

'also commit your changes, when inserting , deleting or updating' \

# connection.commit()
# connection.close()

'after running the insert script,go and check data.db'

'HOW TO CREATE MULTIPLE USERS IN ONE GO'
'''
users_list=[(2,'ayu',99906),
       (3,'sam',82929)]
insert_query_for_many_users="insert into users values(?,?,?)"

cursor.executemany(insert_query_for_many_users,users_list)

connection.commit()
connection.close()
'''

'HOW TO FETCH DATA FROM TABLES'
select_query="select * from users"
for row in cursor.execute(select_query):
    print(row)

select_query_using_id="select username from users"
for row in cursor.execute(select_query_using_id):
    print(row)