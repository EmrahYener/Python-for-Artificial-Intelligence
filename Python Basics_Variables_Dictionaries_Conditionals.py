# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:00:16 2021

@author: emrah yener
"""

#Hello! My name is Emrah Yener. Below you can find my Python notes for beginners. 
#Each section explains a specific subject or use case.


#%%
#Section 1: Identifiers and Variables Introduction

#variable
#function
#object
#Note: If you want to comment multiple lines, just select them and press ctrl+1

var1=10 #integer
var2=20
var22=var1+var2
print(var22)
day="monday" #string

var3=6.42 #double

#SyntaxError example
var4=44  #correct.
5var=22  #incorrect. SyntaxError: invalid syntax

my name="Adams" #incorrect. SyntaxError: invalid syntax
my_name="Adams" #correct.
myName="Adams"  #correct.


#advisable
var6=12 #begin with lowercase
Var7=13  #not a syntax error but first letter lower case is more common. 


#Like any other programming language, Python has a set of rules. 
#These rules define how to write a program in that language. 
#It also explains how the interpreter understands the code. 
#These rules are set on the runtime system and followed by the person writing the code
#The name you use to identify a function, module, class, variable, or any other object is called an Identifier. 
#There are certain rules for creating these identifiers:
#-The identifier can start with a letter: A-Z or a-z.
#-It can start with the underscore character.
#-It cannot start with a number or any other special character.
#-The identifier can contain only alpha-numeric characters and underscore provided it does not start with a number.
#-And the variables are case sensitive so Apple and apple are two different variables.

#%%

#to create a section, use #%%
#in order to run a section press control+enter.
#in roder to run a section and pas to the next one, press shift+enter
#in roder to run just a selected code, pess F9

#%%

#Section 2:Identify Variable Types

sentence="The wetter is sunny today"
print(sentence)

variable_type=type(sentence)
print(variable_type)


#%%
#Section 3: Identify String length

sentence_length=len(sentence)
print(sentence_length)

#%%
#Section 4: Functions Introduction / Built-in Functions

#String  to integer
numberAsText="4538"
print(type(numberAsText))  #Returns str

print(type(int(numberAsText))) #Returns int


#integer to float
integer1=12
float1=float(integer1)
print(float1)

#float to integer
float2=22.4
integer2=int(float2)
print(integer2)
 
#As you see, the int function ignores the value after the point.
#We use antoher function to Round a float value


#Round float to integer
roundedFloat=round(float2)
print(roundedFloat)



#%% 
#Section 5: User Defined Functons

def firstUserDefFunction(input1,input2):
    
    """
    #This is a docString. We use it to explain the use case of the function 

    Parameters: Takes two inputs as input1 and input2. 
        
    Returns: Then returns the Result.
 
    """
    result=input1*input2+(50*(input1/input2))
    
    return result

myFirstCalculation=firstUserDefFunction(12, 31)
print(myFirstCalculation)

#%%
#Section 6: Default and Flexible Functions

def calculateCircle1(r,pi):
    
    """
    Parameters: Takes two inputs as r and pi
    
    Returns: Calculates the circumference of a circle and returns the result.
    
    """
    
    result=2*pi*r
    return result
    


example1=calculateCircle(12, 3.14)

print(example1)



def calculateCircle2(r,pi=3.14):
    
    """
    Parameters: Takes two inputs as r and pi. We do not want to enter the pi value everytime.
    Because pi is always same, it is a constant. You can define constansts in the function.
    
    Returns: Calculates the circumference of a circle and returns the result.
    
    """
    
    result=2*pi*r
    return result

example2=calculateCircle2(13)
print(example2)


def sumTypedNumbers(num1, num2,*args):
    #This function requires minimum two inputs.
    result=num1+num2
    for i in args:
        result=i+result
    print (result)
    
sumTypedNumbers(2,3,4,11,10,8)


def sumTypedNumbersVersion2(num1, num2,*args):
    #This function requires minimum two inputs.
    result=num1+num2+args[0]
    for i in args:
        result=i+result
    print (result)
    
sumTypedNumbersVersion2(2,3,4,1,10)

#%%
#Section7: Use of *args

#“We use the *args OR **kwargs – as our function’s argument when we have doubts about the number of  arguments we should pass in a function.” 

# arg stands for "arguments". 
# The notation "*" is used to define variable number of arguments.
# You do not have to write *args or *kwargs
# The important point here is to write the "*" notation.
# Instead of *args  you can write *var. It means non-keyworded arguments
# Instead of *kwargs you can write *vars. It means keyworded arguments
# But the use of *args and *kwargs is common.


def argsExample(word1,*otherWords):
    print(word1)
    for each in otherWords:
        print("This is one of the words in the `otherWords`iterable object: " + each )
        
letsTest=argsExample("Monday", "Thuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday")


#%%
#Section8: Use of **kwargs

#You should use **kwargs if you want to handle named arguments in a function. 


def capital_cities(**kwargs):
    result=[]
    
    for key,value in kwargs.items():
        result.append("The capital city of {} is {}."  .format(key,value))
    return result

print (capital_cities (Germany="Berlin",England="London", USA="Washington"))

#Output is:
#['The capital city of Germany is Berlin.', 'The capital city of England is London.', 'The capital city of USA is Washington.']


#%%
#Section9: Lambda Function

#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.


#One Argument Example (for square of a number):
    
x=lambda a:a*a

print(x(12))


#Two Argument Example (to multiply two  numbers)

myLambdaFunction=lambda a,b:a*b

print(myLambdaFunction(12, 9))


#Why do we use lambda function?
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#In the function x, you want to multiply the argument of the function x with another unknown number

def x(a):
    
    return lambda b:b+a+a

#Now the first thing to do is defining a value for the variable "a"
myFunction=x(2)

#Now lets define the variable "b" and show the result:
result=myFunction(11)
print(result)
#Result is 15


#%%
#Section10: List
#We use the lists to store multiple arguments in a single variable.
#The Lists are commonly used in python programming.
#We crete a list by using square brackets []
#Just like the Lists, there are 3 more data types in python, which we use to store data collections.
#These are Tuple, Set and Dictionary.


#List of strings
myStringList=["Monday", "Thuesday", "Wednesday"]
print(type(myStringList))

#List of integers
myIntegerList=[12, 26, 48, 66, 135, 99]
print(type(myIntegerList))

#As you see, the data type of the both lists is "List", no matter which data stored inside of it.


#If you want to access any item in a list, you should write it inside the square brackets


print(myIntegerList[0])    #Prints 12

print(myIntegerList[4])    #Prints 135

print(myIntegerList[5])    #Prints 135

print(myIntegerList[-1])   #Prints 99 because "-1" is the first item of the other end of the list.

print(myIntegerList[0:2])  #Prints "12,26". This code includes the first index and excludes the last index.

print(myIntegerList[2:5])  #Prints "48,66,135".

print(myIntegerList[0:])   #Prints the first item and the rest of all after this item. in this case "12, 26, 48, 66, 135, 99"

print(myIntegerList[2:])   #Prints "48, 66, 135, 99"

print(myIntegerList[:2])   #Prints the first item of list and the others until the second item(excluding). in this case "12, 26"


#If you want to see the all features which can be used in the List, type "dir(liste)"

dir(myIntegerList)

     # ['__add__',
     # '__class__',
     # '__contains__',
     # '__delattr__',
     # '__delitem__',
     # '__dir__',
     # '__doc__',
     # '__eq__',
     # '__format__',
     # '__ge__',
     # '__getattribute__',
     # '__getitem__',
     # '__gt__',
     # '__hash__',
     # '__iadd__',
     # '__imul__',
     # '__init__',
     # '__init_subclass__',
     # '__iter__',
     # '__le__',
     # '__len__',
     # '__lt__',
     # '__mul__',
     # '__ne__',
     # '__new__',
     # '__reduce__',
     # '__reduce_ex__',
     # '__repr__',
     # '__reversed__',
     # '__rmul__',
     # '__setattr__',
     # '__setitem__',
     # '__sizeof__',
     # '__str__',
     # '__subclasshook__',
     # 'append',
     # 'clear',
     # 'copy',
     # 'count',
     # 'extend',
     # 'index',
     # 'insert',
     # 'pop',
     # 'remove',
     # 'reverse',
     # 'sort']
 
 #If you want to get information about any of the features above, please tpye "help(list.feature)"
 #Let`s see what "append" is:

help(list.count)
 
    # Help on method_descriptor:
    # count(self, value, /)
    #     Return number of occurrences of value.


#Lets make an example witch "count":
    
myIntegerList2=[12, 26, 48, 66, 135, 99, 12, 66, 12]

howManyWeHave=myIntegerList2.count(12)

print(howManyWeHave)  #Prints "3" and shows us how many "12" we have.


#%%
#Section11: Tuple

#As we have discussed in the previous section, tuples contains a data collection just like Lists.
#The list is dynamic, whereas the tuple has static characteristics. 
#Tuple is a smaller and faster alternative for Lists
#You can see the difference between list and tuple below:
    # 1	Lists are mutable
    #   Tuples are immutable
    # 2	Implication of iterations is Time-consuming	
    #   The implication of iterations is comparatively Faster
    # 3	The list is better for performing operations, such as insertion and deletion.	
    #   Tuple data type is appropriate for accessing the elements
    # 4	Lists consume more memory	
    #   Tuple consume less memory as compared to the list
    # 5	Lists have several built-in methods	
    #   Tuple does not have many built-in methods.
    # 6	The unexpected changes and errors are more likely to occur	
    #   In tuple, it is hard to take place.


myFirstTuple=(12, 26, 48, 66, 135, 99, 12, 66, 12)

dir(myFirstTuple)
    # ['__add__',
    #  '__class__',
    #  '__contains__',
    #  '__delattr__',
    #  '__dir__',
    #  '__doc__',
    #  '__eq__',
    #  '__format__',
    #  '__ge__',
    #  '__getattribute__',
    #  '__getitem__',
    #  '__getnewargs__',
    #  '__gt__',
    #  '__hash__',
    #  '__init__',
    #  '__init_subclass__',
    #  '__iter__',
    #  '__le__',
    #  '__len__',
    #  '__lt__',
    #  '__mul__',
    #  '__ne__',
    #  '__new__',
    #  '__reduce__',
    #  '__reduce_ex__',
    #  '__repr__',
    #  '__rmul__',
    #  '__setattr__',
    #  '__sizeof__',
    #  '__str__',
    #  '__subclasshook__',
    #  'count',
    #  'index']

#When you compare the available methods of tuples with the methods of lists.
#Appearently the List has more methods available.
#This less functionality means less memory need.
#Both Lists and Tuples are iterable
#List allow adding, removing, changing data. They are mutable.
#Tuples do not allow changing data. They are immutable.
#Lets create a List and a Tuple

negativeNumbers=[-1,-2,-3,-4,-5,-6]

positiveNumbers=(42,43,44,45,46,47,48)

for n in negativeNumbers:
    print(n)
    
for p in positiveNumbers:
    print(p)


#Lets import the sys module and use the getsizeof method in it.
#This method returns the size of the object in bytes
#Lets make a comparison. Both have the exact same content.
import sys

comparisonList=[1,2,3,4,5,6,"Washington",3.45879,True,False]
comparisonTuple=(1,2,3,4,5,6,"Washington",3.45879,True,False)

print("The size of the List= ",sys.getsizeof(comparisonList))
print("The size of the Tuple= ",sys.getsizeof(comparisonTuple))

        #The size of the List=  136 bytes
        # The size of the Tuple=  120 bytes
        

#Creating tuple is faster than creating list.
#Lets create a tupe and list containing 1 million items. 
#For this we will import a module called as "timeit"
#The timeit module also a function with same name "timeit".
#It returns the necessary time to perform a task at a given numer of times.

import timeit

myTestList=timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
myTestTuple=timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)

print("Time it Takes for List: ",myTestList)
print("Time it Takes for List: ",myTestTuple)

    # Time it Takes for List:  0.07676159999937227
    # Time it Takes for List:  0.01031929999953718
    
#As you see creating a list takes 7 times much more than creating tuple. 
#When you work with billions of data, this makes a significant performance difference.


#In order to create a tuple with one argument, write a comma at the end

emptyTuple=()
oneElement=("a")
twoElement=("a","b")
threeElement=("a","b","c")

print(emptyTuple)
print(oneElement)
print(twoElement)
print(threeElement)



    #Returns:
    # ()
    # a                (this is not a tuple, this is string. because we should write comma)
    # ('a', 'b')
    # ('a', 'b', 'c')
    
    
oneElement=("a",)  
print(oneElement)   

    #Returns:
    # ('a',)   now this is a tuple.
    
#Lets create tuples without parentheses
tuple1=1,
tuple2=1,2
tuple3=1,2,3

print(tuple1)
print(tuple2)
print(tuple3)

    # returns
    # (1,)
    # (1, 2)
    # (1, 2, 3)
    

#Two types of tuple argument assignment, True is passed, false is notPassed

examResults  =("John","Math",True)  
name=examResults[0]
lesson=examResults[1]
isPassed=examResults[2] 
print("Name :",name)    
print("Lesson :",lesson)       
print("Did he pass? :",isPassed)     

#Lets make the second method, the faster method:

examResults2  =("Mike","Biology",False)  
name,lesson,isPassed=examResults2 #The numer of elements and variables should be matched. Otherwise python raises "ValueError". When working with tuples you have less room for errors.
print("Name :",name)    
print("Lesson :",lesson)       
print("Did he pass? :",isPassed)  



#%%
#Section12: Dictionaries

#Dictionaries are very useful in artificial inteligence use cases

#Dictionaries have two items. Key and Value.

#Dictionaries do not allow key duplication. Otherwise overwrites on existing key.

#You can change a dictionary(editing, deleting, adding)

#With Python version 3.7 dictionaries are ordered. That order do not change.


myFirstBlankDictionary={}

def myExamResults():

    results={"Maths":75,"Physics":90,"Biology":84}
    return results

showMeResult=myExamResults()

print (showMeResult["Maths"])  #Returns: 75
  
#In the example above, the key is "Maths" and the Value is "75".


print (showMeResult) #Returns: {'Maths': 75, 'Physics': 90, 'Biology': 84}

checkDuplication={"Maths":75,"Maths":90,"Biology":84}
print(checkDuplication)
    #Returns: {'Maths': 90, 'Biology': 84}


checkDuplication2={"Maths":65,"Maths":40,"Biology":84}
print(checkDuplication2)
    #Returns: {'Maths': 40, 'Biology': 84}
    
    #That means if a Key is duplicated, python overwrites the next value on the previous one.

#%%
#Section13: If Else Statement

int1=39
int2=33

if(int1>int2):
    print("The first number is larger.")

elif(int1<int2):
    print("The second number is larger.")

else:
    print("Both numbers are the same")




#Lets use the if conditional with a List
myExamResults2={"Maths":73,"Physics":90,"Biology":84}
myScore=myExamResults2["Maths"]
if (myScore>=75):
    print("I passed")
else:
    print("I failed")
    
    
    
    
#Lets make antoher example with a function.
#This function requires a lesson name and returns the result as passed or failed.
def checkScore(lesson):
    myExamResults2={"Maths":73,"Physics":82,"Biology":94}
    myScore=myExamResults2[lesson]
    if (myScore>=75):
        return ("You passed")
    else:
        return ("You failed")
print(checkScore("Maths"))




#lets write a function if a lesson result exists in the list
def is_result_available(lesson):
    lessons=myExamResults2.keys()
    if lesson in lessons:
       return ("The exam result is available")
    else:
       return ("The exam result is not available")       
print(is_result_available("Chemistry"))
print(is_result_available("History"))
print(is_result_available("Maths"))




#Now lets write a function which we write the year and get the century.
def which_century_is_this(year):
    str_year=str(year)
    
    if (len(str_year)<3):
        return ("This is the 1st Century")
    elif (len(str_year)==3):
        first_digit=str_year[:1]
        last_two_digit=str_year[1:]
        if  last_two_digit=="00":
            return ("The century is: "+first_digit)   
        else:
            return ("The century is: "+str(int(first_digit)+1))  
    else:
        first_digit=str_year[:2]
        last_two_digit=str_year[2:]
        if  last_two_digit=="00":
            return ("The century is: "+first_digit)   
        else:
            return ("The century is: "+str(int(first_digit)+1))  
      
print(which_century_is_this(65))
print(which_century_is_this(1856))



#%%
#Section14: For Loop

#Prints each number between 12(including) and 23(exluding)
for each in range(12,23):
    print(each)

#Prints each letter and space in the given string
for each in "This is my first for loop":
    print(each)

#Prints each word. Makes splitting with spaces(default value).
for each in "This is my first for loop".split():
    print(each)

#Splits sentence from the letter "t". In return the letter "t" will be excluded
for each in "This is my first for loop".split("t"):
    print(each)
        # This is my firs
        #  for loop

#Lets sum all numbers in a list in easy way:
myList=[1,2,3,4,5,6,7,8,9,10]
summation=sum(myList)
print(summation)

#Now lets sum all numbers in a list by using for loop:
myList2=[1,2,3,4,5,6,7,8,9]
count=0
for each in myList2:
    count=count+each
print(count)



#%%
#Section15: While Loop


i=5
while i<12:
    i=i+1
    print (i)




#Lets make the List sum exercise which we did above by using while loop
myList3=[1,2,3,4,5,6,7,8,9,21]
size=len(myList3)
count=0
i=0
while i<size:
    count=count+myList3[i]
    i=i+1
print(count)




#Lets find the minimum item in the list by using while loop
myList4=[1,2,3,65,24,55,98,125,-423,-3,15,-9,67,-609,32]
minimum=1000
for each in myList4:
    if (each<minimum):
        minimum=each
    else:
        continue  #You do not need to write this. Just for training purposes.
print(minimum)


















#%%
#Sources
"""
https://book.pythontips.com/en/latest/args_and_kwargs.html
https://code.tutsplus.com/articles/understanding-args-and-kwargs-in-python--cms-29494
https://www.geeksforgeeks.org/args-kwargs-python/
https://www.w3schools.com/python/python_lambda.asp
https://www.w3schools.com/python/python_lists.asp
https://docs.python.org/3/tutorial/datastructures.html
https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/
https://www.youtube.com/watch?v=NI26dqhs2Rk&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=16




"""





