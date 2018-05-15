import maze
import maze_samples
import random

'''
 FILES:
 maze.py : maze class that can visualize a given maze with series of moves
 maze_samples.py : 2 data structures to hold a maze and length of dna strand
'''

'''
moves = ['U','D','R','L']
stands for: up, down, right, left

grid contents = ['x', '-', 'C', 'M']
stands for: blocked, open, cheese, mouse (initial position)

maze: a maze is a rowxcol grid
You start out where the mouse is and follow the moves.
For example, if the mouse is at maze[3][4] and the move is up,
then move the mouse up one row to maze[4][4]
'''


'''
# In our version of the GA using the fitness function described below,
# A population size of 1000 that ran for a few generations 
# converged for maze_sample[1] - meaning found the cheese.
# For maze_sample[0] - still hadn't converged after 1000 generations.

Genetic Algorithm Logic
  choose how many individuals to put in a population
  choose how many generations you want to evolve the population
  population = create a new population of random individuals
  for g generations or until the cheese is found:
    for p in population:
      calculate fitness of individual p
    new generation = []
    for p in size of population // 2:
      # See Code below for Monte Carlo Selection
      parent1 = select using monte carlo based on fitness
      parent2 = select using monte carlo based on fitness
      new_individual1, new_individual2 = cross-breed parent1 with parent2
      if mutate:
        randomly change 1 move in new individual
      add new individuals to new generation
'''




'''
INDIVIDUAL / Mouse / Series of Moves:
  An individual is a string of moves (i.e. chromosomes in GA vocab).
  The string should be of length maze_samples.string_length[test_case].
  For example, for maze_samples.maze[1], an individual has length 20.
  Initialize the individual (mouse) with a series of moves:
    for example, a mouse dna might start out as 'UULDRDDLLLUURRD...'
  The fitness of an individual is made up by the designer of the genetic algorithm
  and has some relationship to the problem being solved.
  A suggested fitness function for this problem is below.
  You can use this fitness measure or make up your own.
  You can also experiment with the length of the string, which might impact convergence.
'''

'''
Fitness Function Logic
  - count how many of the moves are in open places on the maze (if it makes it to
       the cheese, use the length of the string.
  - count how many moves the mouse makes before being blocked or going off maze
  - if the last location is on the cheese, add as many points as the length of the string
  - fitness is the sum of these two numbers
  - IF MOVE is not to open space, ignore the move
  - The mouse will probably evolve better if you add in some fitness points related
        to how close the last position of the mouse is to the cheese
'''

'''
Cross Breed Logic
  b = randomly select a break point in the dna strand
  make new individual based on parent1[0:b] + parent2[b:]
  make new individual based on parent2[0:b] + parent1[b:]
'''

'''
Mutate Logic
  if random number < mutate rate then mutate individual
  if mutate individual
    idx = randomly select a move in the string of moves
    m = randomly select one of the 4 moves
    individual[idx] = m # note this shows logic, not proper syntax
'''

def SetWeightsForMonteCarloSelection(values):
  # Take a list of values
  # Normalize using sum(values)
  # Transform each value to rounded integer
  # The greater this value, the more likely to be selected (a weighting)
  # Transform values to accumulated selection weights
  normalized_values = [int(v/sum(values)*100+.5) for v in values]
  accum = 0
  selection_weights = []
  for w in normalized_values:
    accum += w
    selection_weights.append(accum)
  return selection_weights

def MonteCarloSelection(selection_weights):
  selection = random.randint(0,selection_weights[-1])
  for i,w in enumerate(selection_weights):
    if selection <= w:
      return i

# This uses the above code so that you can see how it works.
population_size = 12
L = [ 10, 8, 7, 7, 5, 4, 3, 2, 2, 1, 1, 0]
S = SetWeightsForMonteCarloSelection(L)
print(S)
for i in range(population_size//2):
  # Weighted random selection with replacement of parents
  p1 = MonteCarloSelection(S)
  p2 = MonteCarloSelection(S)
  print('Parents ',p1,' ',p2)


  

