from time import sleep
# your code goes here!

def countdown(number = 10):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1

    print("HAPPY NEW YEAR!")


def countdown_with_sleep(number = 10):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        sleep(1)

    print("HAPPY NEW YEAR!")