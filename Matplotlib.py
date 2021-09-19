# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:59:41 2021

@author: emrah
"""

# In this lecture series, we will learn how to use Matplotlib library
# Matplotlib is used for visualisation.
# It is a comprehensive library for creating static, animated, and interactive visualizations in Python.

#%%
#Lecture1: Import data by using pandas and extract general info about the dataset

import pandas as pd

df=pd.read_csv("iris.csv")

#Lets see which features we have in this dataset:
print(df.columns)
    #Returns:
        # Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'], dtype='object')



#Lets see how many entries we have:
print(df.info())
    #Returns:
        # <class 'pandas.core.frame.DataFrame'>
        # RangeIndex: 150 entries, 0 to 149
        # Data columns (total 6 columns):
        #  #   Column         Non-Null Count  Dtype  
        # ---  ------         --------------  -----  
        #  0   Id             150 non-null    int64  
        #  1   SepalLengthCm  150 non-null    float64
        #  2   SepalWidthCm   150 non-null    float64
        #  3   PetalLengthCm  150 non-null    float64
        #  4   PetalWidthCm   150 non-null    float64
        #  5   Species        150 non-null    object 
        # dtypes: float64(4), int64(1), object(1)
        # memory usage: 7.2+ KB
        # None


#OK, now we have 150 entries, but how many unique species?
print(df.Species.unique())
    #Returns:
        # ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']


#Lets compare the numerical values:
print(df.describe())
    #Returns:
        #                Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
        # count  150.000000     150.000000    150.000000     150.000000    150.000000
        # mean    75.500000       5.843333      3.054000       3.758667      1.198667
        # std     43.445368       0.828066      0.433594       1.764420      0.763161
        # min      1.000000       4.300000      2.000000       1.000000      0.100000
        # 25%     38.250000       5.100000      2.800000       1.600000      0.300000
        # 50%     75.500000       5.800000      3.000000       4.350000      1.300000
        # 75%    112.750000       6.400000      3.300000       5.100000      1.800000
        # max    150.000000       7.900000      4.400000       6.900000      2.500000




#Now, in order to analyse each species separately, we can define a dataframe for each:
    
dataframe_setosa=df[df.Species=="Iris-setosa"]
dataframe_versicolor=df[df.Species=="Iris-versicolor"]

#Lets compare the two datasets in a general way by using "describe":
    
print(dataframe_setosa.describe())
print(dataframe_versicolor.describe())
    #Returns:
        #              Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
        # count  50.00000       50.00000     50.000000      50.000000      50.00000
        # mean   25.50000        5.00600      3.418000       1.464000       0.24400
        # std    14.57738        0.35249      0.381024       0.173511       0.10721
        # min     1.00000        4.30000      2.300000       1.000000       0.10000
        # 25%    13.25000        4.80000      3.125000       1.400000       0.20000
        # 50%    25.50000        5.00000      3.400000       1.500000       0.20000
        # 75%    37.75000        5.20000      3.675000       1.575000       0.30000
        # max    50.00000        5.80000      4.400000       1.900000       0.60000
        #               Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
        # count   50.00000      50.000000     50.000000      50.000000     50.000000
        # mean    75.50000       5.936000      2.770000       4.260000      1.326000
        # std     14.57738       0.516171      0.313798       0.469911      0.197753
        # min     51.00000       4.900000      2.000000       3.000000      1.000000
        # 25%     63.25000       5.600000      2.525000       4.000000      1.200000
        # 50%     75.50000       5.900000      2.800000       4.350000      1.300000
        # 75%     87.75000       6.300000      3.000000       4.600000      1.500000
        # max    100.00000       7.000000      3.400000       5.100000      1.800000


# We can each value of setosa withthe value of versicolor.
# For example, average petal length of versicoloris almost 3 times longer than the setosa.



#%%
#Lecture2: Line Plot

import matplotlib.pyplot as plt

#Firstly we can drop the ID column:

dataframe_without_ID=df.drop(["Id"],axis=1)
dataframe_without_ID.plot()  #This method is by default "Line Plot"
plt.show()



#Lets plot each species and more specific datas:
dataframe_setosa=df[df.Species=="Iris-setosa"]
dataframe_versicolor=df[df.Species=="Iris-versicolor"]
dataframe_virginica=df[df.Species=="Iris-virginica"]

#Setosa, Versicolor, Virginica
plt.plot(dataframe_setosa.Id, dataframe_setosa.PetalLengthCm, color="red", label="Setosa-PetalLength",linestyle=":")
plt.plot(dataframe_versicolor.Id, dataframe_versicolor.PetalLengthCm, color="green", label="Versicolor-PetalLength",alpha=0.3)
plt.plot(dataframe_virginica.Id, dataframe_virginica.PetalLengthCm, color="blue", label="Virginica-PetalLength")
plt.legend()  #Writes the Label on the graphic
plt.xlabel("ID")
plt.ylabel("PetalLengthCm")
plt.grid(True)
plt.show()
    # We use "linestyle" to change the line style of the plot and "alpha" to change the opacity
    # For more detail about the linestyles please refer to the:
        # https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html



#%%
#Lecture3: Scatter Plot

# We use scatter plot mostly for data comparisons.
# The plot function will be faster for scatterplots where markers don't vary in size or color.
#The scatter() function plots one dot for each observation. 
#It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis.


dataframe_setosa=df[df.Species=="Iris-setosa"]
dataframe_versicolor=df[df.Species=="Iris-versicolor"]
dataframe_virginica=df[df.Species=="Iris-virginica"]

plt.scatter(dataframe_setosa.PetalLengthCm,dataframe_setosa.PetalWidthCm,color="red",label="Setosa")
plt.scatter(dataframe_versicolor.PetalLengthCm,dataframe_versicolor.PetalWidthCm,color="green",label="Versicolor")
plt.scatter(dataframe_virginica.PetalLengthCm,dataframe_virginica.PetalWidthCm,color="blue",label="Virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel(PetalWidthCm)
plt.title("Scatter Plot")
plt.show()



#%%
#Lecture4: Histogram

# We use histogram to see data frequency distribution.
# It is simply a graph showing the number of observations within each given interval.
# For large numbers of bins (>1000), 'step' and 'stepfilled' can be significantly faster than 'bar' and 'barstacked'.

plt.hist(dataframe_setosa.PetalLengthCm, bins=10) #Each bar is called as "bin". The number of bins is default 10. How many bar/column should matplotlib draw in total range?
plt.xlabel("PetalLengthCm")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()


#%%
#Lecture5: Bar Plot

import numpy as np

x=np.array([1,2,3,4,5,6,7,8])
y=x*1.5+6
countries=["Thailand","Japan","Germany","USA","France","England","Italy","Brasil"]

plt.bar(countries,y)
plt.title("Bar Plot")
plt.xlabel("Contries")
plt.show()

#%%
#Lecture6: Subplot

#Used to plot multiple graphs:

dataframe_setosa=df[df.Species=="Iris-setosa"]
dataframe_versicolor=df[df.Species=="Iris-versicolor"]
dataframe_virginica=df[df.Species=="Iris-virginica"]

plt.subplot(3,1,1)   #We will plot 3 graps. In one column. Now we plot the first row:
plt.plot(dataframe_setosa.Id,dataframe_setosa.PetalWidthCm, color="red", label="Setosa")
plt.ylabel("Setosa-PetalWidthCm")
plt.title("Subplot")

plt.subplot(3,1,2)   #Now we plot the second row:
plt.plot(dataframe_versicolor.Id,dataframe_versicolor.PetalWidthCm, color="green", label="Versicolor")
plt.ylabel("Versicolor-PetalWidthCm")

plt.subplot(3,1,3)   #Now we plot the third row:
plt.plot(dataframe_virginica.Id,dataframe_virginica.PetalWidthCm, color="blue", label="Virginica")
plt.ylabel("Virginica-PetalWidthCm")

plt.show()



#%%
#Sources:
"""
https://matplotlib.org/
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
https://www.udemy.com/course/python-sfrdan-uzmanlga-programlama-1/learn/lecture/10710116#questions
https://www.w3schools.com/python/matplotlib_scatter.asp
https://www.w3schools.com/python/matplotlib_histograms.asp



"""