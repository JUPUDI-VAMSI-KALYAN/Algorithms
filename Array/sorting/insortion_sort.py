from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################


def insartion_sort(arr):
    for i in range(1,len(arr)):
        num = arr[i]
        j=i
        while arr[j-1]>num:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
        arr[j]=num
    print(arr)

arr = [2,4,6,8,3,5,7,9]
insartion_sort(arr)


