
# 1. TASK: print "Hello World"

print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable

name = "Carlos"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +

# 3. print "Hello 42!" with the number in a variable

name = 42
print("Hello", name, "!")	# with a comma
print("Hello " + str(name) + "!")	# with a +	-- this one should give us an error! 
                                # SOLUTION =To fix this error we can either add "" to the number 42 = "42" OR write str() and place name within the parenthesis = str(name). With this last option you are changing the variable to a string.

# 4. print "I love to eat sushi and pizza." with the foods in variables

fave_food1 = "tacos"
fave_food2 = "sushi"
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

# NINJA BONUS: Spend a few minutes playing around with other string methods to see what’s out there!

#string.upper():

sports = "i like to practive boxing, swimming, and kayaking"
print(sports.upper())

#string.lower():

fruits = "I liKE tO eAt ManGoEs, APPleS, and WaTErMEloN"
print(fruits.lower())

#string.count(substring): 

gnr= "Knock-knock-knockin' on heaven's door, Knock-knock-knockin' on heaven's door, Knock-knock-knockin' on heaven's door, Knock-knock-knockin' on heaven's door, eh yeah"

substring = "heaven's"
count = gnr.count(substring)
print("The count is", count)

#string.isalnum()

name = "CaRL02 C0SS1o"
print(name.isalnum())

name = "CaRL02C0SS1o"
print(name.isalnum())

#string.endswith(substring)

story="Once upon a time there was a beautiful princess named Ella"
substring = story.endswith ("named Ella")
print(substring)

story="Once upon a time there was a beautiful princess named Ella"
substring = story.endswith ("Ela")
print(substring)







