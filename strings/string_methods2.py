txt = "My name is Ståle"
x = txt.encode()
print(x)

txt1 = "Hello, welcome to my world."
x1 = txt1.endswith(".")
print(x1)

txt2 = "H\te\tl\tl\to"
x2 =  txt2.expandtabs(2)
print(x2)

txt3 = "Hello, welcome to my world."
x3 = txt3.find("welcome")
print(x3)