#
# Reading data from the internet
#

import urllib.request

def main():
    
    # try to connect to google.com
    web_url = urllib.request.urlopen("http://www.bing.com")
    
    # read status code
    print("result code:" + str(web_url.getcode()))
    
    # read web page
    web_data = web_url.read()
    print(web_data)


if __name__ == "__main__":
    main()