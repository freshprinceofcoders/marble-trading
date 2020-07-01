import random
start_purse = 1000
purse = start_purse
last_round = []
rounds = 6


print(f"you start the game with {start_purse}")
bag = ('green','green','green','green','green','black','white','red','red','red',)
marble = random.choice(bag)
for draw in range(1,rounds+1):
    bet = int(input(f"Current Purse: {purse} \nRound {draw} - Enter a number you want to bet: "))
    if marble == "green":
        result = bet
        print("yes you get your money back and added on")
    elif bet > purse:
        print("You cannot bet that high")
        break
    elif marble == "red":
        result = -bet
        print("unlucky")
    elif marble == "black":
        print("yessss your rich")
        result = start_purse * 10
    else:
        print("your broke")
        result = start_purse *-5
    purse += result

    if purse < 0.5 * start_purse:
        print(f'Game over! You lost to much!!!')
        break
    print(f"purse: {purse} last result = ({marble}):{result}")

    #print("start purse/endpurse:",start_purse,purse)
    #print('gain/loss',((purse-start_purse)/start_purse *100)"%")