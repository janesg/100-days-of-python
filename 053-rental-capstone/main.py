import requests
from bs4 import BeautifulSoup
# from pprint import pprint

RENTAL_SEARCH_URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScbyFSS77-fn9Ts9t3DxSWqZGF3WS6Utegx413VXPV7OjbePw/viewform?usp=sf_link"


def clean_price(styled_price: str) -> str:
    if len(styled_price.split("+")) > 1:
        return styled_price.split("+")[0]
    elif len(styled_price.split("/")) > 1:
        return styled_price.split("/")[0]
    else:
        return styled_price


def clean_address(styled_addr: str) -> str:
    return styled_addr.strip().replace(" |", ",")


response = requests.get(RENTAL_SEARCH_URL)
soup = BeautifulSoup(response.text, features="html.parser")

links = [link.get("href") for link in soup.select("a.StyledPropertyCardDataArea-anchor")]
prices = [clean_price(price.get_text()) for price in soup.select("span.PropertyCardWrapper__StyledPriceLine")]
addresses = [clean_address(addr.get_text()) for addr in soup.select("address")]
