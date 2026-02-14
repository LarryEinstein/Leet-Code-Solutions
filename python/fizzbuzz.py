for i in range(100):
    if i < 5:
        print(i)

my_range = range(100+1)
print(type(my_range))

for i in my_range:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)