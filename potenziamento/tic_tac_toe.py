import math
import random

class TicTacToeAI:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.human = 'X'
        self.ai = 'O'
    
    def display_board(self):
        print("\n   0   1   2")
        for i in range(3):
            print(f"{i}  {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]} ")
            if i < 2:
                print("  -----------")
    
    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False
    
    def undo_move(self, row, col):
        self.board[row][col] = ' '
    
    def check_winner(self):
        # Controlla righe
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Controlla colonne
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Controlla diagonali
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def get_empty_cells(self):
        cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    cells.append((i, j))
        return cells
    
    def minimax(self, depth, is_maximizing):
        winner = self.check_winner()
        
        # Condizioni terminali
        if winner == self.ai:
            return 10 - depth  # AI vince
        elif winner == self.human:
            return depth - 10  # Player vince
        elif self.is_board_full():
            return 0  # Pareggio
        
        if is_maximizing:
            best_score = -math.inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = self.ai
                score = self.minimax(depth + 1, False)
                self.board[row][col] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for row, col in self.get_empty_cells():
                self.board[row][col] = self.human
                score = self.minimax(depth + 1, True)
                self.board[row][col] = ' '
                best_score = min(score, best_score)
            return best_score
    
    def get_ai_move(self):
        best_score = -math.inf
        best_moves = []
        
        # Trova tutte le mosse con il punteggio migliore
        for row, col in self.get_empty_cells():
            self.board[row][col] = self.ai
            score = self.minimax(0, False)
            self.board[row][col] = ' '
            
            if score > best_score:
                best_score = score
                best_moves = [(row, col)]
            elif score == best_score:
                best_moves.append((row, col))
        
        # Se ci sono più mosse ottime, scegline una a caso per variare il gioco
        return random.choice(best_moves) if best_moves else None
    
    def play(self):
        print("=== TIC TAC TOE vs AI ===")
        print("Tu sei X, l'AI è O")
        print("L'AI usa l'algoritmo Minimax - non può perdere!")
        print("Inserisci le coordinate come: riga colonna esempio: (0-2)")
        print("Prova a ottenere almeno un pareggio!")
        
        # Chiedi chi inizia
        while True:
            first = input("\nVuoi iniziare tu? (s/n): ").lower()
            if first in ['s', 'si', 'y', 'yes']:
                human_turn = True
                break
            elif first in ['n', 'no']:
                human_turn = False
                break
            else:
                print("Rispondi con 's' o 'n'")
        
        game_count = 0
        
        while True:
            game_count += 1
            print(f"\n{'='*30}\nPARTITA {game_count}\n{'='*30}")
            
            current_human_turn = human_turn
            
            while True:
                self.display_board()
                
                if current_human_turn:
                    print(f"\nIl tuo turno (X)")
                    try:
                        move = input("Inserisci la tua mossa (riga colonna): ").split()
                        if len(move) != 2:
                            print("Inserisci esattamente due numeri separati da spazio!")
                            continue
                        
                        row, col = int(move[0]), int(move[1])
                        
                        if row < 0 or row > 2 or col < 0 or col > 2:
                            print("Le coordinate devono essere tra 0 e 2!")
                            continue
                        
                        if not self.make_move(row, col, self.human):
                            print("Quella posizione è già occupata!")
                            continue
                        
                    except ValueError:
                        print("Inserisci solo numeri validi!")
                        continue
                    except KeyboardInterrupt:
                        print("\n\nGioco interrotto. Arrivederci!")
                        return
                
                else:
                    print("\nTurno dell'AI (O)...")
                    print("L'AI sta calcolando la mossa ottimale...")
                    ai_move = self.get_ai_move()
                    if ai_move:
                        row, col = ai_move
                        self.make_move(row, col, self.ai)
                        print(f"L'AI ha giocato in posizione ({row}, {col})")
                
                # Controlla se c'è un vincitore
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    if winner == self.human:
                        print(f"\n INCREDIBILE! Hai vinto! (hai barato!!!)")
                        print("Hai battuto l'AI! (Questo non dovrebbe accadere...)")
                    else:
                        print(f"\n L'AI ha vinto! ")
                        print("Come previsto, l'AI è imbattibile!")
                    break
                
                if self.is_board_full():
                    self.display_board()
                    print("\n Pareggio! ")
                    print("Ottimo lavoro umanoide! Ottenere un pareggio contro di me è già un successo!")
                    break
                
                current_human_turn = not current_human_turn
            
            # Chiedi se giocare ancora
            while True:
                play_again = input("\nVuoi giocare ancora? (s/n): ").lower()
                if play_again in ['s', 'si', 'y', 'yes']:
                    # Reset del tabellone
                    self.board = [[' ' for _ in range(3)] for _ in range(3)]
                    # Alterna chi inizia
                    human_turn = not human_turn
                    break
                elif play_again in ['n', 'no']:
                    print(f"\nGrazie per aver giocato! Hai completato {game_count} partite.")
                    print("Ricorda: contro Minimax, il pareggio è già una vittoria!")
                    return
                else:
                    print("Rispondi con 's' o 'n'")

# Avvia il gioco
if __name__ == "__main__":
    game = TicTacToeAI()
    game.play()