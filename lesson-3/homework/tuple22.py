start = int(input("Start: "))
end = int(input("End: "))

mytuple = ()
for i in range(end-start+1):
    i += start
    mytuple += (i, )

print(mytuple)