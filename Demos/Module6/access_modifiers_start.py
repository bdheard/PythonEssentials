# program to illustrate access modifiers of a class
  
# super class
class Parent:
    public_variable = None
    _protected_variable = None
    __private_variable = None

    def __init__(self, var1, var2, var3):  
        self.public_variable = var1
        self._protected_variable = var2
        self.__private_variable = var3     
    def display_public_members(self):
        print("Public Data Member: ", self.public_variable)
    def _display_protected_members(self):
        print("Protected Data Member: ", self._protected_variable)
    def __display_private_members(self):
        print("Private Data Member: ", self.__private_variable)
    def access_private_members(self):     
        self.__display_private_members()

# derived class
class Child(Parent):
    def __init__(self, var1, var2, var3): 
        super().__init__(var1, var2, var3)
    def access_protected_members(self):
        self._display_protected_members()
   
# creating objects of the derived class     
obj = Child("Geeks", 4, "Geeks !") 
  
# calling public member functions of the class
obj.display_public_members()
obj.access_protected_members()
obj.access_private_members() 

print("Object is accessing public member:", obj.public_variable)
print("Object is accessing protected member:", obj._protected_variable)
#print("Object is accessing private member:",obj.__private_variable)