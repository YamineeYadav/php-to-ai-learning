# f = open("demo.txt" ,"r")
# line1 = f.read()
# print(line1)
# line2 = f.readline()
# print(line2)
# add "a" at the end
f = open("demo.txt" ,"r+")
f.write("abc")
print(f.read())
f.close()
# r+ read and overrife existing data(pointer at start)- no truncate

# w+  read override truncate  - truncate
#  a+   read + append  (pointer end) - no truncate