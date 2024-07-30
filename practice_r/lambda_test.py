import time

cn = 0


def hello_dummy():
    data1 = lambda: f"cn :{cn}, ct:{50}"
    print(data1())


hello_dummy()


def recursive_function():
    global cn
    cn += 1
    ct = 100
    ct += 1
    time.sleep(1)
    print(cn)
    while cn <= 5:
        print("hello", cn, "ct:", ct)
        recursive_function()


data2 = lambda: recursive_function()

data2()

data3 = lambda: "welcome to python"

data4 = data3()
print(data4)

li = [1, 2, 3, 4, "nithin", "python"]
li2 = [4, 5, 6, 7]

# Lambda to combine two lists
second_return_func_lambda = lambda a, s: (a.copy(), a.copy().extend(s))[0]

# Using the lambda
data5 = second_return_func_lambda(li, li2)
data6 = second_return_func_lambda(li2, li2)
data7 = second_return_func_lambda(li2, li)

print(data5)
print(data6)
print(data7)

multiple_arg = lambda a, b: (print(type(a), type(b)), sum([a, b]))[1]

m_data = multiple_arg(1, 2)
m_data2 = multiple_arg(6, 7)
m_data3 = multiple_arg(3, 4)
m_data6 = multiple_arg(3, 4)
m_data4 = multiple_arg(m_data, m_data2)
m_data5 = multiple_arg(m_data4, m_data3)
print(m_data5)

star_arg = lambda *c: (print(c), print(type(c)), sum(c))[2]

data8 = star_arg(1, 3, 4, 5, 6)

print(data8)

double_str_arg = lambda **d: (print(d), print(type(d)), sum(d.values()))[2]

data9 = double_str_arg(a=2, b=3, c=3, d=33)

print(data9)