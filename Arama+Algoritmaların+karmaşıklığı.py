
# coding: utf-8

# In[16]:

def createRandom(n):
    import random
    myarray=[]
    for i in range(n):
        myarray.append(random.randint(0,100))
    return myarray
createRandom(5)

def myBubble_Sort(my_array):
    number_of_comparison=0
    for passnum in range(len(my_array)-1,0,-1):
        for i in range(passnum):
            number_of_comparison=number_of_comparison+1
            if my_array[i]>my_array[i+1]:
                temp = my_array[i]
                my_array[i] = my_array[i+1]
                my_array[i+1] = temp
    return (my_array,number_of_comparison)

def insertionSort(alist):
    number_of_comparision=0
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            number_of_comparision=number_of_comparision+1
            alist[position]=alist[position-1]
            position = position-1

    alist[position]=currentvalue
    return(alist,number_of_comparision)


# In[14]:

n=10
for i in range(3):
    print(myBubble_Sort(createRandom(n)))


# In[ ]:




# In[ ]:




# In[ ]:




# In[17]:

from random import randrange

def createRandomList(n):
    myarray = []
    for i in range(n):
        foo = [0,1,2,3,4,5,6,7,8,9]
        random_index = randrange(0,len(foo))
        myarray.append(foo[random_index])
    return myarray

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue

newArray = createRandomList(5)
print("----------bubbleSort----------------")
print("----------old list baby-------------")
print(newArray)
bubbleSort(newArray)
print("----------new list baby-------------\n")
print(newArray)

newArray = createRandomList(5)
print("----------insertionSort----------------")
print("----------old list baby-------------")
print(newArray)
insertionSort(newArray)
print("----------new list baby-------------")
print(newArray)


# In[43]:

from random import randrange

def createRandomList(n):
    myarray = []
    for i in range(n):
        foo = [0,1,2,3,4,5,6,7,8,9]
        random_index = randrange(0,len(foo))
        myarray.append(foo[random_index])
    return myarray

def bubbleSort(alist):
    step = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                step += 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return step
def insertionSort(alist):
   step = 0
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         step += 1
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue
   return step

newArray = createRandomList(50)
print("----------bubbleSort----------------")
print("----------old list baby-------------")
print(newArray)
step = bubbleSort(newArray)
print("----------new list baby-------------\n")
print(newArray)
print("----------step = " , step , "-------------\n")

newArray = createRandomList(50)
print("----------insertionSort----------------")
print("----------old list baby-------------")
print(newArray)
step = insertionSort(newArray)
print("----------new list baby-------------")
print(newArray)
print("----------step = " , step , "-------------")


# In[55]:

from random import randrange

def createRandomList(n):
    myarray = []
    for i in range(n):
        foo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
        random_index = randrange(0,len(foo))
        myarray.append(foo[random_index])
    return myarray

def bubbleSort(alist):
    step = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                step += 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return step
def insertionSort(alist):
   step = 0
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         step += 1
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue
   return step

newArray = createRandomList(30)
print("----------bubbleSort----------------")
print("----------old list baby-------------")
print(newArray)
step = bubbleSort(newArray)
print("----------new list baby-------------")
print(newArray)
print("----------step = " , step , "-------------\n")

newArray = createRandomList(30)
print("----------insertionSort----------------")
print("----------old list baby-------------")
print(newArray)
step = insertionSort(newArray)
print("----------new list baby-------------")
print(newArray)
print("----------step = " , step , "-------------")


# In[ ]:



