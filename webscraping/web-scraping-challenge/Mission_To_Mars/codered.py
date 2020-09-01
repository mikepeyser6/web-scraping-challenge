# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)
    # Run all scraping functions and store results in a dictionary
    data = {
    }
    # Stop webdriver and return data
    browser.quit()
    return data
def mars_news(browser):
    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    # Optional delay for loading the page
    # Convert the browser html to a soup object and then quit the browser
    # Add try/except for error handling
    try:
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        # Use the parent element to find the paragraph text
    except AttributeError:
        return None, None
    return news_title, news_p
def featured_image(browser):
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    # Find and click the full image button
    # Find the more info button and click that
    # Parse the resulting html with soup
    # Add try/except for error handling
    try:
        # find the relative image url
    except AttributeError:
        return None
    # Use the base url to create an absolute url
    return img_url
def mars_facts():
    # Add try/except for error handling
    try:
        # use 'read_html' to scrape the facts table into a dataframe
    except BaseException:
        return None
    # assign columns and set index of dataframe
    # Convert dataframe into HTML format, add bootstrap
def hemispheres(browser):
    # A way to break up long strings
    # Click the link, find the sample anchor, return the href
    for i in range(4):
        # Find the elements on each loop to avoid a stale element exception
        # Append hemisphere object to list
        # Finally, we navigate backwards
    return hemisphere_image_urls
def scrape_hemisphere(html_text):
    # parse html text
    # adding try/except for error handling
    try:
    except AttributeError:
        # Image error will return None, for better front-end handling
    return hemispheres
if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())