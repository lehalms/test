import random
winning_num=random.randint(1,100)
guess_num=int(input("guess any number between (1,100): "))
guess=1
game_over=False
while not game_over:
    if guess_num==winning_num:
        print(f"you win in {guess} guess")
        game_over=True
    else:
        if guess_num<winning_num:
            print("too low")
            # guess+=1
            # guess_num=int(input("Again guess: "))
        else:
            print("too high")
            # guess+=1
            # guess_num=int(input("Again guess; "))
        guess+=1
        guess_num=int(input("Again guess: "))