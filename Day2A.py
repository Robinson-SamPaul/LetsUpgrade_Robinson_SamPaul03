import random as rd

print("\tLottery")

a = []
n = int(input("\nEnter the no.of Participants\t: "))

for i in range(n):

    print()
    x = "Enter Participant Name "+str(i+1)+"\t: "
    b = input(x)
    a.append(b)

c = rd.randint(1,n)

print("\nThe Participants were ",end = '')

for j in a:
    print(j,end = ' ')
    
print("\n")    
print(a[c-1],"won the lottery")


