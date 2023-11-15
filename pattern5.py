#num=int(input("enter the number of rows"))
#for i in range (num):
#    x=75
#    for j in range(i+1):
#        character=chr(x)
#        print(character,end=" ")
#        x=x-1
#    print()



#num=int(input("enter the number of rows"))
#for i in range (num):
#    x=75
#    for j in range(i+1):
#        character=chr(x)
#        print(character,end= '*')
#        x=x-1
#    print()





#n=int(input("enter the number"))
#for i in range(1,n+1):
#    for j in range(1,n+2-i):
#        print("*",end=" ")
#    print()



#num=int(input("enter the number of rows"))
#for i in range (1,num+1):
#    x=75
#    for j in range(1,num+2-i):
#        character=chr(x)
#        print(character,end=" ")
#        x=x-1
#    print()



#num=int(input("enter the number of rows"))
#for i in range(0,num):
#    for j in range(0,num-i-1):
#        print(end=" ")
#    for j in range(0,i+1):
#        print("*",end=" ")
#    print()


num=int(input("enter the number of rows"))
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()