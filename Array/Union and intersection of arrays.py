from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################
"""
Dictionary is best to check wheather the elemet id visited or not
list is waste it need to search. so it take time
but dict can check in O(1) time

only dict for hashing

here Union and Intersection and finding unique elements we use hashing


"""



def UnionAndIntersectionofArray(a,b):
    visited = {a[0]:1}
    count=1
    for element in a:
        if element not in visited:
            visited[element]=1
            count+=1
    for element in b:
        if element not in visited:
            visited[element]=1
            count+=1
    return count

a = [1,2,3,4,5,6]
b = [1,7,8,9]
output = 9
print(UnionAndIntersectionofArray(a,b))