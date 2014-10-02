number = 1
div = 1
answer = 0

while div <=10 and answer != 10:

    if number % div == 0:
    
        answer += 1
        div += 1
    
    else:

        div = 1

print (number)
print (div)

