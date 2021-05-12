import re

test = "1assWord"
x = re.search(".[A-Z0-9]", test)

print(x)

string = "asdfjksdlfjldskfsd,"
y = len(string) - 1
print(string[:y])