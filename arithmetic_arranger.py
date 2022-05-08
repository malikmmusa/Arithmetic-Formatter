import re

def arithmetic_arranger(problems, solve=None):
  if len(problems) > 5: return 'Error: Too many problems.' 
  topNum = []
  bottomNum = []
  lines = []
  solutions = []
  
  for problem in problems:
    problem = problem.split()
    
    if re.search("\D+", problem[0]) or re.search("\D+", problem[2]): return 'Error: Numbers must only contain digits.'
    if problem[1] != '+' and problem[1] != '-': return "Error: Operator must be '+' or '-'."
    if len(problem[0]) > 4 or len(problem[2]) > 4: return 'Error: Numbers cannot be more than four digits.'

    if problem[1] == '+': solved = str(int(problem[0]) + int(problem[2]))
    else: solved = str(int(problem[0]) - int(problem[2]))
    solvedLength = len(solved)
    
    if (len(problem[0]) > len(problem[2])): 
      longerLength = len(problem[0]) 
      shorterLength = len(problem[2]) 
      topSpaces = 2
      bottomSpaces = 1 + (longerLength - shorterLength)
    elif (len(problem[0]) < len(problem[2])): 
      longerLength = len(problem[2])
      shorterLength = len(problem[0]) 
      topSpaces = 2 + (longerLength - shorterLength)
      bottomSpaces = 1
    else:
      topSpaces = 2
      bottomSpaces = 1
      longerLength = shorterLength = len(problem[2])

    solvedSpaces = (longerLength + 2) - solvedLength
      
    if not topNum: topNum.append((' ' * topSpaces) +  problem[0])
    else: topNum.append('    ' + (' ' * topSpaces) +  problem[0])

    if not bottomNum: bottomNum.append(problem[1] + (' ' * bottomSpaces) +  problem[2])
    else: bottomNum.append('    ' + problem[1] + (' ' * bottomSpaces) +  problem[2])

    if not lines: lines.append('-' * (longerLength + 2))
    else: lines.append('    ' + ('-' * (longerLength + 2)))

    if not solutions: solutions.append((' ' * solvedSpaces) + solved)
    else: solutions.append('    ' + (' ' * solvedSpaces) + solved)

  if solve: return ''.join(topNum) + '\n' + ''.join(bottomNum) + '\n' + ''.join(lines) + '\n' + ''.join(solutions)
  else: return ''.join(topNum) + '\n' + ''.join(bottomNum) + '\n' + ''.join(lines)
  