
class Game:
    """ 
    Custom data type to manage game and scores.
    """
  
    def __init__(self, title="Enter Game Name"):
        # Each dictionary stores a player's name and score.
        self.players = []
        self.game_title = title

    def add_player(self, name):
        """Adds player to game with score of 0."""
        player_data = {'name': name, 'score': 0}
        self.players.append(player_data)
        print(f"[SYSTEM] Added player: {name}\n")

    def update_score(self, player_name, points):
        """Updates the player score."""
        for player in self.players:
            # Player data (name, score) is accessed
            # Modifies the self.players list
            if player['name'] == player_name:
                player['score'] += points # Use += shortcut
                print(f"[SYSTEM] {player_name} = {points}\n")
                return

    def display_scores(self):
        """Displays the current scores for all players."""
        print(f"\n--- {self.game_title} Current Scores ---")
        # Sorting players by score in descending order
        sorted_players = sorted(self.players, key=lambda p: p['score'], reverse=True)
        for player in sorted_players:
            print(f"* {player['name']}: {player['score']} points")

# Front End Display and Program Flow

def main_menu(game_instance):
    """
    Handles user interaction.
    Local variables.
    """
    while True:
        print("Score Keeper Main Menu:")
        print("1. Add new player")
        print("2. Update player scores")
        print("3. View current scores")
        print("4. Exit")
        choice = input("Select (1-4): ")

        if choice == '1':
            name = input("Enter player name: ")
            game_instance.add_player(name)
        elif choice == '2':
            name = input("Enter player name to update score: ")
            try:
                points = int(input("Adjust points: "))
                game_instance.update_score(name, points)
            except ValueError:
                print("[SYSTEM] Invalid input. Please enter a number.\n")
        elif choice == '3':
            game_instance.display_scores()
        elif choice == '4':
            print("Exiting game.")
            sys.exit() # Exits the entire program
        else:
            print("[SYSTEM] Invalid choice. Please enter a number from 1 to 4.\n")

# Initialize the system
if __name__ == "__main__":
    my_game = Game("Moose")
    # Start the front end menu loop
    main_menu(my_game)
