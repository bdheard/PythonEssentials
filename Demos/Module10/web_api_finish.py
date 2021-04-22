#
# Reading data from the internet
#

import requests

def main():
    
    # read status code
    web_request = requests.get("https://www.bing.com")
    
    print("result code:" + str(web_request.status_code))
    
    # read web page
    web_request = requests.get("http://httpbin.org/html")
    web_data = web_request.text
    #print(web_data)


if __name__ == "__main__":
    main()