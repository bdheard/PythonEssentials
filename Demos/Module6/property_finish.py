#
# Properties
#

class Person:
    
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if len(first_name) == 0:
            self.__first_name = "Not provided"
        else:
            self.__first_name = first_name

john = Person("John")
print("john:" + john.first_name)

