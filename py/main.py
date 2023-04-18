import re
import sys,os

class Graph:
    def __init__(self):
        self.graph = {}
    #add edge
    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)

    #breadth algorthim that return the path and the visited node as a string
    def BFS(self, start, goal):
        visit = ''
        visted = []
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node in visted:
                continue
            visted.append(node)
            if node == goal:
                return path, visit
            else:
                adjacent_nodes = self.graph.get(node, [])
                for node2 in adjacent_nodes:
                    if node2 not in path:
                        new_path = list(path)
                        new_path.append(node2)
                        queue.append(new_path)
            array=visted
            names=(toCitys(array))
            visit = visit + str(names) + '\n'
    #depth algorthim that return the path and the visited node as a string
    def DFS(self, start, goal):
        visit = ''
        visted = []
        stack = [[start]]
        while stack:
            path = stack.pop()
            node = path[-1]
            if node in visted:
                continue
            visted.append(node)
            if node == goal:
                return path, visit
            else:
                adjacent_nodes = self.graph.get(node, [])
                for node2 in adjacent_nodes:
                    if node2 not in path:
                        new_path = list(path)
                        new_path.append(node2)
                        stack.append(new_path)
            # print(visted)
            array = visted
            names = (toCitys(array))
            visit = visit + str(names) + '\n'
    #A* algorthim that return the path and the visited node as a string
    def aStarWalk(self, start, goal):
        visit = ''
        visted = []
        queue = [[start]]
        while queue:
            # queue.sort(key=getCost)
            queue = sorted(queue, key=lambda queue: getCostWalkAreal(queue, goal))
            path = queue.pop(0)
            node = path[-1]
            if node in visted:
                continue
            visted.append(node)
            if node == goal:
                return path, visit
            else:
                adjacent_nodes = self.graph.get(node, [])
                for (node2) in adjacent_nodes:
                    new_path = path.copy()
                    new_path.append(node2)
                    queue.append(new_path)
            array = visted
            names = (toCitys(array))
            visit = visit + str(names) + '\n'
    #A* algorthim that return the path and the visited node as a string
    def aStarWalkAreal(self, start, goal):
        visit = ''
        visted = []
        queue = [[start]]
        while queue:
            # queue.sort(key=getCost)
            queue = sorted(queue, key=lambda queue: getCostCarWalkH(queue, goal))
            path = queue.pop(0)
            node = path[-1]
            if node in visted:
                continue
            visted.append(node)
            if node == goal:
                return path, visit
            else:
                adjacent_nodes = self.graph.get(node, [])
                for (node2) in adjacent_nodes:
                    new_path = path.copy()
                    new_path.append(node2)
                    queue.append(new_path)
            array=visted
            names=(toCitys(array))
            visit = visit + str(names) + '\n'
    #uniform cost algorthim that return the path and the visited node as a string
    def ucs(self, start, goal):
        visted = []
        visit = ''
        queue = [[start]]
        node = start
        while queue:
            queue.sort(key=getCostcar)
            path = queue.pop(0)
            node = path[-1]
            if node in visted:
                continue
            visted.append(node)
            if node == goal:
                return path, visit
            else:
                adjacent_nodes = self.graph.get(node, [])
                for (node2) in adjacent_nodes:
                    new_path = path.copy()
                    new_path.append(node2)
                    queue.append(new_path)
            array = visted
            names = (toCitys(array))
            visit = visit + str(names) + '\n'

#function to read the car file and added the vertices to the graph
def readCarFile(Graph):
    # from which city =fr
    g = Graph
    x = []
    file = open("car.txt", "r")
    Lines = file.readlines()
    length = len(Lines)
    j = 0
    fr = 0
    for i in Lines:
        i = re.split(',|\n', i)
        i.pop()
        addEdges(i, g, fr)
        fr += 1

#function that return the total cost (heystric and walk cost)
def getCostWalkAreal(path, goal):
    cost: int = 0
    file = open("walk.txt", "r")
    Lines = file.readlines()
    length = len(Lines)
    i = 0
    start = 0
    next = 0
    costResult = []
    while i < len(path) - 1:
        start = path[i]
        next = path[i + 1]
        line = Lines[start]
        line = re.split(",|\n", line)
        line.pop()
        costResult.append(int(line[next]))
        cost += int(line[next])
        i += 1
    total = 0
    cost = int(cost)
    total = int(getArealCostTwoNodes(int(path[-1]), goal) + cost)
    return total

#return the cost for the given path
def getCostcar(path):
    cost: int = 0
    file = open("car.txt", "r")
    Lines = file.readlines()
    length = len(Lines)
    i = 0
    start = 0
    next = 0
    costResult = []
    while i < len(path) - 1:
        start = path[i]
        next = path[i + 1]
        line = Lines[start]
        line = re.split(",|\n", line)
        line.pop()
        costResult.append(int(line[next]))
        cost += int(line[next])
        i += 1
    total = 0
    cost = int(cost)
    return cost

