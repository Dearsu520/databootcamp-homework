# **Web Design Homework - Web Visualization Dashboard (Latitude)**

Submitted by: Yijing Su

Date: December 29th, 2020


# **Description** 

For this homework, I create a web application to showcase content scraped from the NASA websites. The NASA websites include the news site, the featured image site, the facts site, and the high resolution site. Information are scraped from these four sites using BeautifulSoup, and are stored into the local MongoDB server. Then with Flask and PyMongo, the website is hosted with the scraped information. 

In the repository, there is the scrape.ipynb file which illustrates the scraping the four NASA websites. scrape_mars.py contains function to store the scraped information into the local MongoDB server. app.py is the flask app script which renders the index page and host it in local host.

The following is the screen shot of the web page:

[City Latitude vs. Max Tempurature](screen_shots/web_app_screen_shot.PNG)