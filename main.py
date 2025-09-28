from funkce import *  
from data_file import *
from webscraping import *


def main():
    scrape_data_toExcel(list_url, tags)  
    send(textfile_to_list(path), msg0)  
    list_to_textfile(path)


if __name__ == "__main__":
    main()
