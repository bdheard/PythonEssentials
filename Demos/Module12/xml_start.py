#
# Reading XML and operate on DOM
#

import xml.dom.minidom

def main():

    # Load xml document
    xml_file = xml.dom.minidom.parse("sample_xml.xml")

    # get node and the name of the first child tag
    print(xml_file.nodeName)
    print(xml_file.firstChild.tagName)

    # get list of XML tags
    to_list = xml_file.getElementsByTagName("to")
    print("Number of recipients:" + str(to_list.length))
    for recipient in to_list:
        print(recipient.getAttribute("name"))


    # create a new xml tag
    new_recipient = xml_file.createElement("to")
    new_recipient.setAttribute("name","John Smith")
    xml_file.firstChild.appendChild(new_recipient)


    # get list of XML tags
    to_list = xml_file.getElementsByTagName("to")
    print("Number of recipients:" + str(to_list.length))
    for recipient in to_list:
        print(recipient.getAttribute("name"))



    
if __name__ == "__main__":
    main()