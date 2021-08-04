""""Test Cases For Fifteen Puzzle, Principles of Computing part 2"""

import unittest

#import user48_YwsbqxMFSF_28 of 29 as program
import user48_zT1ywYMIct_24 as program



class mytest(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(str(program.Puzzle(4,4)), "[0, 1, 2, 3]\n[4, 5, 6, 7]\n[8, 9, 10, 11]\n[12, 13, 14, 15]\n")
    def test_check(self):
        self.assertEqual(program.Puzzle(4,4).lower_row_invariant(0,0), True)
        
    def test_solve_interior_13_at_top_right(self):
        puz = program.Puzzle(4,4)
        puz.update_puzzle("ddrdluurdrulurdrulldldrd")
#        print puz
#        self.assertEqual(puz.lower_row_invariant(3,1), True)
        
        puz.solve_interior_tile(3,1)
        
        self.assertEqual(puz.lower_row_invariant(3,0), True)
        
    def test_solve_interior_13_at_mid_right(self):
        puz = program.Puzzle(4,4)
        puz.update_puzzle('ddrdluurrdlurrdlurdlllrd')
        
#        print puz
        zp = puz.current_position(0,0)    #zp : zero_position
        puz.solve_interior_tile(zp[0],zp[1])
        
#        print puz
        
        self.assertEqual(puz.lower_row_invariant(zp[0], zp[1] - 1), True)
        
    def test_solve_interior_13_no_space(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rdddluurrdlurrdlld')
#        print puz
        zp = puz.current_position(0,0)    #zp : zero_position
        puz.solve_interior_tile(zp[0],zp[1])
        
#        print puz
        
        self.assertEqual(puz.lower_row_invariant(zp[0], zp[1] - 1), True)
        
        
        
    def test_solve_interior_close_ur(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrdlddluurrdld')
#        print puz
        zp = puz.current_position(0,0)    #zp : zero_position
        puz.solve_interior_tile(zp[0],zp[1])
        
#        print puz
        
        self.assertEqual(puz.lower_row_invariant(zp[0], zp[1] - 1), True)

    def test_solve_interior_u(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('ddrd')
#        print puz
        zp = puz.current_position(0,0)    #zp : zero_position
        puz.solve_interior_tile(zp[0],zp[1])
        
#        print puz
        
        self.assertEqual(puz.lower_row_invariant(zp[0], zp[1] - 1), True)
        
    def test_solve_interior_top_left(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rdddluurdluurdlurddd')
#        print puz
        zp = puz.current_position(0,0)    #zp : zero_position
        puz.solve_interior_tile(zp[0],zp[1])
        
#        print puz
        
        self.assertEqual(puz.lower_row_invariant(zp[0], zp[1] - 1), True)
        
    def test_solve_interior_just_left(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rddldr')
#        print puz
        zp = puz.current_position(0,0)    #zp : zero_position
        puz.solve_interior_tile(zp[0],zp[1])
        
#        print puz
        
        self.assertEqual(puz.lower_row_invariant(zp[0], zp[1] - 1), True)

    def test_solve_col0_above_easy(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('ddd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)

    def test_solve_col0_top_right(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('dddrulurddlurrulurdrulllddd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)
    
    def test_solve_col0_mid_right(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('dddrulurrdluurrddlurdlldlud')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)
    
    def test_solve_col0_low_right(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('dddrulurrdlurrdlldl')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)

    def test_solve_col0_above_right(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('dddrulurddluruldudd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)
    
    def test_solve_col0_top_same(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('dddruuldrdlurulurdldd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)

    def test_solve_col0_top_left(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('dddruuldrdlurulurdldduuurdldd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)

    def test_solve_col0_second_row_top_left(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('ddruuldrdl')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)

    def test_solve_col0_second_row_top_same(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('ddruuldrdluruldd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)


    
    def test_solve_col0_second_row_right(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('drdluurddluurrdluldrulddruld')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)

    def test_solve_col0_second_just_above(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('ddruuldrdluruldruldd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)

    
    
    def test_solve_col0_second_row_mid_right(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('ddruuldrdluruldrurdlurrdllld')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)
   
    def test_solve_col0_second_row_top_right(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('ddruuldrdluruldrrulldd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)


    

    def test_solve_col0_second_row_top_right_corner(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('ddruuldrdluruldrruldrrullldd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_col0_tile(zp[0])
        
#        print puz
        self.assertEqual(puz.lower_row_invariant(zp[0] -1 , puz.get_width() - 1), True)


    
    
    
    
    
unittest.main()
