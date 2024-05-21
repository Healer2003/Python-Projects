import phonenumbers
from PhoneNumber import number

from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
carrier_name = carrier.name_for_number(service_pro, "en")
print(carrier_name, location)

from opencage.geocoder import OpenCageGeocode
key ="4711837404054cbf8eb1d82cfe4aa3f7"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

import folium
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup = location).add_to(myMap)
myMap.save("location.html")




