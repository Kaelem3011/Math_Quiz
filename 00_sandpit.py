import random

num_01 = random.randint(1, 10)
num_02 = random.randint(1, 10)

print(num_01)
print(num_02)

operation = "/"

print()

if operation == "/":
    num_01 = num_01 * num_02
    print("new num 1", num_01)
    question = "{} {} {}".format(num_01, operation, num_02)

    print(question)
