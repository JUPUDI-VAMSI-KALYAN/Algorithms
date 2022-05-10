from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################



import heapq

arr = [4,7,3,5,7,4,2]
heapq.heapify(arr)
print(arr)
print(heapq.heappop(arr))
print(arr)