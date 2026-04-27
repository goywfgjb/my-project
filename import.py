import time
from readline import get_history_item

name = input("введи имя: ")
print("hello, ", name)

file = open("user.txt", "w")
file.write("hello, " + name)
file.write(" -сейчас: " + time.ctime())
file.close()

print("сохранено")

