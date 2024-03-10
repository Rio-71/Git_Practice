l = []
for i in range(0, 6):
    x = input("enter something to append: ")
    l.append(x)
a = input("enter something to search: ")
if a in l:
    print("search results")
else:
    print("no results found!")
