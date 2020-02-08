##
##
# Import URL in code to create the URL for RESTful API 
import urllib.parse
import requests

# Create RESTful API call to MapQuest...
# Create variable for base URL 
base_api_url = "http://www.mapquestapi.com/directions/v2/route?"
#start_location = "Baltimore"
#dst_location = "Miami"
api_key = "wUVBAWuwYk7FTz8JYOexkXcO3QDobmOB"
while True:
    start_location = input("Please enter location: ")
    dst_location = input("Please enter destination: ")
# Create the final URL with urlencode form urllib
    url = base_api_url + urllib.parse.urlencode({"key":api_key, "from":start_location, "to":dst_location})
# Sending a get request from variable url and requesting JSON data format
    json_response = requests.get(url).json()
    print(json_response)
    print(url)
# Check status code of call to RESTful API...
    returned_status = json_response["info"]["statuscode"]
    mapquest_copyright = json_response["info"]["copyright"]["text"]
    print()
    if returned_status == 0:
        print("The status of your API call was: " + str(returned_status))
        print(mapquest_copyright)
    print()



