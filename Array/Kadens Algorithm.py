from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

########################################################################
    """  Kaden's Algorithm

    To Find Maximum Sum Sub Array

    INPUT: Array(Negative and Positive mixed) or (Negative Numbers)
    Output: Maximum sub Array Sum
    """
def Kadens(arr):

    curr_sum = 0
    max_sum= - 10**9 #should be Negative infynity for all Negative array input
    for element in arr:
        curr_sum+=element
        if curr_sum<element:
            curr_sum=element
        max_sum=max(max_sum,curr_sum)
    return max_sum


array = [1,2,3,-2,5] # negative and Positive NUmbers
array2 = [-1,-2,-3,-4] # all Negative Numbers
print(Kadens(array))

