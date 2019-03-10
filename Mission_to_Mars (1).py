#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:slateblue";> Unit 12 Homework - Mission to Mars</h1> 

# <div class="alert alert-block alert-info" style="color:black;">
# 
# <p>In this assignment, you will build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what you need to do. </p></div>

# In[196]:


# Define Dependecies

# use the splinter library with the Browser module to launch browser through Python, using splinter over request for this 
# homework to be able to see site and navigate through as needed
from splinter import Browser

# pulling in the BeautifulSoup python library to extract data from the website and assigning it to shortened version bs
from bs4 import BeautifulSoup as bs

# importing Pandas library to use with the Pandas Scraping section
import pandas as pd



# <h2 style="color:slateblue";>Step 1: Scraping</h2>
# 

# <div class="alert alert-block alert-info" style="color:black;">
# 
# - Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
# 
# - Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. 
# The following outlines what you need to scrape.
# 
# </div>

# <h3>NASA Mars News</h3>

# <div class="alert alert-block alert-info" style="color:black;">
# <p>Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.</p>
# 
# 
#  *python Example:* 
# > news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
#     
# > news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
# </font>
# </div>

# In[197]:


# define executable path and define which browser is being uses, in this case Chrome. ChromeDriver saved in path with this notebook
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Website subdirectory to be scraped
url = "https://mars.nasa.gov/news/"

# visit method tells the chrome browser previously defined to go to the URL and browser. 
browser.visit(url)
html = browser.html

# use BeautifulSoup to scrape website and store results in soup object and parse contents using lxml parser over html parser 
# in case html is not correctly structured. BeautifulSoup defined as bs when imported
soup = bs(html,"lxml")

#print scraped content in structured (prettified) format
# print(soup.prettify())


# In[198]:


# use BeautifulSoup method to look in soup object created in previous cell and  grab all data under the div class content_title 
# and assign to var news_article_title as text
news_article_title = soup.find("div", class_="content_title").text

# print news article title
print(news_article_title)

# use BeautifulSoup method to look in soup object grab all data under the div class article_teaser_body nd assign to var 
#article_teaser as text
article_teaser = soup.find("div", class_="article_teaser_body").text

#print article teaser paragraph
print(article_teaser)


#    <h3>JPL Mars Space Images</h3>

# <div class="alert alert-block alert-info" style="color:black;">
# 
# - Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
# 
# - Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# 
# - Make sure to find the image url to the full size .jpg image.
# 
# - Make sure to save a complete url string for this image.
# 
# <h5>python Example:</h5>
# 
# >featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
# </div>

# In[199]:


# Define the url for the website subdirectory to be scraped
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

# use the splinter visit method to tell the chrome browser previously defined to go to the URL in a chrome browser. 
browser.visit(url)
html = browser.html

# use BeautifulSoup to scrape website and store results in soup object and parse contents using lxml parser over html parser 
# in case html is not correctly structured
soup = bs(html,"lxml")

#print scraped content in structured (prettified) format
#print(soup.prettify())


# In[200]:


# use BeautifulSoup method to look in soup object created in previous cell and  grab all data under the foot anchor tag with class 
# button and style attribute and assign to var

#find_featured_image = soup.find("article", class_="carousel_item")["style"] <== did not return correct image
find_featured_image = soup.find("a", class_="button fancybox")["data-fancybox-href"]
#print (find_featured_image)

# since the returned content string contains additional test that is not needed 
# "background-image: url('/spaceimages/images/wallpaper/PIA17200-1920x1200.jpg');", 
# use the string replace method to remove unwanted text
partial_featured_image =find_featured_image.replace("background-image: url('","").replace(");","")

# now that the extra content has been removed, concatenate the partial image URL with the main home home page URL

home_pg_url = "https://www.jpl.nasa.gov"
featured_image_url = home_pg_url + partial_featured_image


# NOTE: when clicking on the current featured image FULL IMAGE button, full image is mediumsize, not largesize, please see code from website below
# <a class="button fancybox" data-description="This low-angle self-portrait of NASA's Curiosity Mars rover shows the vehicle 
# at the site from which it reached down to drill into a rock target called 'Buckskin' on lower Mount Sharp." 
# data-fancybox-group="images" data-fancybox-href="/spaceimages/images/mediumsize/PIA19808_ip.jpg" 
# data-link="/spaceimages/details.php?id=PIA19808" data-title="Looking Up at Mars Rover Curiosity in 'Buckskin' Selfie" 
# id="full_image">FULL IMAGE</a>

print(featured_image_url)


# ### Mars Weather

# <div class="alert alert-block alert-info" style="color:black;">
# 
# - Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.
# 
# <h5>python Example:</h5>
# 
# > mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
# </div>

# In[201]:


# Website subdirectory to be scraped
url = "https://twitter.com/marswxreport?lang=en"

# visit method tells the chrome browser previously defined to go to the URL and browser. Initialize spliter.
browser.visit(url)
html = browser.html

# use BeautifulSoup to scrape website and store resutling DOM in soup object and parse contents using lxml parser over html parser 
# in case html is not correctly structured
soup = bs(html,"lxml")

