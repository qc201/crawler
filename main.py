
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

        # open a csv file and write a header.
        csvContent = open("ChamberData.csv", "a", newline="")
        headerList = ["Chamber's Name", "State", "City", "ZIP", "Website"]
        writer = csv.writer(csvContent)
        writer.writerow(headerList)

        #for state in range(1):
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
                    webLink = str(link.get("href"))[2:]

                    # find the parent block of the valid link
                    parent = link.parent.parent.parent
                    rawName = parent.find('header', 'chamber-finder__title')
                    nameObj = re.compile(r'<header class="chamber-finder__title">(?P<name>.*?)</header>', re.S)
                    nameIteral = nameObj.finditer(str(rawName))

                    rawAddress = parent.find('a', 'chamber-finder__card-details')
                    #print(rawAddress)
                    addressObj_city = re.compile(r'<br/>(?P<city>.*?),', re.S)
                    addressObj_zip = re.compile(r'<br/>(?P<address>.*?)</a>', re.S)
                    addressIteral_city = addressObj_city.finditer(str(rawAddress))
                    addressIteral_zip = addressObj_zip.finditer(str(rawAddress))

                    # get Chamber's name from the raw HTML
                    # add state base on the current page
                    for name in nameIteral:
                        links.append(name.group("name").replace("\n", "").strip())
                        links.append(str(state))

                        # get zip code from the raw HTML
                        for address in addressIteral_city:
                            fullAddress = address.group("city")
                            #print(fullAddress)
                            #fullAddress = address.group("address")
                            #zip = re.search(r"\d+", fullAddress)
                            
                            links.append(fullAddress.strip())
                            #links.append(zip.group().strip())
                            for cityName in addressIteral_zip:
                                zipCode = cityName.group("address")
                                zip = re.search(r"\d+", zipCode)
                                links.append(zip.group().strip())
                                links.append(webLink)



                        #print(links)
                        
                        # write to csv file line by line
                        writer.writerow(links)
        
        # close the csv file
        csvContent.close()


if __name__ == "__main__":
    cursor = Crawler()
    cursor.getStateLink()