# %% [markdown]
# JOINING TWO CSV FILES USING INNER JOIN IN PANDAS 
# 
# -- We need to define index for both csv files (unique ID)
# -- The default join is left
# -- We will be joining the orders and customers file 
# 
# 

# %%
import json 
import pandas as pd 

# %%
## to get the index, we will need to write a function 

def get_column_names (schemas, file_name, sorting_key = 'column_position'):             #schemas will be read as a json file while file_name is a table from the file
    column_details = schemas[file_name]
    columns = sorted (column_details, key = lambda col: col [sorting_key])
    return [col ['column_name'] for col in columns]                                     #column name is from the json file

# %%

# the schema is a json file
schemas = json.load(open('C:\\Users\\HAKEEM OLUWATOBI\\Research\\data\\retail_db\\schemas.json'))       

# variable to get the column headers for orders table
orders_columnHeader = get_column_names (schemas, 'orders')        

# variable to get the column headers for customers table 
customers_columnHeader = get_column_names (schemas, 'customers')          

orders_df = pd.read_csv(                        # reading the orders table into a df
    'C:\\Users\\HAKEEM OLUWATOBI\\Research\\data\\retail_db\\orders\\part-00000',
    names = orders_columnHeader
)


customers_df = pd.read_csv(                        # reading the customers table into a df
    'C:\\Users\\HAKEEM OLUWATOBI\\Research\\data\\retail_db\\customers\\part-00000',
    names = customers_columnHeader
)


# %%
customers_df


# %%
orders_df

# %%
## creating the index / primary key 
# order_customer_id and customer_id are the FK and PK respectively 
# we will use set_index to set the index for both columns 

orders_df = orders_df.set_index('order_customer_id')

customers_df = customers_df.set_index('customer_id')

# %%
#Joining both tables 

CustomersAndOrders_df = customers_df.\
join(orders_df, how =  'inner')

CustomersAndOrders_df               #notice its now 11 columns 

# %%
CustomersAndOrders_df.shape

# %%
# now that we av join thge data, we need to reset index incase we want to do aggregation on the CustomersAndOrders_df
# we will be using the reset_index function 

CustomersAndOrders_df. \
    reset_index(names = 'customer_id')


# %%
## now to get the count of each customer per order 
# meaning how many times a customer (customer_id) made an order 

CustomersAndOrders_df.\
    groupby('customer_id')['order_id'].\
    agg (order_count = 'count')               #groupby customer_id based on order_id and count 

# %%
#to get customers that has orders grreater than 15

CustomersAndOrders_df.\
    groupby('customer_id')['order_id'].\
    agg (order_count = 'count').\
    query('order_count >= 15')

# %%
## sorting
# sorting based on order_date

orders_df.sort_values('order_date')                     #ascending 
orders_df.sort_values('order_date', ascending = False)           #descending 

# %%
## sorting with more than one columns (composite sorting)
## sorting order_customer_id and order_date 

orders_df.sort_values(['order_customer_id', 'order_date']) 

#using it with ascending 
orders_df.sort_values(['order_customer_id', 'order_date'], ascending=[True, False])


