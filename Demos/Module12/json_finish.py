#
# Reading json
#

import urllib.request
import json


def output_results(data):
    # load string data into a dictionary
    json_data = json.loads(data)

    # access json elements
    if "title" in json_data["metadata"]:
        print(json_data["metadata"]["title"])

    # get the number of events, plus the magninute and event names
    event_count = json_data["metadata"]["count"]
    print("Events Recorded: " + str(event_count))

    # get the place of each event
    print("The Place of each event:")
    for feature in json_data["features"]:
        print(feature["properties"]["place"])
    print("_______________________________________\n")

    # get events of magnitude 4 or greater
    print("Events of magnitude 4 or greater:")
    if feature in json_data["features"]:
        event_magnitude = feature["properties"]["mag"]
        event_place = feature["properties"]["place"]

        if event_magnitude >= 4.0:
            print("%2.1f" % event_magnitude, event_place)
    print("_______________________________________\n")

    # get events that were felt
    print("Events that were felt:")
    if feature in json_data["features"]:
        event_magnitude = feature["properties"]["mag"]
        felt_count = feature["properties"]["felt"]
        event_place = feature["properties"]["place"]

        if felt_count != None:
            if felt_count > 0:
                print("%2.1f" % event_magnitude, event_place, " reported " + str(felt_count) + " times")
    print("_______________________________________\n")

def main():

    # https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    
    # check connection
    web_url = urllib.request.urlopen(url)
    
    print("result code:" + str(web_url.getcode()))

    if(web_url.getcode() == 200):
        data = web_url.read()
        output_results(data)
    else:
        print("Cannot connect to internet service.")
    


if __name__ == "__main__":
    main()