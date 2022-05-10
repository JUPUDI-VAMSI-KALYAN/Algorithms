from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################
    """_summary_

        This is a Ductch National Flag Varient Problem 
        Solved with three pointers low,mid,high
        also called as counting sort a varient of dutch national flag

        time complexity = o(n)
        space complexity = o(1)
    """



def countsort(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    while mid<= high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr

arr = [0,1,0]
print(countsort(arr))