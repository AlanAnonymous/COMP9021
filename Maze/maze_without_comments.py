
class MazeError(Exception):
    def __init__(self, message):
        self.message = message



class Maze():
    def __init__(self, filename):
        array_2d, set_of_all_elements = [], set()
        with open(filename, 'r') as f:
            for line in f:
                new_line = line.strip().replace(' ', '')
                if new_line:
                    new_line_list = list(new_line)
                    array_2d.append(new_line_list)
                    set_of_all_elements.update(new_line_list)
        
        self.eror_detection(array_2d, set_of_all_elements)
        
        self.len_array_row = len(array_2d)
        self.len_array_col = len(array_2d[0])
        self.array_2d = array_2d
        self.len_matrix_row = 2 * self.len_array_row + 1
        self.len_matrix_col = 2 * self.len_array_col + 1
        self.matrix = [['6' for _ in range(self.len_matrix_col)] for _ in range(self.len_matrix_row)]

    
    def eror_detection(self, array_2d, set_of_all_elements):
        if not all(s in {'0', '1', '2', '3'} for s in set_of_all_elements):
            raise MazeError('Incorrect input.')
        number_of_row = len(array_2d)
        if not 2 <= number_of_row <= 41:
            raise MazeError('Incorrect input.')
        length_of_the_first_line = len(array_2d[0])
        if not 2 <= length_of_the_first_line <= 31:
            raise MazeError('Incorrect input.')
        if not all(length_of_the_first_line == len(array_2d[i]) for i in range(1, number_of_row)):
            raise MazeError('Incorrect input.')
        if not all(e in {'0', '1'} for e in array_2d[-1]):
            raise MazeError('Input does not represent a maze.')
        if not all(e in {'0', '2'} for e in {row[-1] for row in array_2d}):
            raise MazeError('Input does not represent a maze.')


    def analyse(self):
        gates = self.number_of_gates()
        walls = self.number_of_sets_of_walls()
        areas = self.number_of_accessible_areas()
        inner_points = self.number_of_inaccessible_points()
        cul_de_sacs = self.number_of_sets_of_cul_de_sacs()
        paths = self.number_of_entry_exit_paths()
        
        if gates == 0:
            print(f"The maze has no gate.")
        elif gates == 1:
            print(f"The maze has a single gate.")
        else:
            print(f"The maze has {gates} gates.")
        
        if walls == 0:
            print(f"The maze has no wall.")
        elif walls == 1:
            print(f"The maze has walls that are all connected.")
        else:
            print(f"The maze has {walls} sets of walls that are all connected.")

        if inner_points == 0:
            print(f"The maze has no inaccessible inner point.")
        elif inner_points == 1:
            print(f"The maze has a unique inaccessible inner point.")
        else:
            print(f"The maze has {inner_points} inaccessible inner points.")

        if areas == 0:
            print(f"The maze has no accessible area.")
        elif areas == 1:
            print(f"The maze has a unique accessible area.")
        else:
            print(f"The maze has {areas} accessible areas.")

        if cul_de_sacs == 0:
            print(f"The maze has no accessible cul-de-sac.")
        elif cul_de_sacs == 1:
            print(f"The maze has accessible cul-de-sacs that are all connected.")
        else:
            print(f"The maze has {cul_de_sacs} sets of accessible cul-de-sacs that are all connected.")

        if paths == 0:
            print(f"The maze has no entry-exit path with no intersection not to cul-de-sacs.")
        elif paths == 1:
            print(f"The maze has a unique entry-exit path with no intersection not to cul-de-sacs.")
        else:
            print(f"The maze has {paths} entry-exit paths with no intersections not to cul-de-sacs.")


    def number_of_gates(self):
        the_count = 0

        for j in range(self.len_array_col - 1):
            if self.array_2d[0][j] in {'0', '2'}:
                y = 2 * j + 1
                self.matrix[0][y + 1] = 'g'
                the_count += 1
            if self.array_2d[-1][j] == '0':
                y = 2 * j + 1
                self.matrix[-1][y + 1] = 'g'
                the_count += 1
        
        for i in range(self.len_array_row - 1):
            if self.array_2d[i][0] in {'0', '1'}:
                x = 2 * i + 1
                self.matrix[x + 1][0] = 'g'
                the_count += 1
            if self.array_2d[i][-1] == '0':
                x = 2 * i + 1
                self.matrix[x + 1][-1] = 'g'
                the_count += 1
        
        return the_count

    
    def number_of_sets_of_walls(self):
        for i in range(self.len_array_row):
            for j in range(self.len_array_col):
                current_element = self.array_2d[i][j]
                x, y = 2*i+1, 2*j+1
                if current_element in {'1', '3'}:
                    self.matrix[x][y] = self.matrix[x][y + 1] = self.matrix[x][y + 2] = 'w'
                if current_element in {'2', '3'}:
                    self.matrix[x][y] = self.matrix[x + 1][y] = self.matrix[x + 2][y] = 'w'
                if current_element == '0' and self.matrix[x - 1][y] == '6' and self.matrix[x][y - 1] == '6':
                    self.matrix[x][y] = 'p'

        the_count = 0
        matrix_copy = [line[:] for line in self.matrix]
        for x in range(self.len_matrix_row):
            for y in range(self.len_matrix_col):
                if matrix_copy[x][y] == 'w':
                    matrix_copy[x][y] == '7'
                    wall_list = [(x, y)]
                    for (m, n) in wall_list:
                        if m - 1 >= 0 and matrix_copy[m - 1][n] == 'w':
                            wall_list.append((m - 1, n))
                            matrix_copy[m - 1][n] = '7'
                        if m + 1 < self.len_matrix_row and matrix_copy[m + 1][n] == 'w':
                            wall_list.append((m + 1, n))
                            matrix_copy[m + 1][n] = '7'
                        if n - 1 >= 0 and matrix_copy[m][n - 1] == 'w':
                            wall_list.append((m, n - 1))
                            matrix_copy[m][n - 1] = '7'
                        if n + 1 < self.len_matrix_col and matrix_copy[m][n + 1] == 'w':
                            wall_list.append((m, n + 1))
                            matrix_copy[m][n + 1] = '7'
                    the_count += 1
        return the_count

    
    def number_of_accessible_areas(self):
        the_count = 0
        for x in range(1, self.len_matrix_row - 1):
            for y in range(1, self.len_matrix_col - 1):
                if self.matrix[x][y] != 'a' and \
                (self.matrix[x - 1][y] == 'g' or self.matrix[x + 1][y] == 'g' \
                or self.matrix[x][y - 1] == 'g' or self.matrix[x][y + 1] == 'g'):
                    self.matrix[x][y] = 'a'
                    aa_list = [(x, y)]
                    for (m, n) in aa_list:
                        if m - 1 >= 0 and self.matrix[m - 1][n] == '6':
                            aa_list.append((m - 1, n))
                            self.matrix[m - 1][n] = 'a'
                        if m + 1 < self.len_matrix_row and self.matrix[m + 1][n] == '6':
                            aa_list.append((m + 1, n))
                            self.matrix[m + 1][n] = 'a'
                        if n - 1 >= 0 and self.matrix[m][n - 1] == '6':
                            aa_list.append((m, n - 1))
                            self.matrix[m][n - 1] = 'a'
                        if n + 1 < self.len_matrix_col and self.matrix[m][n + 1] == '6':
                            aa_list.append((m, n + 1))
                            self.matrix[m][n + 1] = 'a'
                    the_count += 1
        return the_count


    def number_of_inaccessible_points(self):
        List = []
        for x in range(1, self.len_matrix_row - 1):
            for y in range(1, self.len_matrix_col - 1):
                if self.matrix[x][y] == '6':
                    self.matrix[x][y] = 'i'
                    i_list = [(x, y)]
                    for (m, n) in i_list:
                        if m - 1 >= 0 and self.matrix[m - 1][n] == '6':
                            i_list.append((m - 1, n))
                            self.matrix[m - 1][n] = 'i'
                        if m + 1 < self.len_matrix_row and self.matrix[m + 1][n] == '6':
                            i_list.append((m + 1, n))
                            self.matrix[m + 1][n] = 'i'
                        if n - 1 >= 0 and self.matrix[m][n - 1] == '6':
                            i_list.append((m, n - 1))
                            self.matrix[m][n - 1] = 'i'
                        if n + 1 < self.len_matrix_col and self.matrix[m][n + 1] == '6':
                            i_list.append((m, n + 1))
                            self.matrix[m][n + 1] = 'i'
                    List.append(i_list)
        the_count = 0
        for subList in List:
            for (m, n) in subList:
                if not m & 1 and not n & 1:
                    the_count += 1
        return the_count
    

    def number_of_sets_of_cul_de_sacs(self):
        for x in range(1, self.len_matrix_row - 1):
            for y in range(1, self.len_matrix_col - 1):
                if self.matrix[x][y] == 'a':
                    cds_list = [(x, y)]
                    for (m, n) in cds_list:
                        if m - 1 >= 0 and m + 1 < self.len_matrix_row \
                        and n - 1 >= 0 and n + 1 < self.len_matrix_col:
                            up, down = self.matrix[m - 1][n], self.matrix[m + 1][n]
                            left, right = self.matrix[m][n - 1], self.matrix[m][n + 1]
                            if (up == 'a' or 'g') and (down == 'w' or down == 'c') \
                            and (left == 'w' or left == 'c') and (right == 'w' or right == 'c'):
                                cds_list.append((m - 1, n))
                                self.matrix[m][n] = 'c'
                            elif (up == 'w' or up == 'c') and (down == 'a' or 'g') \
                            and (left == 'w' or left == 'c') and (right == 'w' or right == 'c'):
                                cds_list.append((m + 1, n))
                                self.matrix[m][n] = 'c'
                            elif (up == 'w' or up == 'c') and (down == 'w' or down == 'c') \
                            and (left == 'a' or 'g') and (right == 'w' or right == 'c'):
                                cds_list.append((m, n - 1))
                                self.matrix[m][n] = 'c'
                            elif (up == 'w' or up == 'c') and (down == 'w' or down == 'c') \
                            and (left == 'w' or left == 'c') and (right == 'a' or 'g'):
                                cds_list.append((m, n + 1))
                                self.matrix[m][n] = 'c'

        the_count = 0
        matrix_copy = [line[:] for line in self.matrix]
        for x in range(1, self.len_matrix_row - 1):
            for y in range(1, self.len_matrix_col - 1):
                if matrix_copy[x][y] == 'c':
                    matrix_copy[x][y] = '7'
                    cds_list = [(x, y)]
                    for (m, n) in cds_list:
                        if matrix_copy[m - 1][n] == 'c':
                            cds_list.append((m - 1, n))
                            matrix_copy[m - 1][n] = '7'
                        if matrix_copy[m + 1][n] == 'c':
                            cds_list.append((m + 1, n))
                            matrix_copy[m + 1][n] = '7'
                        if matrix_copy[m][n - 1] == 'c':
                            cds_list.append((m, n - 1))
                            matrix_copy[m][n - 1] = '7'
                        if matrix_copy[m][n + 1] == 'c':
                            cds_list.append((m, n + 1))
                            matrix_copy[m][n + 1] = '7'
                    the_count += 1

        return the_count
    

    def number_of_entry_exit_paths(self):
        the_count = 0
        matrix_copy = [line[:] for line in self.matrix]
        for x in range(2, self.len_matrix_row - 1, 2):
            for y in range(2, self.len_matrix_col - 1, 2):
                if matrix_copy[x][y] == 'a':
                    if [self.matrix[x - 1][y] == 'a', self.matrix[x + 1][y] == 'a', 
                    self.matrix[x][y - 1] == 'a', self.matrix[x][y + 1] == 'a'].count(True) >= 3:
                        matrix_copy[x][y] = '8'

        for x in range(self.len_matrix_row):
            for y in range(self.len_matrix_col):
                if matrix_copy[x][y] == 'g':
                    matrix_copy[x][y] = '9'
                    flag = False
                    path_list = [(x, y)]
                    for (m, n) in path_list:
                        if m - 1 >= 0:
                            up = matrix_copy[m - 1][n]
                            if up == 'a':
                                path_list.append((m - 1, n))
                                matrix_copy[m - 1][n] = '9'
                            elif up == 'g':
                                flag = True
                                break
                        if m + 1 < self.len_matrix_row:
                            down = matrix_copy[m + 1][n]
                            if down == 'a':
                                path_list.append((m + 1, n))
                                matrix_copy[m + 1][n] = '9'
                            elif down == 'g':
                                flag = True
                                break
                        if n - 1 >= 0:
                            left = matrix_copy[m][n - 1]
                            if left == 'a':
                                path_list.append((m, n - 1))
                                matrix_copy[m][n - 1] = '9'
                            elif left == 'g':
                                flag = True
                                break
                        if n + 1 < self.len_matrix_col:
                            right = matrix_copy[m][n + 1]
                            if right == 'a':
                                path_list.append((m, n + 1))
                                matrix_copy[m][n + 1] = '9'
                            elif right == 'g':
                                flag = True
                                break
                    if flag == True:
                        the_count += 1
                        for (p, q) in path_list:
                            if self.matrix[p][q] != 'g':
                                self.matrix[p][q] = 'e'
        
        return the_count

