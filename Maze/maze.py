
# =============================================================
# 下面的程序代码（代码量小于300行）仅能解决第一个问题，即仅能调用
# >>> maze = Maze('file_name.txt')
# >>> maze.analyse()
# 
# 如还想继续写出display()，
# （那么得充钱，不充钱怎么能变得更强(划掉，开玩笑的 xD)）
# 那么需要将下面的函数改动一下，使之能更好地同时适配analyse()和display()
# （当然，不改动也行，只要你没有多余的打印或输出就行）


# =============================================================
# 不使用递归，不使用标准库，也是可以做出来的！
# 不过需要一些“骚”操作(此骚操作可以应用于很多地方，例如排列组合，迷宫等)


# =============================================================
# 主要思路：将原二维数组转化为一个更容易分析的矩阵，然后依次统计各个部分的数量即可
# 【转换和统计数量需要用到“骚”操作】
# （可以根据下面的matrix作图， 6 没有实际意义，就占个地方方便作图和判断）
# 例如：(一步一步 地将从文本中提取的array_2d转化为matrix)
# array_2d        matrix
#   0 2   -->   6 6 g 6 6   便于观看 --->       g    
#   1 0         6 p e w 6                     p e w  
#               g e e w 6                   g e e w  
#               6 w w w 6                     w w w  
#               6 6 6 6 6                      
# g: gate  入口
# w: wall  墙
# p: point(green)  绿色的点
# a: accessible areas  可到到区域
# i: inaccessible inner points  不可到达区域
# c: cul_de_sacs 死胡同
# e: entry-exit paths 独立的通道
# 那么就可以得知：
# 2 gates
# 1 wall
# 1 entry-exit path
# ...
# 
# 定义：如果array_2d的某个点的坐标为(i,j), matrix的某个点的坐标为(x,y)
#       那么，它们之间的坐标转换规则为：x = 2*i+1, y = 2*j+1


# =============================================================
# 关于self的用法 1：
#   若 B = 1
#   self.A = B 等价于:  global A
#                       A = B
#   也就是让A成为了“全局变量”

# 关于self的用法 2：
# 调用“全局变量”需要写成：self.A

# 关于self的用法 3：
#   调用当前类中的函数时，必须在前面加上self
#   即：self.function(args)



# =============================================================
# 题目中 generate a MazeError exception 处说明需要一个生成错误信息的类
# 创建自定义异常如下：
class MazeError(Exception):
    def __init__(self, message):
        self.message = message


