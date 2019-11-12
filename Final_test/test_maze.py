#!/usr/bin/env python3

# You can get a high marks if you pass most of the following tests



from maze import *


def test():

    '''
    >>> maze = Maze('incorrect_input_1.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Incorrect input.

    >>> maze = Maze('incorrect_input_2.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Incorrect input.

    >>> maze = Maze('incorrect_input_3.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Incorrect input.

    >>> maze = Maze('incorrect_input_4.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Incorrect input.

    >>> maze = Maze('incorrect_input_5.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Incorrect input.

    >>> maze = Maze('incorrect_input_6.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Incorrect input.



    >>> maze = Maze('not_a_maze_1.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Input does not represent a maze.

    >>> maze = Maze('not_a_maze_2.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Input does not represent a maze.

    >>> maze = Maze('not_a_maze_3.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Input does not represent a maze.

    >>> maze = Maze('not_a_maze_4.txt')
    Traceback (most recent call last):
        ...
    maze.MazeError: Input does not represent a maze.



    >>> maze = Maze('maze_1.txt')
    >>> maze.analyse()
    The maze has 12 gates.
    The maze has 8 sets of walls that are all connected.
    The maze has 2 inaccessible inner points.
    The maze has 4 accessible areas.
    The maze has 3 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('maze_2.txt')
    >>> maze.analyse()
    The maze has 20 gates.
    The maze has 4 sets of walls that are all connected.
    The maze has 4 inaccessible inner points.
    The maze has 13 accessible areas.
    The maze has 11 sets of accessible cul-de-sacs that are all connected.
    The maze has 5 entry-exit paths with no intersections not to cul-de-sacs.

    >>> maze = Maze('maze_3.txt')
    >>> maze.analyse()
    The maze has 4 gates.
    The maze has no wall.
    The maze has no inaccessible inner point.
    The maze has a unique accessible area.
    The maze has no accessible cul-de-sac.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('maze_4.txt')
    >>> maze.analyse()
    The maze has no gate.
    The maze has walls that are all connected.
    The maze has 2 inaccessible inner points.
    The maze has no accessible area.
    The maze has no accessible cul-de-sac.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('maze_5.txt')
    >>> maze.analyse()
    The maze has 8 gates.
    The maze has walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has 2 accessible areas.
    The maze has no accessible cul-de-sac.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('maze_6.txt')
    >>> maze.analyse()
    The maze has 8 gates.
    The maze has walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has 3 accessible areas.
    The maze has no accessible cul-de-sac.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.

    >>> maze = Maze('maze_7.txt')
    >>> maze.analyse()
    The maze has 2 gates.
    The maze has 2 sets of walls that are all connected.
    The maze has 15 inaccessible inner points.
    The maze has a unique accessible area.
    The maze has no accessible cul-de-sac.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('maze_8.txt')
    >>> maze.analyse()
    The maze has 6 gates.
    The maze has walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has 3 accessible areas.
    The maze has accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('maze_9.txt')
    >>> maze.analyse()
    The maze has 10 gates.
    The maze has walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has 5 accessible areas.
    The maze has accessible cul-de-sacs that are all connected.
    The maze has 3 entry-exit paths with no intersections not to cul-de-sacs.

    >>> maze = Maze('maze_10.txt')
    >>> maze.analyse()
    The maze has 29 gates.
    The maze has 21 sets of walls that are all connected.
    The maze has 12 inaccessible inner points.
    The maze has 8 accessible areas.
    The maze has 26 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('maze_11.txt')
    >>> maze.analyse()
    The maze has 2 gates.
    The maze has 3 sets of walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has a unique accessible area.
    The maze has 3 sets of accessible cul-de-sacs that are all connected.
    The maze has no entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('maze_12.txt')
    >>> maze.analyse()
    The maze has 45 gates.
    The maze has 41 sets of walls that are all connected.
    The maze has 91 inaccessible inner points.
    The maze has 17 accessible areas.
    The maze has 98 sets of accessible cul-de-sacs that are all connected.
    The maze has 4 entry-exit paths with no intersections not to cul-de-sacs.

    >>> maze = Maze('maze_13.txt')
    >>> maze.analyse()
    The maze has 80 gates.
    The maze has 72 sets of walls that are all connected.
    The maze has 195 inaccessible inner points.
    The maze has 26 accessible areas.
    The maze has 180 sets of accessible cul-de-sacs that are all connected.
    The maze has 2 entry-exit paths with no intersections not to cul-de-sacs.



    >>> maze = Maze('labyrinth.txt')
    >>> maze.analyse()
    The maze has 2 gates.
    The maze has 2 sets of walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has a unique accessible area.
    The maze has 8 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('labyrinth_2.txt')
    >>> maze.analyse()
    The maze has 2 gates.
    The maze has 2 sets of walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has a unique accessible area.
    The maze has 6 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('labyrinth_3.txt')
    >>> maze.analyse()
    The maze has 2 gates.
    The maze has 2 sets of walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has a unique accessible area.
    The maze has 3 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('labyrinth_4.txt')
    >>> maze.analyse()
    The maze has 2 gates.
    The maze has 2 sets of walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has a unique accessible area.
    The maze has 8 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.

    >>> maze = Maze('labyrinth_5.txt')
    >>> maze.analyse()
    The maze has 2 gates.
    The maze has 2 sets of walls that are all connected.
    The maze has no inaccessible inner point.
    The maze has a unique accessible area.
    The maze has 32 sets of accessible cul-de-sacs that are all connected.
    The maze has a unique entry-exit path with no intersection not to cul-de-sacs.
    '''



if __name__ == '__main__':
    import doctest
    doctest.testmod()

