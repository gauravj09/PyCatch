from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


myUrl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# opens connection and grabs page
uClient = uReq(myUrl)
pageHTML = uClient.read()
uClient.close()

#html parsing
pageSoup = soup(pageHTML, "html.parser")

#grabs each product
containers = pageSoup.findAll("div",{"class": "item-container"})

for container in containers:
	checkBrand			= container.find("div", "item-branding")
	brand 				= container.find("div", "item-branding").a.img["title"]
	titleContainer  	= container.findAll("a", {"class":"item-title"})
	productName 		= titleContainer[0].text
	shippingContainer 	= container.findAll("li", {"class":"price-ship"})
	shipping 			= shippingContainer[0].text.strip() #clean the /r and /n from input 

	print("brand: " + brand)
	print("productName: " + productName)
	print("shipping: " + shipping)




