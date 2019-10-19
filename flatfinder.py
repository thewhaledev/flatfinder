import requests, bs4, webbrowser

def rightmove():
        r_rightmove = requests.get("#")
        soup_rightmove = bs4.BeautifulSoup(r_rightmove.text, 'html.parser')
        results_rightmove = soup_rightmove.find_all("a", attrs={"class": "propertyCard-link"})
        for i in range(0,10):
                link_rightmove = results_rightmove[i].get("href")
                webbrowser.open("https://rightmove.co.uk" + link_rightmove)

def zoopla():
        r_zoopla = requests.get("#")
        soup_zoopla = bs4.BeautifulSoup(r_zoopla.text, 'html.parser')
        results_zoopla = soup_zoopla.find_all("a", attrs={"class": "listing-results-price text-price"})
        for i in range(0,10):
                link_zoopla = results_zoopla[i].get("href")
                webbrowser.open("https://zoopla.co.uk" + link_zoopla)

def openrent():
        r_openrent = requests.get("#")
        soup_openrent = bs4.BeautifulSoup(r_openrent.text, 'html.parser')
        results_openrent = soup_openrent.find_all("a", attrs={"class": "banda pt listing-title"})
        for i in range(0,10):
                link_openrent = results_openrent[i].get("href")
                webbrowser.open("https://openrent.co.uk" + link_openrent)

site = input("Rightmove, Zoopla, or OpenRent? ")

if site.lower() == "rightmove":
        rightmove()
elif site.lower() == "zoopla":
        zoopla()
else:
        openrent()
