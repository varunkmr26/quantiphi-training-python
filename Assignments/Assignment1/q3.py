def binarySearch (arr,l,r,x): 
    # Check base case
    if r >= l: 
        mid = l + (r - l)/2 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid         
        #If the element is smaller than the middle element recursively
		#search the left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x) 
        # Else the element can only be present 
        # in right subarray
        else:
            return binarySearch(arr, mid+1, r, x) 
    else:
        # Element is not present in the array
        raise Exception('Element not found')

arr = [ 2, 3, 4, 10, 40 ]
search_element = 4
 
# Function call
index = binarySearch(arr, 0, len(arr)-1, search_element)
print "The index of the given value: ",index
