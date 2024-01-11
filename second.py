import random

class DiceRollGame:
    def __init__(self):
        self.user_name = ""
        self.user_score = 0
        self.computer_score = 0

    def get_user_name(self):
        self.user_name = input("Enter your name: ")

    def roll_dice(self):
        return random.randint(1, 6)

    def play_round(self):
        user_roll = self.roll_dice()
        computer_roll = self.roll_dice()

        print(f"{self.user_name}'s roll: {user_roll}")
        print(f"Computer's roll: {computer_roll}")

        if user_roll > computer_roll:
            self.user_score += 1
            print(f"{self.user_name} wins this round!")
        elif user_roll < computer_roll:
            self.computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")

    def display_scores(self):
        print(f"\nScores - {self.user_name}: {self.user_score} | Computer: {self.computer_score}\n")

    def play_game(self):
        self.get_user_name()
        rounds = int(input("Enter the number of rounds: "))

        for _ in range(rounds):
            self.play_round()
            self.display_scores()

        if self.user_score > self.computer_score:
            print(f"{self.user_name} wins the game!")
        elif self.user_score < self.computer_score:
            print("Computer wins the game!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game = DiceRollGame()
    game.play_game()