# class MyClass: # this how to declare a class
  #  x = 5

# p1 = MyClass() # this a objected that is created in  a class
# print([p1.x])

# class MyClass1:
  #  def __init__(self,name,message,age ):
   #     self.name = name
    #    self.message = message
     #   self.age = age

   # def output (self):
        print("Hello there" + self.name + "this is a message to you" + self.message + "this is your age" + self.age )

# p1 = MyClass1("Will","Welcome to Pyhton" , "19")
# p1.age = "30"
# p1.output()

class A:
    def function1(self):
        print("My first function")

    def function2(self):
        print("My second function")

class B(A):
    def function3(self):
        print("My third function")

    def function4(self):
         print("My fourth function")

R1 = A()

R1.function1()
R1.function2()

R2 = B()

R2.