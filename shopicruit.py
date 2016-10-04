import json, urllib

# SHOPIFY shopicruit challenge by Jacob Madrid, 2016
# Please don't actually look and steal this code if you plan on taking the test.

url = "http://shopicruit.myshopify.com/products.json?page="
total = 0.0
x = 1

def isClockWatch(product):
    pType = product["product_type"].lower()
    return pType == "clock" or pType == "watch"

while True:
    newurl = url + str(x)
    rawJSON = urllib.urlopen(newurl)
    parsedJSON = json.loads(rawJSON.read())
    if len(parsedJSON["products"]) == 0: 
        break #if there's nothing on the page we're done
    for product in parsedJSON["products"]:
        if isClockWatch(product): #if it's a clock/watch add the price of every variant
            for variant in product["variants"]:
                total += float(variant["price"])
    x+=1

print "It'd cost $" + str(total) + " to buy every clock and watch available."