#function that return the total cost heystric + car cost
def getCostCarWalkH(path, goal):
    cost: int = 0
    file = open("car.txt", "r")
    Lines = file.readlines()
    length = len(Lines)
    i = 0
    start = 0
    next = 0
    costResult = []
    while i < len(path) - 1:
        start = path[i]
        next = path[i + 1]
        line = Lines[start]
        line = re.split(",|\n", line)
        line.pop()
        costResult.append(int(line[next]))
        cost += int(line[next])
        i += 1
    total = 0
    cost = int(cost)
    total = int(getwalk_H_CostTwoNodes(int(path[-1]), goal) + cost)
    return total


# added the vertices to the graph
def addEdges(list, Graph, fr):
    g = Graph
    value = 0
    # to :  to which city
    to = 0
    for j in list:
        value = int(j)
        if value != 0:
            g.addEdge(fr, to)
        to += 1

#read the file that contain the citys names and return it as a array
def readCity():
    array = []
    file = open("citys.txt", "r")
    Lines = file.readlines()
    for i in Lines:
        string = re.split("\n", i)
        string.pop()
        array.append(string[0])
    return array

#convert the given path as nodes to path as a citys names
def toCitys(path):
    result = []
    citys = readCity()
    for i in path:
        result.append(citys[i])
    return result


def getArealCostTwoNodes(start, goal):
    file = open("areal.txt", "r")
    Lines = file.readlines()
    costResult = []
    first = Lines[start].split(",")

    return int(first[goal])

#return the value of the heyastric for start and goal nodes given
def getwalk_H_CostTwoNodes(start, goal):
    file = open("walk_h.txt", "r")
    Lines = file.readlines()
    costResult = []
    first = Lines[start].split(",")

    return int(first[goal])

#return the cost for given path and return it as an array
def getCostDfsBfs(path):
    cost = 0
    file = open("car.txt", "r")
    Lines = file.readlines()
    length = len(Lines)
    i = 0
    start = 0
    next = 0
    costResult = []
    while i < len(path) - 1:
        start = path[i]
        next = path[i + 1]
        line = Lines[start]
        line = re.split(",|\n", line)
        line.pop()
        costResult.append(int(line[next]))
        cost += int(line[next])
        i += 1
    string = "TotalCost= " + str(cost)
    costResult.append(string)
    return costResult

# if the user select choice one
def getCostDfsBfsNEWW(path):
    cost = 0
    file = open("walk.txt", "r")
    Lines = file.readlines()
    length = len(Lines)
    i = 0
    start = 0
    next = 0
    costResult = []
    while i < len(path) - 1:
        start = path[i]
        next = path[i + 1]
        line = Lines[start]
        line = re.split(",|\n", line)
        line.pop()
        costResult.append(int(line[next]))
        cost += int(line[next])
        i += 1
    string = "TotalCost= " + str(cost)
    costResult.append(string)
    return costResult

# if the user select choice one
def selectOne():
    try:
        while (1):
            start = int(input("Enter The Start Node:"))
            if start > 19 or start < 0:
                print("start node should be between 0 and 19")
            else:
                break
        while (1):
            numOfGoals = int(input("Enter The Number of The Goals:"))
            if numOfGoals < 1 or numOfGoals > 19:
                print("number of goals should be between 1 an 19")
            else:
                break
        for i in range(numOfGoals):
            print("Enter The Goal Number:", i + 1)
            goal = int(input())
            city1 = (readCity())[start]
            city2 = (readCity())[goal]
            string = "The path From " + str(city1) + " to " + str(city2)
            solu, visit = g_bd.BFS(start, goal)
            result.append(string)
            result.append(toCitys(solu))
            string = "The Cost From " + str(city1) + " to " + str(city2)
            result.append(string)
            result.append(getCostDfsBfs(solu))
            result.append("This is how The algorthm works and passes the visited node")
            result.append(visit)
            if start == goal:
                result.append("No visited node because the start and goal node is same")
            result.append("===========================================================================")
    except:
        print("Your input is wrong \nEnter a number only")
        print("=============================================================================")
    for i in result:
        print(i)

#if the user select the choice two
def selectTwo():
    try:
        while (1):
            start = int(input("Enter The Start Node:"))
            if start > 19 or start < 0:
                print("start node should be between 0 and 19")
            else:
                break
        while (1):
            numOfGoals = int(input("Enter The Number of The Goals:"))
            if numOfGoals < 1 or numOfGoals > 19:
                print("number of goals should be between 1 an 19")
            else:
                break
        for i in range(numOfGoals):
            print("Enter The Goal Number:", i + 1)
            goal = int(input())
            city1 = (readCity())[start]
            city2 = (readCity())[goal]
            string = "The path From " + str(city1) + " to " + str(city2)
            solu, visit = g_bd.DFS(start, goal)
            result.append(string)
            result.append(toCitys(solu))
            string = "The Cost From " + str(city1) + " to " + str(city2)
            result.append(string)
            result.append(getCostDfsBfs(solu))
            result.append("This is how The algorthm works and passes the visited node")
            result.append(visit)
            if start == goal:
                result.append("No visited node because the start and goal node is same")
            result.append("===========================================================================")

    except:
        print("Your input is wrong \nEnter a number only")
        print("=============================================================================")

    for i in result:
        print(i)

