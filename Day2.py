# count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
 
# Driver Code
lst = []

# elements to put in list
nummber = int(input("Enter number of elements in list: "))
 
#  num to append number in list
for i in range(1, nummber + 1):
    n1 = int(input("Enter elements: "))
    lst.append(n1)


x =int(input("Enter number to be count in list: "))

print('{} has occurred {} times'.format(x,countX(lst, x)))
