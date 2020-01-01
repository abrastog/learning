#!/usr/bin/python
import json

roopa = {
   "name": "My_love",
   "looks": "best in word",
   "profession": "Dancer"
}

print(roopa)
print(roopa["name"])   

roopa["name"] = "appuchu"
print(roopa)


x = type(roopa)
print(x)


x= roopa["name"]
print(x)


roopa["name"] = "Pumpkin"
print(roopa)

y= roopa.get("name")
print(y)

del roopa["looks"]
print(roopa)

roopa.clear()
print(roopa)


abhay = {
  "details": {
  "wife" :  "appuchu",
  "life_partner" : "abhay"
  },
  "wedding" : {
  "date" : "25 & 26th feb",
  "location" : "bangalore",
  }
}
tapachu = json.loads(abhay)

print(tapachu)
