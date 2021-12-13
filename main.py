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
        self.states = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west-virginia", "wisconsin", "wyoming"]
        #self.states = {1: "alabama", 2: "alaska", 50: "arizona", 3: "arkansas", 4: "california", 5: "colorado", 6: "connecticut", 7: "delaware", 8: "florida", 9: "georgia", 10: "hawaii", 11: "idaho", 12: "illinois", 13: "indiana", 14: "iowa", 15: "kansas", 16: "kentucky", 17: "louisiana", 18: "maine", 19: "maryland", 20: "massachusetts", 21: "michigan", 22: "minnesota", 23: "mississippi", 24: "missouri", 25: "montana", 26: "nebraska", 27: "nevada", 28: "new-hampshire", 29: "new-jersey", 30: "new-mexico", 31: "new-york", 32: "north-carolina", 33: "north-dakota", 34: "ohio", 35: "oklahoma", 36: "oregon", 37: "pennsylvania", 38: "rhode-island", 39: "south-carolina", 40: "south-dakota", 41: "tennessee", 42: "texas", 43: "utah", 44: "vermont", 45: "virginia", 46: "washington", 47: "west-virginia", 48: "wisconsin", 49: "wyoming"}
        # http message header
        self.header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

    def getStateLink(self):
        for state in self.states:
            #individualUrl = self.URL + state
            individualUrl = 'https://www.uschamber.com/co/chambers/alabama'
            response = requests.get(individualUrl)
            soup = BeautifulSoup(response.text, "html.parser")
            div = soup.find('div', {"class": "chamber-finder__content "})
            #subDiv = div.findAll('div', {"class":"chamber-finder__chamber-expanded"})
            print(soup.a)
            #for link in soup.find_all('a'):
                #print(link.get('href'))






if __name__ == "__main__":
    cursor = Crawler()
    cursor.getStateLink()
