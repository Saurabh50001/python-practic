# num=(int(input("enter the value: ")))
# if (num % num == 0) and (num % 1 == 0):
#     print(num, "Prime number")
# 
# else:
#     print(num,"Not a prime number")

# num=(int(input("enter the value: ")))
# if (num % 2 == 0):
#     print(num, "not a prime no")
# else:
#     print(num, " prime no")

 

# n=(int(input("enter the value: ")))
# count=0
# i=1
# while(i<=n):
#     if(n % i == 0):
#         count=count+1
#     i=i=1
# if(count==2):
#     print(n,"prime no")
# else:
#     print(n,"prime no")        

num=(int(input("enter the value: ")))
prime= True
for r in range(2,num):
    if (num % r == 0):
        prime = False
if prime:
    print( num,"prime no")
else:
    print(num," not prime no")