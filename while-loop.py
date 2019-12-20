# # while
# i = 1
# while (i < 5):
#     print(i)
#     i+=1
# # break
# i = 1
# while (i < 5):
#     if (i == 3):
#         break
#     print(i)
#     i+=1
# continue  
i = 1
while (i < 5):
    i+=1
    if( i == 4): continue
    print(i)
# while else
i = 1
while (i < 5):
    i+=1
    if( i == 4): continue
    print(i)
else:
    print('here is i value',i)
