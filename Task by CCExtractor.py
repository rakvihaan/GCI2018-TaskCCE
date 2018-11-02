for i in range(1,11):
    print("GCI is great!!")
print("Hey there, what is your name?")
name=input()
print("Hello {}, please to meet you!".format(name))

def reversedname(name):
    return"".join(reversed(name))
print("Did you know that your name spelled backwards is '{}'!!".format(reversedname(name))) 
