from bs4 import BeautifulSoup
import requests
import unicodedata
import pandas as pd

list_url = ['https://crypto.com/price/bitcoin','https://crypto.com/price/ethereum', 'https://crypto.com/price/dogecoin', 'https://www.google.com/finance/quote/AAPL:NASDAQ', 'https://www.google.com/finance/quote/TSLA:NASDAQ']
tags = {"Name": [['h2', 'chakra-heading css-spkkpi'], ['div', 'zzDege']],
        "Price": [['span', 'chakra-text css-13hqrwd'], ['div', 'YMlKec fxKbKc']]
        }

def scrape_data_toExcel(list_url, ListOfTags):
    list_name = []
    list_price = []
    dict = {}
    for url in list_url:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,  'lxml')
        for tag in ListOfTags.values():
            for i in tag:
                id_, class_ = i
                scrapped_data = soup.find(id_, class_)
                if scrapped_data is None:
                    pass
                else:
                    data_ = unicodedata.normalize("NFKD", scrapped_data.text)
                    if any(char.isdigit() for char in data_):
                        list_price.append(data_)
                    else:
                        list_name.append(data_)
    dict["Name"] = list_name
    dict["Price"] = list_price
    pd.DataFrame(dict).to_excel('output.xlsx', index=False)
scrape_data_toExcel(list_url, tags)
