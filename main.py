file=open('Brian.txt','r')
print(file.read())
file.close()

file=open("Brian.txt","w")
print(file.write("My name is Breezy,Im 24 years old"))
file.close()

file=open("Brian.txt","a")
print(file.write("I have added something else here"))
file.close()