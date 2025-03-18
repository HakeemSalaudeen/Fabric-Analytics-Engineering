import sqlite3
import pandas as pd

#use SQLite3 to create and connect your process to a new database STAFF
conn = sqlite3.connect('STAFF.db')


#create a table in the database
table_name = 'INSTRUCTOR'

#create an attribute for the table 
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

#read the CSV using Pandas using the read_csv() function

file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

## Loading the data to a table

df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')


## Running basic queries on data
# SQL queries can be executed on the data using the read_sql function in pandas

#Viewing all the data in the table.
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#Viewing only FNAME column of data
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

## Viewing the total number of entries in the table.
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)


# try appending some data to the table
#  create the dataframe of the new data.

data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)


# append the data to the INSTRUCTOR table.
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

## Now, repeat the COUNT query. 
## to observe an increase by 1 in the output of the first COUNT query and the second one.

## Viewing the total number of entries in the table.
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()






# practice problems 

#create a table in the database
table2_name = 'DEPARTMENTS'

#create an attribute for the table 

table2_attribute_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']



#read the CSV using Pandas using the read_csv() function

file_pathDept = '/home/project/Departments.csv'
dff = pd.read_csv(file_pathDept, names = table2_attribute_list)

## Loading the data to a table

df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')


# try appending some data to the table
#  create the dataframe of the new data.

data_dict_dept = {'DEPT_ID' : [9],
            'DEP_NAME' : ['Quality Assurance'],
            'MANAGER_ID' : [30010],
            'LOC_ID' : ['L0010']}
data_append_dept = pd.DataFrame(data_dict_dept)


# append the data to the INSTRUCTOR table.
data_append_dept.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')



## Running basic queries on data
# SQL queries can be executed on the data using the read_sql function in pandas

#Viewing all the data in the table.
query_statement = f"SELECT * FROM {table2_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

#Viewing only FNAME column of data
query_statement = f"SELECT FNAME FROM {table2_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

## Viewing the total number of entries in the table.
query_statement = f"SELECT COUNT(*) FROM {table2_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)