#if the user select the choice threeA
def selectThreeA():
    while (1):
        start = int(input("Enter The Start Node:"))
        if start > 19 or start < 0:
            print("start node should be between 0 and 19")
        else:
            break
    while (1):
        numOfGoals = int(input("Enter The Number of The Goals:"))
        if numOfGoals < 1 or numOfGoals > 19:
            print("number of goals should be between 1 an 19")
        else:
            break
    for i in range(numOfGoals):
        print("Enter The Goal Number:", i + 1)
        goal = int(input())
        city1 = (readCity())[start]
        city2 = (readCity())[goal]
        string = "The path From " + str(city1) + " to " + str(city2)
        solu, visit = g_star.aStarWalk(start, goal)
        result.append(string)
        result.append(toCitys(solu))
        string = "The Cost From " + str(city1) + " to " + str(city2)
        result.append(string)
        result.append(getCostDfsBfsNEWW(solu))
        result.append("This is how The algorthm works and passes the visited node")
        result.append(visit)
        if start == goal:
            result.append("No visited node because the start and goal node is same")
        result.append("===========================================================================")

    for i in result:
        print(i)

#select threeB
def selectThreeB():
    try:
        while (1):
            start = int(input("Enter The Start Node:"))
            if start > 19 or start < 0:
                print("start node should be between 0 and 19")
            else:
                break
        while (1):
            numOfGoals = int(input("Enter The Number of The Goals:"))
            if numOfGoals < 1 or numOfGoals > 19:
                print("number of goals should be between 1 an 19")
            else:
                break
        for i in range(numOfGoals):
            print("Enter The Goal Number:", i + 1)
            goal = int(input())
            city1 = (readCity())[start]
            city2 = (readCity())[goal]
            string = "The path From " + str(city1) + " to " + str(city2)
            solu, visit = g_star.aStarWalkAreal(start, goal)
            result.append(string)
            result.append(toCitys(solu))
            string = "The Cost From " + str(city1) + " to " + str(city2)
            result.append(string)
            result.append(getCostDfsBfs(solu))
            result.append("This is how The algorthm works and passes the visited node")
            result.append(visit)
            if start == goal:
                result.append("No visited node because the start and goal node is same")
            result.append("===========================================================================")
    except:
        print("Your input is wrong \nEnter a number only")
        print("=============================================================================")
    for i in result:
        print(i)

#select Four
def selectFour():
    try:
        while (1):
            start = int(input("Enter The Start Node:"))
            if start > 19 or start < 0:
                print("start node should be between 0 and 19")
            else:
                break
        while (1):
            numOfGoals = int(input("Enter The Number of The Goals:"))
            if numOfGoals < 1 or numOfGoals > 19:
                print("number of goals should be between 1 an 19")
            else:
                break
        for i in range(numOfGoals):
            print("Enter The Goal Number:", i + 1)
            goal = int(input())
            city1 = (readCity())[start]
            city2 = (readCity())[goal]
            string = "The path From " + str(city1) + " to " + str(city2)
            solu, visit = g_uni.ucs(start, goal)
            result.append(string)
            result.append(toCitys(solu))
            string = "The Cost From " + str(city1) + " to " + str(city2)
            result.append(string)
            result.append(getCostDfsBfs(solu))
            result.append("This is how The algorthm works and passes the visited node")
            result.append(visit)
            if start == goal:
                result.append("No visited node because the start and goal node is same")
            result.append("===========================================================================")
    except:
        print("Your input is wrong \nEnter a number only")
        print("=============================================================================")
    for i in result:
        print(i)

#print the citys name with node value
def getNodeName():
    readCity()
    result = []
    j = 0
    for i in readCity():
        string = str(j) + str(':') + str(i)
        result.append(string)
        j += 1
    print(result)


if __name__ == '__main__':
    g_bd = Graph()
    g_a = Graph()
    g_star = Graph()
    g_uni = Graph()
    readCarFile(g_bd)
    readCarFile(g_a)
    readCarFile(g_star)
    readCarFile(g_uni)
    result = []
    while (1):
        getNodeName()
        print("1-Bradth\n2-Depth\n3-A* \n4-Uniform Cost\n0-Exit ")
        try:
            select = int(input('Enter the number of operation:-\n'))
            print("=============================================================================")
            if select == 0:
                print("!!! EXIT DONE !!!")
                break
            elif select == 1:
                selectOne()
            elif select == 2:
                selectTwo()
            elif select == 3:
                print(
                    "1-A* for walking distance using Areal distance as the heuristic\n2-A* for driving distance using walk distance as the heuristic")
                select = int(input('Enter the number of operation:-\n'))
                if select == 1:
                    selectThreeA()
                else:
                    selectThreeB()
            elif select == 4:
                selectFour()
            else:
                print("You have to choose number between 0-3")
                print("=============================================================================")

        except:
            print("Your input is wrong \nEnter a number only")
            print("=============================================================================")