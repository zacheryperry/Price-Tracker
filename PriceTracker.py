import requests
from bs4 import BeautifulSoup as soup
from selenium import webdriver


driver = webdriver.Firefox()
url = "https://www.guitarcenter.com/"
data = []

def page_scrape():
    global web_soup
    driver.get(url)  ## works without but makes browser display webpage
    web_r = requests.get(url)
    ##html = driver.execute_script("return document.documentElement.outerHTML")
    web_soup = soup(web_r.content, 'html.parser')
    web_soup.get_text()

def guitar_strip():
    global web_r, html, web_soup
    page_scrape()

    stripped_price_list = []
    final_list = []
    product_list = []

    prices = web_soup.find_all("span", {'class':'productPrice'})
    products = web_soup.find_all("div", {'class':'productTitle'})##link is missing the leading(guitarcenter.com)
    price_list = [things.get_text() for things in prices]
    link_list = [div.a['href'] for div in products]

    for text in products:
        product_list.append(text.get_text().strip())

    for string in price_list:
        stripped_price_list.append(string[11:])

    for x in range(len(price_list)):
        final_list.append(product_list[x])
        final_list.append(stripped_price_list[x])
        final_list.append('guitarcenter.com' + link_list[x])
    return(final_list)


def keyword_search(keywords):
    global url, data
    for words in keywords:
        url = "https://www.guitarcenter.com/search?typeAheadSuggestion=true&typeAheadRedirect=true&fromRecentHistory=false&Ntt=" + words
        page_scrape()
        data.append(guitar_strip())
    return(data)


keywords = ["beatstep", "minilogue"]
page_scrape()
print(keyword_search(keywords))
driver.close()