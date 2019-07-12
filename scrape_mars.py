
# Import Dependecies 
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time

# Initialize browser
def init_browser():
    # Choose the executable path to driver 
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

# Create Mission to Mars dictionary 
mars_info = {}


def scrape_mars_news():

    # Initialize browser 
    browser = init_browser()

    # Visit Nasa news url through splinter module
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the latest element that contains news title and news_paragraph
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    #Enter into the dictionary
    mars_info['news_title'] = news_title
    mars_info['news_paragraph'] = news_p

    return mars_info

    # Close the browser after scraping
    browser.quit()


def scrape_mars_image():

    # Initialize browser 
    browser = init_browser()

    # Visit Mars Space Images through splinter module
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    time.sleep(1)

    # HTML Object 
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_image, 'html.parser')

    # Find the background-image url 
    featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # main Url 
    main_url = 'https://www.jpl.nasa.gov'

    # Concatenate website urls
    featured_image_url = main_url + featured_image_url

    # Display full link
    featured_image_url

    #Enter into the dictionary
    mars_info['featured_image_url'] = featured_image_url

    return mars_info

    # Close the browser after scraping
    browser.quit()

    

def scrape_mars_weather():

    # Initialize browser 
    browser = init_browser()

    # Visit Mars Weather Twitter through splinter module
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)

    time.sleep(1)

    # HTML Object 
    html_weather = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_weather, 'html.parser')

    # Find all elements that contain tweets
    latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

    # Find all elements that contain news title 
    for tweet in latest_tweets: 
        weather_tweet = tweet.find('p').text
        if 'Sol' and 'pressure' in weather_tweet:
            print(weather_tweet)
            break
        else: 
            pass

    #Enter into the dictionary
    mars_info['weather_tweet'] = weather_tweet

    return mars_info

    # Close the browser after scraping
    browser.quit()


def scrape_mars_facts():

    # Initialize browser 
    browser = init_browser()

    # Visit Mars facts url 
    facts_url = 'http://space-facts.com/mars/'
    browser.visit(facts_url)

    # Use Panda's `read_html` to parse the url
    mars_facts = pd.read_html(facts_url)

    #Display the mars facts dataframe 
    mars_df = mars_facts[1]

    # Add the column names
    mars_df.columns = ['Parameter','Value']

    # Set the index 
    mars_df.set_index('Parameter', inplace=True)

    #Save html code in table
    table = mars_df.to_html()

    #Enter into the dictionary
    mars_info['mars_facts'] = table

    return mars_info

    # Close the browser after scraping
    browser.quit()


def scrape_mars_hemispheres():

    # Initialize browser 
    browser = init_browser()

    # Visit Mars Hemisphere url through splinter module 
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    time.sleep(1)

    # HTML Object 
    html_hemisphere = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemisphere, 'html.parser')

    # Find all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []

    #The hemisphere main url 
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    # Loop through the items 
    for i in items:

        #Store the title
        title = i.find('h3').text

        #Store link that leads to the image website
        img_url = i.find('a', class_='itemLink product-item')['href']

        #Concatenate website urls
        image_link = hemispheres_main_url + img_url

        # Visit the link that contains the full image website
        browser.visit(image_link)

        #HTML Object of individual hemisphere website 
        html = browser.html

        #Parse HTML with Beautiful Soup for every individual hemisphere website
        soup = BeautifulSoup(html, 'html.parser')

        #Find the image source
        full_img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']

        #Append the above information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : title, "img_url" : full_img_url})

    #Enter into the dictionary
    mars_info['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_info

    # Close the browser after scraping
    browser.quit()


    
    













    







    




