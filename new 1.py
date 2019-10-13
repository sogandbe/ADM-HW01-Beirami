###################Part 1- Homework 1:
###############################Introduction:

######Say "Hello, World!" With Python:
print("Hello, World!")

******Python If-Else:
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
if n%2==0:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
	
######Arithmetic Operators:
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    summ=a+b
    dif=a-b
    pro=a*b
    print(summ)
    print(dif)
    print(pro)

######Python: Division:
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c=a//b
    d=a/b
    print(c)
    print(d)

######Loops:
if __name__ == '__main__':
    n = int(input())
    if n>=0:
        for i in range(0,n):
            print(i**2)
			
######Write a function:
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
            leap=True
    else:
        leap=False
    

    return leap
	
######Print Function:
if __name__ == '__main__':
    n = int(input())
    s=""
    for i in range(1,n+1):
        s=s+str(i)
    print(s)

###########Basic Data Types:

######List Comprehensions:
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lt=[]
    for i in range(0,x+1):

        for j in range (0,y+1):
        
            for k in range(0,z+1):
                
                if i+j+k!=n:
                    lt.append([i,j,k])
    print(lt)

######Finding the percentage:
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    s=0
    for a in student_marks:
        if a==query_name:
            for i in student_marks[a]:
                s+=i
            gpa=s/len(student_marks[a])
    print("%.2f"%gpa)

######Lists:
if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        st=input().split(" ")
        if st[0]=="insert":
            list.insert((int(st[1])),(int(st[2])))
        elif st[0]=="print":
            print(list)
        elif st[0]=="remove":
            list.remove(int(st[1]))
        elif st[0]=="append":
            list.append(int(st[1]))
        elif st[0]=="sort":
            list.sort()
        elif st[0]=="pop":
            list.pop()
        elif st[0]=="reverse":
            list.reverse()
			
######Tuples:
if __name__ == '__main__':
    a = int(input())
    a_l = map(int, input().split())
    t= tuple(a_l)
    print(hash(t))

###############################Strings:

######sWAP cASE:
def swap_case(s):
    e=""
    for i in s:
        if i.islower()==True:
            e+=(i.upper())
        elif i.isupper()==True:
            e+=(i.lower())
        else:
            e+=i
    return(e)
	
######String Split and Join:
    st=(line)
    st=st.split(" ")
    st="-".join(st)
    return(st)
	
######What's Your Name?:
def print_full_name(a, b):
    st=[]
    st.append(a)
    st.append(b)
    
    print("Hello"+" "+ st[0]+" "+st[1]+ "! You just delved into python.")

######Mutations:
def mutate_string(string, position, character):
    s=string
    i=position
    c=character
    s_new=[]
    s_new=[s]
    s_new=s[:int(i)]+str(c)+s[int(i+1):]
    return(s_new)

######Find a string:
def count_substring(string, sub_string):
    c=0
    count=0
    for i in range(len(string)-1):
        for j in range (len(sub_string)-1):
            if string[i]==sub_string[j]:
                if string[i:i+len(sub_string)]==sub_string:
                    count+=1

    return(count)
	
######String Validators:
if __name__ == '__main__':
    s = input()
    c=0
    for i in range(len(s)):
        if s[i].isalnum():
            c+=1
    if c>0:
        print("True")
    else:
        print("False")
    c=0
    for i in range(len(s)):
        if s[i].isalpha():
            c+=1
    if c>0:
        print("True")
    else:
        print("False")
    c=0       
    for i in range(len(s)):
        if s[i].isdigit():
            c+=1
    if c>0:
        print("True")
    else:
        print("False")
    c=0
    for i in range(len(s)):
        if s[i].islower():
            c+=1
    if c>0:
        print("True")
    else:
        print("False")
    c=0
    for i in range(len(s)):
        if s[i].isupper():
            c+=1
    if c>0:
        print("True")
    else:
        print("False")

######Text Alignment:
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

######Text Wrap:
def wrap(string, max_width):
    e=""
    for i in range(0,len(string),max_width):
        e+=(string[i:max_width+i])+"\n"
    return(e)
	
######Alphabet Rangoli:
import math 
def print_rangoli(size):
    l="abcdefghijklmnopqrstuvwxyz"
    n=l[0:size]
    for i in range(0,size):
        string1=n[size-i-1:size]
        if(len(string1)==1):
            print(string1.center((4*size-3),'-'))
        else:
            string2=string1[1:len(string1)]
            stringgReverse=string2[::-1]
            correctString=stringgReverse+string1
            final=""
            for j in range(0,len(correctString)):
                if(j==len(correctString)-1):
                  final=final+correctString[j]
                else:  
                 final=final+correctString[j]+"-"
            print(final.center((4*size-3),'-'))    
    for i in range(size,1,-1):
        string3=n[size-i+1:size]
        if(len(string3)==1):
            print(string3.center((4*size-3),'-'))
        else:
            string4=string3[1:len(string3)]
            stringgReverse2=string4[::-1]
            correctString2=stringgReverse2+string3
            final2=""
            for j in range(0,len(correctString2)):
                if(j==len(correctString2)-1):
                  final2=final2+correctString2[j]
                else:  
                 final2=final2+correctString2[j]+"-"
            print(final2.center((4*size-3),'-'))    

######String Formatting:
def print_formatted(number):
    strLen = len(bin(number)) - 2
    for i in range(number):
        strFormat = "{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}"
        print(strFormat.format(i+1,strLen))
		
######The Minion Game:
def minion_game(string):
    strLength = len(string)
    p1 = 0
    p2 = 0
    for i in range(strLength):
        if string[i] in "AEIOU":
            p1 += strLength - i
        else:
            p2 += strLength - i       
    if p1 == p2:
        print ("Draw")
    else:
        print (*(["Kevin",p1],["Stuart",p2])[p1<p2])
		
######Capitalize!:
for i in "abcdefghijklmnopqrstuvwxyz":
        s = s.replace(" " + i, " "+i.upper())
    s = s[0].upper()+s[1:]
    return s


###############################Numpy:
######Arrays:
    return numpy.flip(numpy.array(arr, float))
	
######Shape and Reshape:
import numpy
a = list(map(int,input().split()))
b = numpy.array(a)
print(numpy.reshape(b, (3, 3)))

######Transpose and Flatten:
import numpy
import sys
a = []
N, M = list(map(int, input().split()))
for i in range(N):
    n = input().split()
    a.append(n)
for i in range(len(a)):
    a[i] = list(map(int, a[i]))

a = numpy.array(a)
print(numpy.transpose(a))
print(a.flatten())

######Concatenate:
import numpy
N, M, P = list(map(int,input().split()))
l1 = []
for i in range(N):
    n = list(map(int, input().split()))
    l1.append(n)
l2 = []
for j in range(N+1, N+M+1):
    n = list(map(int, input().split()))
    l2.append(n)
a1 = numpy.array(l1)
a2 = numpy.array(l2)
c = numpy.concatenate((a1,a2), axis=0)
print(c)

######Zeros and Ones:
import numpy
T = tuple(map(int, input().split()))
z = numpy.zeros(T, dtype = numpy.int)
o = numpy.ones(T, dtype = numpy.int)
print(z)
print(o)

######Sum and Prod:
import numpy
N, M = list(map(int,input().split()))
a = numpy.array([list(map(int,input().split())) for i in range(N)])
s=numpy.sum(a , axis=0)
p=numpy.prod(s)
print(p)



    








