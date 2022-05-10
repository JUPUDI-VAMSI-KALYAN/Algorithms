from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################

def reverse(arr):
    i=0
    print(len(arr)//2)
    while i<len(arr)//2 :
        arr[i],arr[-i-1]=arr[-i-1],arr[i]
        i+=1
    return arr 

array = [1,2,3,4,5,6]
print(reverse(array))