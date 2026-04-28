import random

score = 0
cscore = 0

print("WELCOME")
print("you are even ")
a = random.randint(1, 10)
print("enter your number")
number = int(input().strip())
print(a)
z = a + number
print(z)

if z % 2 == 0:
    print("even , choose batting or bowling")
    choice = input().strip()

    if choice == "batting":
        # player bats first
        score = 0
        while True:
            print("enter ur number")
            num = int(input().strip())
            c = random.randint(1, 10)
            print(c)
            if num == c:
                print("out")
                print("your final score =", score)
                break
            else:
                score = num + score
                print("score=", score)

        # player bowls second
        print("your chance to bowl now")
        cscore = 0
        while True:
            j = random.randint(1, 10)
            print("enter your number")
            nu = int(input().strip())
            print(j)
            if nu == j:
                print("out")
                print("my final score =", cscore)
                break
            else:
                cscore = j + cscore
                print("score=", cscore)

    elif choice == "bowling":
        # player bowls first
        print("your chance to bowl first")
        cscore = 0
        while True:
            j = random.randint(1, 10)
            print("enter your number")
            nu = int(input().strip())
            print(j)
            if nu == j:
                print("out")
                print("my final score =", cscore)
                break
            else:
                cscore = j + cscore
                print("score=", cscore)

        # player bats second
        print("your chance to bat now")
        score = 0
        while True:
            print("enter ur number")
            num = int(input().strip())
            c = random.randint(1, 10)
            print(c)
            if num == c:
                print("out")
                print("your final score =", score)
                break
            else:
                score = num + score
                print("score=", score)

else:
    print("odd , i choose bowling")
    # computer bowls, player bats
    score = 0
    while True:
        print("enter ur number")
        num = int(input().strip())
        c = random.randint(1, 10)
        print(c)
        if num == c:
            print("out")
            print("your final score =", score)
            break
        else:
            score = num + score
            print("score=", score)

    # player bowls second
    print("your chance to bowl now")
    cscore = 0
    while True:
        j = random.randint(1, 10)
        print("enter your number")
        nu = int(input().strip())
        print(j)
        if nu == j:
            print("out")
            print("my final score =", cscore)
            break
        else:
            cscore = j + cscore
            print("score=", cscore)

# result
if score > cscore:
    print("you win!")
elif cscore > score:
    print("i win!")
else:
    print("draw!")
