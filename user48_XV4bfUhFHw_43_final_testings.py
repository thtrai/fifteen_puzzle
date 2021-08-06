""""Test Cases For Fifteen Puzzle, Principles of Computing part 2"""

import unittest

#import user48_YwsbqxMFSF_28 of 29 as program
#import user48_zT1ywYMIct_29 as program
#import user48_bLKoWFuqo4_38 as program
import user48_0CDJq4DzYU_1 as program



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
###############################################################################
#######################  PHASE 2  #############################################

    def test_solve_row1_invariant_first_zero(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rdlurrdlrurdlurdlurdllurrdluldrurdlurdlr')
        
        #print puz
        zp = puz.current_position(0,0) #zp : zero_position
        self.assertEqual(puz.row1_invariant(zp[1]), True)

    def test_solve_row1_invariant_first_one(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrldlrurdlurd')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
        self.assertEqual(puz.row1_invariant(zp[1]), True)
#    
    def test_solve_row1_invariant_false(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rdrurdluldrurdlurdl')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
        self.assertEqual(puz.row1_invariant(zp[1]), False)
#    

#
    def test_solve_row1_tile_secondcol(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrdlurdlrrulldrr')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row1_tile(zp[1])
#        print puz
        self.assertEqual(puz.row0_invariant(zp[1]), True)

    def test_solve_row1_tile_easy(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrdlurdlr')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row1_tile(zp[1])
#        print puz
        self.assertEqual(puz.row0_invariant(zp[1]), True)

    def test_solve_row1_tile_faraway(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrrdlurdllurdllurdrr')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row1_tile(zp[1])
#        print puz
        self.assertEqual(puz.row0_invariant(zp[1]), True)
    
    
    def test_solve_row1_tile_same_row(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('drrrulldrulldrrr')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row1_tile(zp[1])
#        print puz
        self.assertEqual(puz.row0_invariant(zp[1]), True)
    
    def test_solve_row1_tile_next_to_edge(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrdlurdlr')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row1_tile(zp[1])
#        print puz
        self.assertEqual(puz.row0_invariant(zp[1]), True)

    
    def test_solve_row0_tile_easy(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrr')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row0_tile(zp[1])
#        print puz
        self.assertEqual(puz.row1_invariant(zp[1]-1), True)

    def test_solve_row0_tile_harder(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrrdluldrudru')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row0_tile(zp[1])
#        print puz
        self.assertEqual(puz.row1_invariant(zp[1]-1), True)
    
    def test_solve_row0_tile_harder2(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('durrdluldrruldlurr')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row0_tile(zp[1])
#        print puz
        self.assertEqual(puz.row1_invariant(zp[1]-1), True)
    
    def test_solve_row0_tile_hardest(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrrdluldrudrullldruldrrur')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zprrrdluldrruldlrulldrlrrur
        puz.solve_row0_tile(zp[1])
#        print puz
        self.assertEqual(puz.row1_invariant(zp[1]-1), True)

    def test_solve_row0_tile_hardest2(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrrdluldrruldlrulldrlrrur')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row0_tile(zp[1])
#        print puz
        self.assertEqual(puz.row1_invariant(zp[1]-1), True)
    

    def test_solve_row0_tile_hardest3(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrdluldrru')
#        print puz
        zp = puz.current_position(0,0) #zp : zero_position
#        print zp
        puz.solve_row0_tile(zp[1])
#        print puz
        self.assertEqual(puz.row1_invariant(zp[1]-1), True)

#    def test_solve2x2_broken(self):
#        puz  =  program.Puzzle(4,4)
#        puz.update_puzzle('r')
##        print puz
#        zp = puz.current_position(0,0) #zp : zero_position
##        print zp
##        print puz
#        self.assertEqual(puz.solve_2x2(), False)
    
    
    def test_solve2x2_one_right(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rd')
#        print puz
        puz.solve_2x2()
#        print puz
        self.assertEqual(puz.row0_invariant(0), True)
    
    def test_solve2x2_one_left(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('dr')
#        print puz
        puz.solve_2x2()
#        print puz
        self.assertEqual(puz.row0_invariant(0), True)
                         
    def test_solve2x2_middle(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rdlurd')
#        print puz
        puz.solve_2x2()
#        print puz
        self.assertEqual(puz.row0_invariant(0), True)
    
    
    
##################  last function  #############

    def test_solve_already_solved(self):
        puz  =  program.Puzzle(4,4)
#        print puz
        answer = puz.solve_puzzle()
#        print puz
        self.assertEqual(answer, "")
    
    def test_solve_half_solved(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rdldrururdll')
#        print puz
        answer = puz.solve_puzzle()
#        print puz
        self.assertEqual(puz.row0_invariant(0),True)
#    
    
    def test_solve_one_tile_ready(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('ddrrdlurruldlluurrr')
#        print puz
        answer = puz.solve_puzzle()
#        print puz
        self.assertEqual(puz.row0_invariant(0),True)

    def test_solve_totally_scrambled(self):
        puz  =  program.Puzzle(4,4)
        puz.update_puzzle('rrrdddluruldldrrulluluddd')
#        print puz
        answer = puz.solve_puzzle()
#        print puz
        self.assertEqual(puz.row0_invariant(0),True)
    

    
unittest.main()