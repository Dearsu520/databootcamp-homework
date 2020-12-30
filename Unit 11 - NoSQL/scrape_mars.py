#!/usr/bin/env python
# coding: utf-8

## import necessary modules
import requests
import json
from bs4 import BeautifulSoup as bs
import splinter
import pandas as pd

def scrape_all():
    '''
    This function is used for data scraping
    '''

    ## declare a chrome driver
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = splinter.Browser('chrome', **executable_path)

    ## obtain the html format of the webpage
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html

    ## display the soup instance
    soup = bs(html, "html.parser")

    ## declare content
    content = soup.find("div", class_="content_page")

    ## Extract the news title
    titles = content.find_all("div", class_="content_title")
    if len(titles) != 0:
        title = titles[0].text.strip()
    else:
        title = "Latest news not available"

    ## Extract the news text
    article_text = content.find_all("div", class_="article_teaser_body")
    if len(article_text) != 0:
        news_p = article_text[0].text.strip()
    else:
        news_p = "Please scrape again to update"

    ## scrape the image page
    images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(images_url)
    html = browser.html
    soup = bs(html, "html.parser")

    ## obtain the featured image
    featured_image = soup.find("article", class_="carousel_item")['style']
    latter = featured_image.split('/spaceimages/')[1].split("'")[0]
    former = images_url.split("?")[0]
    featured_image_url = former + latter

    ## Scrape the mars facts from the mars facts table
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    html = browser.html

    soup = bs(html, "html.parser")
    table = soup.find_all('table')[0]
    table_df = pd.DataFrame(columns=range(0,2), index=[0])   

    row_marker = 0
    rows = table.find_all('tr')
    for row in rows:
        column_marker = 0
        columns = row.find_all('td')
        for column in columns:
            table_df.at[row_marker, column_marker] = column.text.strip()
            column_marker += 1
        row_marker += 1

    ## scrape the high resolution images from the USGS Astrogeology site
    images_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    root_url = "https://astrogeology.usgs.gov"

    browser.visit(images_url)
    html = browser.html
    soup = bs(html, "html.parser")

    ## load the image title and image urls into a list of dictionaries
    hemisphere_image_urls = []
    items = soup.find_all("div", class_="item")
    for item in items:
        item_url = root_url + item.find("a")["href"]
        browser.visit(item_url)
        html = browser.html
        soup = bs(html, "html.parser")
        
        image_url = root_url + soup.find("img", class_="wide-image")["src"]
        image_title = item.find("div", class_="description").find("a").find("h3").text
        
        hemisphere_image_urls.append({"title": image_title, "img_url": image_url})

    if len(hemisphere_image_urls) == 0:
        hemisphere_image_urls.append(
            {"title": "Image not Available", 
            "img_url": "https://media.immediate.co.uk/volatile/sites/3/2017/11/imagenotavailable1-39de324.png?quality=90&resize=620,413"
        })
    
    # return hemisphere_image_urls
    return {
        "facts_table": table_df.values.tolist(),
        "featured_image": featured_image_url,
        "high_resolution_images": hemisphere_image_urls,
        "title": title,
        "description": news_p,
    }

if __name__ == "__main__":
    db_content = scrape_all()
    print(db_content)



