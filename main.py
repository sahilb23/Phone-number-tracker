import phonenumbers
import opencage
import folium

# Save user Input from the terminal
number = input("Enter your phone number with country code:")

# Phone Location
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

# Carrier Provider
from phonenumbers import carrier

service_pro = phonenumbers.parse(number)
carrier_name = carrier.name_for_number(service_pro, "en")
print(carrier_name)

# Location on Google Maps
from opencage.geocoder import OpenCageGeocode
from keys import key

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("MyLocation.html")