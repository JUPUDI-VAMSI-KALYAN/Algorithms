from os import path
import sys

if(path.exists('input.txt')):
	sys.stdin=open("input.txt","r")
	sys.stdout=open("output.txt","w")

######################################################################


def main():
    # Your code goes here
    t = int(input())
    for _ in range(t):
        s = input()
        position = (ord(s[0])-ord('a'))*25
        position+= (ord(s[1])-ord('a'))-1
        print(position)

    
if __name__ == "__main__":
    main()

