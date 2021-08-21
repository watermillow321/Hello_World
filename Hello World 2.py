
class myClass():
    def mymethod(self):
        print("myClass method1")



    def mymethod1(self,sonestring):
        print("myclass method2" + sonestring)

def main():
    c = myClass()
    c.mymethod()
    c.mymethod1("this is a string")


if __name__ == '__main__':
    myClass()
