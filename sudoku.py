#!/usr/bin/env python3

from itertools import combinations
import time

def sampleToughPuzzle():

### Blank puzzle
## ----------- || 1 | 2 | 3 | 4|| 5 | 6 | 7 | 8|| 9 |10 |11 |12||13 |14 |15 |16||
#  puzzle[0]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[1]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[2]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[3]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
## ----------- ||---|---|---|--||---|---|---|--||---|---|---|--||---|---|---|--||
#  puzzle[4]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[5]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[6]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[7]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
## ----------- ||---|---|---|--||---|---|---|--||---|---|---|--||---|---|---|--||
#  puzzle[8]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[9]  = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[10] = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[11] = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
## ----------- ||---|---|---|--||---|---|---|--||---|---|---|--||---|---|---|--||
#  puzzle[12] = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[13] = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[14] = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#  puzzle[15] = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
## ----------- ||---|---|---|--||---|---|---|--||---|---|---|--||---|---|---|--||


  puzzle = [[] for z in range(16)]

# ----------- || 1 | 2 | 3 | 4|| 5 | 6 | 7 | 8|| 9 |10 |11 |12||13 |14 |15 |16||
  puzzle[0]  = [' ',' ',' ',' ','c',' ',' ',' ',' ',' ',' ','g',' ',' ','b',' ']
  puzzle[1]  = ['1',' ','3','e','b','6',' ',' ',' ',' ',' ',' ','2','4','a',' ']
  puzzle[2]  = [' ','c','a','d',' ',' ','2',' ',' ',' ',' ',' ','3',' ',' ',' ']
  puzzle[3]  = ['2',' ',' ',' ','1',' ','5','f',' ','6','a','b',' ',' ',' ',' ']
# ----------- ||---|---|---|--||---|---|---|--||---|---|---|--||---|---|---|--||
  puzzle[4]  = [' ','d',' ','8','g','7','c',' ',' ','e',' ',' ',' ','9','f',' ']
  puzzle[5]  = [' ',' ',' ',' ',' ',' ',' ','2',' ',' ','4',' ','e',' ',' ',' ']
  puzzle[6]  = [' ',' ','4','5',' ','8','e',' ','g',' ','1','9',' ','3','6',' ']
  puzzle[7]  = [' ',' ',' ','f','d','5',' ','3','a','c',' ',' ',' ',' ',' ',' ']
# ----------- ||---|---|---|--||---|---|---|--||---|---|---|--||---|---|---|--||
  puzzle[8]  = ['5',' ',' ','a',' ','f','8',' ',' ','d',' ',' ',' ',' ',' ','4']
  puzzle[9]  = [' ',' ',' ','1','3',' ','a',' ','b','5','7',' ',' ','d',' ',' ']
  puzzle[10] = ['9','4','8','b','2',' ',' ',' ',' ',' ',' ','f',' ','5',' ','1']
  puzzle[11] = [' ',' ',' ',' ','7','g',' ',' ',' ',' ',' ',' ',' ','8',' ','9']
# ----------- ||---|---|---|--||---|---|---|--||---|---|---|--||---|---|---|--||
  puzzle[12] = [' ','f',' ',' ',' ',' ',' ',' ','c','2',' ',' ',' ',' ',' ',' ']
  puzzle[13] = [' ','6',' ',' ',' ','b','g',' ',' ','7',' ',' ','d',' ',' ','3']
  puzzle[14] = [' ','e',' ','c',' ',' ',' ',' ',' ',' ',' ','5','g','7','2',' ']
  puzzle[15] = [' ',' ',' ',' ',' ',' ',' ','1','8',' ',' ',' ',' ',' ','9','c']
# ----------- ||---|---|---|--||---|---|---|--||---|---|---|--||---|---|---|--||
  for i in range(16):
    for j in range(16):
      if puzzle[i][j] in "123456789aAbBcCdDeEfFgG":
        soloFound("Sample Puzzle", i, j, str(puzzle[i][j]))

