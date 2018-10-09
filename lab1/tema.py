"""Lista algoritmi

A. Stratgeii de cautare neinformate:

   a.Blind Search:
    Foloseste doar informatii existente in definirea problemei
    Nodul poate fi:
        necunoscut-nodul apartine partii neexplorare a spatiului de cautare
        evaluat - nodul este cunoscut dar fie nu se cunoaste nici un succesor al lui fie se cunosc doar o parte din succesori lui
        extins - nodul este cunoscut si se cunosc toti succesori lui

    In procesul de cautare se for folosi doua liste:
        -Frontiera- lista nodurilor evaluate
        -Teritoriu- lista nodurilor extinse


    1.  Breadth First Search (Cautare pe nivel)
    2.  Uniform Cost Search
    3.  Depth First Search(Cautare in adancime)
    4.  Depth-limited search
    5.  Iterative deeping search.
    
     #def cost(self,state,action,state2):
        #return 1 
    #NOTE: this is used only for algorithms that consider the cost of action( uniform search cost ) 

     #def heuristic(self,state):
        #how far are we from the goal?
        #wrong = sum([i if state[i] != GOAL[i] else 0
        #                for i in range(len(state))])
        #missing = len(GOAL) - len(state)
        #return wrong + missing

     #NOTE: this is used only for algorithms that are informed( A* or greedy search



    #NOTE: method cost has to recive two states and an action, it shall return the cost of applying the action from the first state to the second state

    #NOTE: method heuristic recives a state, and must return an interget value of the estimation of the remaining cost from that state to the solution
    REFER TO AIM on how to build heuristics


    #NOTE: finally, to create an instance of the problem that can be used on search algorithms.
    the Problem class initializer recives one paramtere: the inital state, from where the search will begin

    myproblem=NameOfTheProblem(initial_state='')

    Graful testat cu fiecare algoritm

         A
       / |  \
      B - E - C
      |  /  / | \
      J  D  F G  H
     / \ /
    I   K



         A
       / | \
      B - E  C
      | /   /  \
      D     F   G  
     
    
    """

#=============================================
#               Imports
#=============================================

from simpleai.search import SearchProblem, astar
#import simpleai.search.traditional
#=============================================
#               Variables
#============================================= 
# sample graph implemented as a dictionary
graph1 = {
         'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C'],
         'H': [' '],
         'I': [' '],
         'J': [' '],
         'K': [' ']
         }         


graph2 = {
         'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']
         }


print "*********************"
print "First Problem"
print "*********************"

GOAL = 'COSMA DRAGOS'

class Nume(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        # how far are we from the goal?
        wrong = sum([1 if state[i] != GOAL[i] else 0
                    for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing

problem = Nume(initial_state='')
result = astar(problem)

print(result.state)
print(result.path())
 
print "*********************"
print       "Done"
print "*********************"


print "===================="
print "Breadth First Search"
print "===================="

GOAL = 'COSMA DRAGOS'

class TestBreadthFirst(SearchProblem):
    def actions(self, state):
        if len(state) < len(GOAL):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        # how far are we from the goal?
        wrong = sum([1 if state[i] != GOAL[i] else 0
                    for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing

problem = TestBreadthFirst(initial_state='')
result = breadth_first(problem)

print(result.state)
print(result.path())

print "*********************"
print       "Done"
print "*********************"
def breadthFirst():
    pass
