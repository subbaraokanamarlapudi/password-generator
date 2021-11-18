import random

lower = "hello"
upper = "venkata subbarao"
numbers = "0123456"
symbols = "[]{}()"

all = lower + upper + numbers + symbols
length = 2
password = "".join(random.sample(all, length))
print(password)