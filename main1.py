grade = []
ccc = 0 
total = people = www = 0
while www != -1 :
     www = int(input("Grade"))
     grade.append(www)
print("People number: %d" % (len(grade)-1))
for i in range(0,len(grade) - 1):
    total += grade[i]
    ccc = total / (len(grade) - 1)
print("Total: %d piece: %d" % (total,ccc))