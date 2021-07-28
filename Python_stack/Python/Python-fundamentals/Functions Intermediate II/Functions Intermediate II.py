                            # ASSIGNMENT: FUNCTIONS INTERMEDIATE II


#1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)

#2 Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]["last_name"] = "Bryant"
print(students)

#3 In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

#4 Change the value 20 in z to 30

z = [ {'x': 10, 'y': 20} ]

z[0]["y"] = 30
print(z)



#2  Iterate Through a List of Dictionaries
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
                                    #first_name - Michael, last_name - Jordan
                                    #first_name - John, last_name - Rosales
                                    #first_name - Mark, last_name - Guillen
                                    #first_name - KB, last_name - Tonel

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for val in students:                                
        print(f"first_name - {val['first_name']}, last_name - {val['last_name']}")

iterateDictionary(students)




#3 Get Values From a List of Dictionaries
    #Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
     for val in some_list:
        
         print(f"{val[key_name]}")        # VS ---->print({val[key_name]})  returns first/last names ==> {"Michael"}{"Jordan"}. etc..

    
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)




#4 Iterate Through a Dictionary with List Values
    #Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]))   #len(str) = 70,75  VS   # str(len) =7,8  vs len() =7,8
        for list in some_dict[key]:
                print(list)                 

printInfo(dojo)              


# NOTES!!!! =====> just printing instructor's list not locations??...I had to nest the second for within the first for so the function runs/flows in order in one step and not in two steps. The reason i was no getting the location was because once the first "FOR" was completed, it would just run the second "FOR" once and exited the function??

# Python has a built-in function len() for getting the total number of items in a list, tuple, arrays, dictionary etc.








