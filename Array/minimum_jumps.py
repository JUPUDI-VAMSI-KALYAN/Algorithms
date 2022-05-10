from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################

#Very Important and confusing


def minJumps(arr, n):
    #code here
    if n<=1:
        return 0
    if arr[0]==0:
        return -1
    steps=arr[0]
    max_reach = arr[0]
    jumps = 1

    for i in range(1,n):
        if i==n-1:
            return jumps
        max_reach = max(max_reach,i+arr[i])
        steps-=1
        if steps==0 :
            jumps+=1
            if max_reach<=i:
                return -1
            steps = max_reach-i
    return -1
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr, len(arr)))