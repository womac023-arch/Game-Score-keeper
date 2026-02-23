
class Game:
    """
    A custom data type (class) to manage game state and scores.
    Variables within the class (self.players, self.game_title) have a lifetime
    tied to the Game object instance.
    """
    def __init__(self, title="Generic Game"):
        # self.players is a list of dictionaries, demonstrating fundamental data types
        # Each dictionary stores a player's 'name' (string) and 'score' (integer).
        self.players = []
        self.game_title = title

    def add_player(self, name):
        """Adds a new player to the game with an initial score of 0."""
        player_data = {'name': name, 'score': 0}
        self.players.append(player_data)
        print(f"[SYSTEM] Added player: {name}\n")

    def update_score(self, player_name, points):
        """Updates the score for a specific player."""
        for player in self.players:
            # Player data (name, score) is local to the function's loop scope
            # but modifies the class-level self.players list.
            if player['name'] == player_name:
                player['score'] += points # Use += shortcut
                print(f"[SYSTEM] {player_name}'s score updated by {points} points.\n")
                return
        print(f"[SYSTEM] Error: Player '{player_name}' not found.\n")

    def display_scores(self):
        """Displays the current scores for all players."""
        print(f"\n--- {self.game_title} Current Scores ---")
        # Sorting players by score in descending order
        sorted_players = sorted(self.players, key=lambda p: p['score'], reverse=True)
        for player in sorted_players:
            print(f"* {player['name']}: {player['score']} points")
        print("--------------------------------------\n")

# --- Front End Display and Program Flow (Text-based Console) ---

def main_menu(game_instance):
    """
    Handles user interaction through a text-based console interface.
    Local variables (e.g., choice, name) have a lifetime within this function's execution.
    """
    while True:
        print("Welcome to the Score Keeper System Main Menu:")
        print("1. Add a new player")
        print("2. Update a player's score")
        print("3. View current scores")
        print("4. Exit program")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter player name: ")
            game_instance.add_player(name)
        elif choice == '2':
            name = input("Enter player name to update score: ")
            try:
                points = int(input("Enter points to add/subtract: "))
                game_instance.update_score(name, points)
            except ValueError:
                print("[SYSTEM] Invalid input. Please enter a number.\n")
        elif choice == '3':
            game_instance.display_scores()
        elif choice == '4':
            print("Exiting game score system. Goodbye!")
            sys.exit() # Exits the entire program
        else:
            print("[SYSTEM] Invalid choice. Please enter a number from 1 to 4.\n")

# Initialize the system
if __name__ == "__main__":
    # The 'my_game' object is a global variable with a lifetime for the program duration.
    my_game = Game("Ultimate Tic-Tac-Toe")
    # Start the front end menu loop
    main_menu(my_game)
