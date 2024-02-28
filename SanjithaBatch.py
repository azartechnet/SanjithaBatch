# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 18:05:19 2024

@author: azart
"""
import numpy as np

# arr=[10,20,30,40]
# f1=np.array(arr)
# print(f1)
# print(type(f1))

#Dimensions in Array

# arr=np.array(10)
# print(arr)
# print(arr.ndim)
# arr1=np.array([10,20,30,40])
# print(arr1)
# print(arr1.ndim)
# arr2=np.array([[1,2,3],[4,5,6]])
# print(arr2)
# print(arr2.ndim)
# arr3=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr3)
# print(arr3.ndim)

# arr4=np.array([[1,2,3,4],[5,6,7,8]],ndmin=3)
# print(arr4)
# print(arr4.ndim)

#Access the array elements
# arr1=np.array([10,20,30,40])
# print(arr1)
# print(arr1[0])
# print(arr1[0:3])
# print(arr1[-3:-1])
# print(arr1[::2])
# print(arr1[0]+arr1[1])

# arr5=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr5)
# print(arr5[1,0])

#Copy the array

#arr=np.array([[10,20,30,40,50]])
# x=arr.copy()
# print(x)
# arr[0]=42
#print(arr)
# arr5=np.array([[1,2,3,4,5],[6,7,8,9,10]])
#print(arr.shape)
# print(arr5.shape)
# print(arr5)

#Reshape

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr=arr.reshape(4,3)
# print(newarr)

# arr=np.array([1,2,3,4,5,6,7,8])
# for x in arr:
#     print(x.reshape(1,1))


# arr=np.array([[1,2,3],[4,5,6]])
# for x in arr:
#     for y in arr:
#         print(y)
#         print("******")
#         print(x)


# arr=list([[1,2,3],[4,5,6]])
# for x in arr:
#     for y in arr:
#         print(y)
#         print("******")
#         print(x)
# print(type(arr))

# arr1=np.array([[1,2],[3,4]])
# arr2=np.array([[4,5],[7,8]])
# arr=np.concatenate((arr1,arr2),axis=1)
# print(arr)

#StackFunction

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# #arr=np.hstack((arr1,arr2))
# arr=np.vstack((arr1,arr2))
# print(arr)

#Stacking along height(depth)

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])

# arr=np.dstack((arr1,arr2))

# print(arr)


#Filtering Arrays

# arr=np.array([41,42,43,44])
# x=[True,True,False,False]
# newarr=arr[x]
# print(newarr)

# from numpy import random
# import numpy as np

# arr=np.array([1,2,3,4,5])
# random.shuffle(arr)
# print(arr)


#Generate Random Numbers

from numpy import random
x=random.randint(10,size=(2,3))
x

#Pandas Concepts

import pandas as pd
# a=["azar","bbbb","cccc","dddd"]
# my1=pd.Series(a)
# print(my1)

# print(my1[0])

# my1=pd.Series(a,index=["x","y","z","f"])
# print(my1)

# print(my1['x'])

# my2={101:"azar",102:"mohamed",103:"sai"}
# result=pd.Series(my2,index=[101,102])
# print(result)

import pandas as pd

# #Making the dataframe

# df=pd.read_csv("Life Expectancy Data.csv")
# print(df)
# # ser=pd.Series(df["Country"])
# # d1=ser.head(10)
# # d1

# # #using indexing operator
# # d1[3:6]

# # d1.loc[3:6]

# print(d1.iloc[3:6])

#DataFrame Concepts

# data={"c1":[100,200,300],"c2":[400,500,600]}
# my2=pd.DataFrame(data)
# print(my2)

# # data1=[10,20,30,40]
# # my1=pd.DataFrame(data1)
# # print(my1)

# # print(my1.loc[0])

# #Using list index
# print(my2.loc[[0,1]])

# #Named Indexes
# #With the index argument you can name your own indexes

# print(my2)

# my3=pd.DataFrame(data,index=["d1","d2","d3"])
# print(my3)

# #Locate Named Indexes

# print(my3.loc["d1"])

# # print(pd.options.display.max_rows)

# # print(pd.options.display.max_columns)

# pd.options.display.max_rows = 100

# pd.options.display.max_columns = 100

# print(pd.options.display.max_rows)

# print(pd.options.display.max_columns)





# data={"c1":[100,200,300],"c2":[400,500,600]}
# my2=pd.DataFrame(data)
# print(my2)
# # my3=pd.DataFrame(data,index=["d1","d2","d3"])
# # print(my3)

#Load file into a dataframe

# df=pd.read_csv("D:\SDLCNMK\PythonOT-6.30PM\Position_Salaries.csv")
# print(df)
# #print(pd.options.display.max_rows)

# import numpy as np

data={'One':pd.Series([1,2,3,4],index=['a','b','c','d']),
      'two':pd.Series([10,20,30,40],index=['a','b','c','d'])
      }
table=pd.DataFrame(data)
table

data={'One':pd.Series([1,2,3,4],index=['a','b','c','d']),
      'two':pd.Series([10,20,30,40],index=['a','b','c','d'])
      }
table=pd.DataFrame(data)
table['three']=pd.Series([10,20,30,40],index=['a','b','c','d'])
print("After Insertion::")
print(table)

# # del table['One']
# # print(table)

# # table.pop('two')
# # print(table)

# from numpy.random import randint

# dict={"Name":["mohamed","azar","raja","mohan"],
#       "Math":[89,98,78,67],
#       "Science":[83,99,84,76]}

# arr=pd.DataFrame(dict)

# print(arr)

# arr.loc[len(arr.index)]=["xyz",89,100]
# print(arr)

# row=pd.DataFrame([[11,12,13],[14,15,16]],columns=['One','two','three'])
# table=table.append(row)
# table

# table=table.drop('a')
# table

df_test=pd.DataFrame(np.random.rand(5,5),['A','B','C','D','E'],['W','X','Y','Z','A'])
print(df_test)

print(df_test[['W','A']])

print(df_test.loc['A'])

print(df_test.loc[['A'],['W']])

print(df_test.loc[['A','B'],['W','X']])

df_test['NEWCOL']=df_test['W']+df_test['X']
df_test

print(df_test[(df_test['NEWCOL']>1)])
print("*************************************************")
print(df_test[(df_test['W']<0.4)&(df_test['Y']>0.3)])

df_test

df_test.to_excel('test1.xlsx',sheet_name="mysheet")
print(df_test)

df_test.to_csv('test2.csv')
print(df_test)

#isnull

df_test.isnull()

t1=pd.read_csv("C:\\Users\\azart\\Documents\\Python_UK_DS\\titanic.csv")

print(t1)

print(t1.head(7))

print(t1.tail(10))

print(t1.dtypes)

#info

#Age is retervied

#Age and Sex

#Age >75

t1.info()

print(t1['Age'])

arr=t1[['Age',"Sex"]]
arr

t1['Age'].shape

above_35=t1[t1["Age"]>35]
above_35