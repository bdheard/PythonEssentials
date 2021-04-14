#
# Reading json
#

import urllib.request
import json


def output_results(data):
    
    # load string data into a dictionary
    json_data = json.loads(data)

    # access json elements


    # get the number of events, plus the magninute and event names


    # get the place of each event

    print("_______________________________________\n")

    # get events of magnitude 4 or greater
    print("Events of magnitude 4 or greater:")
 
    print("_______________________________________\n")

    # get events that were felt
    print("Events that were felt:")
 
    print("_______________________________________\n")

def main():

    # https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    
    # check connection
    web_url = urllib.request.urlopen(url)
    
    print("result code:" + str(web_url.getcode()))

    # if successful then parse results
    
    


if __name__ == "__main__":
    main()