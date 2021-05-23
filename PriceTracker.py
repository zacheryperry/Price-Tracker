import requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver
import mysql.connector

# ~ Web interface ~
driver = webdriver.Firefox()
url = "https://www.guitarcenter.com/"
final_list = []

# ~ Database interface ~
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='',
    database="price_tracker_beta"
)

mycursor = mydb.cursor()


def page_scrape():
    global web_soup

    driver.get(url)
    web_r = requests.get(url)
    web_soup = soup(web_r.content, 'html.parser')
    web_soup.get_text()


def guitar_strip():
    global web_r, web_soup, final_list
    page_scrape()

    stripped_price_list = []
    staging_tuple = []  # converted to tuple before appended to final_list
    product_list = []

    prices = web_soup.find_all("span", {'class': 'productPrice'})
    products = web_soup.find_all("div", {'class': 'productTitle'})  # link is missing the leading(guitarcenter.com)
    price_list = [things.get_text() for things in prices]
    link_list = [div.a['href'] for div in products]

    for text in products:
        product_list.append(text.get_text().strip())

    for string in price_list:
        stripped_price_list.append(string[11:])

    for x in range(len(price_list)):
        staging_tuple.append(product_list[x])
        staging_tuple.append(stripped_price_list[x])
        staging_tuple.append('guitarcenter.com' + link_list[x])
        staging_tuple = tuple(staging_tuple)
        final_list.append(staging_tuple)
        staging_tuple = []


def keyword_search(keywords):
    global url, final_list
    for words in keywords:
        url = "https://www.guitarcenter.com/search?typeAheadSuggestion=true&typeAheadRedirect=true&fromRecentHistory=false&Ntt=" + words
        page_scrape()
        guitar_strip()
    print(final_list)

# scrape test(


keywords = ("beatstep", "minilogue")
page_scrape()
print(keyword_search(keywords))
driver.close()

# )

def create_database(mycursor):
    mycursor.exicute("CREATE DATABASE price_tracker_beta")


def create_table(mycursor):
    mycursor.exicute("CREATE TABLE item_entries(product_desc varchar(100),price varchar(20),url varchar(500))")


def push_to_db(mydb, mycursor):
    sql = "INSERT INTO item_entries (product_desc, price, url) VALUES (%s, %s, %s)"
    val = final_list

    mycursor.executemany(sql, val)
    mydb.commit()