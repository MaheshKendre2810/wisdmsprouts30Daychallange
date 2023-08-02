# empty list
numberlist = []
 
# elements to put in list
nummber = int(input("Enter number of elements in list: "))
 
#  num to append number in list
for i in range(1, nummber + 1):
    n1 = int(input("Enter elements: "))
    numberlist.append(n1)
 
 
# Printing maximum number index
print("Largest element index is:",(numberlist.index( max(numberlist))+1))
