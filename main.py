
"""
encoding: urf-8
author: qchan.cs@gmail.com
"""

import requests
from bs4 import BeautifulSoup
import re
import csv


class Crawler:
    def __init__(self):
        # main webpage
        self.URL = "https://www.uschamber.com/co/chambers/"
        # all 50 states
        self.states = ["alabama", "alaska", "arizona", "arkansas", "american-samoa", "california", "colorado", "connecticut", "washington-dc", "delaware", "florida", "georgia", "guam", "hawaii", "iowa", "idaho", "illinois", "indiana", "kansas", "kentucky", "louisiana", "massachusetts" ,"maryland"
                       ,"maine" ,"michigan", "minnesota", "missouri", "northern-mariana-islands", "mississippi", "montana", "north-carolina" ,"north-dakota" ,"nebraska", "new-hampshire", "new-jersey", "new-mexico" ,"nevada", "new-york", "ohio", "oklahoma", "oregon", "pennsylvania", "puerto-rico"
                       ,"rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "virgin-islands" ,"washington", "west-virginia", "wisconsin", "wyoming"]
        # http message header
        self.header = \
            {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

    def getStateLink(self):

        # for state in range(1):
        for state in self.states:
            for state in self.states:
                individualUrl = self.URL + state
            #individualUrl = 'https://www.uschamber.com/co/chambers/american-samoa'
            #individualUrl = 'https://www.uschamber.com/co/chambers/virgin-islands'
            #individualUrl = 'https://www.uschamber.com/co/chambers/connecticut'
                response = requests.get(individualUrl)
                soup = BeautifulSoup(response.text, "html.parser")

                superLinks = soup.find_all("a")


                for link in superLinks:
                    # verify if the form contain the website link
                    if link.get("href").startswith("//"):
                        links = []
                        webLink = "https:" + str(link.get("href"))

                        # find the parent block of the valid link
                        parent = link.parent.parent.parent
                        rawName = parent.find('header', 'chamber-finder__title')
                        nameObj = re.compile(r'<header class="chamber-finder__title">(?P<name>.*?)</header>', re.S)
                        nameIteral = nameObj.finditer(str(rawName))

                        rawAddress = parent.find('a', 'chamber-finder__card-details')
                        addressObj = re.compile(r'<br/>(?P<address>.*?)</a>', re.S)
                        addressIteral = addressObj.finditer(str(rawAddress))

                        # get Chamber's name from the raw HTML
                        # add state base on the current page
                        for name in nameIteral:
                            links.append(name.group("name").replace("\n", "").strip())
                            links.append(str(state))

                            # get zip code from the raw HTML
                            for address in addressIteral:
                                fullAddress = address.group("address")
                                zip = re.search(r"\d+", fullAddress)
                                links.append(zip.group().strip())
                                links.append(webLink)



                            csvContent = open("ChamberData.csv", "a", newline="")
                            writer = csv.writer(csvContent)
                            writer.writerow(links)
            csvContent.close()


if __name__ == "__main__":
    cursor = Crawler()
    cursor.getStateLink()