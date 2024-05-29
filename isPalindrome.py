inp=input()
def my_function(x):
  return x[::-1]

if inp == my_function(inp):
    print("palindrome")
else:
   print("not palindrome")