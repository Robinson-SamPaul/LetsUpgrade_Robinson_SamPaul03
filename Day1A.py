print("\tSimple Calculator")

a = int(input("\nEnter a positive integer : "))
b = int(input("Enter a positive integer : "))
        
print("\n\t<1> to Get Total")
print("\t<2> to Get Difference")
print("\t<3> to Get Product")
print("\t<4> to Get Quitient")
print("\t<5> to Get Reaminder")

c = int(input("\nEnter your choice\t : "))

if c == 1:
    print("\nThe sum of ",a,"&",b,"is",a+b)

elif c == 2:
    print("\nThe difference between ",a,"&",b,"is",a-b)

elif c == 3:
    print("\nThe product of ",a,"&",b,"is",a*b)

elif c == 4:
    print("\nThe Quitent of ",a,"&",b,"is",a/b)

elif c == 5:
    print("\nThe Remainder of ",a,"&",b,"is",a%b)

else:
    print("\nThe calculation can't be done")

