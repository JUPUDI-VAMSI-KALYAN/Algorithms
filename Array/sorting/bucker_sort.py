from cmath import sqrt
from collections import defaultdict
from math import ceil
from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################
'''
 number of buckets  = round(sqrt(len(arr)))

 appropriate bucket of each element : 
        ceil(num*bucket/max_value)

Divide the array into buckets
Insert each element into appropriate buckets
sort all the buckets
combine all buckets into one
'''

def bucket_sort(arr):
    n = len(arr)
    bucket = round(n**(1/2))
    print(bucket)
    lis = defaultdict(list)
    for num in arr:
        position = ceil((num*bucket)/max(arr))
        lis[position].append(num)
    print(lis)
    for i in range(1,bucket+1):
        lis[i] = sorted(lis[i])
    print(lis)
    result = []
    for i in range(1,bucket+1):
        result.extend(lis[i])
    print(result)

bucket_sort([3,1,5,6,7,2,8,9,4])