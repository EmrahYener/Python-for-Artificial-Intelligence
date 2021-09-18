# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 10:55:51 2021

@author: emrah
"""

#In this file, you will find the basic applications of Numpy.
#It is the fundamental library of python, used to perform scientific computing.
#It provides high-performance multidimensional arrays and tools to deal with them. 
#A numpy array is a grid of values (of the same type) that are indexed 
#by a tuple of positive integers, numpy arrays are fast, easy to understand, and
#give users the right to perform calculations across arrays.
#We use Numpy because it is very useful in matrix operations.


#%%
#Lecture1: Numpy Basics

#First things first, lets import the Numpy Library and get started:
    
import numpy as np

#Lets create a Matrix which has one row and 20 columns:
    
array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print(array.shape)
    #Returns (6,) which means that it has one row,6 columns. 1*20 Matrix




#New lets change the shape of the matrix. It is 1*20, we make it 4*5
new_array=array.reshape(4,5)
print(new_array.shape)
    #Returns (4, 5) which means that it has four rows,5 columns. 4*5 Matrix



print("Dimens on if the new array is: ", new_array.ndim)
    #Returns "2" because our matrix has two dimensions, x and y
    
    
    
print("The data type in the new array is: ", new_array.dtype.name)
    #Returns "int32"
    
    
    
print("The size of the new array is: ", new_array.size)
    #Returns "20". As you see, the "size" function returns the size before reshaping.



print("Data type of the new array is: ",type(new_array))
    #Returns "<class 'numpy.ndarray'>"




#Let create a new array with 3 rows and 5 columns.
#Each square bracked [] creates a row:
array2=np.array([[1,2,3,5,4],[4,8,7,9,0],[7,6,9,2,1]])
array2
    #Returns:
        # array([[1, 2, 3, 5, 4],
        #        [4, 8, 7, 9, 0],
        #        [7, 6, 9, 2, 1]])
    



#Lets create a matrix just by using zeros:
zeros_matrix=np.zeros((3,4))
zeros_matrix    
    #Returns    
        # array([[0., 0., 0., 0.],
        #        [0., 0., 0., 0.],
        #        [0., 0., 0., 0.]])
    
#This may seem unnecessary at first. But it is very useful and we use it frequently.
#This is done for memory allocation.
#You create an array with zeroes and then update the values when necessary.
#Otherwise you should use append method to insert a value to a matrix and this is not preferred for a faster processing




#Lets update an element of the zeros_matrix:
zeros_matrix[0,3]=6    
zeros_matrix    
    #Returns:
        # array([[0., 0., 0., 6.],
        #        [0., 0., 0., 0.],
        #        [0., 0., 0., 0.]])        
    
    
    
    
#Now lets create a matrix with ones:
ones_matrix=np.ones((4,6))
ones_matrix
    #Returns:
        # array([[1., 1., 1., 1., 1., 1.],
        #        [1., 1., 1., 1., 1., 1.],
        #        [1., 1., 1., 1., 1., 1.],
        #        [1., 1., 1., 1., 1., 1.]])
    
    
    

#Now an empty matrix:
empty_matrix=np.empty((2,2))
empty_matrix
    #Returns
        # array([[0.00000000e+000, 6.95230896e-310],
        #        [4.94065646e-324,             nan]])
    #Instead of null, python assings a very small number or nan(not a number)




#If you want to assing numbers between a specific range and a specific increment:
ranged_array=np.arange(4,22,2) #Not "arrange". Just like "a-range"
ranged_array
    #Returns: 
        # array([ 4,  6,  8, 10, 12, 14, 16, 18, 20])




#If you want to create numbers between a range:
numbers_within_range=np.linspace(11, 16,50)
numbers_within_range
    #Returns:
        # array([11.        , 11.10204082, 11.20408163, 11.30612245, 11.40816327,
        #        11.51020408, 11.6122449 , 11.71428571, 11.81632653, 11.91836735,
        #        12.02040816, 12.12244898, 12.2244898 , 12.32653061, 12.42857143,
        #        12.53061224, 12.63265306, 12.73469388, 12.83673469, 12.93877551,
        #        13.04081633, 13.14285714, 13.24489796, 13.34693878, 13.44897959,
        #        13.55102041, 13.65306122, 13.75510204, 13.85714286, 13.95918367,
        #        14.06122449, 14.16326531, 14.26530612, 14.36734694, 14.46938776,
        #        14.57142857, 14.67346939, 14.7755102 , 14.87755102, 14.97959184,
        #        15.08163265, 15.18367347, 15.28571429, 15.3877551 , 15.48979592,
        #        15.59183673, 15.69387755, 15.79591837, 15.89795918, 16.        ])        
    #As you see the limit numbers are also included         
    
    
#%%
#Lecture2: Numpy Basic Operations
import numpy as np

#Lets create two arrays
array1=np.array([2,4,6,8])
array2=np.array([1,3,5,7])





#Sum of arrays:
result_sum=array1+array2
print(result_sum)
    #Returns:
        #[ 3  7 11 15]
 
    
 


#Sum of arrays, method 2:
result_sum=np.add(array1,array2)
print(result_sum)
    #Returns:
        #[ 3  7 11 15]
 



        
#Substraction of arrays:
result_subs=array1-array2
print(result_subs)
    #Returns:
        #[1 1 1 1]
 



        
#Substraction of arrays, method 2:
result_subs=np.subtract(array1,array2)
print(result_subs)
    #Returns:
        #[1 1 1 1]





#Lets do array multiplication:
result_mult=array1*array2
print(result_mult)
    #Returns:
        #[ 2 12 30 56]
        
        



#Lets do array multiplication, method 2:
result_mult=np.multiply(array1,array2)
print(result_mult)
    #Returns:
        #[ 2 12 30 56]




    
#Lets do array division:
result_div=array1/array2
print(result_div)
    #Returns:
        #[2.       1.33333333        1.2        1.14285714]
        
        



#Lets do array division, method 2:
result_div=np.divide(array1,array2)
print(result_div)
    #Returns:
        #[2.       1.33333333        1.2        1.14285714]
    
    
    
    
    
#Lets do matrix multiplication, this one will be a little bit long:      
#Remember! We have a rule, the number of colums of matrix_a = no. of rows in matrix_b

matrix_a=np.array([[2,4,6],[8,10,12]])  #The dimensions of the matrix is 2*3
matrix_b=np.array([[1,3,5],[7,9,11]])   #The dimensions of the matrix is 2*3

matrix_mult_1=matrix_a*matrix_b
print(matrix_mult_1)
    #Returns:
        # [[  2  12  30]
        #  [ 56  90 132]]
    #Here, python just multiplied each row elements with the other row elements
    #This is NOT matrix multiplication!
    #In order to do the correct multiplication use the "dot" method:

matrix_mult=matrix_a.dot(matrix_b)
print(matrix_mult)
    #Returs:
        #ValueError: shapes (2,3) and (2,3) not aligned: 3 (dim 1) != 2 (dim 0)
        
    #Python can not do this calculation because we have a rule, dimensions!
    #Lets align the matrix a with b. Now a is 2*3 and b is 2*3. But b should be 3*2
    #To convert the b matrix from 2*3 to 3*2, we use "T" (transpose) method:
        
    #Lets try again, this is the correct multiplication code:
matrix_mult_correct=matrix_a.dot(matrix_b.T)
print(matrix_mult)        
    #Returns:
        # [[ 44 116]
        # [ 98 278]]

    #or we can take the transpose of the matrix b before the multiplication:
matrix_b_transpose=matrix_b.transpose()
matrix_mult=matrix_a.dot(matrix_b_transpose)
print(matrix_mult)        
    #Returns:
        # [[ 44 116]
        # [ 98 278]]        
        
        
        


#Lets see how to understand rows and colums of a matrix and a matrix transpose:
#matrix_b=[[1,3,5],[7,9,11]]    matix_b_trasnpose=[[1,3,5],[7,9,11]] 
#           row1     row2                          column1  column2

print(matrix_b)
print(matrix_b.T)
    #Returns:
        # [[ 1  3  5]
        #  [ 7  9 11]]
        
        # [[ 1  7]
        #  [ 3  9]
        #  [ 5 11]]
        
        
        
        
    
#Square of an array:
result_square1=array1**2
print(result_square1)
    #Returns:
        #[ 4 16 36 64]
     
        
     
        

#Lets calculate the cosine of the array2
cos_array2=np.cos(array2)
print(cos_array2)
    #Returns:
        #[ 0.54030231 -0.9899925   0.28366219  0.75390225]
        #Returns the cosine value of each number in the array





#Now, we want to check every number in an array if it is smaller than 3.
#It returns true or false
array2_under3=array2<3
print(array2_under3)
    #Returns:
        #[ True False False False]





#Lets find the exponantial value of the matrix_a
#We use matrix exponentials in order to approximate the probality distributions.
#For more detail please check the youtube link given below in the source section.

matrix_a_exp=np.exp(matrix_a)
print(matrix_a_exp)
    #Returns:
        # [[7.38905610e+00 5.45981500e+01 4.03428793e+02]
        # [2.98095799e+03 2.20264658e+04 1.62754791e+05]]





#Lets create a matrix with random numbers between 0 and 1. 
#We have to define the dimension
random_matrix=np.random.random((4,4))
print(random_matrix)
    #Returns:
        # [[0.27416782 0.77551197 0.09953641 0.60646816]
        # [0.38361574 0.18845808 0.8017737  0.93584514]
        # [0.02623638 0.46036515 0.73942381 0.49842046]
        # [0.10815046 0.48858786 0.58898218 0.93537246]]
     
        
     
        
        
#Lets sum all values in the random_matrix
print(random_matrix.sum())
    #Returns
        #7.910915777385354





#Lets sum only the columns, not all values.
#In this example we will sum all values in the columns:
print(random_matrix.sum(axis=0))
    #Returns
        #[0.79217041 1.91292305 2.2297161  2.97610621]
        #    cl_1       cl_2      cl_3        cl_4





#In this example we will sum all values in the rows:
print(random_matrix.sum(axis=1))
    #Returns
        #[1.75568436 2.30969266 1.7244458  2.12109296]
        #    row_1      row_2     row_3       row_4





#Lets sum only a certain row, not all values.
#I this example we will sum all values in the second row:
print(random_matrix.sum(axis=1))
    #Returns
        #7.910915777385354





#Lets find the maximum value in the random_matrix
print(random_matrix.max())
     #Returns
        #0.9358451370414097





#Lets find the minimum value in the random_matrix
print(random_matrix.min())
     #Returns
        #0.02623638431540065





#Lets find the square root of every value in random_matrix
print(np.sqrt(random_matrix))
     #Returns
        # [[0.52361037 0.88063157 0.31549392 0.77876066]
        #  [0.61936721 0.43411759 0.89541817 0.96739089]
        #  [0.16197649 0.67850213 0.85989756 0.70598899]
        #  [0.32886237 0.6989906  0.76745174 0.96714655]]





#Lets find the square of every value in random_matrix
print(np.square(random_matrix))
     #Returns
        # [[7.51679939e-02 6.01418814e-01 9.90749707e-03 3.67803632e-01]
        #  [1.47161038e-01 3.55164474e-02 6.42841072e-01 8.75806121e-01]
        #  [6.88347862e-04 2.11936068e-01 5.46747571e-01 2.48422951e-01]
        #  [1.16965222e-02 2.38718098e-01 3.46900005e-01 8.74921634e-01]]





#%%
#Lecture 3: Indexing and Slicing

#Lets create a one-dimesional array, a vector:
array_3=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

#Lets create a two-dimesional array, a matrix:
array_4=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

print(array_4)
        #Returns:
            # [[ 1  2  3  4  5]
            #  [ 6  7  8  9 10]
            #  [11 12 13 14 15]]


#Lets print the number "14" by indexing:
print(array_4[2,3])
    #Returns:
        #"14"


#Lets print the second row:
print(array_4[1,:])  #This means, print the second row(index1) and all columns
    #Returns:
        #[ 6  7  8  9 10]


#Lets print the fourth column:
print(array_4[:,3])  #This means, print the fourth column(index3) and all rows
    #Returns:
        #[ 4  9 14]


#Lets print the last column:
print(array_4[:,-1])  #This means, print the fourth column(index3) and all rows
    #Returns:
        #[ 5 10 15]


#Lets print the last row:
print(array_4[-1,:])  #This means, print the fourth column(index3) and all rows
    #Returns:
        #[11 12 13 14 15]



#Lets print the first three items of the row two:
print(array_4[1,0:3])  #This means, print the fourth column(index3) and all rows
    #Returns:
        #[6 7 8]


#Lets print the first three items of the row two:
print(array_4[1,0:3])  #This means, print the fourth column(index3) and all rows
    #Returns:
        #[6 7 8]



#Lets print the reverse of the array_4:
print(array_4[::-1])
    #Returns:
        # [[11 12 13 14 15]
        #  [ 6  7  8  9 10]
        #  [ 1  2  3  4  5]]





#%%
#Lecture4: Shape Manupilation of a Matrix
 import numpy as np

matrix1=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(matrix1)
    # Returns:
    #     [[ 1  2  3  4  5]
    #      [ 6  7  8  9 10]
    #      [11 12 13 14 15]]





#Now lets flatten this 3x5 matrix above. We will convert it from 3x5 to 1x15
matrix2= matrix1.ravel()
print(matrix2)
    #Returns
        # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]





#Lets convet it from 1x15 to a 5x3 matrix:
matrix3=matrix2.reshape(5,3)
print(matrix3)
    #Returns:
        # [[ 1  2  3]
        #  [ 4  5  6]
        #  [ 7  8  9]
        #  [10 11 12]
        #  [13 14 15]]
        
        
        
        
        
#Lets make it again a 3x5 matrix:
matrix4=matrix3.ravel()
matrix5=matrix4.reshape(3,5)  #By using "Reshape" method, you define a new  matrix
print(matrix5)
    # Returns:
    #     [[ 1  2  3  4  5]
    #      [ 6  7  8  9 10]
    #      [11 12 13 14 15]]





#If you do not want matrix5 to a new matrix and directly reshape the matrix5 itself,
#you should use the "resize" method:
print(matrix4.reshape(3,5))  # This returns a 3x5 matrix BUT, this reshaping is temporary, if yo do not assing, it is not kept.
print(matrix4) #This returns a 1x15 matrix, which is the original "matrix4".

#Let make this reshaping permanent this time:
matrix4.resize(3,5)
print(matrix4)   #This returns a 3x5 matrix because "resize" method changed the shape permanently.






matrix5T=matrix5.transpose()  #or matrix5T=matrix5.T
print(matrix5T)
    # Returns:
        # [[ 1  6 11]
        #  [ 2  7 12]
        #  [ 3  8 13]
        #  [ 4  9 14]
        #  [ 5 10 15]]




matrix6=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(matrix6.shape)        #Returns:  (4, 3)





#%%
#Lecture5: Stacking of Arrays

#We can stack arrays vertically or horizontally. Lets define two arrays:
    
array5=np.array([[1,2,3],[4,5,6]])
array6=np.array([[7,8,9],[10,11,12]])

print(array5)
print(array6)
    #Returns:
        # [[1 2 3]
        #  [4 5 6]]
        # [[ 7  8  9]
        #  [10 11 12]]


#Lets do the vertical stacking first:
array7=np.vstack((array5,array6))
print(array7)
    #Returns:
        # [[ 1  2  3]
        #  [ 4  5  6]
        #  [ 7  8  9]
        #  [10 11 12]]
        

#Now, the horizontal stacking:
array8=np.hstack((array5,array6))
print(array8)    
    #Returns:
        # [[ 1  2  3  7  8  9]
        #  [ 4  5  6 10 11 12]]
    
    
    
#%%
# Lecture6: Convert and Copy Arrays

#As you now, an array contains lists inside of it.
#That means, instead of writing every row, you can also write a list.

my_list=[1,2,3,4,5,6]

#we can convert this list to an array:
array9=np.array(my_list)
print(array9)
print(type(array9))
    #Returns:
        #[1 2 3 4 5 6]
        #<class 'numpy.ndarray'>




#Lets convert this matrix to an array again:
my_list2=list(array9)
print(my_list2)
print(type(my_list2))
    #Returns:
        #[1 2 3 4 5 6]
        #<class 'list'>








#Now lets talk about copying arrays:
#In order to copy a numpy array, you should not use the assignent operator"="
#If you do so, you do not create a new array but a reference to the existing array:
array_a=np.array([1,2,3,4,5,6])
array_b=array_a
array_b[2]=0
print(array_a)
    #Returns: [1 2 0 4 5 6]
    
#As you see, by changing b, you change the original array which the b refers to.






#The correct way of copying a numpy array is using "copy" method:
array_c=np.copy(array_a)
array_c[5]=0
print(array_a)
    #Returns: [1 2 0 4 5 6]   The array_a did not change

print(array_c)
    #Returns: [1 2 0 4 5 0]   Only the array_c changed
    
    
    
    
    
    
    
    
    

#%%
#Sources
"""
https://www.udemy.com/course/python-sfrdan-uzmanlga-programlama-1/
https://www.youtube.com/watch?v=O85OWBJ2ayo  #Explanation of matrix exponentials
https://www.hindawi.com/journals/mpe/2014/610907/
https://www.geeksforgeeks.org/difference-between-pandas-vs-numpy/




"""

    
    
    
    
