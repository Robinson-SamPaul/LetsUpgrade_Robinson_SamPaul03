print("\tPrimeNumber")

def Prime(n):

    for i in range(2,n):

        if n % i == 0:
            return True
            break

        else:
            return False
            break

print()

x = int(input("Enter a positive integer : "))
a = Prime(x)

if a:
    print("\n",x," is a Prime Number")

else:
    print("\n",x," is a Composite Number")

