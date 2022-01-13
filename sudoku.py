#!/usr/bin/env python3

from itertools import combinations

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

  Matrix[y][x] = [z]
  clearRow(y,x,z)
  clearCol(y,x,z)
  clearCube(y,x,z)

def checkNotFoundVariables():

  global changes
  not_found_row = [list(range(1,17)) for i in range(16)]
  not_found_col = [list(range(1,17)) for i in range(16)]
  not_found_cell = [list(range(1,17)) for i in range(16)]
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
    if ((z in Matrix[y][i]) and (i != x)):
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
    if ((z in Matrix[i][x]) and (i != y)):
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
      if ((z in Matrix[y][x]) and (x != x1) and (y != y1)):
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
    if (len(Matrix[y][x]) == 1):
      z = Matrix[y][x][0]
      soloFound("row", y, x, z)

def searchColForSolo(x):

  for y in range(16):
    if (len(Matrix[y][x]) == 1):
      z = Matrix[y][x][0]
      soloFound("col", y, x, z)

def searchCubeForSolo(cell):

  first_row = (cell // 4) * 4
  first_col = (cell % 4) * 4
  for y in range(first_row, first_row+4):
    for x in range(first_col, first_col+4):
      if (len(Matrix[y][x]) == 1):
        z = Matrix[y][x][0]
        soloFound("cell", y, x, z)

def searchRowForSingle(y):

  for z in range(1,17):
    count = 0
    for x in range(16):
      if (z in Matrix[y][x]):
        count += 1
        x_found = x
    if (count == 1):
      soloFound("row", y, x_found, z)

def searchColForSingle(x):

  for z in range(1,17):
    count = 0
    for y in range(16):
      if (z in Matrix[y][x]):
        count += 1
        y_found = y
    if (count == 1):
      soloFound("col", y_found, x, z)
      
def searchCubeForSingle(cell):

  first_row = (cell // 4) * 4
  first_col = (cell % 4) * 4
  for z in range(1,17):
    count = 0
    for y in range(first_row, first_row+4):
      for x in range(first_col, first_col+4):
        if (z in Matrix[y][x]):
          count += 1
          y_found = y
          x_found = x
    if (count == 1):
      soloFound("cell", y_found, x_found, z)

Matrix = [[list(range(1,17)) for x in range(16)] for y in range(16)]
found_row = [[] for i in range(16)]
found_col = [[] for i in range(16)]
found_cell = [[] for i in range(16)]
not_found_row = [list(range(1,17)) for i in range(16)]
not_found_col = [list(range(1,17)) for i in range(16)]
not_found_cell = [list(range(1,17)) for i in range(16)]
search_set = []
changes = 0
for y in range(16):
  for x in range(16):
    value = str(input("Value for " + str(y+1) + "," + str(x+1) + ": "))
    if (value.isdigit() and (int(value) in range(1,10))):
      soloFound("INITIALIZATION", y, x, int(value))
    elif (value == "a"):
      soloFound("INITIALIZATION", y, x, int(10))
    elif (value == "b"):
      soloFound("INITIALIZATION", y, x, int(11))
    elif (value == "c"):
      soloFound("INITIALIZATION", y, x, int(12))
    elif (value == "d"):
      soloFound("INITIALIZATION", y, x, int(13))
    elif (value == "e"):
      soloFound("INITIALIZATION", y, x, int(14))
    elif (value == "f"):
      soloFound("INITIALIZATION", y, x, int(15))
    elif (value == "g"):
      soloFound("INITIALIZATION", y, x, int(16))

level = 1
loop = 1
while loop < 20:
  print("Previous Changes = " + str(changes) + " and level = " + str(level))
  changes = 0
  rows_done = 0
  print("Loop #" + str(loop))
  for i in range(16):
    print("Row "+str(i+1)+": "+str(Matrix[i])) 
    found_row[i].sort()
    found_col[i].sort()
    found_cell[i].sort()
    if (len(found_row[i]) == 16):
      rows_done += 1
  print("ROWS DONE: " + str(rows_done))
  if (rows_done == 16):
    loop = 100
    break
  print("Found row " + str(found_row))
  print("Found col " + str(found_col))
  print("Found cell " + str(found_cell))

  for y in range(16):
    searchRowForSolo(y)
    searchRowForSingle(y)
  for x in range(16):
    searchColForSolo(x)
    searchColForSingle(x)
  for cell in range(16):
    searchCubeForSolo(cell)
    searchCubeForSingle(cell)

  if ((changes < 5) and (level == 1)):
    level = 2
    print("Changes = " + str(changes) + " and level = " + str(level))
    print("Adding in next level of logic")
  if (level == 2):
    for y in range(16):
      quad_set = [set(), set(), set(), set()]
      for quad in range(4):
        for x in range(quad*4,(quad+1)*4):
          if (len(Matrix[y][x]) > 0):
            for z in Matrix[y][x]:
              quad_set[quad].add(z)
      if (unique_set := quad_set[0] - quad_set[1] - quad_set[2] - quad_set[3]):
        uniqueQuadRow(y,0,unique_set)
      if (unique_set := quad_set[1] - quad_set[0] - quad_set[2] - quad_set[3]):
        uniqueQuadRow(y,1,unique_set)
      if (unique_set := quad_set[2] - quad_set[0] - quad_set[1] - quad_set[3]):
        uniqueQuadRow(y,2,unique_set)
      if (unique_set := quad_set[3] - quad_set[0] - quad_set[1] - quad_set[2]):
        uniqueQuadRow(y,3,unique_set)

    for x in range(16):
      quad_set = [set(), set(), set(), set()]
      for quad in range(4):
        for y in range(quad*4,(quad+1)*4):
          if (len(Matrix[y][x]) > 0):
            for z in Matrix[y][x]:
              quad_set[quad].add(z)
      if (unique_set := quad_set[0] - quad_set[1] - quad_set[2] - quad_set[3]):
        uniqueQuadCol(x,0,unique_set)
      if (unique_set := quad_set[1] - quad_set[0] - quad_set[2] - quad_set[3]):
        uniqueQuadCol(x,1,unique_set)
      if (unique_set := quad_set[2] - quad_set[0] - quad_set[1] - quad_set[3]):
        uniqueQuadCol(x,2,unique_set)
      if (unique_set := quad_set[3] - quad_set[0] - quad_set[1] - quad_set[2]):
        uniqueQuadCol(x,3,unique_set)

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
      if (unique_set := quad_set[0] - quad_set[1] - quad_set[2] - quad_set[3]):
        uniqueQuadCellRow(cell,0,unique_set)
      if (unique_set := quad_set[1] - quad_set[0] - quad_set[2] - quad_set[3]):
        uniqueQuadCellRow(cell,1,unique_set)
      if (unique_set := quad_set[2] - quad_set[0] - quad_set[1] - quad_set[3]):
        uniqueQuadCellRow(cell,2,unique_set)
      if (unique_set := quad_set[3] - quad_set[0] - quad_set[1] - quad_set[2]):
        uniqueQuadCellRow(cell,3,unique_set)
          
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
      if (unique_set := quad_set[0] - quad_set[1] - quad_set[2] - quad_set[3]):
        uniqueQuadCellCol(cell,0,unique_set)
      if (unique_set := quad_set[1] - quad_set[0] - quad_set[2] - quad_set[3]):
        uniqueQuadCellCol(cell,1,unique_set)
      if (unique_set := quad_set[2] - quad_set[0] - quad_set[1] - quad_set[3]):
        uniqueQuadCellCol(cell,2,unique_set)
      if (unique_set := quad_set[3] - quad_set[0] - quad_set[1] - quad_set[2]):
        uniqueQuadCellCol(cell,3,unique_set)
          
    for y in range(16):
      row_set = [set(),set(),set(),set(),set(),set(),set(),set(
               ),set(),set(),set(),set(),set(),set(),set(),set()]
      for x in range(16):
        row_set[x] = set(Matrix[y][x])
      not_found_row, not_found_col, not_found_cell = checkNotFoundVariables()
      for size in range(2,8):
        search_list = list(combinations(not_found_row[y],size))
        for search_item in search_list:
          found = 0
          for x in range(16):
            if ((len(row_set[x])<=size) and (not(row_set[x]-set(search_item)))):
              found += 1
          if found == size:
            for x in range(16):
              if ((row_set[x] - set(search_item)) and (
                   row_set[x] & set(search_item))):
                for z in search_item:
                  if z in row_set[x]:
                    row_set[x].remove(z)
                    Matrix[y][x].remove(z)
                    changes += 1
                    print("row_set-Removing " +str(z)+" from: "+str(y+1
                           )+","+str(x+1)+" for row_set: "+str(row_set[x]
                           )+" and search_item: "+str(search_item))

    for x in range(16):
      col_set = [set(),set(),set(),set(),set(),set(),set(),set(
               ),set(),set(),set(),set(),set(),set(),set(),set()]
      for y in range(16):
        col_set[y] = set(Matrix[y][x])
      not_found_row, not_found_col, not_found_cell = checkNotFoundVariables()
      for size in range(2,8):
        search_list = list(combinations(not_found_col[x],size))
        for search_item in search_list:
          found = 0
          for y in range(16):
            if ((len(col_set[y])<=size) and (not(col_set[y]-set(search_item)))):
              found += 1
          if found == size:
            for y in range(16):
              if ((col_set[y] - set(search_item)) and (
                   col_set[y] & set(search_item))):
                for z in search_item:
                  if z in col_set[y]:
                    col_set[y].remove(z)
                    Matrix[y][x].remove(z)
                    changes += 1
                    print("col_set-Removing " +str(z)+" from: "+str(y+1
                           )+","+str(x+1)+" for col_set: "+str(col_set[y]
                           )+" and search_item: "+str(search_item))

    for cell in range(16):
      cell_set = [set(),set(),set(),set(),set(),set(),set(),set(
                ),set(),set(),set(),set(),set(),set(),set(),set()]
      first_row = (cell // 4) * 4
      first_col = (cell % 4) * 4
      for y in range(first_row, first_row+4):
        for x in range(first_col, first_col+4):
          i = ((y % 4)*4 + (x % 4))
          cell_set[i] = set(Matrix[y][x])
      not_found_row, not_found_col, not_found_cell = checkNotFoundVariables()
      for size in range(2,8):
        search_list = list(combinations(not_found_cell[cell],size))
        for search_item in search_list:
          found = 0
          for i in range(16):
            if ((len(cell_set[i])<=size) and (not(cell_set[i]-set(search_item)))):
              found += 1
          if found == size:
            for i in range(16):
              if ((cell_set[i] - set(search_item)) and (
                   cell_set[i] & set(search_item))):
                for z in search_item:
                  if z in cell_set[i]:
                    cell_set[i].remove(z)
                    y = ((cell // 4) * 4 + (i // 4))
                    x = ((cell % 4) * 4 + (i % 4))
                    Matrix[y][x].remove(z)
                    changes += 1
                    print("cell_set-Removing " +str(z)+" from: "+str(y+1
                           )+","+str(x+1)+" for cell_set: "+str(cell_set[i]
                           )+" and search_item: "+str(search_item))
          

  loop += 1
