# f=open("shubhz.txt","w")
# f.write("Welcom to my World")
# f.close()

# f=open("shubhz.txt","a")
# s=f.write("Hey Im Shubhangi\n")
# print(s)
# f.close()

f=open("shubhz.txt","r+")
print(f.read())

f.write("Python Training \n")
f.close()