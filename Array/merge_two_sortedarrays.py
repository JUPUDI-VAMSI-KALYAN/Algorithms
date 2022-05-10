from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################

def merge(arr1, arr2, n, m): 
        # code here
        i=0
        j=0
        while i<n:
            if arr1[i]>arr2[j]:
                arr1[i],arr2[j]=arr2[j],arr1[i]
            if arr2[j]>arr2[j+1]:
                while j<m-1:
                    if arr2[j]>arr2[j+1]:
                        arr2[j],arr2[j+1]=arr2[j+1],arr2[j]
                    j+=1
            i+=1
            j=0
            print(arr1)
            print(arr2)
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
merge(arr1,arr2,6,2)