# 从题目要求来看，是要写一个名为Maze的class
# 必须要写的类Maze！！！名称需要一模一样！！！ #
class Maze():
    # 初始化一些东西，也就是做一些准备工作
    def __init__(self, filename):
        # --- 一：提取文本中的信息，即格式化不规则的输入 --- #
        array_2d = []   # 二维数组
        set_of_all_elements = set() # 文本中的所有的元素集合
        # 用 with open 比用 open 更好
        with open(filename, 'r') as f:
            for line in f:
                new_line = line.strip().replace(' ', '') # 去除 \n', '\r', '\t', ' '
                if new_line:    # 例：new_line == '123' 继续。new_line == '' 不继续
                    new_line_list = list(new_line)  # 例：将'123'变成['1', '2', '3']
                    array_2d.append(new_line_list)
                    set_of_all_elements.update(new_line_list)
        
        # --- 二：检测错误，并需要生成错误信息 --- #
        # array_2d  ===>  [ ['1','0','2',...], ['3','2','2',...] ... ]
        # set_of_all_elements  ===>  {'3', '2', '0', '1'}
        self.eror_detection(array_2d, set_of_all_elements)

        # --- 三：初始化一些“全局变量” --- #
        # 将一些数据设置成全局变量(其他函数要用到. 不用反复求)
        self.len_array_row = len(array_2d)
        self.len_array_col = len(array_2d[0])
        self.array_2d = array_2d
        self.len_matrix_row = 2 * self.len_array_row + 1
        self.len_matrix_col = 2 * self.len_array_col + 1
        # 一点一点地将array_2d转化为matrix，即就是转化为自己喜欢的形式/易于分析的形式
        # '6' 这个字符型的数字不重要，就占个位置。写成 True, 'fasweqtihgwnoi', ' ', 8848 都可以
        self.matrix = [['6' for _ in range(self.len_matrix_col)] for _ in range(self.len_matrix_row)]
        # 接下来就要依次改变matrix中的元素，同时统计不同的元素的个数



    
    # 检测错误，并生成相应的错误信息
    def eror_detection(self, array_2d, set_of_all_elements):
        # （注意：这里的检测顺序可以有效地避免各种特殊情况）
        # 1. 检测txt文本中出现的数字是不是都在 {0, 1, 2, 3} 中
        #    (使用 s in set 来判断可以让速度快那么一丢丢)
        if not all(s in {'0', '1', '2', '3'} for s in set_of_all_elements):
            raise MazeError('Incorrect input.')
        
        # 2. 检测迷宫的大小是否合规
        number_of_row = len(array_2d)
        if not 2 <= number_of_row <= 41:
            raise MazeError('Incorrect input.')
        
        length_of_the_first_line = len(array_2d[0])
        if not 2 <= length_of_the_first_line <= 31:
            raise MazeError('Incorrect input.')
        
        # 3. 检测文本中的每行的数字的总个数是不是一样的（用any()也行，写个循环判断也行）
        if not all(length_of_the_first_line == len(array_2d[i]) for i in range(1, number_of_row)):
            raise MazeError('Incorrect input.')
        
        # 4. 检测本中的最下面的元素是不是为0或1，最右边的元素是不是为0或2
        if not all(e in {'0', '1'} for e in array_2d[-1]):
            raise MazeError('Input does not represent a maze.')
        
        if not all(e in {'0', '2'} for e in {row[-1] for row in array_2d}):
            raise MazeError('Input does not represent a maze.')



    # ---------------------------------------------------------
    # 打印出此时的矩阵，便于debug，最终程序删不删这个函数无所谓
    def print_matrix(self, msg):
        print('after ' + msg)
        print('self.matrix =')
        for line in self.matrix:
            print(line)
        print()
    # ---------------------------------------------------------


    ###########################################################
    # 必须要写的函数analyse！！！名称需要一模一样！！！ #
    # 为了提升可读性，分部分写了很多不同的函数，需要的时候调用即可
    # 如果还想写出display()，那么下面的函数将会被拆分成多个函数
    def analyse(self):

        # -----------------------------------------------------
        # 调用各个函数：
        # gates
        gates = self.number_of_gates()

        # walls
        walls = self.number_of_sets_of_walls()

        # areas 
        # (先调用number_of_accessible_areas，再调用number_of_inaccessible_points)
        areas = self.number_of_accessible_areas()

        # inner_points
        # (先打印inner_points，再打印areas)
        inner_points = self.number_of_inaccessible_points()

        # cul_de_sacs
        cul_de_sacs = self.number_of_sets_of_cul_de_sacs()

        # paths
        paths = self.number_of_entry_exit_paths()

        # 调用完上述函数后，可以打印一下self.matrix试试看
        # self.print_matrix('all the end')


        # -----------------------------------------------------
        # 打印部分：
        # gates
        if gates == 0:
            print(f"The maze has no gate.")
        elif gates == 1:
            print(f"The maze has a single gate.")
        else:
            print(f"The maze has {gates} gates.")

        # walls
        if walls == 0:
            print(f"The maze has no wall.")
        elif walls == 1:
            print(f"The maze has walls that are all connected.")
        else:
            print(f"The maze has {walls} sets of walls that are all connected.")

        # inner_points
        if inner_points == 0:
            print(f"The maze has no inaccessible inner point.")
        elif inner_points == 1:
            print(f"The maze has a unique inaccessible inner point.")
        else:
            print(f"The maze has {inner_points} inaccessible inner points.")

        # areas
        if areas == 0:
            print(f"The maze has no accessible area.")
        elif areas == 1:
            print(f"The maze has a unique accessible area.")
        else:
            print(f"The maze has {areas} accessible areas.")

        # cul_de_sacs
        if cul_de_sacs == 0:
            print(f"The maze has no accessible cul-de-sac.")
        elif cul_de_sacs == 1:
            print(f"The maze has accessible cul-de-sacs that are all connected.")
        else:
            print(f"The maze has {cul_de_sacs} sets of accessible cul-de-sacs that are all connected.")

        # paths
        if paths == 0:
            print(f"The maze has no entry-exit path with no intersection not to cul-de-sacs.")
        elif paths == 1:
            print(f"The maze has a unique entry-exit path with no intersection not to cul-de-sacs.")
        else:
            print(f"The maze has {paths} entry-exit paths with no intersections not to cul-de-sacs.")
    ###########################################################



    # 将matrix中的某些元素改成 'g', 并统计 'g' 出现的次数
    def number_of_gates(self):
        the_count = 0   # 计数
        # 将matrix的第一行和最后一行(除了最后一个元素)中符合条件的地方变成'g'，并统计次数
        for j in range(self.len_array_col - 1):
            if self.array_2d[0][j] in {'0', '2'}:
                y = 2 * j + 1 # 坐标转换
                self.matrix[0][y + 1] = 'g'
                the_count += 1
            if self.array_2d[-1][j] == '0': # 最后一行里面不会有'2'，所以不用写出 in {'0', '2'}
                y = 2 * j + 1 # 坐标转换
                self.matrix[-1][y + 1] = 'g'
                the_count += 1
        
        # 将matrix的第一列和最后一列(除了最后一个元素)中符合条件的地方变成'g'，并统计次数
        for i in range(self.len_array_row - 1):
            if self.array_2d[i][0] in {'0', '1'}:
                x = 2 * i + 1 # 坐标转换
                self.matrix[x + 1][0] = 'g'
                the_count += 1
            if self.array_2d[i][-1] == '0': # 最后一列里面不会有'1'，所以不用写出 in {'0', '1'}
                x = 2 * i + 1 # 坐标转换
                self.matrix[x + 1][-1] = 'g'
                the_count += 1
        
        # self.print_matrix('gates')
        return the_count

    
    
    # 将matrix中的某些元素改成 'w', 并统计连着的 'w' 共有多少个
    # 顺便将某些元素改成'p'，也就是绿色的点
    def number_of_sets_of_walls(self):
        # 先改matrix中的某些元素的值
        for i in range(self.len_array_row):
            for j in range(self.len_array_col):
                current_element = self.array_2d[i][j]
                x, y = 2*i+1, 2*j+1 # 坐标转换
                # 下面3个条件都会被运行一遍
                # 将matrix中的某些元素改成 'w'
                if current_element in {'1', '3'}:
                    self.matrix[x][y] = self.matrix[x][y + 1] = self.matrix[x][y + 2] = 'w'
                if current_element in {'2', '3'}:
                    self.matrix[x][y] = self.matrix[x + 1][y] = self.matrix[x + 2][y] = 'w'
                # 将matrix中的某些元素改成 'p'
                if current_element == '0' and self.matrix[x - 1][y] == '6' and self.matrix[x][y - 1] == '6':
                    self.matrix[x][y] = 'p'

        # self.print_matrix('walls')

        # 再计算当前的matrix中连着的 'w' 共有多少个
        # 若想用递归，请直接抄(稍微改写即可)Martin老师给的关于有多少个骑士能走完棋盘的代码答案
        # 我这里不用递归，用其他方法做出来，这方法可能也只有python能很好地实现吧
        # (如果这个地方弄懂了或者会写了，其他就是举一反三了，就可以开始枯燥且无聊地“抄袭”本部分了)
        the_count = 0
        # 当前的self.matrix不能被改变(因为walls已经弄好了)，所以需要用self.matrix的副本进行如下运行
        matrix_copy = [line[:] for line in self.matrix]  # deep copy, not shallow copy
        # 思路：
        # 遍历matrix_copy，找到其中一面墙的某个点的坐标
        # 将其添加进入一个list中，并且将此点标记为已经遍历过了
        # 遍历这个list，找出与list中的这个点的上下左右的值为'w'的点，并将其添加进list中
        # 再次遍历这个list(此时的list已经变了)，找出与list中的这个点的上下左右的值为'w'的点，并将其添加进list中
        # 重复上述过程，直到这面墙的所有坐标都被添加进入了list中
        # 那么，此时，matrix_copy中的一面墙被遍历过了，所以，the_count += 1
        # 当整个matrix_copy被遍历完后，所有的墙都被遍历过了，计数也完成了，那么返回the_count即可
        # 此方法的优点：无论多大的self.matrix，给我时间，我都能准确算出墙的个数。而递归对于超大型数组直接GG
        #               （不过，这道题的递归深度绝对不会太大的，所以用递归也是可以完美通过所有测试）
        # 此方法的缺点：额，大概就是一般人想不到，知道的人不是太多，而且写得跟递归好像啊。
        for x in range(self.len_matrix_row):
            for y in range(self.len_matrix_col):
                # 先找到其中一面墙的某个点的坐标
                if matrix_copy[x][y] == 'w':
                    # 标记为遍历过了
                    # 注意这里是改变了matrix_copy中的某个坐标的值，
                    # 所以，不使用self.matrix，而是使用了self.matrix的副本
                    matrix_copy[x][y] == '7'
                    wall_list = [(x, y)]    # 初始化/重置wall_list
                    # wall_list是变长的一个list！它在不断地变长！
                    # 也就是len(wall_list)在不断的增大！直到不满足条件才停止变长！
                    # 这个就是规避递归的做法之一！(虽然写起来挺像递归的，但绝不是递归！)
                    for (m, n) in wall_list:
                        # 下面4个条件都会被判断一遍，也就是wall_list里面可能一次性添加进入了0/1/2/3/4个点的坐标
                        if m - 1 >= 0 and matrix_copy[m - 1][n] == 'w':                     # 上
                            # 此点(m - 1,n)将被用作下次运算，所以将其添加进wall_list
                            # 下次运算中，此点的上下左右的为w的点会被添加进wall_list
                            wall_list.append((m - 1, n))
                            # 重新赋的值是什么不重要，只要不是'w'就行
                            # 相当于抹除此点，让此点不参与下一个条件判断
                            # 也相当于将此点标记一下，标记为已遍历过
                            matrix_copy[m - 1][n] = '7'
                        if m + 1 < self.len_matrix_row and matrix_copy[m + 1][n] == 'w':    # 下
                            wall_list.append((m + 1, n))
                            matrix_copy[m + 1][n] = '7'
                        if n - 1 >= 0 and matrix_copy[m][n - 1] == 'w':                     # 左
                            wall_list.append((m, n - 1))
                            matrix_copy[m][n - 1] = '7'
                        if n + 1 < self.len_matrix_col and matrix_copy[m][n + 1] == 'w':    # 右
                            wall_list.append((m, n + 1))
                            matrix_copy[m][n + 1] = '7'
                    # 在wall_list循环结束后，其中一面墙的所有坐标就都在此wall_list中了（可以打印试试）
                    # 并且在循环中，已经将此面墙给抹除掉了（可以打印看看当前的matrix_copy），避免了重复计算墙的个数
                    # 现在，找完并抹除一面墙的所有点了，所以，计数可以加1了
                    the_count += 1
                    # 然后开始找下一面墙

        return the_count
        # 顺带一提，此处算墙的个数还可以用交集法 (不推荐)
        # (能做出来并通过所有测试，不过里面有些暗坑，很容易就踩中。而且这种方法效率低下)
        # 简单说下：
        # 找到第一个matrix_copy[i][j] == 'w'，将其与它的四周的为'w'的点的坐标放到一个list中，形成list1 = [p1, p2]
        # 找到第二个matrix_copy[i][j] == 'w'，将其与它的四周的为'w'的点的坐标放到一个list中，形成list2 = [p2, p1, p3]
        # 找到第三个matrix_copy[i][j] == 'w'，将其与它的四周的为'w'的点的坐标放到一个list中，形成list3 = [p4, p5]
        # 然后遍历 big_list = [ [p1, p2], [p2, p1, p3], [p4, p5] ]，找到它们之间有交集的list
        # 也就是 list1 和 list2 交集不为空，那么合并 list1 和 list2 (这里有暗坑)
        # 形成 new_big_list = [ [p1, p2, p3], [p4, p5] ]
        # 最后，这个 new_big_list 的长度即是墙的个数，里面的某个list的元素就是这一面墙的所有的坐标点
        # (庆幸不是8个方向，不然要是可以走8个方向的话，代码量得翻个一倍。。。。。。)

    
    
    # 将matrix中的某些元素改成 'a', 并统计连着的 'a' 共有多少个
    def number_of_accessible_areas(self):
        the_count = 0
        # 跟上面那个number_of_sets_of_walls函数中写得差不多(枯燥且无聊地抄就完事儿了)
        # 注意下遍历的范围即可
        for x in range(1, self.len_matrix_row - 1):
            for y in range(1, self.len_matrix_col - 1):
                # 找到一个没有遍历过的点，并且这个点的上(或下或左或右)是入口
                if self.matrix[x][y] != 'a' and \
                (self.matrix[x - 1][y] == 'g' or self.matrix[x + 1][y] == 'g' \
                or self.matrix[x][y - 1] == 'g' or self.matrix[x][y + 1] == 'g'):
                    self.matrix[x][y] = 'a' # 先改变当前这个点的值
                    # 然后就开始用“骚”操作了
                    aa_list = [(x, y)]
                    for (m, n) in aa_list:
                        if m - 1 >= 0 and self.matrix[m - 1][n] == '6':                     # 上
                            aa_list.append((m - 1, n))
                            self.matrix[m - 1][n] = 'a' # 更改self.matrix中的某些元素的值
                        if m + 1 < self.len_matrix_row and self.matrix[m + 1][n] == '6':    # 下
                            aa_list.append((m + 1, n))
                            self.matrix[m + 1][n] = 'a'
                        if n - 1 >= 0 and self.matrix[m][n - 1] == '6':                     # 左
                            aa_list.append((m, n - 1))
                            self.matrix[m][n - 1] = 'a'
                        if n + 1 < self.len_matrix_col and self.matrix[m][n + 1] == '6':    # 右
                            aa_list.append((m, n + 1))
                            self.matrix[m][n + 1] = 'a'
                    the_count += 1

        # self.print_matrix('accessible_areas')
        return the_count



    # 将matrix中的某些元素改成 'a'，再统计进不去的区块的数量
    # (先调用了上面那个 number_of_accessible_areas 函数，现在就轻松多了)
    def number_of_inaccessible_points(self):
        # 稍微修改下“骚”操作即可
        List = []
        for x in range(1, self.len_matrix_row - 1):
            for y in range(1, self.len_matrix_col - 1):
                if self.matrix[x][y] == '6':
                    self.matrix[x][y] = 'i'
                    i_list = [(x, y)]
                    for (m, n) in i_list:
                        if m - 1 >= 0 and self.matrix[m - 1][n] == '6':                     # 上
                            i_list.append((m - 1, n))
                            self.matrix[m - 1][n] = 'i'
                        if m + 1 < self.len_matrix_row and self.matrix[m + 1][n] == '6':    # 下
                            i_list.append((m + 1, n))
                            self.matrix[m + 1][n] = 'i'
                        if n - 1 >= 0 and self.matrix[m][n - 1] == '6':                     # 左
                            i_list.append((m, n - 1))
                            self.matrix[m][n - 1] = 'i'
                        if n + 1 < self.len_matrix_col and self.matrix[m][n + 1] == '6':    # 右
                            i_list.append((m, n + 1))
                            self.matrix[m][n + 1] = 'i'
                    List.append(i_list)
        # i_list中的某些点并不算做inner point，所以还要进行一下简单的排除
        the_count = 0
        for subList in List:
            for (m, n) in subList:
                # 横纵坐标都需要是偶数（奇数的坐标点是为了连线，方便人观看而已）
                if not m & 1 and not n & 1:
                    # 横纵坐标都需要是偶数的坐标点才能算作是 innner point，the_count才能自增1
                    the_count += 1
        # self.print_matrix('inaccessible_areas')
        return the_count
    


    # 将matrix中的某些原等于'a'的元素改成 'c'，再统计连着的 'c' 共有多少个
    # 主要思路：从一个死胡同的点开始标记，依次向外标记
    # 因为死胡同最里面的点必然是3面墙，1个可以走的方向，所以从死胡同最里面的点开始唯一的方向走
    def number_of_sets_of_cul_de_sacs(self):
        for x in range(1, self.len_matrix_row - 1):
            for y in range(1, self.len_matrix_col - 1):
                # 看看当前这个点的值是不是'a'
                # 再看看当前这个点的周围四个点中是不是有3个是'w'或者'c'
                # 然后，将所有死胡同里的点全部标记为'c'
                if self.matrix[x][y] == 'a':
                    cds_list = [(x, y)]
                    for (m, n) in cds_list:
                        # 限制范围，因为有时候 self.matrix[m][n] == 'g'
                        if m - 1 >= 0 and m + 1 < self.len_matrix_row \
                        and n - 1 >= 0 and n + 1 < self.len_matrix_col:
                            up, down = self.matrix[m - 1][n], self.matrix[m + 1][n]
                            left, right = self.matrix[m][n - 1], self.matrix[m][n + 1]
                            # 用if elif判断是因为下面的情况只能出现其中一个，
                            # 也就是说，一个死胡同里的点只可能有一个方向可以走
                            # 上为'a'或'g'，其余为'w'或'c'
                            if (up == 'a' or 'g') and (down == 'w' or down == 'c') \
                            and (left == 'w' or left == 'c') and (right == 'w' or right == 'c'):
                                cds_list.append((m - 1, n))
                                self.matrix[m][n] = 'c'
                            # 下为'a'或'g'，其余为'w'或'c'
                            elif (up == 'w' or up == 'c') and (down == 'a' or 'g') \
                            and (left == 'w' or left == 'c') and (right == 'w' or right == 'c'):
                                cds_list.append((m + 1, n))
                                self.matrix[m][n] = 'c'
                            # 左为'a'或'g'，其余为'w'或'c'
                            elif (up == 'w' or up == 'c') and (down == 'w' or down == 'c') \
                            and (left == 'a' or 'g') and (right == 'w' or right == 'c'):
                                cds_list.append((m, n - 1))
                                self.matrix[m][n] = 'c'
                            # 右为'a'或'g'，其余为'w'或'c'
                            elif (up == 'w' or up == 'c') and (down == 'w' or down == 'c') \
                            and (left == 'w' or left == 'c') and (right == 'a' or 'g'):
                                cds_list.append((m, n + 1))
                                self.matrix[m][n] = 'c'

        # 然后统计连着的'c'有多少个
        the_count = 0
        matrix_copy = [line[:] for line in self.matrix]
        for x in range(1, self.len_matrix_row - 1):
            for y in range(1, self.len_matrix_col - 1):
                if matrix_copy[x][y] == 'c':
                    matrix_copy[x][y] = '7'
                    cds_list = [(x, y)]
                    for (m, n) in cds_list:
                        if matrix_copy[m - 1][n] == 'c':    # 上
                            cds_list.append((m - 1, n))
                            matrix_copy[m - 1][n] = '7'     # 更改matrix_copy中的某些元素的值
                        if matrix_copy[m + 1][n] == 'c':    # 下
                            cds_list.append((m + 1, n))
                            matrix_copy[m + 1][n] = '7'
                        if matrix_copy[m][n - 1] == 'c':    # 左
                            cds_list.append((m, n - 1))
                            matrix_copy[m][n - 1] = '7'
                        if matrix_copy[m][n + 1] == 'c':    # 右
                            cds_list.append((m, n + 1))
                            matrix_copy[m][n + 1] = '7'
                    the_count += 1

        # self.print_matrix('cul_de_sacs')
        return the_count
    


    # 将matrix中的某些原本是'a'的元素改成 'e'，再统计连着的 'e' 共有多少个
    # 思路：（下面这种做法能完美通过各种测试，是已知的最好的方法）
    # 若矩阵副本中 matrix_copy[x][y] == 'a'，且这个点的上下左右共有3个或4个方向可以走
    # 那么将这个点堵住，也就是设置一个路障
    # 然后重新遍历矩阵副本，看此时共有几条通路
    # 此时找到的通路就是独立的通路，不与其他路相交，也就是此路就是 entry_exit_paths
    # （设置了路障后，其中一个'g'最多能与另外1个'g'相连，不可能与另外2个'g'相连）
    def number_of_entry_exit_paths(self):
        the_count = 0

        matrix_copy = [line[:] for line in self.matrix]
        # 没有必要遍历所有的点，有些点只是连线而已，所以跳着遍历，当然，一个一个挨个遍历也行
        for x in range(2, self.len_matrix_row - 1, 2):
            for y in range(2, self.len_matrix_col - 1, 2):
                if matrix_copy[x][y] == 'a':
                    # 上下左右为'a'的数量至少为3
                    if [self.matrix[x - 1][y] == 'a', self.matrix[x + 1][y] == 'a', 
                    self.matrix[x][y - 1] == 'a', self.matrix[x][y + 1] == 'a'].count(True) >= 3:
                        matrix_copy[x][y] = '8' # 随便设置一个数字代表路障( 8可以看作：8行(不行) )

        # 在现在的matrix_copy中找通路，也就是有两个入口的路（或者说有两个'g'的路）
        # 从'g'开始找(下面这种写法时间复杂度高了点，不过写起来简单点)
        # (因为'g'只可能在矩阵的四周，所以只需要遍历矩阵的四周即可，不过那样的话代码太多)
        for x in range(self.len_matrix_row):
            for y in range(self.len_matrix_col):
                if matrix_copy[x][y] == 'g':
                    matrix_copy[x][y] = '9' # 设置当前这个坐标为已遍历（这个点是起点）
                    # 现在已经找到一个'g'了，那么从这个'g'出发，是否走到另一个'g'呢
                    # 所以用一个flag来判断是否找到了另一个'g'
                    flag = False
                    path_list = [(x, y)]
                    for (m, n) in path_list:
                        if m - 1 >= 0:                          # 上
                            up = matrix_copy[m - 1][n]
                            if up == 'a':
                                path_list.append((m - 1, n))
                                matrix_copy[m - 1][n] = '9' # 设为9代表遍历过了
                            # 找到'g'，即找到了终点，可以直接结束了
                            # 因为这种堵路法非常好，不可能存在有3个或以上的'g'相连
                            elif up == 'g':
                                flag = True
                                break
                        if m + 1 < self.len_matrix_row:         # 下
                            down = matrix_copy[m + 1][n]
                            if down == 'a':
                                path_list.append((m + 1, n))
                                matrix_copy[m + 1][n] = '9'
                            elif down == 'g':
                                flag = True
                                break
                        if n - 1 >= 0:                          # 左
                            left = matrix_copy[m][n - 1]
                            if left == 'a':
                                path_list.append((m, n - 1))
                                matrix_copy[m][n - 1] = '9'
                            elif left == 'g':
                                flag = True
                                break
                        if n + 1 < self.len_matrix_col:         # 右
                            right = matrix_copy[m][n + 1]
                            if right == 'a':
                                path_list.append((m, n + 1))
                                matrix_copy[m][n + 1] = '9'
                            elif right == 'g':
                                flag = True
                                break
                    if flag == True:    # 代表现在找到了一对出入口
                        the_count += 1  # 计数增加1不要忘了
                        # 当前地path_list中的坐标就是entry_exit_paths中的所有坐标
                        # 所以，根据path_list提供的坐标来改变self.matrix中的某些坐标的值即可
                        for (p, q) in path_list:
                            if self.matrix[p][q] != 'g':    # 不要将出入口的值给改了
                                self.matrix[p][q] = 'e'
        
        # self.print_matrix('entry_exit_paths')
        return the_count


