#!/usr/bin/env python
# coding: utf-8

# In[1]:


ansof question.1= the for loop is used when we already know the number of iterations,which means when we know how many times a statement has has to be executed.
example-
l = [1,2,3,4,5,6,7,8]
for i in l:
    print(i)
(here in this example we know that how many times this for loop going to run)

when we need to end the loop on a condition other than the number of times,we use a while loop.
for example=
x = 1
while x<9:
    print(x)
    x = x+1
    if x==3:
        continue
ans of question number2:-#Q2.  Write a python program to print the sum and product of the first 10 natural numbers using for 
#and while loop
strt_point = 1
counter = 1
for i in range(10):
    strt_point = strt_point+counter
    counter = counter+1
print(strt_point)
# product of 1st 10 natural numbers by for loop
strt_point = 1
counter = 1
for i in range(10):
    strt_point = strt_point*counter
    counter = counter+1
print(strt_point)

#sum of 1st 10 natural; num by while loop
strt_point = 0
counter = 1
while n<= 10:
    strt_point = strt_point+counter
    counter = counter+1
print(strt_point) 

# product of 1st 10 natural num by while loop
strt_point = 1
counter = 1
while counter<= 10:
    strt_point = strt_point*counter
    counter = counter+1
print(strt_point) 
 
 
 ans of question no 3:- 
n = int(input("enter the unit"))
if n<=100:
    print(n*4.5)
elif n>100 and n<=200:
    print((100*4.5)+(n-100)*6)
elif n>200 and n<=300:
    print((100*4.5)+(100)*6+(n-200)*10)
elif n>300:
    print((100*4.5)+((100)*6)+(100*10)+(n-300)*20)
    
        
ans of question no4:-#Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each 
#number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print 
#that list
l1 = range(1,101)
l2 = [] 
for i in l1:
    if i**3 % 4 == 0 or i**3 % 5 ==0:
        l2.append(i)
    else:
        pass
print(l2)  

count = 1
l2 = [] 
while count<=100:
    if count**3 % 4 == 0 or count**3 % 5 ==0:
        l2.append(count)
        count+=1
    else:
        count+=1
print(l2)
 ans of question num5:-#Write a program to filter count vowels in the below-given string.
#string = "I want to become a data scientist

n = input('enter the string:-')
count = 0
l = "aAeEiIoOuU"
for i in n:
    if i in l:
        count += 1
count    

