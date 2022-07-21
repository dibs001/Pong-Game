#Create a list with ten elements using list constructor
word=input("Enter a 10 letter word:")
word_list=list(word)#using list constructor
print(word_list)
#Showing the last item from the list
print("The last item from the list:",word_list[-1])
#Change the third value of the list by replacing it with three new values
word_list[2:3]=['o','q','r']
print(word_list)
#Insert a new item in a specified position
item=input("Enter the item to be inserted:")
pos=int(input("Enter the position where the item is to be inserted:"))
word_list.insert(pos-1,item)
print(word_list)
#Remove the fifth item from the list
word_list.pop(4)
print("After removing 5th element from the list:",word_list)
#Sort the list in descending order
word_list.sort(reverse=True)
print("List printed in descending order:",word_list)
# Create another list by copying the elements of the first list
word_list=list(word)
word_list2=word_list.copy()
print("The copied list:",word_list)
# Concatenate two lists
word_list.extend(word_list2)
print('Concatenated list:',word_list)
# Make all the elements of the second list in upper case letter
word_list3=[x.upper() for x in word_list2]
print(word_list3)
# Make the entire list empty
word_list.clear()
print(word_list)
word_list2.clear()
print(word_list2)
word_list3.clear()
print(word_list3)