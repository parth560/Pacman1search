# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack() # creating a stack to explore the nodes in 
    visited = set()

    start_state = problem.getStartState()  # Get the initial state
    stack.push((start_state, []))  # Push the initial state onto the stack with empty actions

    # Continuing the search of the nodes still present in the stack using while loop 
    while not stack.isEmpty():
        current_state, actions = stack.pop()

        # Checking if the current state is the goal state
        if problem.isGoalState(current_state):
            return actions

        if current_state not in visited:
            visited.add(current_state)

            successors = problem.getSuccessors(current_state)

            for next_state, action, _ in successors:
                if next_state not in visited:
                    # Now pushing the next state and the list of actions which are being done
                    stack.push((next_state, actions + [action]))

    return []               
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue() # Creating the queue to manage the nodes which are needed to explored
    visited  = set()

    queue.push((problem.getStartState(), []))

    # To continue the search in the queue using while loop 
    while not queue.isEmpty():
        current_state, actions = queue.pop()

        # check if the current state is goal state 
        if problem.isGoalState(current_state):
            return actions
        
        if current_state not in visited:
            visited.add(current_state)

            successors = problem.getSuccessors(current_state)

            for next_state, action, _ in successors:
                if next_state not in visited:
                    # Now by pushing the next state, actions the new action to the queue.
                    queue.push((next_state, actions + [action]))
    return []                

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue() # Priority queue created to manage the order of the nodes to be explored
    visited = set()

    priority_queue.push((problem.getStartState(), [], 0), 0)
 
    # While loop to continue searching the nodes in the queue
    while not priority_queue.isEmpty():
        current_state, actions, cost = priority_queue.pop()

        # check if the current state is goal state
        if problem.isGoalState(current_state):
            return actions
        
        if current_state not in visited:
            visited.add(current_state)

            successors = problem.getSuccessors(current_state)

            # Now iterating through the successors
            for next_state, action, step_cost in successors:
                if next_state not in visited:
                     # Calculate the total cost to reach the successor
                    total_cost = cost + step_cost

                    # Pushing the successor, action state and total cost into the priority queue
                    priority_queue.push((next_state, actions + [action], total_cost), total_cost)

    return []            
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priority_queue = util.PriorityQueue() # Priority queue created to manage the order of the nodes to be explored
    visited = set()
    initial_state = problem.getStartState()

    # Calculating the priority of the initial state on the initial cost and heuristic
    priority_queue.push((initial_state, [], 0), 0 + heuristic(initial_state, problem))
    
    # While loop to continue searching the nodes in the queue
    while not priority_queue.isEmpty():
        current_state, actions, cost = priority_queue.pop()
        
        # check if the current state is goal state
        if problem.isGoalState(current_state):
            return actions
        
        if current_state not in visited:
            visited.add(current_state)
            successors = problem.getSuccessors(current_state)
            
            # Now iterating through the successors
            for next_state, action, step_cost in successors:
                if next_state not in visited:
                    # Calculate the total cost to reach the successor
                    total_cost = cost + step_cost

                    # Pushing the successor, action state and total cost into the priority queue
                    priority_queue.push((next_state, actions + [action], total_cost), total_cost + heuristic(next_state, problem))
    
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
