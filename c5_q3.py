# Write a program to find the average of four numbers entered by the user using a set.
s=set()
n=int(input("enter the numbers : "))
s.add(n)
n=int(input("enter the numbers : "))
s.add(n)
n=int(input("enter the numbers : "))
s.add(n)
n=int(input("enter the numbers : "))
s.add(n)
average=sum(s)/len(s)
print(average)

