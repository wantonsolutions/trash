import random
print("Hello Brendan: generating a random number")
# max=100
# number = random.randint(0,max)
# guess=int(max/2)
# guess_size=int(guess/2)

# i=1
# while True:
#     print("Brendan: " + str(i))
#     i=i+i

    # print(guess)
    # if guess > number:
    #     guess = guess - guess_size
    # elif guess < number:
    #     guess = guess + guess_size
    # else:
    #     print("YOU WIN!!")
    #     exit(1)

    # guess_size=int(guess_size/2)
    # if guess_size == 0:
    #     guess_size=1

    # guess = input("Guess a random number: ")

    # try: 
    #     guess=int(guess)
    # except:
    #     print("Enter a real fucking number you moron. You entered "+ guess)

    # if guess:
    #     print("Too High!")
    # elif guess < number:
    #     print("Too Low!")
    # else:
    #     print("YOU WIN!!")


    #     exit(1)
rows = 5
while rows < 1000000:
    k = 2 * rows - 2
    for i in range(rows, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("")
    rows = rows + 1

