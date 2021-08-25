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

# Nested If..else

num5 = float(input('Please input a number'))
if num5 >= 0: # Will execute if a number is greater than 0
    if num5 == 0: # Will execute if a number is equals to 0
        print('The number is 0 ')
    else: # Will execute if a number is not equals to 0
        print("The number is a positive number ")
else: # Will execute if a number is less than 0
    print('The number is a negative number ')

#conditional statement

    def condi_statement():
        x,y = 10,100

st = "x is less than y " if (x<y) else "x is greater than or the same as y "
print(st)


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

# for loops with range

for x in range(5, 10):
    print(x)