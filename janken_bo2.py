'''
Created on 2023/10/13

@author: t21cs023
'''
import random

def get_user_choice():
    while True:
        user_choice = input("じゃんけん：（0: グー, 1: チョキ, 2: パー）を選んでください：")
        if user_choice in ['0', '1', '2']:
            return int(user_choice)
        else:
            print("0, 1, 2のいずれかを入力してください。")

def get_computer_choice():
    return random.randint(0, 2)

def get_string(num):
    if num == 0:
        return "グー"
    elif num == 1:
        return "チョキ"
    elif num == 2:
        return "パー"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "引き分け"
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        return "あなたの勝ち"
    else:
        return "コンピュータの勝ち"

# 勝利カウンターを初期化
user_wins = 0
computer_wins = 0
rounds = 3

for _ in range(rounds):
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"あなたの選択: ",get_string(user_choice))
    print(f"コンピュータの選択: ",get_string(computer_choice))

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "あなたの勝ち":
        user_wins += 1
    elif result == "コンピュータの勝ち":
        computer_wins += 1

# 最終的な勝者を決定
if user_wins > computer_wins:
    print("最終的な勝者はあなたです！")
elif computer_wins > user_wins:
    print("最終的な勝者はコンピュータです！")
else:
    print("最終的な結果は引き分けです！")
