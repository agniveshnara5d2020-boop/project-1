print("enter a number (numerator):")
numbern = int(input())
print("enter a number(denominator):")
numberd = int(input()) 

if numbern%numberd==0:
    print("\n" + str(numbern)+ "is divisible by"+ str(numberd))
else:
    print("\n" + str(numbern)+ "is not divisible by"+ str(numberd))
    