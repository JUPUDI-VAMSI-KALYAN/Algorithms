from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################

''''
this Algrithm is only for Sorted Arrays
Search for key in log(n) Time complexity

Time Complexity: log(n)
space = log(n) #due to recurssion stack space else constant
'''

def binary_search(arr,key,start,end):
    mid = (start+end)//2
    if arr[mid]==key:
        return "Key Found At Index : "+ str(mid)
    elif start>=end:
        return "Key Not Found"
    elif key>arr[mid]:
        return binary_search(arr,key,mid+1,end)
    elif key<arr[mid]:
        return binary_search(arr,key,start,mid)
    else:
        return "Key Not Found"

arr = [1,2,3,4,5,6,7,8,9]
key = 1
print(binary_search(arr,key,0,len(arr)-1))