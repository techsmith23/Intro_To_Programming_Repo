import random

# Part 1: Implement Player Class

class Player: 

   # Set an initial starting score:
   score = 0

   # Create initial method:
   def __init__(self):
       self.my_move = None
       self.their_move = None
    
   #Store the moves of a player: 
   def record(self, my_move, their_move): 
       self.my_move = my_move
       self.their_move = their_move

# Create different subclasses of players: 

     #Asks the user what moves they would like to make: 
class HumanPlayer(Player):
     
     #Create initial method:
    def __init__(self):
        super().__init__()
        self.behaivor = 'Primary Player'

     # Create a move method: 
    def move(self): 
        while True: 
            # Get the input of the user through a different set of options
            move = input('please choose rock, paper, or scissors').lower()
            
            # Validate the users input: 
            
            if move in moves: 
                return move
            else: 
                print('Invalid response! Please Try Again.')

    
    # Go through random moves: 
class RandomPlayer(Player):
    def move(self):
        # Return random options of the moves
        return random.choice(moves)

     
class RepeatPlayer(Player):
     def move(self):
         # Play rock
         return 'rock'

     # Remembers what moves the oppent player played during the last round, and would
     # play back that move during the current round
class ReflectPlayer(Player):
    def move(self): 
        #Plays randomly if the other player has not moved
        if self.their_move is None: 
            return random.choice(moves)
        else: 
            # Return the same as the other player
            return self.their_move

     # Remembers what moves it played last round, and cycles through different moves
class CyclePlayer(Player):
     def move(self):
         if self.my_move is None: 
             return random.choice(moves)
         else: 
             index = moves.index(self.my_move) + 1
             if index ==  len(moves):
                 index = 0
             return moves[index]

 
 # Create Options To Win For Both Player 1 and 2: 

 # Player 1: 
def p1_win(one, two):
    return (

            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or
            (one == 'rock' and two == 'scissors')

    )

 #Player 2:
def p2_win(one, two):
    return (

          (one == 'paper' and two == 'scissors') or
          (one == 'rock' and two == 'paper') or
          (one == 'scissors' and two == 'rock')

    )

# Part 2: Implement Game Class: 

class Game: 
 
  # Create Initial Methods: 
    def __init__(self, player1, player2):
        
        #Define Players:
        self.player1 = player1
        self.player2 = player2
    
  # Create method for playing rounds:
    def play_round(self):
        # Create Moves:
        move1 = self.player1.move()
        move2 = self.player2.move()
       
        # Print the Moves Of The Player: 
        print(f'Player 1: {move1} Player 2: {move2}')

        # Scenario where Player 1 Wins:
        if p1_win(move1, move2) is True and p2_win(move1, move2) is False: 
            # Add points to the score each time player 1 wins: 
            self.player1.score += 1
            print('You Won!')
        
        # Scenario where Player 2 Wins: 
        elif p2_win(move1, move2) is True and p1_win(move1, move2) is False: 
           # Add points to the score each time player 2 wins:
           self.player2.score += 1
           print('Player 2 Won! You Lose!')

        # Scenario where it's a tie: 
        else: 
            print('It is a tie!')

        # Remeber the moves of the player for the score: 
        self.player1.record(move1, move2)
        self.player2.record(move1, move2) 

        print(' Here Is The Score: ')
        # Show results: 
        print(f'Player 1: {self.player1.score} | Player 2: {self.player2.score}\n')

    def play_game(self):
            print('Game Has Started!\n')
            # Each Game is 3 Rounds:
            for round in range(3):
                print(f'Round {round + 1}:')
                self.play_round()
            print('Game Over!\n\n')
            # Reset The Score: 
            self.player1.score = 0
            self.player2.score = 0
            exit(0)

#Inital Main Method: 

if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']

    behaivors = { 

        'human': HumanPlayer(),
        'reflect': ReflectPlayer(),
        'cycle': CyclePlayer(),
        'random': RandomPlayer(),
        'repeat': RepeatPlayer()

    }

    while True: 
        print('ROCK, PAPER, SCISSORS, GO!\n')
        print('Get Started! Everybody already knows the rules:\n'
              'Rock beats Scissors, Scissors beats Paper, Paper beats Rock\n'
              'Best out of 3 rounds wins!\n'        
        )

        # Let the player choose: 
        choice = input (
            'Choose your Player: (random, reflect, repeat, cycle)\n'
        ).lower()

        # Once the player chooses, the game will start: 
        if choice in behaivors:
            game = Game(behaivors['human'], behaivors[choice])
            game.play_game()
        else:
            print('Wrong player! Please Try Again.')