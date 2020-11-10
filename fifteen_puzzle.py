import pprint
pp = pprint.PrettyPrinter(indent=4)


def puzz_astar(start,end):
    """
    A* algorithm
    """
    heuristic = heuristic_2     #optional: heuristic_2
    open_list = [[heuristic(start), start]] 
    close_list = []
    while open_list:
        # select the node with least heuristic element to expand
        # if len(close_list)>1000:    break
        i = 0
        for j in range(1, len(open_list)):
            if open_list[i][0] > open_list[j][0]:
                i = j
        path = open_list.pop(i)
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in close_list: continue
        for k in moves(endnode):
            if k in close_list: continue
            # newpath = [path[0] + heuristic(k) - heuristic(endnode)] + path[1:] + [k] 
            newpath = [heuristic(k) + 1 * len(path)] + path[1:] + [k] 
            open_list.append(newpath)
        close_list.append(endnode)
    print("Expanded nodes:", len(close_list))
    print("Solution:")
    pp.pprint(path)
    print("Path nodes:\n", len(path))
    


def moves(mat): 
    """
    Returns a list of all possible moves
    """
    output = []  

    m = eval(mat)   
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); #blank space (zero)

    if i > 0:                                   
        m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
        output.append(str(m))
        m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
      
    if i < 3:                                   
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
        output.append(str(m))
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:                                                      
        m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
        output.append(str(m))
        m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < 3:                                   
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
        output.append(str(m))
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

    return output

def heuristic_1(puzz):
    """
    Counts the number of misplaced tiles
    """ 
    misplaced = 0
    compare = 1
    m = eval(puzz)
    for i in range(4):
        for j in range(4):
            if m[i][j] != compare:
                misplaced += 1
            compare = (compare + 1) % 16
    return misplaced

def heuristic_2(puzz):
    """
    Manhattan distance
    """  
    distance = 0
    m = eval(puzz)          
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0: continue
            distance += abs(i - int((m[i][j]-1)/4)) + abs(j -  ((m[i][j]-1)%4));
    return distance

if __name__ == '__main__':
    puzzle = str([[11, 9, 4, 15],[1, 3, 0, 12], [7, 5, 8, 6],[13, 2, 10, 14]])
    end = str([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])
    puzz_astar(puzzle,end)