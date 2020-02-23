from random import randint

count = 0
cows = 0
bulls = 0
number = randint(1000,10000)
number_list = list(str(number))
print(number)

while True:
    while True:
        guess = input("Insert a 4 digit number: ")
        if len(guess) == 4:
            try:
                guess_int = int(guess)
                count += 1
                break
            except:
                print("Submission must be a NUMBER.")
        else:
            print("Answer must be 4 digits.")
            continue

    count_list = list(guess)
    cows = 0
    bulls = 0

    if int(guess) == number:
        print(f"You won! Number of tries: {count}.")
        break
    for item in count_list:
        if item in number_list:
            if item == number_list[0]:
                cows += 1

            elif item == number_list[1]:
                cows += 1

            elif item == number_list[2]:
                cows += 1

            elif item == number_list[3]:
                cows += 1

            else:
                bulls += 1

    print(f"Please try again. You had {cows} cow(s) and {bulls} bulls(s).")