#Defining the function
def sort(tuples):
    return sorted(tuples, key=lambda x: x[-1])
 
a= [(2,5),(1,2),(4,4),(2,3)]

#Callling the function
print("Sorted List:")
print(sort(a))
