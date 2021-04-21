#
# Example file for classes
#

# create one class
class myClass():
    
    # self is like this keyword in JS or c#
    def method1(self):
        print("myClass method1")
    
    def method2(self, someString):
        print("myClass method2 " + someString)

# create another class
class anotherClass(myClass):
    # self is like this keyword in JS or c#
    def method1(self):
        # call parent class
        myClass.method1(self)
        print("anotherClass method1")
    
    def method2(self, someString):
        print("anotherClass method2 ")

def main():
    
    # use classes
    # python runtime automatically supplies the self object
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    c2.method2("This is a string")


if __name__ == "__main__":
    main()