def getMaxColumnWidth():

  width = [1 for z in range(16)]
  for i in range(16):
    for j in range(16):
      width[i] = max(width[i], len(Matrix[j][i]))
  return width

def uniqueQuadCellRow(cell,y_quad,unique_set):

  global changes
  y = (cell // 4) * 4 + y_quad
  x_quad = cell % 4
  for quad in range(4):
    if (quad != x_quad):
      for x in range(quad*4, (quad*4)+4):
        for i in unique_set:
          if i in Matrix[y][x]:
            Matrix[y][x].remove(i)
            changes += 1
            print("QuadCellRow-Removing " +str(i)+" from: "+str(y+1)+","+str(x+1))

def uniqueQuadCellCol(cell,x_quad,unique_set):

  global changes
  x = (cell % 4) * 4 + x_quad
  y_quad = cell // 4
  for quad in range(4):
    if (quad != y_quad):
      for y in range(quad*4, (quad*4)+4):
        for i in unique_set:
          if i in Matrix[y][x]:
            Matrix[y][x].remove(i)
            changes += 1
            print("QuadCellCol-Removing " +str(i)+" from: "+str(y+1)+","+str(x+1))

def uniqueQuadRow(row,x_quad,unique_set):

  global changes
  cell, first_row, first_col = determineCell(row,x_quad*4)
  for y in range(first_row, first_row+4):
    if (y != row):
      for x in range(first_col, first_col+4):
        for i in unique_set:
          if i in Matrix[y][x]:
            Matrix[y][x].remove(i)
            changes += 1
            print("QuadRow-Removing " +str(i)+" from: "+str(y+1)+","+str(x+1))
            
def uniqueQuadCol(col,y_quad,unique_set):

  global changes
  cell, first_row, first_col = determineCell(y_quad*4,col)
  for x in range(first_col, first_col+4):
    if (x != col):
      for y in range(first_row, first_row+4):
        for i in unique_set:
          if i in Matrix[y][x]:
            Matrix[y][x].remove(i)
            changes += 1
            print("QuadCol-Removing " +str(i)+" from: "+str(y+1)+","+str(x+1))
            
def soloFound(where, y, x, z):

  if z in "abcdefg":
    if len(z) == 1:
      z = z.capitalize()
  if z in "123456789ABCDEFG" and len(z) == 1:
    z = str(z)
    Matrix[y][x] = [z]
    clearRow(y,x,z)
    clearCol(y,x,z)
    clearCube(y,x,z)

def checkNotFoundVariables():

  global changes
  not_found_row = [[] for i in range(16)]
  not_found_col = [[] for i in range(16)]
  not_found_cell = [[] for i in range(16)]
  alpha_set = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G']
  for alpha in alpha_set:
    for i in range(16):
      not_found_row[i].append(alpha)
      not_found_col[i].append(alpha)
      not_found_cell[i].append(alpha)
  for y in range(16):
    for x in range(16):
      if (len(Matrix[y][x]) == 1):
        z = Matrix[y][x][0]
        cell = ((y // 4) * 4) + (x // 4)
        if z in not_found_row[y]:
          not_found_row[y].remove(z)
          changes += 1
        if z in not_found_col[x]:
          not_found_col[x].remove(z)
          changes += 1
        if z in not_found_cell[cell]:
          not_found_cell[cell].remove(z)
          changes += 1
  return not_found_row, not_found_col, not_found_cell

def clearRow(y,x,z):

  global changes
  if z not in found_row[y]:
    found_row[y].append(z)
    changes += 1
    print("clearRow-Adding " +str(z)+" to found_row["+str(y+1)+"]")
  if z in not_found_row[y]:
    not_found_row[y].remove(z)
    changes += 1
    print("clearRow-Removing " +str(z)+" from not_found_row["+str(y+1)+"]")
  for i in range(16):
    if z in Matrix[y][i] and i != x:
      Matrix[y][i].remove(z)
      changes += 1
      print("clearRow-Removing " +str(z)+" from: "+str(y+1)+","+str(i+1))

def clearCol(y,x,z):
  
  global changes
  if z not in found_col[x]:
    found_col[x].append(z)
    changes += 1
    print("clearCol-Adding " +str(z)+" to found_col["+str(x+1)+"]")
  if z in not_found_col[x]:
    not_found_col[x].remove(z)
    changes += 1
    print("clearCol-Removing " +str(z)+" from not_found_col["+str(x+1)+"]")
  for i in range(16):
    if z in Matrix[i][x] and i != y:
      Matrix[i][x].remove(z)
      changes += 1
      print("clearCol-Removing " +str(z)+" from: "+str(i+1)+","+str(x+1))

def clearCube(y1,x1,z):

  global changes
  cell, first_row, first_col = determineCell(y1,x1)
  if z not in found_cell[cell]:
    found_cell[cell].append(z)
    changes += 1
    print("clearCube-Adding "+str(z)+" to found_cell:"+str(cell+1
          )+" for: "+str(y1+1)+","+str(x1+1))
  if z in not_found_cell[cell]:
    not_found_cell[cell].remove(z)
    changes += 1
    print("clearCube-Removing "+str(z)+" from not_found_cell:"+str(cell+1
          )+" for: "+str(y1+1)+","+str(x1+1))
  for y in range(first_row, first_row+4):
    for x in range(first_col, first_col+4):
      if z in Matrix[y][x] and x != x1 and y != y1:
        Matrix[y][x].remove(z)
        changes += 1
        print("clearCube-Removing " +str(z)+" from: "+str(y+1)+","+str(x+1))

def determineCell(y,x):

  cell = ((y // 4) * 4) + (x // 4)
  first_row = (cell // 4) * 4
  first_col = (cell % 4) * 4
  return cell, first_row, first_col

def searchRowForSolo(y):

  for x in range(16):
    if len(Matrix[y][x]) == 1:
      z = Matrix[y][x][0]
      soloFound("row", y, x, z)

def searchColForSolo(x):

  for y in range(16):
    if len(Matrix[y][x]) == 1:
      z = Matrix[y][x][0]
      soloFound("col", y, x, z)

def searchCubeForSolo(cell):

  first_row = (cell // 4) * 4
  first_col = (cell % 4) * 4
  for y in range(first_row, first_row+4):
    for x in range(first_col, first_col+4):
      if len(Matrix[y][x]) == 1:
        z = Matrix[y][x][0]
        soloFound("cell", y, x, z)

def searchRowForSingle(y):

  full_set = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G']
  for z in full_set:
    count = 0
    for x in range(16):
      if z in Matrix[y][x]:
        count += 1
        x_found = x
    if count == 1:
      soloFound("row", y, x_found, z)

def searchColForSingle(x):

  full_set = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G']
  for z in full_set:
    count = 0
    for y in range(16):
      if z in Matrix[y][x]:
        count += 1
        y_found = y
    if count == 1:
      soloFound("col", y_found, x, z)
      
def searchCubeForSingle(cell):

  first_row = (cell // 4) * 4
  first_col = (cell % 4) * 4
  full_set = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G']
  for z in full_set:
    count = 0
    for y in range(first_row, first_row+4):
      for x in range(first_col, first_col+4):
        if z in Matrix[y][x]:
          count += 1
          y_found = y
          x_found = x
    if count == 1:
      soloFound("cell", y_found, x_found, z)

###
### START OF MAIN PROGRAM
###

###
### Declare main variables (Matrix[][], found_row[], found_col[], found_cell[],
###     not_found_row[], not_found_col[], not_found_cell[], changes)
###

Matrix = [[[] for x in range(16)] for y in range(16)]
alpha_set = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G']
for alpha in alpha_set:
  for y in range(16):
    for x in range(16):
      Matrix[y][x].append(alpha)
found_row = [[] for i in range(16)]
found_col = [[] for i in range(16)]
found_cell = [[] for i in range(16)]
not_found_row = [[] for i in range(16)]
not_found_col = [[] for i in range(16)]
not_found_cell = [[] for i in range(16)]
for alpha in alpha_set:
  for i in range(16):
    not_found_row[i].append(alpha)
    not_found_col[i].append(alpha)
    not_found_cell[i].append(alpha)
search_set = []
changes = 0

###
### Use either the sample puzzle provided (for debugging) OR the keyboard
### puzzle input method to enter your puzzle to be solved
###
"""
###
### Keyboard puzzle input method (remove and use sample puzzle for debugging)
###
for y in range(16):
  for x in range(16):
    value = str(input("Value (1-9, a-g or A-G) for " + str(y+1) + "," + str(x+1) + ": "))
    if value in "123456789aAbBcCdDeEfFgG":
      soloFound("INITIALIZATION", y, x, str(value))
"""

###
### Sample puzzle method (for debugging; remove if input is from keyboard)
###
sampleToughPuzzle()

start = time.perf_counter()
loop = 1
while loop < 40:

###
### Beginning of loop
###
  
  print("Changes = " + str(changes))
  changes = 0
  rows_done = 0
  print("Loop #" + str(loop))

###
### Print puzzle's current state in a simple grid
###
  
  max_width = getMaxColumnWidth()
  line_length = sum(max_width) * 2 + 38
  for i in range(16):
    if not i%4:
      print("        " + "-"*line_length)
    print("Row %2s: || " % (str(i+1)), end='') 
    for j in range(16):
      col_max = int(max_width[j]) * 2 - 1
      if (j+1) % 4:
        print("{:^{w}}".format(','.join(Matrix[i][j]), w=col_max), end = ' | ')
      else:
        print("{:^{w}}".format(','.join(Matrix[i][j]), w=col_max), end = ' || ')
    print()
    if len(found_row[i]) == 16:
      rows_done += 1
  print("        " + "-"*line_length)
  print("ROWS DONE: " + str(rows_done))

###
### Quit program once all rows have been resolved
###
  
  if (rows_done == 16):
    loop = 100
    stop = time.perf_counter()
    print("Elapsed time: " + str(stop - start))
    break

###
### Sorting and printing resolved squares in each row, column and cell
###
  """
  for i in range(16):
    found_row[i].sort()
    found_col[i].sort()
    found_cell[i].sort()
    nonot_found = list(set(alpha_set) - set(found_row[i]))
    nonot_found.sort()
    print("Row %3d - Found: " %(i+1) + ','.join(found_row[i]), end = ' === ')
    print("Not Found: " + ','.join(nonot_found))
  for i in range(16):
    nonot_found = list(set(alpha_set) - set(found_col[i]))
    nonot_found.sort()
    print("Col %3d - Found: " %(i+1) + ','.join(found_col[i]), end = ' === ')
    print("Not Found: " + ','.join(nonot_found))
  for i in range(16):
    nonot_found = list(set(alpha_set) - set(found_cell[i]))
    nonot_found.sort()
    print("Cell %2d - Found: " %(i+1) + ','.join(found_cell[i]), end = ' === ')
    print("Not Found: " + ','.join(nonot_found))
  """

###
### Primary algorithms (run on every pass)
###

  for y in range(16):
    searchRowForSolo(y)
    searchRowForSingle(y)
  for x in range(16):
    searchColForSolo(x)
    searchColForSingle(x)
  for cell in range(16):
    searchCubeForSolo(cell)
    searchCubeForSingle(cell)

###
### Secondary algorithms (run only if primary ones are unsuccessful)
###

  if (changes == 0):
    print("Changes = " + str(changes) + ".  Primary algorithms unsuccessful.")
    print("Trying secondary algorithms.")

    ###
    ### Secondary algorithm for rows
    ###
    for y in range(16):
      quad_set = [set(), set(), set(), set()]
      for quad in range(4):
        for x in range(quad*4,(quad+1)*4):
          if len(Matrix[y][x]) > 0:
            for z in Matrix[y][x]:
              quad_set[quad].add(z)
      if unique_set := quad_set[0] - quad_set[1] - quad_set[2] - quad_set[3]:
        uniqueQuadRow(y,0,unique_set)
      if unique_set := quad_set[1] - quad_set[0] - quad_set[2] - quad_set[3]:
        uniqueQuadRow(y,1,unique_set)
      if unique_set := quad_set[2] - quad_set[0] - quad_set[1] - quad_set[3]:
        uniqueQuadRow(y,2,unique_set)
      if unique_set := quad_set[3] - quad_set[0] - quad_set[1] - quad_set[2]:
        uniqueQuadRow(y,3,unique_set)

    ###
    ### Secondary algorithm for columns
    ###
    for x in range(16):
      quad_set = [set(), set(), set(), set()]
      for quad in range(4):
        for y in range(quad*4,(quad+1)*4):
          if len(Matrix[y][x]) > 0:
            for z in Matrix[y][x]:
              quad_set[quad].add(z)
      if unique_set := quad_set[0] - quad_set[1] - quad_set[2] - quad_set[3]:
        uniqueQuadCol(x,0,unique_set)
      if unique_set := quad_set[1] - quad_set[0] - quad_set[2] - quad_set[3]:
        uniqueQuadCol(x,1,unique_set)
      if unique_set := quad_set[2] - quad_set[0] - quad_set[1] - quad_set[3]:
        uniqueQuadCol(x,2,unique_set)
      if unique_set := quad_set[3] - quad_set[0] - quad_set[1] - quad_set[2]:
        uniqueQuadCol(x,3,unique_set)

    ###
    ### Secondary algorithm for horizontal clump of each cell
    ###
    for cell in range(16):
      first_row = (cell // 4) * 4
      first_col = (cell % 4) * 4
      quad_set = [set(), set(), set(), set()]
      quad = 0
      for y in range(first_row, first_row+4):
        for x in range(first_col, first_col+4):
          for z in Matrix[y][x]:
            quad_set[quad].add(z)
        quad += 1
      if unique_set := quad_set[0] - quad_set[1] - quad_set[2] - quad_set[3]:
        uniqueQuadCellRow(cell,0,unique_set)
      if unique_set := quad_set[1] - quad_set[0] - quad_set[2] - quad_set[3]:
        uniqueQuadCellRow(cell,1,unique_set)
      if unique_set := quad_set[2] - quad_set[0] - quad_set[1] - quad_set[3]:
        uniqueQuadCellRow(cell,2,unique_set)
      if unique_set := quad_set[3] - quad_set[0] - quad_set[1] - quad_set[2]:
        uniqueQuadCellRow(cell,3,unique_set)
          
    ###
    ### Secondary algorithm for vertical clump of each cell
    ###
    for cell in range(16):
      first_row = (cell // 4) * 4
      first_col = (cell % 4) * 4
      quad_set = [set(), set(), set(), set()]
      quad = 0
      for x in range(first_col, first_col+4):
        for y in range(first_row, first_row+4):
          for z in Matrix[y][x]:
            quad_set[quad].add(z)
        quad += 1
      if unique_set := quad_set[0] - quad_set[1] - quad_set[2] - quad_set[3]:
        uniqueQuadCellCol(cell,0,unique_set)
      if unique_set := quad_set[1] - quad_set[0] - quad_set[2] - quad_set[3]:
        uniqueQuadCellCol(cell,1,unique_set)
      if unique_set := quad_set[2] - quad_set[0] - quad_set[1] - quad_set[3]:
        uniqueQuadCellCol(cell,2,unique_set)
      if unique_set := quad_set[3] - quad_set[0] - quad_set[1] - quad_set[2]:
        uniqueQuadCellCol(cell,3,unique_set)
          
###
### Tertiary algorithms (run only if secondary ones are unsuccessful)
### :: Look for combinations of 2 to 4 unfound values 'range(2,5)'
### :: since tests showed that to be the fastest.  But if this
### :: program fails to solve a future puzzle, increase the range.
###

  ###
  ### Tertiary algorithm for rows
  ###

  if (changes == 0):
    print("Changes = " + str(changes) + ".  Secondary algorithms unsuccessful.")
    print("Trying tertiary algorithms.")
    for y in range(16):
      row_set = [set(),set(),set(),set(),set(),set(),set(),set(
               ),set(),set(),set(),set(),set(),set(),set(),set()]
      for x in range(16):
        row_set[x] = set(Matrix[y][x])
      #not_found_row, not_found_col, not_found_cell = checkNotFoundVariables()
      for size in range(2,5):
        search_list = list(combinations(not_found_row[y],size))
        for search_item in search_list:
          found = 0
          for x in range(16):
            if len(row_set[x])<=size and not(row_set[x]-set(search_item)):
              found += 1
          if found == size:
            for x in range(16):
              if (row_set[x] - set(search_item)) and (
                   row_set[x] & set(search_item)):
                for z in search_item:
                  if z in row_set[x]:
                    row_set[x].remove(z)
                    Matrix[y][x].remove(z)
                    changes += 1
                    print("row_set-Removing " +str(z)+" from: "+str(y+1
                           )+","+str(x+1)+" for row_set: "+str(row_set[x]
                           )+" and search_item: "+str(search_item))

  ###
  ### Tertiary algorithm for columns
  ###

  if (changes == 0):
    for x in range(16):
      col_set = [set(),set(),set(),set(),set(),set(),set(),set(
               ),set(),set(),set(),set(),set(),set(),set(),set()]
      for y in range(16):
        col_set[y] = set(Matrix[y][x])
      #not_found_row, not_found_col, not_found_cell = checkNotFoundVariables()
      for size in range(2,5):
        search_list = list(combinations(not_found_col[x],size))
        for search_item in search_list:
          found = 0
          for y in range(16):
            if len(col_set[y])<=size and not(col_set[y]-set(search_item)):
              found += 1
          if found == size:
            for y in range(16):
              if (col_set[y] - set(search_item)) and (
                   col_set[y] & set(search_item)):
                for z in search_item:
                  if z in col_set[y]:
                    col_set[y].remove(z)
                    Matrix[y][x].remove(z)
                    changes += 1
                    print("col_set-Removing " +str(z)+" from: "+str(y+1
                           )+","+str(x+1)+" for col_set: "+str(col_set[y]
                           )+" and search_item: "+str(search_item))

  ###
  ### Tertiary algorithm for cells
  ###

  if (changes == 0):
    for cell in range(16):
      cell_set = [set(),set(),set(),set(),set(),set(),set(),set(
                ),set(),set(),set(),set(),set(),set(),set(),set()]
      first_row = (cell // 4) * 4
      first_col = (cell % 4) * 4
      for y in range(first_row, first_row+4):
        for x in range(first_col, first_col+4):
          i = (y % 4) * 4 + (x % 4)
          cell_set[i] = set(Matrix[y][x])
      #not_found_row, not_found_col, not_found_cell = checkNotFoundVariables()
      for size in range(2,5):
        search_list = list(combinations(not_found_cell[cell],size))
        for search_item in search_list:
          found = 0
          for i in range(16):
            if len(cell_set[i])<=size and not(cell_set[i]-set(search_item)):
              found += 1
          if found == size:
            for i in range(16):
              if (cell_set[i] - set(search_item)) and (
                   cell_set[i] & set(search_item)):
                for z in search_item:
                  if z in cell_set[i]:
                    cell_set[i].remove(z)
                    y = (cell // 4) * 4 + (i // 4)
                    x = (cell % 4) * 4 + (i % 4)
                    Matrix[y][x].remove(z)
                    changes += 1
                    print("cell_set-Removing " +str(z)+" from: "+str(y+1
                           )+","+str(x+1)+" for cell_set: "+str(cell_set[i]
                           )+" and search_item: "+str(search_item))
          
  loop += 1
