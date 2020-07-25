import random
from sys import exit
playing_cards = {
    "♠A": 1, "♠2": 2, "♠3": 3, "♠4": 4, "♠5": 5, "♠6": 6, "♠7": 7, "♠8": 8, "♠9": 9, "♠10": 10, "♠J": 10, "♠Q": 10, "♠K": 10,
    "♥A": 1, "♥2": 2, "♥3": 3, "♥4": 4, "♥5": 5, "♥6": 6, "♥7": 7, "♥8": 8, "♥9": 9, "♥10": 10, "♥J": 10, "♥Q": 10, "♥K": 10,
    "♦A": 1, "♦2": 2, "♦3": 3, "♦4": 4, "♦5": 5, "♦6": 6, "♦7": 7, "♦8": 8, "♦9": 9, "♦10": 10, "♦J": 10, "♦Q": 10, "♦K": 10,
    "♣A": 1, "♣2": 2, "♣3": 3, "♣4": 4, "♣5": 5, "♣6": 6, "♣7": 7, "♣8": 8, "♣9": 9, "♣10": 10, "♣J": 10, "♣Q": 10, "♣K": 10
}
A_list = ["♠A", "♥A", "♦A", "♣A"]
poker_number = 1
poker_names = list(playing_cards.keys())
poker = poker_names * poker_number
#洗牌
def poker_shuff(rand_poker_list):
    random.shuffle(rand_poker_list)
#開局發牌2/1
def init_get_poker(poker_list):
    return [poker_list.pop(random.randint(0, len(poker_list)-1)),poker_list.pop(random.randint(0, len(poker_list)-1))]
#加牌1/1
def one_poker(poker_list):
    return poker_list.pop(random.randint(0, len(poker_list)-1))
#計算牌的代表值
def count(hand_poker):
    score = 0
    for i in hand_poker:
        score += playing_cards.get(i)
    # 判斷有沒有A
    for i in hand_poker:
        if i in A_list:
            if score + 10 <= 21:
                score = score + 10
            else:
                break
    return score
#輸贏
def pk(your_card, pc_card):
    if your_card <= 21 and pc_card > 21:    #電腦爆了
        print("你贏了餒skr skr")
    elif your_card > 21 and pc_card > 21:   #一起爆了
        print("咱倆平局")
    elif your_card > 21 and pc_card <= 21:  #玩家爆了
        print("你輸了辣")
    else:   #不爆的情況
        if your_card > pc_card:
            print("你贏了餒skr skr")
        elif your_card == pc_card:
            print("咱倆平局")
        else:
            print("你輸了辣")
#加牌ㄇ
def more_poker():
    moreP = input("加牌ㄇ(Y/N)：")
    if moreP.upper() == "Y":
        return True
    elif moreP.upper() == "N":
        return False
    else:
        print("要輸入Y或N辣")
        more_poker()
#續玩/不玩/無牌可玩
def game_over():
    if_continue = input("繼續玩ㄇ(Y/N)：")
    if if_continue.upper() == "Y":
        if len(poker) < 10 :
            print("牌不夠了，剩餘卡數：{}".format(len(poker)))
            print("")
            exit(1)
        else:
            return True
    elif if_continue.upper() == "N":
        print("玩家已翻滾退場")
        exit(0)
    else:
        print("要輸入Y或N辣")
        game_over()
#每局
def every_round(poker_list):
    # 給玩家和電腦的手牌們空間
    your_poker = []
    pc_poker = []
    # 檯面上的牌，電腦會蓋一張
    your_init_poker = init_get_poker(poker_list)
    pc_init_poker = init_get_poker(poker_list)
    print("玩家的牌：{}和{}".format(your_init_poker[0], your_init_poker[1]))
    print("電腦的牌：{}和？".format(pc_init_poker[0]))
    # 顯示加牌後
    your_poker.extend(your_init_poker)
    pc_poker.extend(pc_init_poker)
    # 檯面有沒有21p
    your_card = count(your_init_poker)
    pc_card = count(pc_init_poker)
    if your_card == 21 or pc_card == 21:
        print("太神辣!檯面有21點")
        return pk(your_card, pc_card)
    else:
        # 玩家加牌
        while True:
            more_your = more_poker()
            if more_your == True:
                m_poker = one_poker(poker_list)
                your_poker.append(m_poker)
                your_card = count(your_poker)
                print("玩家的牌：{}".format(your_poker))
                if your_card > 21:
                    print("你輸了辣，爆嘍")
                    print("電腦的牌：{}，電腦贏的輕輕鬆鬆ㄟ".format(pc_poker))
                    exit(0)
                else:
                    continue
            else:
                print("玩家停止加牌")
                while pc_card < 19:
                    m_poker = one_poker(poker_list)
                    pc_poker.append(m_poker)
                    pc_card = count(pc_poker)
                print("電腦的牌:{}".format(pc_poker))
                return pk(your_card, pc_card)
input("按ENTER鍵，遊戲開始")
while True:
    poker_shuff(poker)# 先洗牌
    every_round(poker)# 開始每一局
#    print("此時剩餘數：{}".format(len(poker)))
    game_over()
    print("")