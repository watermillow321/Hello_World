
# variables

j = 5 # int
a = 1.15 # float
jarvis_hello="Hello jarvis " # string
char = 'p' # char

# basic def function

def hello(): # creates the def function
    global jarvis_hello # the variable is now declared on the whole code
    jarvis_hello = 'Hello World '
    print(jarvis_hello)

#



#user output and input

Jarvs_name = input("Enter a name:") # input from user

print(Jarvs_name) # user print out

#operators

additon = j + a # addition
substraction = j - a # subtraction
multiplication = j * a # multiplication
division = j/a # division
modulo = j%a # modulo

print(additon)
print(substraction)
print(multiplication)
print(division)
print(modulo)

name_jarvis = Jarvs_name + jarvis_hello # adding strings
print(name_jarvis)

a = 'ohhh'
string_output = a*3 # multiplying strings
print(string_output)

# conversions

testing = 'Hell World'

print(type(testing)) # to know what variable type

results = division + modulo # implicit type of conversion
print(results)

float_number = 1.5 # explicit type of conversion
integer_number = int(float_number)
print(integer_number)


r = '33' # converting string into float and int
integer_numbers = int(r)
float_numbers = int(r)
print(integer_numbers)
print('float_numbers:' , float_numbers)
print('integer_numbers', integer_numbers)
print(type(float_numbers))
print(type(integer_numbers))

floats=15.5
inters= 31
string_outputs = str(floats) # converting float into string
print(string_outputs)
print(type(string_outputs))

string_outputs1 = str (inters) # converting int to string
print(string_outputs1)
print(type(string_outputs1))

#comparison of operators
x = 20
y = 30

print(x > y) # false
print(y < x) # true

print ( x == y ) # false
print (x == 30 ) # true

print( x != y ) # true
print( x != 30 ) # false

print( y >= 30 ) # true
print( y >= 20 ) # false

print(x <= y ) # true
print( x <= 25 ) # false

x=10
y=20

# AND Operator

print(y>x and x<=10) # true
print(x==y and x==10) # true


# Both operands should be true so that the outcome could come true, if one operand is false then the whole statement is false.

# OR Operator

print (y>x or x<y) # true
print (x<=10 or y<=20 ) #true
print (x==30 or y!=20) #true

# One  operands should be true, if both operand is false then the whole statement is false.

# Not Operator

print(x!=10) # true
print(x==10) # false

# An operand should be false to become true and false to become true, in short it is just the oposite.

#If statement

if x > 8:
    print('This number is equals to 10 ') # Will execute if x > 8 is true
print('This number is not equal 10 ') # will execute if x > 8 is not true (Outside of if statement)

#If else statement

if x >= 10:
    print('Ths number is equals to  10') # Will execute if x >= 10 is true
else:
    print('This number is not equals to 10') # Will execute if x >= 10 is false ( inside of if statement )

#Elif statement

if x < 30:
    print('This number is equals to 10 ') # Will execute if x > 30 is true
elif x == 10:
    print('This number is equals to 10 ') # Will execute if x==10 is true and if x > 30 is false
else:
    print('This number is not equals to 10 ') # Will print if both x < 30 and x == 10 is false

#Neste If..else

num5 = float(input('Please input a number'))
if num5 >= 0: # Will execute if a number is greater than 0
    if num5 == 0: # Will execute if a number is equals to 0
        print('The number is 0 ')
    else: # Will execute if a number is not equals to 0
        print("The number is a positive number ")
else: # Will execute if a number is less than 0
    print('The number is a negative number ')

# if statement with a break

Numero = [ 1 ,10 , 0 , 15 ,-6 , -2 , -8 ]

for K in Numero:
    if K < 0:
        break # break is used to terminate a loop, as you can see the loop
        # ends at 15 becuase above 15 are negative numbers
print(K)

#If else with a for and continue

Numero = [ 1 ,10 , 0 , 15 ,-6 , -2 , -8 ]

for O in Numero:
    if O <= 0: # a loop ofr a negative number
        continue # the loop will continue outside the loop and will print the outside text
    print(O)
print('This is outside of the loop')

