from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################

"""
 Search all the elements in the array 

 Time Complexity : O(n)
 Space Complexity : O(1)
 """

def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return "Present at Index " + str(i)
    else:
        return "Not Found"
array = [1,3,4,5,6,7,8,9]
key = 2
print(linear_search(array, key))
