import folium
import opencage
import win32com.client as wincom
import phonenumbers
from phonenumbers import geocoder
number = input("enter the phone number whose location you want to trace")
pepno = phonenumbers.parse(number)
location_access = geocoder.description_for_number(pepno ,"en")
speak = wincom.Dispatch("SAPI.SpVoice"
)
text = f"this number belongs to {location_access} "
speak.speak(text)
print(location_access)

from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
from opencage.geocoder import OpenCageGeocode
ggkey = "19a7a355f11645359e8106a1b8316c67"
geocoder = OpenCageGeocode(ggkey)
query = str(location_access)
result = geocoder.geocode(query)
#print(result)
if result and len(result) > 0:
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']

    # Print coordinates
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Create a map with Folium
    mymapping = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location_access).add_to(mymapping)
    mymapping.save("myLocation.html")
else:
    print("Location could not be determined.")