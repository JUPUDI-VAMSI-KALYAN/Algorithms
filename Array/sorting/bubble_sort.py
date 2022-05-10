from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################

'''
Compare Adjacent elements and swap in correct order until they are sorted
also called sinking sort


Time Complexity = O(n2)
Space Complexity = O(1)
'''

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)

arr = [2,5,7,9,2,3,4,5,6,7,8]
bubble_sort(arr)