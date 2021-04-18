# enums
#
# Enums
#
from enum import IntEnum


class HTTPCode(IntEnum):
    BAD_REQUEST = 400
    NOT_FOUND = 404
    BAD_GATEWAY = 502
    SUCCESS = 200

response_code = 200

if response_code == HTTPCode.NOT_FOUND:
   print("Not Found")
elif response_code == HTTPCode.BAD_GATEWAY:
   print("???")
elif response_code == HTTPCode.BAD_REQUEST:
   print("???")
elif response_code == HTTPCode.SUCCESS:
       print("Success")
else:
   print("Unknown Status Code")