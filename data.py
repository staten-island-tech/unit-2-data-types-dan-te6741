# Use input to make the user input a sentence, then for every i in input print a number

# usersentence = input("Word counter")
# list = usersentence.split()
# def wordcount():
#     print(len(list))

# wordcount()       

     
# numdet = int(input("Type number"))
# if numdet%2 == 0:
#     print ("Even")
# else:
#     print ("Odd")

# base = int(input("Input base bill"))

# tipcalc= int(input("Input service quality. 1= bad, 2= okay, 3= good, 4= great"))
# if tipcalc == 1:
#      print(base)
# elif tipcalc == 2: 
#  print (base + base*0.15)
# elif tipcalc == 3:
#     print (base + base*0.20)
# elif tipcalc== 4:
#      print (base + base*0.25)
# else:
#     print ("Invalid Input")

# x=1
# num = int(input("Input number to calculate all factors of"))
# print(num)
# for i in (range(x,num)):
#     if(num%x == 0):
#         print (x)
    
#     x = x+1


gcf1 = int(input("Input first number of the number pair to find GCF"))
gcf2 = int(input("Input second number of the number pair to find GCF"))
small = 0
if (gcf1 < gcf2):
    small = gcf1
else: small = gcf2


greatest = 0
for i in range (2,small + 1):
    if(gcf1%i == 0) and (gcf2%i == 0):
        greatest = i

print(greatest)


   





