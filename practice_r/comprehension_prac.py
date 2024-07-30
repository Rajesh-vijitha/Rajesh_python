
in_ = int(input("enter your range: "))
set_com = set(f"{i}is even" if i% 2 ==0 else f"{i} is odd" for i in range(in_))
set_com2 = set(f"{i}is even" if i% 2 ==0 else f"{i} is odd" for i in range(10))
print(set_com2)
print(set_com)

li = [1,2,3,4,5,6,7,8,9,10,11,22,44]

list_com = [f"{i}is even" if i%2==0  else f"{i} is odd" for i in li]

print(list_com)
li_ = int(input("enter you range:"))
tuple_com = (f"{i} is even" if i%2==0 else f"{i}is odd" for i in range(li_))
print(list(tuple_com))
