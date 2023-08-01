# empty list
numberlist = []
 
# elements to put in list
nummber = int(input("Enter number of elements in list: "))
 
#  num to append number in list
for i in range(1, nummber + 1):
    n1 = int(input("Enter elements: "))
    numberlist.append(n1)
 
# Print maximum number
print("Largest element is:", max(numberlist))
