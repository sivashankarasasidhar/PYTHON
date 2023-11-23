#write a Python program to swap first and last element of the list.'''
'''def swaping(list):
    list=[1,2,3,34]
    lengt_list=len(list)
    temp=list[0]
    list[0]=list[lengt_list-1]
    list[lengt_list-1]=temp
    return list
print(swaping(list))
##################################################
def swapList(list):
	list=[4,2,3,34]
	list[1],list[-1]=list[-1],list[1]
	return list
print(swapList(list))
##################################################
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	# Storing the first and last element 
	# as a pair in a tuple variable get
	get = list[-1], list[0]
	# unpacking those elements
	list[0], list[-1] = get 
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))
# Python3 program to illustrate 
# the usage of * operand
list = [1, 2, 3, 4]
a,*b,c=list
list=[c,*b,a]
print(list)
# Swap function
def swapList(list):
    list = [1, 2, 3, 4]
    f=list.pop(0)
    l=list.pop(-1)
    list.insert(0,l)
    list.append(f)
    return list
print(swapList(list))'''
def swap_first_last_3(lst):
	# Check if list has at least 2 elements
	if len(lst) >= 2:
		# Swap the first and last elements using slicing
		lst = lst[-1:] + lst[1:-1] + lst[:1]
	return lst

# Initializing the input
inp=[12, 35, 9, 56, 24]

# Printing the original input
print("The original input is:",inp)

result=swap_first_last_3(inp)

# Printing the result
print("The output after swap first and last is:",result)
