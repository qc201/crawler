"""
encoding: urf-8
author: Qiuyu Chen
"""

import requests
from bs4 import BeautifulSoup
class Crawler:
    def __init__(self):
        # main webpage
        self.URL = "https://www.uschamber.com/co/chambers/"
        # all 50 states
        self.states = ["alabama", "alaska", "arizona", "arkansas", "american-samoa", "california", "colorado", "connecticut", "washington-dc", "delaware", "florida", "georgia", "guam", "hawaii", "iowa", "idaho", "illinois", "indiana", "kansas", "kentucky", "louisiana", "massachusetts","maryland","maine","michigan", "minnesota", "missouri", "northern-mariana-islands", "mississippi", "montana", "north-carolina","north-dakota","nebraska", "new-hampshire", "new-jersey", "new-mexico","nevada", "new-york", "ohio", "oklahoma", "oregon", "pennsylvania", "puerto-rico","rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "virgin-islands","washington", "west-virginia", "wisconsin", "wyoming"]
        # http message header
        self.header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

    def getStateLink(self):
        links = []
        for state in range(1):
        #for state in self.states:
            #individualUrl = self.URL + state
            individualUrl = 'https://www.uschamber.com/co/chambers/american-samoa'
            #individualUrl = 'https://www.uschamber.com/co/chambers/virgin-islands'
            response = requests.get(individualUrl)
            soup = BeautifulSoup(response.text, "html.parser")

            linkParents = soup.find_all("a")

            
            
            for link in linkParents:
                if link.get("href").startswith("//"):
                    webLink = "https:" + str(link.get("href"))
                    #r = requests.head(webLink).status_code
                    if webLink not in links: #and r == 200:                    
                        links.append(webLink)

        print(links)
        print(len(links))



if __name__ == "__main__":
    cursor = Crawler()
    cursor.getStateLink()
