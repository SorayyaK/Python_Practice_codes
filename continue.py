for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)

#This equal to the below piece of code:

# for x in range(30):
#     if x % 3 != 0 and x % 5 != 0:
#         print(x)
