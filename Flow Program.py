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