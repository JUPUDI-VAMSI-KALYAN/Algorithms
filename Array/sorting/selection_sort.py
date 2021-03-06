from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################

'''
Select the minimum element in each iteration from unsorted array and
 place at the starting of unsorted array. then increiment the sorted
  array by one 
  Time Complexity = O(n2)
  space Complexity = O(1)
'''

def selection_sort(arr):
    i = 0
    while i<len(arr):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
        i+=1
    print(arr)

selection_sort([2,4,6,8,3,5,7,9])

