def fizzbuzz(num1,num2):
    i = num1
    while(i<=num2):
        if(i%3 == 0 and i%5 == 0):
            print(str(i) + " FizzBuzz")
        elif(i%3 == 0):
            print(str(i) + " Fizz")
        elif(i%5 == 0):
            print(str(i) + " Buzz")
        else:
            print(i)
        i = i + 1