from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
my_url = 'https://www.amazon.in/s?k=iphone&ref=nb_sb_noss_2'



uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "s-include-content-margin s-border-bottom s-latency-cf-section"})
print(len(containers))

print(soup.prettify(containers[0]))

container = containers[0]
print(container.div.img["alt"])

price = container.findAll("span", {"class": "a-price-whole"})
print(price[0].text)

ratings = container.findAll("span", {"class": "a-icon-alt"})
print(ratings[0].text)

filename = "products.csv"
f = open(filename, "w")

headers = "Product_Name, Pricing, Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("span", {"class": "a-price-whole"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("span", {"class": "a-icon-alt"})
    rating = rating_container[0].text.strip()

    price = ''.join(price.split(','))
    rating = ''.join(rating.split(" ", 1)[0])

    print("product name : " + product_name)
    print("price : " + price)
    print("rating : " + rating)

    f.write(product_name + "," + price + "," + rating + "\n")

f.close()