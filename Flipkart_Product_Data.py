#BACKGROUND
#This is a python code that is used to webscrape details from a vendor such as flipkart. 
#The code works for Flipkart and did not work for Amazon.
#Idea behind the code was to find the actual realtime Ecommerce market valuation for a specific query

#LOGIC
#Items webscraped are product name, product price, number of reviews based on padding and XPath values
#The number of pages for the search query is given in a loop to webscrape all the queries
#The output gets saved as an excel file for furthe analysis

#ISSUES
#The code has complexity if we have a lot of data and it will take some time to run
#Other developers can let me know how to reduce the complexity

from bs4 import BeautifulSoup # Importing the BeautifulSoup package
import requests # Importing requests library
import csv # Import CSV library
import pandas as pd # Import Pandas

#The dummy URL below holds the URL link for flipkart where we need to webscrape the details
dummyurl= "https://www.flipkart.com/beauty-and-grooming/body-face-skin-care/pr?sid=g9b%2Cema&q=coconut+oil&otracker=categorytree&p%5B%5D=facets.rating%255B%255D%3D1%25E2%2598%2585%2B%2526%2Babove"
master = []
descriptions = []

# The number of pages in the search query is dynamic. Hence it has to be hardcoded in the below for loop definition
# Example: the below for range has loop from 1st page to 41st page

for i in range(1,41):
    print(i) #Just print to see if the code is working
    req = requests.get(dummyurl + "&page=" + str(i)) # Requesting the content of the URL
    content = req.content # Getting the content
    soup = BeautifulSoup(content,'html.parser') # Here we need to specify the content variable and the parser which is the HTML parser
    # So now soup is a variable of the BeautifulSoup object of our parsed HTML
    desc = soup.find_all('div' , class_='_4ddWXP') # Extracting the descriptions from the website using the find method - grabbing the div tag which has the classname _3wU53n
    # So now this returns all the div tags with the classname of _3wU53n
    # As class is a special keyword in python we have to use the class_ keyword and pass the arguments here
    print(len(desc))
    for j in range(len(desc)):
               descriptions.append(desc[j].text) # We can even access the child tags with dot access.
    master.append(descriptions)
# Example.csv gets created in the current working directory
with open ('Example.csv','w',newline = '',encoding='UTF-8') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerows(descriptions)
    
    #END OF CODE
    
