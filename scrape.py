from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
##my_url = 'https://facebook.com'


#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")
print(page_soup.h1)
print(page_soup.p)
print(page_soup.body)

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

####print(len(containers))
####
####print(containers[0])

##container = containers[0]
##(container.div.div.a.img["title"])

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]
    
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()
                                           
    


