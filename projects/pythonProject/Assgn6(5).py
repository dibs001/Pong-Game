string = input("Enter your string: ")
find = input("Enter character to find in the string: ")
if find in string:
  print("The character is found at ",string.find(find))
if not find in string:
  print("Not found!!!")
