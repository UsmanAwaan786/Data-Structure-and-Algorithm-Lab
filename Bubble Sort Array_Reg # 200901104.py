# Name: Muhammad Usman       Reg # : 200901104
def Sort(arr): # bubble sort function
	 

	for i in range(len(arr)):
        
		print("\nouter loop:",i)
        
		for j in range(0, len(arr)-i-1):
                   
                  print("\ninner loop:",j)
			
                  if arr[j] > arr[j+1] :
                
                         temp=arr[j]
                         arr[j]=arr[j+1]
                         arr[j+1]=temp



arr = [64, 34, 25] # initialize  array
 
Sort(arr) # calling function
 
print ("Sorted: ",end=(""))
for i in range(len(arr)):
    print (arr[i],end=(","))
