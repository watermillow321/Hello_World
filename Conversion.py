# conversions

testing = 'Hello World'

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