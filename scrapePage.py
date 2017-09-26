import time

from bs4 import BeautifulSoup as bs
from selenium import webdriver

browser = webdriver.PhantomJS

while True:
    time.sleep(5)
    browser.get("http://www.tf2center.com/lobbies")

    pageSoup = bs(browser.page_source, "html.parser")
    containers = pageSoup.findAll("div", {"class":"cym-grid lobbyOverviewPanel manual"})
    
