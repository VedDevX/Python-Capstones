import time
import random

WELCOME_TEXT = r'''
╔════════════════════════════════════════════════════╗
║                                                    ║
║   ██████╗  ██████╗  ██████╗██╗  ██╗     ██████╗     ║
║  ██╔═══██╗██╔════╝ ██╔════╝██║ ██╔╝    ██╔═══██╗    ║
║  ██║   ██║██║  ███╗██║     █████╔╝     ██║   ██║    ║
║  ██║   ██║██║   ██║██║     ██╔═██╗     ██║   ██║    ║
║  ╚██████╔╝╚██████╔╝╚██████╗██║  ██╗ ██╗╚██████╔╝    ║
║   ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═╝ ╚═════╝     ║
║                                                    ║
║      ✊ 🤚 ✌  ROCK PAPER SCISSORS GAME  ✌ 🤚 ✊       ║
║                                                    ║
║         Test your luck. Beat the computer!         ║
║                                                    ║
╚════════════════════════════════════════════════════╝
'''

GOODBYE_TEXT = r'''
╔══════════════════════════════════════════════════╗
║                                                  ║
║   ██████╗   ██████╗   ██████╗  ██████╗ ██╗   ██╗  ║
║  ██╔═══██╗ ██╔════╝  ██╔════╝ ██╔═══██╗╚██╗ ██╔╝  ║
║  ██║   ██║ ██║  ███╗ ██║  ███╗██║   ██║ ╚████╔╝   ║
║  ██║   ██║ ██║   ██║ ██║   ██║██║   ██║  ╚██╔╝    ║
║  ╚██████╔╝ ╚██████╔╝ ╚██████╔╝╚██████╔╝   ██║     ║
║   ╚═════╝   ╚═════╝   ╚═════╝  ╚═════╝    ╚═╝     ║
║                                                  ║
║         👋 Thanks for playing. See you soon!      ║
║                                                  ║
╚══════════════════════════════════════════════════╝
'''

ROCK = r'''
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = r'''
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = r'''
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Show Welcome
time.sleep(1)
print(WELCOME_TEXT)
time.sleep(1.5)

CHOICES = [ROCK, PAPER, SCISSORS]
CHOICE_NAMES = ["Rock ✊", "Paper 🤚", "Scissors ✌"]

while True:
    PLAYER_SCORE = 0
    COMPUTER_SCORE = 0

    try:
        POINTS = int(input("\n🎯 Enter how many points you want to play till: "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue

    for i in range(1, POINTS + 1):
        print(f"\n🎮 Round {i}/{POINTS}")
        print("Choose your move: 0 - Rock ✊ | 1 - Paper 🤚 | 2 - Scissors ✌")

        try:
            USER_CHOICE = int(input("👉 Your Choice (0/1/2): "))
            if USER_CHOICE not in [0, 1, 2]:
                raise ValueError
        except ValueError:
            print("⚠️ Invalid input! Please enter 0, 1, or 2.")
            continue

        COMPUTER_CHOICE = random.randint(0, 2)

        print("\n🧑 You chose:")
        print(CHOICES[USER_CHOICE])
        print(f"➡️ {CHOICE_NAMES[USER_CHOICE]}")

        print("🤖 Computer chose:")
        print(CHOICES[COMPUTER_CHOICE])
        print(f"➡️ {CHOICE_NAMES[COMPUTER_CHOICE]}")

        if USER_CHOICE == COMPUTER_CHOICE:
            print("🤝 It's a Tie!")
        elif (USER_CHOICE == 0 and COMPUTER_CHOICE == 2) or \
             (USER_CHOICE == 1 and COMPUTER_CHOICE == 0) or \
             (USER_CHOICE == 2 and COMPUTER_CHOICE == 1):
            print("🎉 You Win this round!")
            PLAYER_SCORE += 1
        else:
            print("💻 Computer Wins this round!")
            COMPUTER_SCORE += 1

        # Scoreboard after each round
        print("\n📊 Current Scoreboard:")
        print(f"🧑 You: {PLAYER_SCORE} | 🤖 Computer: {COMPUTER_SCORE}")
        print("────────────────────────────────────────")

    # Final Round Winner
    print("\n🏁 Round Over!")
    if PLAYER_SCORE > COMPUTER_SCORE:
        print("🏆 You are the Winner of this Round!")
    elif PLAYER_SCORE == COMPUTER_SCORE:
        print("😐 It's a Tie!")
    else:
        print("👾 Computer Wins the Round!")

    # Ask to play again
    PLAY_AGAIN = input("\n🔁 Do you want to play another round? (yes/no): ").strip().lower()
    if PLAY_AGAIN != "yes":
        print("\n" + GOODBYE_TEXT)
        break
