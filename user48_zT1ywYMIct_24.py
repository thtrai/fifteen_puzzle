"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

def position_tile(puzzle, target_row, target_col, temporary_row, temporary_col):
    """Helper function. Takes a puzzle, and a temporary tile that must be posititioned\
    to target tile. Returns only the answer as a string, doesn't update any puzzle"""
    answer = ""
    if temporary_col == target_col:     ###? maybe 'and temporary_row < target_row :'
        upmoves = target_row - temporary_row
        answer += "u" * upmoves 
        answer += "lddru" * (upmoves - 1)
        answer += "ld"
            
    elif temporary_col < target_col and temporary_row == target_row:
        left_moves = target_col - temporary_col
        answer += "l"*left_moves
        answer += "urrdl" * (left_moves - 1)
        
    elif temporary_col > target_col and temporary_row == target_row:
        #"enter here"
        right_moves = temporary_col - target_col
        answer += "r" * right_moves
        answer += "ulldr" * (right_moves -1)
        answer += "ulld"
            
    elif temporary_row < target_row and temporary_col != target_col:
#            print 'pass1', answer
        if temporary_col < target_col:
            upmoves = target_row - temporary_row
            left_moves = target_col - temporary_col
            answer += "u" * upmoves + "l" * left_moves
#                print answer, ' debug 0'
#                print temporary_row
            if temporary_row == 0:
                    answer += "drrul" * (left_moves - 1)
            else:
                answer += "urrdl" * (left_moves - 1)
#                print 'pass 2'
#                print 'debug 1',answer
            answer += "dru"
#                print 'debug 2',answer
            answer += "lddru" * (upmoves -1)
            answer += "ld"
        elif temporary_col > target_col:
            upmoves = target_row - temporary_row
            right_moves = temporary_col - target_col
#                print right_moves,'right_moves'
            answer += "u" * upmoves + "r" * right_moves
#                print answer, 'debug 1'
                
            if temporary_row == 0:
                answer += "dllur" * (right_moves - 1)
            else:
                answer += "ulldr" * (right_moves - 1)
                    
#                print answer, 'debug 2'
                
            if upmoves > 1:
                answer += "dlu"
                answer += "lddru" * (upmoves -1)
            else:
                if temporary_row ==0:
                    answer += "dlu"
                else:
                    answer += "ullddru"
            answer += "ld"
    return answer

        

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        puzzle_height = self.get_height()
        puzzle_width = self.get_width()
        
        # 1st restriction
        zero_value = self.current_position(0,0)
        if zero_value != (target_row, target_col):
            return False
        
#        print 'pass 1'
        # 2nd restriction
        
        for current_row in range(target_row+1, puzzle_height):
            for current_col in range(0,puzzle_width):
                
                if self.current_position(current_row,current_col) != (current_row,current_col):
                    return False
                
#        print 'pass 2'
        # 3rd restrinction
        for current_col in range(target_col, puzzle_width-1):
            if self.current_position(target_row, current_col+1) != (target_row, current_col+1):
                return False
            
            
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, target_col),'broken puzzle'
        assert target_row > 1 and target_col > 0, 'not good straregy'
        
        answer = ""   ##delete this?
        (temporary_row, temporary_col)  = self.current_position(target_row, target_col)
#        if temporary_col == target_col:     ###? maybe 'and temporary_row < target_row :'
#            upmoves = target_row - temporary_row
#            answer += "u" * upmoves 
#            answer += "lddru" * (upmoves - 1)
#            answer += "ld"
#            
#        elif temporary_col < target_col and temporary_row == target_row:
#            left_moves = target_col - temporary_col
#            answer += "l"*left_moves
#            answer += "urrdl" * (left_moves - 1)
#            
#        elif temporary_row < target_row and temporary_col != target_col:
##            print 'pass1', answer
#            if temporary_col < target_col:
#                upmoves = target_row - temporary_row
#                left_moves = target_col - temporary_col
#                answer += "u" * upmoves + "l" * left_moves
##                print answer, ' debug 0'
##                print temporary_row
#                if temporary_row == 0:
#                    answer += "drrul" * (left_moves - 1)
#                else:
#                    answer += "urrdl" * (left_moves - 1)
##                print 'pass 2'
##                print 'debug 1',answer
#                answer += "dru"
##                print 'debug 2',answer
#                answer += "lddru" * (upmoves -1)
#                answer += "ld"
#            elif temporary_col > target_col:
#                upmoves = target_row - temporary_row
#                right_moves = temporary_col - target_col
##                print right_moves,'right_moves'
#                answer += "u" * upmoves + "r" * right_moves
##                print answer, 'debug 1'
#                
#                if temporary_row == 0:
#                    answer += "dllur" * (right_moves - 1)
#                else:
#                    answer += "ulldr" * (right_moves - 1)
#                    
##                print answer, 'debug 2'
#                
#                if upmoves > 1:
#                    answer += "dlu"
#                    answer += "lddru" * (upmoves -1)
#                else:
#                    answer += "ullddru"
#                answer += "ld"
        answer = position_tile(self, target_row, target_col, temporary_row, temporary_col)
        
        
        self.update_puzzle(answer)
        
        return answer

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        assert self.lower_row_invariant(target_row, 0), 'broken puzzle'
        
        self.update_puzzle('ur')
        
        temporary_pos  = self.current_position(target_row,0)
        #temporary_pos is the pos of the tile we want to move.
        #we define it this way, because with the "ur" move (above)
        #we may have changed the position of the tile if it was close
        #that's why it is different from 
        
        
        
        if temporary_pos == (target_row, 0):
            answer = "rr"
            self.update_puzzle(answer)
            return answer
        else:
            target_pos  = self.current_position(0,0)
            answer = position_tile(self, target_pos[0], target_pos[1], temporary_pos[0], temporary_pos[1])
        
#        print self, 'debug -1'
#        print self, 'debug 0',answer,"answer",len(answer)
        self.update_puzzle(answer)
        
        special = "ruldrdlurdluurddlur" #from homework q9
        self.update_puzzle(special)
#        print self, 'debug 1'
        ending = "rr"
        self.update_puzzle(ending)
#        print self, 'debug 2'
        
        return 'ur' + answer + special + ending
            
            

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

##### Start interactive simulation
#puz  =  Puzzle(4,4)
#puz.update_puzzle('ddruuldrdluruldrruldrrullldd')
#puz.solve_col0_tile(2)
#print puz

#puz  =  Puzzle(4,4)
#puz.update_puzzle('ddruuldrdluruldrruldrrulllddur')
#print puz
#answer = position_tile(puz, 1, 1,0,3)
#
#print answer
##puz.update_puzzle(answer)
#print puz





