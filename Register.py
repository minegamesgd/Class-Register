studentnames = ["Rob", "Anna","Huw","Emma","Patrice","Igbal"]
a = 0
p = 0
length = len(studentnames)

for index in range (0,length):
    if index < length:
        print(studentnames[index])
    x = input("Is student present (y/n)? ")
    index =index+1
    if x == "y" or x == "yes":
        p=p+1

    elif x == "n" or x == "no":
        a=a+1

print("the total number of present students are",p)
print("the total number of absent students are",a)