#print scraped content in structured (prettified) format
#print(soup.prettify())


# In[202]:


# use the soup object to find the p with class tweet-text
mars_weather=soup.find("p", class_="tweet-text").text
print(mars_weather)


# ### Mars Facts

# <div class="alert alert-block alert-info" style="color:black;">
# 
# - Visit the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# 
# - Use Pandas to convert the data to a HTML table string.
# </div>

# In[203]:


# defining URL to scrape using Pandas
url = "https://space-facts.com/mars/"

# read in html table using Pandas, returns list of dataframes
factsTable=pd.read_html(url)

# print factsTable
factsTable


# In[204]:


# show what type was returned
type(factsTable)


# In[205]:


# add column names
factsTable_df = factsTable[0]
factsTable_df.columns=["Description","Value"]


# In[206]:


#set the index to Description
factsTable_df.set_index("Description", inplace=True)


# In[207]:


factsTable_df


# In[208]:


# convert list to html table
factsHtmlTable=factsTable_df.to_html()
factsHtmlTable


# In[209]:


# cleanup the table by removing the next line tag
factsHtmlTable.replace("\n","")


# ### Mars Hemispheres

# <div class="alert alert-block alert-info" style="color:black;">
# 
# - Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
# 
# - You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# - Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
# 
# - Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 
# ###### python Example:
#     
# >hemisphere_image_urls = [
# >> {"title": "Valles Marineris Hemisphere", "img_url": "..."},<br>
# >> {"title": "Cerberus Hemisphere", "img_url": "..."},<br>
# >> {"title": "Schiaparelli Hemisphere", "img_url": "..."},<br>
# >> {"title": "Syrtis Major Hemisphere", "img_url": "..."},<br>
#     ]
#     
# </div>

# In[210]:


# define URL to use
url= "http://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

# visit method tells the chrome browser previously defined to go to the URL and browser. 
browser.visit(url)
html = browser.html

# use BeautifulSoup to scrape website and store results in soup object and parse contents using lxml parser over html parser 
# in case html is not correctly structured
soup = bs(html,"lxml")

# Pull content for all hemispheres and store in var - test different options for best solution: div class="collapsible results", div class=item, 
#div class="description"
#hemispheres=soup.find_all("div", class_="collapsible results") - Grabs too much data
# item and description return 

# capture hyperlink and go to next page to grab large image
hemispheres=soup.find_all("div", class_="description") 


#print scraped content in structured (prettified) format
print(hemispheres)


# In[211]:


# this section based on material from units 12.2.7 and 12.2.8
# Create empty hemisphere_image_url var to hold output and define variable for site homepage url
hemisphere_image_urls=[]
home_page_url = "https://astrogeology.usgs.gov"


# In[212]:


# loop through each hemisphere and pull the needed attributes, navigate through h3 which is the image title, a, href

for h in hemispheres:
    
    # since the content under the description class, look for the h3 to find the image title and output as text
    image_title = h.find("h3").text 
    #print(image_title)
    
    # next, look for the nested href tag under the anchor tag to get the link which if clicked, will go to the page with the full size image link
    image_pg_url = h.find("a")["href"] 
    #print(image_pg_link)
    
    # concatenate the home_page_url with the image_pg_link to get the link to the page with the full size image on it
    full_res_image_pg_url = home_page_url + image_pg_url
    # print(full_image_pg_url)
    
    #  now that the URL of the large image pages are known for all four images, visit those pages and find the URL for the actual 
    # image on those pages by passing in the URL from full_image_pg_url
    browser.visit(full_res_image_pg_url)
    full_res_image_html = browser.html
    
    # use BeautifulSoup to scrape the large image pages and store results in soup object, parse contents using lxml parser
    soup = bs(full_res_image_html,"lxml")
    
    # look through "soup" contents for img tag with class of "wide-image" and grab the link defined by the src tag
    full_res_image__partial_url = soup.find("img", class_="wide-image")["src"]
    # print(wide_image_url)
    
    # now that we have found the partial url for the full images, concatenate the home page URL with the partial lg image URL
    full_res_image_url = home_page_url + full_res_image__partial_url
    #print(full_res_image_url)
    
    # final steps: Use a Python dictionary to store the data using the keys img_url and title. Append the dictionary with the 
    # image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    # use append to create dictionaries and add "title" and "image_url"
    hemisphere_image_urls.append({
        "title " : image_title, 
        "image_url " : full_res_image_url})
    
# print (hemisphere_image_urls)
hemisphere_image_urls


#  <h2 style="color:slateblue";>Step 2 - MongoDB and Flask Application</h2>

# <div class="alert alert-block alert-info" style="color:black;">
# 
# <p>Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.</p>
# 
# - Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
# 
# - Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
# 
# > - Store the return value in Mongo as a Python dictionary.
# 
# - Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
# 
# - Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
# 
# > [final_app_part1.png](Images/final_app_part1.png)<br>
# > [final_app_part2.png](Images/final_app_part2.png)
# </div>

# In[ ]:




