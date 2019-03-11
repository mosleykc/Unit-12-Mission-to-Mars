# Removing all of the explanatory text from the Jupyter Notebook file
# scrape_mars.py is solely for the purpose of defining functions which will be executed by the app.py file
# importing time to use for sleep
# Define Dependecies
from splinter import Browser
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# define executable path and define which browser is being uses, in this case Chrome. 
# use def to define the init_browser method, point to chrome browser and return the handle to the browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

# use def to define the scrap function, create browser var, and create an empty dictionary to store scraped data
def scrape():
    browser = init_browser()
    mars = {}


# Website subdirectory to be scraped
url = "https://mars.nasa.gov/news/"

# visit method tells the chrome browser previously defined to go to the URL and browser. 
browser.visit(url)

# add sleep function to prevent load on website
time.sleep(1)

# use BeautifulSoup to scrape website and store resulting DOM in soup object and parse contents using lxml parser
html = browser.html
soup = bs(html,"lxml")

# use BeautifulSoup method to look in soup object created in previous cell and  grab all data under the div class content_title 
# and assign to var news_article_title as text, assign output to mars var
mars[news_article_title] = soup.find("div", class_="content_title").text

# use BeautifulSoup method to look in soup object grab all data under the div class 
# article_teaser_body nd assign to mars var 
mars[article_teaser] = soup.find("div", class_="article_teaser_body").text

# close the browser
#browser.quit()


# JPL Mars Space Images

# Define the url for the website subdirectory to be scraped
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

# use the splinter visit method to tell the chrome browser previously defined to go to the URL in a chrome browser. 
browser.visit(url)

# add sleep function to prevent load on website
time.sleep(1)

# use BeautifulSoup to scrape website and store results in soup object and parse contents using lxml parser over html parser 
# in case html is not correctly structured
html = browser.html
soup = bs(html,"lxml")


# use BeautifulSoup method to look in soup object created in previous cell and  grab all data under the foot anchor tag with class 
# button and style attribute and assign to var
find_featured_image = soup.find("a", class_="button fancybox")["data-fancybox-href"]


# since the returned content string contains additional test that is not needed 
# "background-image: url('/spaceimages/images/wallpaper/PIA17200-1920x1200.jpg');", 
# use the string replace method to remove unwanted text
partial_featured_image =find_featured_image.replace("background-image: url('","").replace(");","")

# now that the extra content has been removed, concatenate the partial image URL with the main home home page URL

home_pg_url = "https://www.jpl.nasa.gov"
mars[featured_image_url] = home_pg_url + partial_featured_image

# close the browser
#browser.quit()



# ### Mars Weather

# Website subdirectory to be scraped
url = "https://twitter.com/marswxreport?lang=en"

# visit method tells the chrome browser previously defined to go to the URL and browser. 
browser.visit(url)

# add sleep function to prevent load on website
time.sleep(1)

# use BeautifulSoup to scrape website and store results in soup object and parse contents using lxml parser over html parser 
# in case html is not correctly structured
html = browser.html
soup = bs(html,"lxml")

# use the soup object to find the p with class tweet-text
mars[mars_weather]=soup.find("p", class_="tweet-text").text

# close the browser
#browser.quit()



# ### Mars Facts

# defining URL to scrape using Pandas
url = "https://space-facts.com/mars/"

# read in html table using Pandas, returns list of dataframes
factsTable=pd.read_html(url)

# add column names
factsTable_df = factsTable[0]
factsTable_df.columns=["Description","Value"]

#set the index to Description
factsTable_df.set_index("Description", inplace=True)


# convert list to html table
factsHtmlTable=factsTable_df.to_html()
#factsHtmlTable

# cleanup the table by removing the next line tag
mars[factsHtmlTable] = factsHtmlTable.replace("\n","")

# close the browser
#browser.quit()



# ### Mars Hemispheres

# define URL to use
url= "http://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

# visit method tells the chrome browser previously defined to go to the URL and browser. 
browser.visit(url)

# add sleep function to prevent load on website
time.sleep(1)


# use BeautifulSoup to scrape website and store results in soup object and parse contents using lxml parser over html parser 
# in case html is not correctly structured
html = browser.html
soup = bs(html,"lxml")

# capture hyperlink and go to next page to grab large image
hemispheres=soup.find_all("div", class_="description") 

# this section based on material from units 12.2.7 and 12.2.8
# Create empty hemisphere_image_url var to hold output and define variable for site homepage url
hemisphere_image_urls=[]
home_page_url = "https://astrogeology.usgs.gov"


# loop through each hemisphere and pull the needed attributes, navigate through h3 which is the image title, a, href

for h in hemispheres:
    
    # since the content under the description class, look for the h3 to find the image title and output as text
    image_title = h.find("h3").text 
        
    # next, look for the nested href tag under the anchor tag to get the link which if clicked, will go to the page with the full size image link
    image_pg_url = h.find("a")["href"] 
        
    # concatenate the home_page_url with the image_pg_link to get the link to the page with the full size image on it
    full_res_image_pg_url = home_page_url + image_pg_url
       
    #  now that the URL of the large image pages are known for all four images, visit those pages and find the URL for the actual 
    # image on those pages by passing in the URL from full_image_pg_url
    browser.visit(full_res_image_pg_url)
    full_res_image_html = browser.html
    
    # use BeautifulSoup to scrape the large image pages and store results in soup object, parse contents using lxml parser
    soup = bs(full_res_image_html,"lxml")
    
    # look through "soup" contents for img tag with class of "wide-image" and grab the link defined by the src tag
    full_res_image__partial_url = soup.find("img", class_="wide-image")["src"]
        
    # now that we have found the partial url for the full images, concatenate the home page URL with the partial lg image URL
    full_res_image_url = home_page_url + full_res_image__partial_url
       
    # final steps: Use a Python dictionary to store the data using the keys img_url and title. Append the dictionary with the 
    # image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    # use append to create dictionaries and add "title" and "image_url"
    hemisphere_image_urls.append({
        "title " : image_title, 
        "image_url " : full_res_image_url
        })
    # assign hemisphere_image_urls output to var mars
    mars["hemisphere_image_urls"] = hemisphere_image_urls
 
# close the browser
#browser.quit()

# return result
return mars