for O in Numero:
    if O <= 0: # a loop ofr a negative number
        continue
    print(O)
print('This is outside of the loop')

#While loops

R = 1
U = 5

while R  <=  U :
    print('This is a While Loop')
    R = R + 1 # This will print the text 5 times, this is what known to be known as iteration
    # the loop will stop printing if it only goes over 5, the loop will be terminated.

# while R :

# This is a infinite loop

# print('This is a never ending loop')

# This is a never ending loop it will never stop

n = 10

Sum = 0

i = 1

while i <= n :

    Sum = Sum + i

    # 1st = 0 = 0 + 3
    # 2nd = 9 = 3 + 3
    # 3rd = 12 = 9 + 3
    # 4th = 15 = 12 + 3
    # until it reaches the 10th which equals to 55

    i = i+1 # i will be always be equals to 3, simply because  i is always 1 and it will always add to 1 which will have
    # a out come of 3
    # 1 = 1 + 1, has an out come of 3

    print('The sum is ', Sum)

# While with else loop

    O = 0

while O < 5:
    print("Hello")
    O = O +  1  # This will print Hello for 5 times
else:
    print('Hi ') # This will print Hi for the 6th time

# Nested while and if loops with break

outcome = 0

while True:
    userinput = input('Please input a number:') # gets a number from the user
    userinput = float(userinput) # converts the userinput to a float

    if userinput < 0 :# if the user inputs the negative number it will end the loop, and show the sum
        break
    outcome += userinput # adds all positive number

print(' sum = ', outcome) # prints the outcome


# For loop

Name = ['Millow J. Gapay','Will Gapay','Milo Gapay'] # known as a list or an array

for Names in Name:
    print(Names)

# For loop

numbers = range(1,10) # it will give a sequence of numbers 1 - 10
sum = 0 # this is a variable to store a sum

for i in numbers:
    sum += i
# Iteration
#     sum      i   outcome
# 1st (sum(0) + 1) =1
# 2nd (sum(2) + 2) =4
# 3rd (sum(4) + 3) =7
# 4th (sum(7) + 4) =10
# 5th (sum(10) + 5) =15
# 6th (sum(15) + 6) =21
# 7th (sum(21) + 7) =28
# 8th (sum(28) + 8) =36
# 9th (sum(15) + 9) =45

print('The sum is', sum)


#For loops with Else

My_name = [19 , 'Hello Millow ']

for J in My_name:
    print(J)
else:
    print('Hi There')

#pass statement

Name = ['Millow J. Gapay','Will Gapay','Milo Gapay']

for Y in Name:
    pass
print("This statement after loop ")

# Functions


def say_hello (): #Class function
    print('Hello') #This will not print

say_hello() #this will print hello





# Some Control Flow Programms
#1

print("Larger or smaller number")
Num1 = input('Please input the first Number')
Num2 = input('Please input the second Number')

for Q in Num1:
    Largest  = Num1 <= Num2
    Largest = Num1
    break
for W in Num2:
    Largest = Num2 <= Num1
    Largest = Num2
    break

print('The largest number is', Largest)

#2.0

print('Leap Year Calculator')

User_YearINPUT = int(input('Please input a year:'))

if User_YearINPUT % 4 == 0 and User_YearINPUT % 100 != 0 :
   print('This is a leap year',User_YearINPUT)
elif User_YearINPUT % 100  == 0:
    print('This is not a leap year',User_YearINPUT)
elif User_YearINPUT % 400 == 0 :
    print('This is a leap year',User_YearINPUT)
else:
    print('This is not a leap year', User_YearINPUT)

#2.1

print('Leap Year Calculator')

User_YearINPUT = int(input('Please input a year:'))

if User_YearINPUT % 4 == 0 and User_YearINPUT % 100 != 0 :
   print('This is a leap year',User_YearINPUT)
elif User_YearINPUT % 100  == 0:
    print('This is not a leap year',User_YearINPUT)
elif User_YearINPUT % 400 == 0 :
    print('This is a leap year',User_YearINPUT)
else:
    print('This is not a leap year', User_YearINPUT)

#3











