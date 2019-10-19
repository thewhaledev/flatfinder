import requests, bs4, webbrowser

def rightmove():
        r_rightmove = requests.get("https://www.rightmove.co.uk/property-to-rent/find.html?searchType=RENT&locationIdentifier=POSTCODE%5E763883&insId=1&radius=1.0&minPrice=&maxPrice=1200&minBedrooms=&maxBedrooms=1&displayPropertyType=&maxDaysSinceAdded=&sortByPriceDescending=&_includeLetAgreed=on&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&letType=&letFurnishType=&houseFlatShare=")
        soup_rightmove = bs4.BeautifulSoup(r_rightmove.text, 'html.parser')
        results_rightmove = soup_rightmove.find_all("a", attrs={"class": "propertyCard-link"})
        for i in range(0,10):
                link_rightmove = results_rightmove[i].get("href")
                webbrowser.open("https://rightmove.co.uk" + link_rightmove)

def zoopla():
        r_zoopla = requests.get("https://www.zoopla.co.uk/to-rent/property/london/armoury-road/se8-4lf/?include_shared_accommodation=false&price_frequency=per_month&price_max=1150&q=se8%204lf&radius=1&results_sort=newest_listings&search_source=home")
        soup_zoopla = bs4.BeautifulSoup(r_zoopla.text, 'html.parser')
        results_zoopla = soup_zoopla.find_all("a", attrs={"class": "listing-results-price text-price"})
        for i in range(0,10):
                link_zoopla = results_zoopla[i].get("href")
                webbrowser.open("https://zoopla.co.uk" + link_zoopla)

def openrent():
        r_openrent = requests.get("https://www.openrent.co.uk/properties-to-rent/se8-4lf-londen-verenigd-koninkrijk?term=SE8%204LF,%20Londen,%20Verenigd%20Koninkrijk&prices_max=1100&bedrooms_min=0&bedrooms_max=1&bathrooms_max=1&sortType=0")
        soup_openrent = bs4.BeautifulSoup(r_openrent.text, 'html.parser')
        results_openrent = soup_openrent.find_all("a", attrs={"class": "banda pt listing-title"})
        for i in range(0,10):
                link_openrent = results_openrent[i].get("href")
                webbrowser.open("https://openrent.co.uk" + link_openrent)

#https://www.onthemarket.com/to-rent/property/se8-4lf/?max-price=1150&radius=0.25&shared=false&view=grid

site = input("Rightmove, Zoopla, or OpenRent? ")

if site.lower() == "rightmove":
        rightmove()
if site.lower() == "zoopla":
        zoopla()
if site.lower() == "openrent":
        openrent()
