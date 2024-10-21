"""
import time
print(range(1,40))
sum =0
for number in range(1,101): #despues de la coma, el 2 implica que irá de 2 en 2
    sum+= number
print(sum)"""




for number in range(1,100):
    if (number %3 ==0) and (number % 5 ==0 ):
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif (number %3 ==0) :
        print("Fizz")
    else:
        print(number)