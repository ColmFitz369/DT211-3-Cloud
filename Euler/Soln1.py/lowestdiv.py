number = 1
div = 1
answer = 0

for i in range(1-10):
    while answer != 0:
        if number % i == 0:
            answer += 1
            i += 1
        else:
            answer = 0
            i = 1
            number += 1
print(number)