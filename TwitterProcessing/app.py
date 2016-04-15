from processor import Scrapper
from time import sleep

while True:
    Scrapper.Scrapping("impeachment", "impeachment-tt")
    sleep(60)
    Scrapper.Scrapping("dilma", "dilma-tt")
    sleep(60)
    Scrapper.Scrapping("lula", "lula-tt")
    sleep(60)
    Scrapper.Scrapping("pt", "pt-tt")
    sleep(60)
