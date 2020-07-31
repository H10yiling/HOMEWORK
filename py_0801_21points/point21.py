import random
import numpy as n
 
class Role:
    def __init__(self):
        self.cards = []
    # 印出手中所有的牌
    def show_card(self, style, show=True):
        lastpoker = len(self.cards) - 1
        if style == 1:
            role = "玩家的牌:"
        else:
            role = "電腦的牌:"
        cardShow = ""
        for i, card in enumerate(self.cards):
            if show:
                if i < lastpoker:
                    cardShow = cardShow + (card.card_color + card.card_text) + ','
                else:
                    cardShow = cardShow + (card.card_color + card.card_text)
            else:
                if i < lastpoker:
                    cardShow = cardShow + (card.card_color + card.card_text) + ','
                else:
                    cardShow = cardShow + ' ?\n'
        print(role + cardShow)

    #計算點數
    def get_value(self, min_or_max):
        Score = 0
        # 手上有幾張A
        A = 0
        for cards in self.cards:
            Score += cards.card_value
            if cards.card_text == "A":
                A += 1
        if min_or_max == "max":
            # 改變A的數量，找出<=21的MAX。
            for i in range(A):
                value = Score - i * 10
                if value <= 21:
                    return value
        # if所有的A都=1，MAX=MIN。
        return (Score - A * 10)
    
    # 清空牌,重新开始
    def clear_card(self):
        self.cards = []
 
class Card:
    def __init__(self, card_color, card_text, card_value):
        self.card_color = card_color
        self.card_text = card_text
        self.card_value = card_value
 
class point21():
    def __init__(self):
        # 玩家角色
        self.player = Role()
        # 電腦角色
        self.computer = Role()
        # 計分器
        self.total_score = n.array([0, 0])
        # 保存一整副52張扑克牌
        self.cards = []
        # 定義所有牌的花色數值
        all_card_color = ["♣", "♦", "♥", "♠"]
        all_card_text = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        all_card_value = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        # 循環牌面類型、牌面數值、牌面點數，用[index]取出其值
        for card_color in all_card_color:
            for index, card_text in enumerate(all_card_text):
                card = Card(card_color, card_text, all_card_value[index])
                self.cards.append(card)
        # 洗牌
        random.shuffle(self.cards)
    def getCard(self):
        return self.cards
    # 發牌1/1
    def give_poker(self, role, num=1):
        for i in range(num):
            card = self.cards.pop(i)
            role.cards.append(card)
    # 判断输赢
    def pk(self, your_score, pc_score):
        if your_score > 21 and pc_score > 21:
            print(f'平局,分数: {your_score}:{pc_score}')
            return n.array([0, 0])
        elif your_score > 21 and pc_score <= 21:
            print(f'你输了,分数: {your_score}:{pc_score}')
            return n.array([0, 1])
        elif your_score <= 21 and pc_score > 21:
            print(f'你赢了,分数: {your_score}:{pc_score}')
            return n.array([1, 0])
        elif your_score <= 21 and pc_score <= 21:
            if your_score < pc_score:
                print(f'你输了,分数: {your_score}:{pc_score}')
                return n.array([0, 1])
            elif your_score > pc_score:
                print(f'你赢了,分数: {your_score}:{pc_score}')
                return n.array([1, 0])
            else:
                print(f'平局,分数: {your_score}:{pc_score}')
                return n.array([0, 0])
    def start_game(self):
        Round = 1
        while len(self.getCard()) > 10:
            self.player.clear_card()
            self.computer.clear_card()
            print("遊戲開始\n")
            print("------------------------------------------")
            print(f"第 {Round} 輪:")
            score = self.every_run()
            self.total_score += score
            print(f"總比分:{self.total_score[0]}:{self.total_score[1]}")
            Round += 1
            again_game = self.QA("再來一局? ( Y / N / y / n ) : ", ["Y", "N", "y", "n"])
            if again_game.upper() == "Y":
                if len(self.getCard()) < 10:
                    print("沒牌了 遊戲結束")
                    break
                else:
                    continue
            elif again_game.upper() == 'N':
                print("遊戲結束")
                break
    def every_run(self):
        self.give_poker(self.player, 2)
        self.give_poker(self.computer, 2)
        self.player.show_card(1)
        self.computer.show_card(0, False)
        score = n.array([self.player.get_value("max"), self.computer.get_value("max")])
        if score[0] == 21 or score[1] == 21:
            print("檯面有21點\n")
            return self.pk(score[0], score[1])
        else:
            while score[0] <= 21:
                Get_New_Poker = self.QA("加牌? ( Y / N / y / n ) : ", ["Y", "N", "y", "n"])
                # 加牌
                if Get_New_Poker.upper() == "Y":
                    self.give_poker(self.player)
                    self.player.show_card(1)
                    self.computer.show_card(0, False)
                    score[0] = self.player.get_value("max")
                    if score[0] > 21:
                        print("玩家超過21點\n")
                        self.computer.show_card(0)
                        return self.pk(score[0], score[1])
                    else:
                        continue
                # 電腦點數比玩家低就加牌
                else:
                    print("玩家停止加牌\n")
                    while score[1] < score[0]:
                        self.give_poker(self.computer)
                        score[1] = self.computer.get_value("max")
                    self.player.show_card(1)
                    self.computer.show_card(0)
                    print()
                    return self.pk(score[0], score[1])
    def QA (self, message, condition):
        while True:
            user_input = input(message)
            if self.input_check(user_input, condition):
                print("請依規定輸入\n")
            else:
                break
        return user_input
    def input_check(self, _input, check):
        return True if _input not in check else False
 
if __name__ == "__main__":
    play = point21()
    play.start_game()