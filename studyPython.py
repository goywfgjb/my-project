name = input("введите ваше имя: ")
print(f"hello {name}")

file= open("user.txt", "w")
file.write(f"hello, " + name)
file.close