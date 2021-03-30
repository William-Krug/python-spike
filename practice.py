print("Hello World")

msg = "Hello William"
print(msg)

age = '36'
name = "William Krug"
print("My name is " + name + " and I am " + age + " years old.")

favoriteNumber = 171
fullName = "William Krug"
print("My name is ", fullName, " and my favorite number is ", favoriteNumber)

number = 171
print(number)

sequence1 = [1, 4, 2, 1]
print(sequence1)

if number < 200:
  print(number, " is less than 200")
else:
  print(number, " is greater than or equal to 200")


newNumber = 3564
if newNumber < 3500:
  print(newNumber, " is less than 3500")
elif newNumber == 3500:
  print(newNumber, " is  equal to 3500")
else:
  print(newNumber, " is greater than 3500")

x = 3500
if x < 3500:
  print(x, " is less than 3500")
elif x == 3500:
  print(x, "is  equal to 3500")
else:
  print(x, " is greater than 3500")

print('*** while loop ***')
while number >= 0:
  print(number)
  number -= 3

print('*** for in loop ***')
number = 171
for i in range(number, 0, -3):
  print(i)

print('*** working with function ***')
print('**!!** Collatz Sequence **!!**')
even = 42
odd = 69
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8]

def compareCollatzSequence(sequence1, sequence2):
  larger = []
  if (len(sequence1) >= len(sequence2)):
    larger = sequence1
  else:
    larger = sequence2
  return larger

def isEven(number):
  return number % 2 == 0

print('calling isEven() on 42, should return `True`:', isEven(even))
print('calling isEven() on 69, should return `False`:', isEven(odd))
print('calling compareCollatzSequence() on [1, 3, 5, 7, 9] and [2, 4, 6, 8], should return [1, 3, 5, 7, 9]:', compareCollatzSequence(list1, list2))