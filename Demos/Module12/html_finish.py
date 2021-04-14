#
# Reading HTML
#

from html.parser import HTMLParser

meta_count = 0

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Comment found:", data)
        position = self.getpos()
        print("\tAt line: ", position[0], " position ", position[1])
    
    def handle_data(self, data):
        if (data.isspace()):
            return
        print("Data found:", data)
        position = self.getpos()
        print("\tAt line: ", position[0], " position ", position[1])

    def handle_starttag(self, tag, attrs):
        global meta_count
        if tag == "meta":
            meta_count += 1
        
        if attrs.__len__() > 0:
            print("\tAttributes:")
            for attribute in attrs:
                print("\t", attribute[0], " = ", attribute[1])
        print("Starttag found:", tag)
        position = self.getpos()
        print("\tAt line: ", position[0], " position ", position[1])

    def handle_endtag(self, tag):
        print("Endtag found:", tag)
        position = self.getpos()
        print("\tAt line: ", position[0], " position ", position[1])


def main():

    # instantiate the html parser and feed it some data. 
    html_parser = MyHTMLParser()
    html_file = open("sample_html.html")
    
    if html_file.mode == 'r':
        file_content = html_file.read()
        html_parser.feed(file_content)

    print("Meta tags count:" + str(meta_count))


if __name__ == "__main__":
    main()