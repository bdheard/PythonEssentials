#
# Enums
#

response_code = 200

if response_code == 404:
    print("Not Found")
elif response_code == 502:
    print("???")
elif response_code == 400:
    print("???")
elif response_code == 200:
    print("Success")
else:
    print("Unknown Status Code")