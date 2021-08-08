from time import sleep
import numpy

def play():
    j = int(input('Type the level you wanna play\nIt must be between 1-9\n\t>'))
    i = 2**j
    n = 0
    while True:
        n += 1
        print("Round: ", n)
        x = numpy.random.randint(0, 100, i)
        print("Guess which number will be chosen by computer from list below\n", x)

        y = numpy.random.choice(x)
        a = int(input('\t>'))
        sleep(.3)

        if a == y:
            print('\nYppppyyyyyy\nWelldone the chosen number was: ', y)
            print(f"You have wone at Round {n} of level {j}")
            return False
            sleep(.6)
        else:
            print(f"Nope\nDidnt matched\nThe chosen number was: {y}\nTry again\n")
            sleep(.2)

        if n > 5:
            i -= 1
        else:
            pass

play()
