import random

def play():
    user_choice = input("What's your choice? [r] for rock, [p] for paper, [s] for scissor: ")
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        return "It's a tie!"
    
    if is_win(user_choice, computer_choice):
        return "You won!"

    return "You lost!"

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
if __name__ == "__main__":
    print(play())