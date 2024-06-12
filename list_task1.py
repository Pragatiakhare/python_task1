#GROCERY LIST MANAGER

list=[]

num=int(input("Enter number of items you want in the list : \n"))
for item in range(num):
 name = input("Enter names of items you want in the grocery list : ")
 list.append(name) #To add items in the list

print(list)

#To remove an item from the list
n1=input("Enter the name of item you want to delete : ")
for item in list:
    if item==n1:
        list.remove(item)
print(list)

#To check if an item is in the list

n2=input("Enter the name you want to check in the list: ")
#for item in list:
if (n2 in list):
 print("The item is present in the list")
else:
 print("The item is not in the list")


#Count the items in the list

i=0
for item in list:
    i=i+1
print("The number of items in the list are : ",i)
