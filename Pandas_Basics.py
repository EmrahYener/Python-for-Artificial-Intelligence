# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 00:31:15 2021

@author: emrah
"""

#Pandas Library 


#Pandas is written in Python Language. 
#pandas is a fast, powerful, flexible and easy to use open source data analysis 
#and manipulation tool.
#Pandas provide high performance in manipulating numeric data and time series. 
#Pandas is built on the numpy library and written in languages like Python, Cython, and C. 
#In pandas, we can import data from various file formats like JSON, SQL, Microsoft Excel,CSV etc.

#Keywords:
    #dataframe manipulation
    #CSV,Excel, text etc. files importing, editing,saving
    #easily handling missing data
    #data reshaping, slicing, indexing
    #time series data analysis
    #optimized processing speed


#%%
#Lecture1: Basic functions
    
import pandas as pd

dictionary={"Employee":["John","Roy","Mike","Mary","Max","Carol"],
            "Age":[19,22,29,62,45,36],
            "Salary":[1600,1850,2500,3600,2100,2900]}
    
#Now lets use the pandas library and convert this dictionary to a dataframe like excel

dictionary_dataframe=pd.DataFrame(dictionary)
print(dictionary_dataframe)
    #Returns:
        #        Employee  Age  Salary
        # 0          John   19    1600
        # 1           Roy   22    1850
        # 2          Mike   29    2500
        # 3          Mary   62    3600
        # 4           Max   45    2100
        # 5         Carol   36    2900
    
    
#Lets see the first 5 rows of the dataframe, we use this frequently to see the file content:
head=dictionary_dataframe.head()
print(head)
    #Returns:
        #        Employee  Age  Salary
        # 0          John   19    1600
        # 1           Roy   22    1850
        # 2          Mike   29    2500
        # 3          Mary   62    3600
        # 4           Max   45    2100
    
    
    
#Lets see the last 5 rows of the dataframe. The first 5 is head, then the last 5 is tail:
tail=dictionary_dataframe.tail()
print(tail)
    #Returns:
        #        Employee  Age  Salary
        # 1           Roy   22    1850
        # 2          Mike   29    2500
        # 3          Mary   62    3600
        # 4           Max   45    2100
        # 5         Carol   36    2900
    
    
    
#In the methods above, you can define the row number inside the parentheses:
head_first3=dictionary_dataframe.head(3)
print(head_first3)
    #Returns:
        #        Employee  Age  Salary
        # 0          John   19    1600
        # 1           Roy   22    1850
        # 2          Mike   29    2500
    
    

#Lets see the column names:
columns=dictionary_dataframe.columns
print(columns)
    #Returns:
        #Index(['Employee', 'Age', 'Salary'], dtype='object')
    
    
    
    
    
#Lets see the general information about our data:
general_info=dictionary_dataframe.info()
print(general_info)
    #Returns:
        # <class 'pandas.core.frame.DataFrame'>
        # RangeIndex: 6 entries, 0 to 5
        # Data columns (total 3 columns):
        #  #   Column         Non-Null Count  Dtype 
        # ---  ------         --------------  ----- 
        #  0   Employee       6 non-null      object
        #  1   Age            6 non-null      int64 
        #  2   Salary         6 non-null      int64 
        # dtypes: int64(2), object(1)
        # memory usage: 272.0+ bytes
        # None
    
    #Note: pandas shows string as "object" data type.





#Lets see which data types (for each feature/column) we have in this file:
data_type=dictionary_dataframe.dtypes
print(data_type)
    #Returns:
        # Employee         object
        # Age               int64
        # Salary            int64
        # dtype: object





#Now, we will learn the "describe" fuction:
    
# The "decribe" function generates descriptive statistics.
# Descriptive statistics include those that summarize the central tendency,
# dispersion and shape of a dataset’s distribution, excluding NaN values.
# That means it returns nformation only about numerical features/columns
# Analyzes both numeric and object series, as well as DataFrame column sets of mixed data types. 
# The output will vary depending on what is provided. 

print(dictionary_dataframe.describe())
    #Returns:
        #              Age       Salary
        # count   6.000000     6.000000   #Count number of non-NA/null observations.
        # mean   35.500000  2425.000000   #Mean of the values.
        # std    16.059265   738.748942   #Standard deviation of the observations.
        # min    19.000000  1600.000000   #Minimum of the values in the object.
        # 25%    23.750000  1912.500000   #The lower percentile of the median
        # 50%    32.500000  2300.000000   #Median
        # 75%    42.750000  2800.000000   #The upper percentile of the median
        # max    62.000000  3600.000000   #Maximum of the values in the object.




#%%
#Lecture2: Indexing and Slicing:
    
import pandas as pd

dictionary2={"Employee":["John","Roy","Mike","Mary","Max","Carol"],
            "Age":[19,22,29,62,45,36],
            "Salary":[1600,1850,2500,3600,2100,2900]}
  



  
dataframe2=pd.DataFrame(dictionary2)
print(dataframe2["Employee"])
    #Returns:
        # 0     John
        # 1      Roy
        # 2     Mike
        # 3     Mary
        # 4      Max
        # 5    Carol
        # Name: Employee, dtype: object
    #As you see, it returns the data with an index number. In numpy you just get the data
    #but in pandas it is also indexed.
    #This method is very useful if the column name has space character.

#You can call the same information by using the following method:   
print(dataframe2.Age)
print(dataframe2.Employee)    
#If the data feature has a space character, this method can not be used.
#The pandas returns "SyntaxError: invalid syntax"





#Lets add a new feature or a new column to the dataframe2:
dataframe2["Experience"]=[1,3,5,30,12,7]
print(dataframe2) 
    #Returns:
        #   Employee  Age  Salary  Experience
        # 0     John   19    1600           1
        # 1      Roy   22    1850           3
        # 2     Mike   29    2500           5
        # 3     Mary   62    3600          30
        # 4      Max   45    2100          12
        # 5    Carol   36    2900           7
  




#There is a third method to list a row or a column:
print(dataframe2.loc[:,"Experience"])
    #Returns:
        # 0     1
        # 1     3
        # 2     5
        # 3    30
        # 4    12
        # 5     7
        # Name: Experience, dtype: int64

print(dataframe2.loc[:2,"Experience"])
    #Returns:
        # 0    1
        # 1    3
        # 2    5
        # Name: Experience, dtype: int64
        
#NOTE: As you see the index number "2" is also listed.
#In numpy last index number is excluded but in pandas it is included!!!

print(dataframe2.loc[:,["Employee","Experience"]])
    #Returns:
        #   Employee  Experience
        # 0     John           1
        # 1      Roy           3
        # 2     Mike           5
        # 3     Mary          30
        # 4      Max          12
        # 5    Carol           7






#Lets list the dataframe2 in the reverse order:
print(dataframe2.loc[::-1,:])
    #Returns:
        #   Employee  Age  Salary  Experience
        # 5    Carol   36    2900           7
        # 4      Max   45    2100          12
        # 3     Mary   62    3600          30
        # 2     Mike   29    2500           5
        # 1      Roy   22    1850           3
        # 0     John   19    1600           1





#Lets list the columns between employee and salary:
print(dataframe2.loc[:,:"Salary"])    #This is pandas, "Salary" is included!
    #Returns:
        #   Employee  Age  Salary
        # 0     John   19    1600
        # 1      Roy   22    1850
        # 2     Mike   29    2500
        # 3     Mary   62    3600
        # 4      Max   45    2100
        # 5    Carol   36    2900




#Allright, we have used the "loc" function a lot, but what is this?
#"loc" is used for "Label Based Locating"
#That means, in order to list the data, you should write the label.
#But what if you do not know the label name, but only the index number?
#Then we have a sister function, the "iloc"
#"iloc" is used for "Integer Based Locating".
#Lets see how it works:
    
print(dataframe2.iloc[:3,:2])
    #Returns:
        #   Employee  Age
        # 0     John   19
        # 1      Roy   22
        # 2     Mike   29
    #It is getting complicated but iloc exculed the index number 2.
    #You just have to get used to it:)




#%%
#Lecture3: Filtering

filter_salary=dataframe2.Salary>2100
print(filter_salary)
    #Returns:
        # 0    False
        # 1    False
        # 2     True
        # 3     True
        # 4    False
        # 5     True
        # Name: Salary, dtype: bool




#Lets apply this filter to the dataframe:
filtered_data=dataframe2[filter_salary]
print(filtered_data)
    #Returns:
        #   Employee  Age  Salary  Experience
        # 2     Mike   29    2500           5
        # 3     Mary   62    3600          30
        # 5    Carol   36    2900           7




#Now, lets apply a second filter:
filter_age=dataframe2.Age<35

print(dataframe2[filter_age & filter_salary])
    #Returns:
        #   Employee  Age  Salary  Experience
        # 2     Mike   29    2500           5




#%%
#Lecture4: List Comprehension

#Lets get the average salary:
average_salary=dataframe2.Salary.mean()
print(average_salary)
    #Returns: 2425.0





#Lets add a new feature/column to show if the salary high or low:

dataframe2["Salary Class"]=["Low" if average_salary>each else "High" for each in dataframe2.Salary]
print(dataframe2)
    #Returns:
        #   Employee  Age  Salary  Experience Salary_Class
        # 0     John   19    1600           1          Low
        # 1      Roy   22    1850           3          Low
        # 2     Mike   29    2500           5         High
        # 3     Mary   62    3600          30         High
        # 4      Max   45    2100          12          Low
        # 5    Carol   36    2900           7         High






#Lets make lower case each letter in Employee feature:

dataframe2.Employee=[each.lower() for each in dataframe2.Employee]
print(dataframe2)
    #Returns:
        #   Employee  Age  Salary  Experience Salary_Class
        # 0     john   19    1600           1          Low
        # 1      roy   22    1850           3          Low
        # 2     mike   29    2500           5         High
        # 3     mary   62    3600          30         High
        # 4      max   45    2100          12          Low
        # 5    carol   36    2900           7         High






#Lets capitalize all letters in all column labels:
dataframe2.columns=[each.upper() for each in dataframe2.columns]
print(dataframe2)
    #Returns:
        #   EMPLOYEE  AGE  SALARY  EXPERIENCE SALARY CLASS
        # 0     john   19    1600           1          Low
        # 1      roy   22    1850           3          Low
        # 2     mike   29    2500           5         High
        # 3     mary   62    3600          30         High
        # 4      max   45    2100          12          Low
        # 5    carol   36    2900           7         High





#Now, lets make al again lowercase.
dataframe2.columns=[each.lower() for each in dataframe2.columns]






#As you see, we have a feature called as "Salary Class"
#We want to change the space with "_" character:
    
dataframe2.columns=[each.split()[0]+"_"+each.split()[1] if (len(each.split())>1) else each for each in dataframe2.columns]
print(dataframe2)
    #Returns:
        #   employee  age  salary  experience salary_class
        # 0     john   19    1600           1          Low
        # 1      roy   22    1850           3          Low
        # 2     mike   29    2500           5         High
        # 3     mary   62    3600          30         High
        # 4      max   45    2100          12          Low
        # 5    carol   36    2900           7         High





#%%
#Lecture5: Dropping and Concatenating

#Lets drop the salary_class feature:
    #Here,  axis=1 means drop the data vertically, column
    #       axis=0 means drop data horizontally, row
dataframe2.drop(["salary_class"],axis=1,inplace=False)
    #Returns:
        #   employee  age  salary  experience
        # 0     john   19    1600           1
        # 1      roy   22    1850           3
        # 2     mike   29    2500           5
        # 3     mary   62    3600          30
        # 4      max   45    2100          12
        # 5    carol   36    2900           7

#Now, lets print the dataframe2 again to see if it is changed permamently:
print(dataframe2)
    #Returns:
        #   employee  age  salary  experience salary_class
        # 0     john   19    1600           1          Low
        # 1      roy   22    1850           3          Low
        # 2     mike   29    2500           5         High
        # 3     mary   62    3600          30         High
        # 4      max   45    2100          12          Low
        # 5    carol   36    2900           7         High
    #Change is temporary.
    #If you make the "inplace" True, then replaces the original dataframe:

        


dataframe2.drop(["salary_class"],axis=1,inplace=True)
print(dataframe2)
    #Returns:
        #   employee  age  salary  experience
        # 0     john   19    1600           1
        # 1      roy   22    1850           3
        # 2     mike   29    2500           5
        # 3     mary   62    3600          30
        # 4      max   45    2100          12
        # 5    carol   36    2900           7
    #Dataframe is changed permanetly.




#Now, lets  see the data concatenating:
#It is just like vstack and hstack in numpy

#Create two dataframes:

dframe1=dataframe2.head()
dframe2=dataframe2.tail()

#vertical:
#axis=0 means concating dframes vertically
data_concat=pd.concat([dframe1,dframe2],axis=0)
print(data_concat)
    #Returns:
        #   employee  age  salary  experience
        # 0     john   19    1600           1
        # 1      roy   22    1850           3
        # 2     mike   29    2500           5
        # 3     mary   62    3600          30
        # 4      max   45    2100          12
        # 1      roy   22    1850           3
        # 2     mike   29    2500           5
        # 3     mary   62    3600          30
        # 4      max   45    2100          12
        # 5    carol   36    2900           7


#Horizontal:

salary=dataframe2.salary
age=dataframe2.age

data_horizontal_concat=pd.concat([salary,age],axis=1)
print(data_horizontal_concat)
    #Returns:
        #    salary  age
        # 0    1600   19
        # 1    1850   22
        # 2    2500   29
        # 3    3600   62
        # 4    2100   45
        # 5    2900   36



#Just to see, what happens if we write "0":
data_horizontal_concat2=pd.concat([salary,age],axis=0)
print(data_horizontal_concat2)
    #Returns:
        # 0    1600
        # 1    1850
        # 2    2500
        # 3    3600
        # 4    2100
        # 5    2900
        # 0      19
        # 1      22
        # 2      29
        # 3      62
        # 4      45
        # 5      36
        # dtype: int64



#%%
#Lecture6: Transforming Data:

#We want to double the values in the age column:
dataframe2["Doubled_Age"]=[each*2 for each in dataframe2.age]
print(dataframe2)
    #Returns:
        #   employee  age  salary  experience  Doubled_Age
        # 0     john   19    1600           1           38
        # 1      roy   22    1850           3           44
        # 2     mike   29    2500           5           58
        # 3     mary   62    3600          30          124
        # 4      max   45    2100          12           90
        # 5    carol   36    2900           7           72


#We have also another method for this:


def double_age(age):
    return age*2

dataframe2["Doubled_Age_with_Function"]=[double_age(each) for each in dataframe2.age]
print(dataframe2)
    #Returns:
        #   employee  age  salary  experience  Doubled_Age  Doubled_Age_with_Function
        # 0     john   19    1600           1           38                         38
        # 1      roy   22    1850           3           44                         44
        # 2     mike   29    2500           5           58                         58
        # 3     mary   62    3600          30          124                        124
        # 4      max   45    2100          12           90                         90
        # 5    carol   36    2900           7           72                         72

#or a shorter version with "apply"

dataframe2["Doubled_Age_with_Apply"]=dataframe2.age.apply(double_age)
print(dataframe2)
    #Returns:
        #   employee  age  ...  Doubled_Age_with_Function  Doubled_Age_with_Apply
        # 0     john   19  ...                         38                      38
        # 1      roy   22  ...                         44                      44
        # 2     mike   29  ...                         58                      58
        # 3     mary   62  ...                        124                     124
        # 4      max   45  ...                         90                      90
        # 5    carol   36  ...                         72                      72


    
    
    
    
#%%
#Sources:
"""
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
https://pandas.pydata.org/
https://www.geeksforgeeks.og/difference-between-pandas-vs-numpy/
https://www.udemy.com/course/python-sfrdan-uzmanlga-programlama-1/learn/lecture/10710078#questions
https://stackoverflow.com/questions/54718821/python-pandas-does-loc-and-iloc-stand-for-anything/54719171




"""