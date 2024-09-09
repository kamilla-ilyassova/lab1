myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

txt = "banana"
x1 = txt.ljust(20)
print(x1, "is my favorite fruit.")

txt1 = "     banana     "
x2 = txt1.lstrip()
print("of all fruits", x2, "is my favorite")

txt2 = "I could eat bananas all day"
x3 = txt2.partition("bananas")
print(x3)

txt3 = "I like bananas"
x4 = txt3.replace("bananas", "apples")
print(x4)