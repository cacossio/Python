#1
for i in range(1, 10, 1):
    print(i)


#2
for t in range(1, 10, 3):
    print(t)


#3
for y in range(5):
    if y < 5:
        print(y)
    elif y == 3:
        print("y is 3")


#4
for j in range(20, 1, -3):
    print(j)



#5
cities = ["London", "Paris", "Tokyo"]
for city in cities:
    print(city)


#6
numbers = [7, 13, 8, 42]
for x in range(0, len(numbers)):
    print(x)
    print(numbers[x])
if numbers[len(numbers) - 1] == 42:       
    print("The answer to life, the universe, and everything.")


#7
for num in range(10):
    if num % 2 == 0:
        print("Hello")
    elif num % 4 == 0:
        print("World")
    else:
        print(num)


#8
for num in range(10):
    if num % 4 == 0:
        print("Hello")
    elif num % 2 == 0:
        print("World")
    else:
        print(num)


#9
pet_info = {"name": "Fido","age": 4,"trick": "rolls over"}

for key in pet_info:
    print(key)
    print(pet_info[key])


#10
things_to_remember = {
    "First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():
    print(num + ", I will " + step)



####### For Loops: Basic I #########

# Basic - Print all integers from 0 to 150.

for i in range(151):
    print(i)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for i in range(0,1005,5):
    print(i)


# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for i in range(0,100,1):
    if i % 5 == 0:
        print("coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for i in range(0,500000,1):
    if i % 2 != 0:
        sum = sum + i

print(sum)


# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for i in range(2018,0,-4):
    print(i)
   


# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)


lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum + 1,):
     if x % mult == 0:
         print(x)











