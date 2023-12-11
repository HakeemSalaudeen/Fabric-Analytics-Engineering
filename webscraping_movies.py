## Importing Libraries
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

## Initialization of known entities
##  You must declare a few entities at the beginning. 
##  For example, you know the required URL, the CSV name for saving the record, the database name, and the table name for storing the record. You also know the entities to be saved. 
##  Additionally, since you require only the top 50 results, you will require a loop counter initialized to 0. 
## You may initialize all these by using the following code in webscraping_movies.py:

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = '/home/project/top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

## loading the entire web page for Webscraping as an HTML document in python using the requests.get().text

html_page = requests.get(url).text

# Then parse the text in the HTML format using BeautifulSoup to enable extraction of relevant information.

data = BeautifulSoup(html_page, 'html.parser')


### Scraping of required information
# write the loop to extract the appropriate information from the web page
# The rows of the table needed can be accessed using the find_all() function with the BeautifulSoup object using the statements below.

#  variable tables gets the body of all the tables in the web page
tables = data.find_all('tbody')

#ariable rows gets all the rows of the first table.
rows = tables[0].find_all('tr')

#  iterate over the rows to find the required data.

for row in rows:                    # Iterate over the contents of the variable 
    if count<50:                    #Check for the loop counter to restrict to 50 entries.
        col = row.find_all('td')    #Extract all the td data objects in the row and save them to col.
        if len(col)!=0:             #Check if the length of col is 0, that is, if there is no data in a current row. This is important since, many timesm there are merged rows that are not apparent in the web page appearance
            data_dict = {"Average Rank": col[0].contents[0],    #Create a dictionary data_dict with the keys same as the columns of the dataframe created for recording the output earlier and corresponding values from the first three headers of data.
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])            #Convert the dictionary to a dataframe and concatenate it with the existing one. This way, the data keeps getting appended to the dataframe with every iteration of the loop.
            df = pd.concat([df,df1], ignore_index=True)         
            count+=1                                            #Increment the loop counter.
    else:
        break                                                   #Once the counter hits 50, stop iterating over rows and break the loop.

print(df)

# After the dataframe has been created, save it to a CSV file 
df.to_csv(csv_path)             #Remember that you defined the variable csv_path earlier.


##To store the required data in a database
## you first need to initialize a connection to the database
## save the dataframe as a table, and then close the connection. 

conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()