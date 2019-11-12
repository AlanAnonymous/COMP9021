#!/usr/bin/env python3

# more test cases (including special cases)


from maze import *



def test():

    '''
    >>> maze = Maze('Ricky_test_0.txt')
    >>> maze.analyse()
    The maze has 28 gates.
    The maze has 12 sets of walls that are all connected.
    The maze has 11 inaccessible inner points.
    The maze has 12 accessible areas.
    The maze has 16 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_1.txt')
    >>> maze.analyse()
    The maze has 54 gates.
    The maze has 30 sets of walls that are all connected.
    The maze has 161 inaccessible inner points.
    The maze has 22 accessible areas.
    The maze has 72 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_2.txt')
    >>> maze.analyse()
    The maze has 38 gates.
    The maze has 20 sets of walls that are all connected.
    The maze has 29 inaccessible inner points.
    The maze has 16 accessible areas.
    The maze has 37 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_3.txt')
    >>> maze.analyse()
    The maze has 64 gates.
    The maze has 50 sets of walls that are all connected.
    The maze has 226 inaccessible inner points.
    The maze has 28 accessible areas.
    The maze has 133 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_4.txt')
    >>> maze.analyse()
    The maze has 28 gates.
    The maze has 15 sets of walls that are all connected.
    The maze has 25 inaccessible inner points.
    The maze has 15 accessible areas.
    The maze has 44 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_5.txt')
    >>> maze.analyse()
    The maze has 32 gates.
    The maze has 30 sets of walls that are all connected.
    The maze has 31 inaccessible inner points.
    The maze has 13 accessible areas.
    The maze has 49 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_6.txt')
    >>> maze.analyse()
    The maze has 56 gates.
    The maze has 53 sets of walls that are all connected.
    The maze has 132 inaccessible inner points.
    The maze has 21 accessible areas.
    The maze has 103 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_7.txt')
    >>> maze.analyse()
    The maze has 36 gates.
    The maze has 20 sets of walls that are all connected.
    The maze has 89 inaccessible inner points.
    The maze has 13 accessible areas.
    The maze has 51 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_8.txt')
    >>> maze.analyse()
    The maze has 11 gates.
    The maze has 2 sets of walls that are all connected.
    The maze has 6 inaccessible inner points.
    The maze has 7 accessible areas.
    The maze has 5 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_9.txt')
    >>> maze.analyse()
    The maze has 46 gates.
    The maze has 32 sets of walls that are all connected.
    The maze has 38 inaccessible inner points.
    The maze has 14 accessible areas.
    The maze has 42 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_10.txt')
    >>> maze.analyse()
    The maze has 54 gates.
    The maze has 44 sets of walls that are all connected.
    The maze has 153 inaccessible inner points.
    The maze has 25 accessible areas.
    The maze has 99 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_11.txt')
    >>> maze.analyse()
    The maze has 36 gates.
    The maze has 18 sets of walls that are all connected.
    The maze has 15 inaccessible inner points.
    The maze has 10 accessible areas.
    The maze has 20 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_12.txt')
    >>> maze.analyse()
    The maze has 28 gates.
    The maze has 8 sets of walls that are all connected.
    The maze has 12 inaccessible inner points.
    The maze has 15 accessible areas.
    The maze has 12 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_13.txt')
    >>> maze.analyse()
    The maze has 51 gates.
    The maze has 39 sets of walls that are all connected.
    The maze has 86 inaccessible inner points.
    The maze has 23 accessible areas.
    The maze has 86 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_14.txt')
    >>> maze.analyse()
    The maze has 7 gates.
    The maze has 2 sets of walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has 3 accessible areas.
    The maze has accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_15.txt')
    >>> maze.analyse()
    The maze has 56 gates.
    The maze has 41 sets of walls that are all connected.
    The maze has 67 inaccessible inner points.
    The maze has 16 accessible areas.
    The maze has 74 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_16.txt')
    >>> maze.analyse()
    The maze has 59 gates.
    The maze has 32 sets of walls that are all connected.
    The maze has 185 inaccessible inner points.
    The maze has 32 accessible areas.
    The maze has 112 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_17.txt')
    >>> maze.analyse()
    The maze has 31 gates.
    The maze has 16 sets of walls that are all connected.
    The maze has 75 inaccessible inner points.
    The maze has 15 accessible areas.
    The maze has 49 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_18.txt')
    >>> maze.analyse()
    The maze has 44 gates.
    The maze has 31 sets of walls that are all connected.
    The maze has 74 inaccessible inner points.
    The maze has 18 accessible areas.
    The maze has 62 sets of accessible cul-de-sacs that are all connected.
    The maze has 5 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_19.txt')
    >>> maze.analyse()
    The maze has 59 gates.
    The maze has 39 sets of walls that are all connected.
    The maze has 211 inaccessible inner points.
    The maze has 28 accessible areas.
    The maze has 127 sets of accessible cul-de-sacs that are all connected.
    The maze has 6 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_20.txt')
    >>> maze.analyse()
    The maze has 48 gates.
    The maze has 29 sets of walls that are all connected.
    The maze has 124 inaccessible inner points.
    The maze has 24 accessible areas.
    The maze has 92 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_21.txt')
    >>> maze.analyse()
    The maze has 11 gates.
    The maze has 3 sets of walls that are all connected.
    The maze has 2 inaccessible inner points.
    The maze has 6 accessible areas.
    The maze has 5 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_22.txt')
    >>> maze.analyse()
    The maze has 39 gates.
    The maze has 22 sets of walls that are all connected.
    The maze has 55 inaccessible inner points.
    The maze has 21 accessible areas.
    The maze has 61 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_23.txt')
    >>> maze.analyse()
    The maze has 30 gates.
    The maze has 10 sets of walls that are all connected.
    The maze has a unique inaccessible inner point.
    The maze has 17 accessible areas.
    The maze has 11 sets of accessible cul-de-sacs that are all connected.
    The maze has 5 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_24.txt')
    >>> maze.analyse()
    The maze has 59 gates.
    The maze has 54 sets of walls that are all connected.
    The maze has 111 inaccessible inner points.
    The maze has 17 accessible areas.
    The maze has 108 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_25.txt')
    >>> maze.analyse()
    The maze has 46 gates.
    The maze has 34 sets of walls that are all connected.
    The maze has 62 inaccessible inner points.
    The maze has 23 accessible areas.
    The maze has 92 sets of accessible cul-de-sacs that are all connected.
    The maze has 8 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_26.txt')
    >>> maze.analyse()
    The maze has 27 gates.
    The maze has 8 sets of walls that are all connected.
    The maze has 13 inaccessible inner points.
    The maze has 12 accessible areas.
    The maze has 19 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_27.txt')
    >>> maze.analyse()
    The maze has 47 gates.
    The maze has 26 sets of walls that are all connected.
    The maze has 37 inaccessible inner points.
    The maze has 19 accessible areas.
    The maze has 78 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_28.txt')
    >>> maze.analyse()
    The maze has 49 gates.
    The maze has 38 sets of walls that are all connected.
    The maze has 89 inaccessible inner points.
    The maze has 20 accessible areas.
    The maze has 102 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_29.txt')
    >>> maze.analyse()
    The maze has 3 gates.
    The maze has 2 sets of walls that are all connected.
    The maze has a unique inaccessible inner point.
    The maze has 2 accessible areas.
    The maze has 2 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_30.txt')
    >>> maze.analyse()
    The maze has 36 gates.
    The maze has 15 sets of walls that are all connected.
    The maze has 16 inaccessible inner points.
    The maze has 10 accessible areas.
    The maze has 21 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_31.txt')
    >>> maze.analyse()
    The maze has 25 gates.
    The maze has 10 sets of walls that are all connected.
    The maze has 23 inaccessible inner points.
    The maze has 11 accessible areas.
    The maze has 17 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_32.txt')
    >>> maze.analyse()
    The maze has 40 gates.
    The maze has 21 sets of walls that are all connected.
    The maze has 55 inaccessible inner points.
    The maze has 13 accessible areas.
    The maze has 47 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_33.txt')
    >>> maze.analyse()
    The maze has 20 gates.
    The maze has 7 sets of walls that are all connected.
    The maze has 2 inaccessible inner points.
    The maze has 8 accessible areas.
    The maze has 9 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_34.txt')
    >>> maze.analyse()
    The maze has 65 gates.
    The maze has 52 sets of walls that are all connected.
    The maze has 213 inaccessible inner points.
    The maze has 40 accessible areas.
    The maze has 183 sets of accessible cul-de-sacs that are all connected.
    The maze has 6 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_35.txt')
    >>> maze.analyse()
    The maze has 26 gates.
    The maze has 9 sets of walls that are all connected.
    The maze has 30 inaccessible inner points.
    The maze has 14 accessible areas.
    The maze has 28 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_36.txt')
    >>> maze.analyse()
    The maze has 54 gates.
    The maze has 34 sets of walls that are all connected.
    The maze has 127 inaccessible inner points.
    The maze has 22 accessible areas.
    The maze has 98 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_37.txt')
    >>> maze.analyse()
    The maze has 42 gates.
    The maze has 32 sets of walls that are all connected.
    The maze has 10 inaccessible inner points.
    The maze has 13 accessible areas.
    The maze has 30 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_38.txt')
    >>> maze.analyse()
    The maze has 39 gates.
    The maze has 18 sets of walls that are all connected.
    The maze has 14 inaccessible inner points.
    The maze has 15 accessible areas.
    The maze has 25 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_39.txt')
    >>> maze.analyse()
    The maze has 36 gates.
    The maze has 18 sets of walls that are all connected.
    The maze has 13 inaccessible inner points.
    The maze has 13 accessible areas.
    The maze has 24 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_40.txt')
    >>> maze.analyse()
    The maze has 37 gates.
    The maze has 31 sets of walls that are all connected.
    The maze has 16 inaccessible inner points.
    The maze has 10 accessible areas.
    The maze has 37 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_41.txt')
    >>> maze.analyse()
    The maze has 53 gates.
    The maze has 48 sets of walls that are all connected.
    The maze has 155 inaccessible inner points.
    The maze has 25 accessible areas.
    The maze has 132 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_42.txt')
    >>> maze.analyse()
    The maze has 27 gates.
    The maze has 7 sets of walls that are all connected.
    The maze has 3 inaccessible inner points.
    The maze has 15 accessible areas.
    The maze has 11 sets of accessible cul-de-sacs that are all connected.
    The maze has 6 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_43.txt')
    >>> maze.analyse()
    The maze has 46 gates.
    The maze has 23 sets of walls that are all connected.
    The maze has 117 inaccessible inner points.
    The maze has 21 accessible areas.
    The maze has 71 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_44.txt')
    >>> maze.analyse()
    The maze has 53 gates.
    The maze has 27 sets of walls that are all connected.
    The maze has 148 inaccessible inner points.
    The maze has 25 accessible areas.
    The maze has 77 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_45.txt')
    >>> maze.analyse()
    The maze has 35 gates.
    The maze has 16 sets of walls that are all connected.
    The maze has 25 inaccessible inner points.
    The maze has 14 accessible areas.
    The maze has 39 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_46.txt')
    >>> maze.analyse()
    The maze has 45 gates.
    The maze has 39 sets of walls that are all connected.
    The maze has 96 inaccessible inner points.
    The maze has 18 accessible areas.
    The maze has 75 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_47.txt')
    >>> maze.analyse()
    The maze has 47 gates.
    The maze has 24 sets of walls that are all connected.
    The maze has 90 inaccessible inner points.
    The maze has 22 accessible areas.
    The maze has 87 sets of accessible cul-de-sacs that are all connected.
    The maze has 5 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_48.txt')
    >>> maze.analyse()
    The maze has 46 gates.
    The maze has 42 sets of walls that are all connected.
    The maze has 138 inaccessible inner points.
    The maze has 17 accessible areas.
    The maze has 87 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_49.txt')
    >>> maze.analyse()
    The maze has 13 gates.
    The maze has 4 sets of walls that are all connected.
    The maze has 21 inaccessible inner points.
    The maze has 7 accessible areas.
    The maze has 8 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_50.txt')
    >>> maze.analyse()
    The maze has 46 gates.
    The maze has 29 sets of walls that are all connected.
    The maze has 118 inaccessible inner points.
    The maze has 23 accessible areas.
    The maze has 90 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_51.txt')
    >>> maze.analyse()
    The maze has 18 gates.
    The maze has 8 sets of walls that are all connected.
    The maze has a unique inaccessible inner point.
    The maze has 8 accessible areas.
    The maze has 12 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_52.txt')
    >>> maze.analyse()
    The maze has 21 gates.
    The maze has 14 sets of walls that are all connected.
    The maze has 18 inaccessible inner points.
    The maze has 6 accessible areas.
    The maze has 17 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_53.txt')
    >>> maze.analyse()
    The maze has 32 gates.
    The maze has 14 sets of walls that are all connected.
    The maze has 38 inaccessible inner points.
    The maze has 17 accessible areas.
    The maze has 28 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_54.txt')
    >>> maze.analyse()
    The maze has 52 gates.
    The maze has 26 sets of walls that are all connected.
    The maze has 47 inaccessible inner points.
    The maze has 16 accessible areas.
    The maze has 57 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_55.txt')
    >>> maze.analyse()
    The maze has 49 gates.
    The maze has 27 sets of walls that are all connected.
    The maze has 57 inaccessible inner points.
    The maze has 15 accessible areas.
    The maze has 54 sets of accessible cul-de-sacs that are all connected.
    The maze has 5 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_56.txt')
    >>> maze.analyse()
    The maze has 29 gates.
    The maze has 12 sets of walls that are all connected.
    The maze has 2 inaccessible inner points.
    The maze has 11 accessible areas.
    The maze has 11 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_57.txt')
    >>> maze.analyse()
    The maze has 32 gates.
    The maze has 18 sets of walls that are all connected.
    The maze has 33 inaccessible inner points.
    The maze has 13 accessible areas.
    The maze has 42 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_58.txt')
    >>> maze.analyse()
    The maze has 57 gates.
    The maze has 39 sets of walls that are all connected.
    The maze has 284 inaccessible inner points.
    The maze has 28 accessible areas.
    The maze has 115 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_59.txt')
    >>> maze.analyse()
    The maze has 40 gates.
    The maze has 24 sets of walls that are all connected.
    The maze has 156 inaccessible inner points.
    The maze has 22 accessible areas.
    The maze has 71 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_60.txt')
    >>> maze.analyse()
    The maze has 22 gates.
    The maze has 18 sets of walls that are all connected.
    The maze has 36 inaccessible inner points.
    The maze has 9 accessible areas.
    The maze has 48 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_61.txt')
    >>> maze.analyse()
    The maze has 39 gates.
    The maze has 37 sets of walls that are all connected.
    The maze has 103 inaccessible inner points.
    The maze has 17 accessible areas.
    The maze has 83 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_62.txt')
    >>> maze.analyse()
    The maze has 46 gates.
    The maze has 34 sets of walls that are all connected.
    The maze has 137 inaccessible inner points.
    The maze has 22 accessible areas.
    The maze has 78 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_63.txt')
    >>> maze.analyse()
    The maze has 58 gates.
    The maze has 35 sets of walls that are all connected.
    The maze has 135 inaccessible inner points.
    The maze has 22 accessible areas.
    The maze has 62 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_64.txt')
    >>> maze.analyse()
    The maze has 19 gates.
    The maze has 12 sets of walls that are all connected.
    The maze has 11 inaccessible inner points.
    The maze has 7 accessible areas.
    The maze has 16 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_65.txt')
    >>> maze.analyse()
    The maze has 59 gates.
    The maze has 37 sets of walls that are all connected.
    The maze has 133 inaccessible inner points.
    The maze has 24 accessible areas.
    The maze has 85 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_66.txt')
    >>> maze.analyse()
    The maze has 39 gates.
    The maze has 21 sets of walls that are all connected.
    The maze has 53 inaccessible inner points.
    The maze has 16 accessible areas.
    The maze has 61 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_67.txt')
    >>> maze.analyse()
    The maze has 28 gates.
    The maze has 8 sets of walls that are all connected.
    The maze has a unique inaccessible inner point.
    The maze has 9 accessible areas.
    The maze has 4 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_68.txt')
    >>> maze.analyse()
    The maze has 24 gates.
    The maze has 11 sets of walls that are all connected.
    The maze has 17 inaccessible inner points.
    The maze has 9 accessible areas.
    The maze has 20 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_69.txt')
    >>> maze.analyse()
    The maze has 48 gates.
    The maze has 36 sets of walls that are all connected.
    The maze has 147 inaccessible inner points.
    The maze has 23 accessible areas.
    The maze has 89 sets of accessible cul-de-sacs that are all connected.
    The maze has 5 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_70.txt')
    >>> maze.analyse()
    The maze has 11 gates.
    The maze has 5 sets of walls that are all connected.
    The maze has 4 inaccessible inner points.
    The maze has 5 accessible areas.
    The maze has 5 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_71.txt')
    >>> maze.analyse()
    The maze has 40 gates.
    The maze has 22 sets of walls that are all connected.
    The maze has 16 inaccessible inner points.
    The maze has 14 accessible areas.
    The maze has 43 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_72.txt')
    >>> maze.analyse()
    The maze has 50 gates.
    The maze has 36 sets of walls that are all connected.
    The maze has 212 inaccessible inner points.
    The maze has 17 accessible areas.
    The maze has 97 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_73.txt')
    >>> maze.analyse()
    The maze has 35 gates.
    The maze has 16 sets of walls that are all connected.
    The maze has 60 inaccessible inner points.
    The maze has 11 accessible areas.
    The maze has 28 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_74.txt')
    >>> maze.analyse()
    The maze has 33 gates.
    The maze has 19 sets of walls that are all connected.
    The maze has 48 inaccessible inner points.
    The maze has 9 accessible areas.
    The maze has 30 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_75.txt')
    >>> maze.analyse()
    The maze has 60 gates.
    The maze has 38 sets of walls that are all connected.
    The maze has 87 inaccessible inner points.
    The maze has 23 accessible areas.
    The maze has 85 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_76.txt')
    >>> maze.analyse()
    The maze has 39 gates.
    The maze has 13 sets of walls that are all connected.
    The maze has 35 inaccessible inner points.
    The maze has 16 accessible areas.
    The maze has 39 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_77.txt')
    >>> maze.analyse()
    The maze has 37 gates.
    The maze has 9 sets of walls that are all connected.
    The maze has 98 inaccessible inner points.
    The maze has 21 accessible areas.
    The maze has 47 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_78.txt')
    >>> maze.analyse()
    The maze has 54 gates.
    The maze has 30 sets of walls that are all connected.
    The maze has 135 inaccessible inner points.
    The maze has 32 accessible areas.
    The maze has 106 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_79.txt')
    >>> maze.analyse()
    The maze has 56 gates.
    The maze has 56 sets of walls that are all connected.
    The maze has 111 inaccessible inner points.
    The maze has 20 accessible areas.
    The maze has 107 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_80.txt')
    >>> maze.analyse()
    The maze has 45 gates.
    The maze has 39 sets of walls that are all connected.
    The maze has 88 inaccessible inner points.
    The maze has 12 accessible areas.
    The maze has 84 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_81.txt')
    >>> maze.analyse()
    The maze has 39 gates.
    The maze has 36 sets of walls that are all connected.
    The maze has 99 inaccessible inner points.
    The maze has 15 accessible areas.
    The maze has 74 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_82.txt')
    >>> maze.analyse()
    The maze has 18 gates.
    The maze has 12 sets of walls that are all connected.
    The maze has 12 inaccessible inner points.
    The maze has 6 accessible areas.
    The maze has 9 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_83.txt')
    >>> maze.analyse()
    The maze has 36 gates.
    The maze has 18 sets of walls that are all connected.
    The maze has 26 inaccessible inner points.
    The maze has 11 accessible areas.
    The maze has 32 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_84.txt')
    >>> maze.analyse()
    The maze has 27 gates.
    The maze has 10 sets of walls that are all connected.
    The maze has 12 inaccessible inner points.
    The maze has 17 accessible areas.
    The maze has 31 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_85.txt')
    >>> maze.analyse()
    The maze has 68 gates.
    The maze has 40 sets of walls that are all connected.
    The maze has 157 inaccessible inner points.
    The maze has 24 accessible areas.
    The maze has 125 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_86.txt')
    >>> maze.analyse()
    The maze has 51 gates.
    The maze has 25 sets of walls that are all connected.
    The maze has 172 inaccessible inner points.
    The maze has 24 accessible areas.
    The maze has 67 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_87.txt')
    >>> maze.analyse()
    The maze has 53 gates.
    The maze has 49 sets of walls that are all connected.
    The maze has 139 inaccessible inner points.
    The maze has 20 accessible areas.
    The maze has 95 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_88.txt')
    >>> maze.analyse()
    The maze has 34 gates.
    The maze has 13 sets of walls that are all connected.
    The maze has 31 inaccessible inner points.
    The maze has 15 accessible areas.
    The maze has 49 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_89.txt')
    >>> maze.analyse()
    The maze has 61 gates.
    The maze has 39 sets of walls that are all connected.
    The maze has 111 inaccessible inner points.
    The maze has 31 accessible areas.
    The maze has 82 sets of accessible cul-de-sacs that are all connected.
    The maze has 5 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_90.txt')
    >>> maze.analyse()
    The maze has 52 gates.
    The maze has 34 sets of walls that are all connected.
    The maze has 102 inaccessible inner points.
    The maze has 18 accessible areas.
    The maze has 72 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_91.txt')
    >>> maze.analyse()
    The maze has 58 gates.
    The maze has 28 sets of walls that are all connected.
    The maze has 233 inaccessible inner points.
    The maze has 27 accessible areas.
    The maze has 79 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_92.txt')
    >>> maze.analyse()
    The maze has 62 gates.
    The maze has 50 sets of walls that are all connected.
    The maze has 180 inaccessible inner points.
    The maze has 26 accessible areas.
    The maze has 134 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_93.txt')
    >>> maze.analyse()
    The maze has 32 gates.
    The maze has 26 sets of walls that are all connected.
    The maze has 32 inaccessible inner points.
    The maze has 14 accessible areas.
    The maze has 36 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_94.txt')
    >>> maze.analyse()
    The maze has 18 gates.
    The maze has 4 sets of walls that are all connected.
    The maze has 13 inaccessible inner points.
    The maze has 12 accessible areas.
    The maze has 10 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_95.txt')
    >>> maze.analyse()
    The maze has 44 gates.
    The maze has 18 sets of walls that are all connected.
    The maze has 22 inaccessible inner points.
    The maze has 14 accessible areas.
    The maze has 32 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_96.txt')
    >>> maze.analyse()
    The maze has 46 gates.
    The maze has 19 sets of walls that are all connected.
    The maze has 57 inaccessible inner points.
    The maze has 20 accessible areas.
    The maze has 52 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_97.txt')
    >>> maze.analyse()
    The maze has 29 gates.
    The maze has 14 sets of walls that are all connected.
    The maze has 17 inaccessible inner points.
    The maze has 11 accessible areas.
    The maze has 26 sets of accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_98.txt')
    >>> maze.analyse()
    The maze has 52 gates.
    The maze has 41 sets of walls that are all connected.
    The maze has 165 inaccessible inner points.
    The maze has 16 accessible areas.
    The maze has 72 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.
    
    >>> maze = Maze('Ricky_test_99.txt')
    >>> maze.analyse()
    The maze has 7 gates.
    The maze has 3 sets of walls that are all connected.
    The maze has a unique inaccessible inner point.
    The maze has 4 accessible areas.
    The maze has 3 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.

    '''



if __name__ == '__main__':
    import doctest
    doctest.testmod()

