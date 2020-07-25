import random
playing_cards = {
"♠2": 40, "♠3": 41, "♠4": 42, "♠5": 43, "♠6": 44, "♠7": 45, "♠8": 46, "♠9": 47, "♠10": 48, "♠J": 49, "♠Q": 50, "♠K": 51, "♠A": 52,
"♥2": 27, "♥3": 28, "♥4": 29, "♥5": 30, "♥6": 31, "♥7": 32, "♥8": 33, "♥9": 34, "♥10": 35, "♥J": 36, "♥Q": 37, "♥K": 38, "♥A": 39,
"♦2": 14, "♦3": 15, "♦4": 16, "♦5": 17, "♦6": 18, "♦7": 19, "♦8": 20, "♦9": 21, "♦10": 22, "♦J": 23, "♦Q": 24, "♦K": 25, "♦A": 26, 
"♣2":  1, "♣3":  2, "♣4":  3, "♣5":  4, "♣6":  5, "♣7":  6, "♣8":  7, "♣9":  8, "♣10":  9, "♣J": 10, "♣Q": 11, "♣K": 12, "♣A": 13
}
poker_number = 1
poker_names = list(playing_cards.keys())
poker = poker_names * poker_number
#把牌洗亂
def poker_shuff(rand_poker_list):
    random.shuffle(rand_poker_list)
#抽到的牌
def init_get_poker(poker_list):
    return [poker_list.pop(random.randint(0, len(poker_list)-1))]
#牌的代表值
def count(hand_poker):
    score = 0
    for i in hand_poker:
        score = playing_cards.get(i)
    return score
def pk(your_card, pc_card):
    if your_card > pc_card:
        print("你贏了餒skr skr")
    elif your_card == pc_card:
        print("咱倆平局")
    else:
        print("你輸了辣")
def game_over():
    if_continue = input("是否繼續下一輪(Y/N):")
    if if_continue.upper() == "Y":
        if len(poker) == 0:
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

def every_round(poker_list):
    # 各自的牌
    your_init_poker = init_get_poker(poker_list)
    pc_init_poker = init_get_poker(poker_list)
    print("玩家的牌：{}".format(your_init_poker))
    print("電腦的牌：{}".format(pc_init_poker))
    # 牌的代表值
    your_card = count(your_init_poker)
    pc_card = count(pc_init_poker)
    return pk(your_card, pc_card)
    while True:
        if_game_go = game_over() 
        if if_game_go == True:
            print("玩家的牌：{}".format(your_init_poker))
            print("電腦的牌：{}".format(pc_init_poker))
            exit(0)
        return pk(your_card, pc_card)

input("按ENTER鍵，遊戲開始")
while True:
    poker_shuff(poker)# 先洗牌
    every_round(poker)# 開始每一局
#    print("此時剩餘數：{}".format(len(poker)))
    game_over()