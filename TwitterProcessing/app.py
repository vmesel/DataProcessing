from processor import Scrapper
from time import sleep

while True:
    print("Scrapping Impeachment")
    Scrapper.Scrapping("impeachment", "impeachment-tt")
    sleep(15)
    print("Scrapping Dilma")
    Scrapper.Scrapping("dilma", "dilma-tt")
    sleep(15)
    print("Scrapping Lula")
    Scrapper.Scrapping("lula", "lula-tt")
    sleep(15)
    print("Scrapping PT")
    Scrapper.Scrapping("pt", "pt-tt")
    sleep(15)
