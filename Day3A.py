print("\tContactBook\n")

a = int(input("Enter the number of Persons : "))
b = {}

print()

for i in range(a):

    s = "no."+str(i+1)
    name = input("Enter {} name : ".format(s))
    num1 = int(input("Enter {} num1 : ".format(s)))
    num2 = int(input("Enter {} num2 : ".format(s)))
    mail = input("Enter {} mail : ".format(s))
    webl = input("Enter {} link : ".format(s))

    print()

    b[name] = {
        "name" : name,
        "num1" : num1,
        "num2" : num2,
        "mail" : mail,
        "link" : webl,
        }
    
for key, value in b.items():
    print("{} = {}".format(key,value))











