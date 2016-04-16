from processor import Scrapper
from time import sleep

while True:
    try:
        print("Scrapping Impeachment")
        Scrapper.Scrapping("impeachment", "impeachment-tt")
        sleep(15)
    except:
        pass
