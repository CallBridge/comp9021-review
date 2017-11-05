'''
一个著名的博弈论游戏，起源大概是一个美国电视游戏节目叫做Let's make a deal，这个问题名字来源于节目主持人Monty Hall 。
游戏简述：
“参赛者会看见三扇关闭了的门，其中一扇的后面有一辆汽车或者是奖品，选中后面有车的那扇门就可以赢得该汽车或奖品，而另外两扇门后面则各藏有一只山羊或者是后面没有任何东西。当参赛者选定了一扇门，但未去开启它的时候，知道门后情形的节目主持人会开启剩下两扇门的其中一扇，露出其中一只山羊。主持人其后会问参赛者要不要换另一扇仍然关上的门。问题是：换另一扇门会否增加参赛者赢得汽车的机会率？如果严格按照上述的条件的话，答案是会。—换门的话，赢得汽车的概率是2/3。”
用python仿写这个游戏

作者：Sisyphus235
链接：http://www.jianshu.com/p/a036a8a14a4c
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
'''
It is a game theory trick, the player would be given 3 closed door, one of the door has a prize behind, and other two doors
have one sheep behind.
After player made a choice, the , to make sure a stable result, the game holder will open a door which has a sheep behind(definately
 the game holder knows where is the sheep), and ask the player if he would like to change his choice.
 So the program should be:
    3 -> 1
    2 -> 1(sheep)
    change or not?
    give result
'''
from random import randint,seed
# set seed = 0

seed(0)

while True:
    try:
        times = int(input('Enter the number of times to run the simulation: '))
        choice = str(input('Do you want the contestant to switch door?'))
        if choice == 'no' or 'No' or 'N' or 'NO' or 'n':
            choice = None
            choice = False
        elif choice == 'yes' or 'Yes' or 'YES' or 'Y':
            choice = None
            choice = True
        else:
            raise Exception
        break
    except:
        print('Incorrect Input, retry please.')

def simulate(n):
    probablity = 0
    for _ in range(n):
        prize_place = randint(1,3)
        print(f'Contestant does not know it, but car happens to be behind door {chr(64+prize_place)}',end='.')
        which_one = randint(1,2)
        game_host = 0
        contestant = randint(1,3)
        L = [1,2,3]
        L.remove(prize_place)
        if which_one == 1:
            game_host = L[0]

        else:
            game_host = L[1]

        print(f'Contestant chooses door {chr(64+contestant)}',end='.\n')
        print(f'Game host opens door {chr(64+game_host)}',end='.\n')
        if choice:
            # choose to change another door.
            L.remove(contestant)
            contestant = L[0]
            print(f'Contestant chooses door {chr(64+contestant)} and {"win"if contestant==prize_place else "lose"} the game', end='.\n')
        else:
            print(f'Contestant chooses door {chr(64+contestant)} and {"win"if contestant==prize_place else "lose"} the game', end='.\n')
        if contestant == prize_place:
            probablity+=1
    p = probablity/n
    print('The probability of win :',round(p,3)*100,'%')

simulate(times)