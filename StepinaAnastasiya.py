"def size(row,col):
  s = 0
  for t in range(row-1,row+2):
    if 0<=t<9 :
      for r in range(col-1,col+2):
        if 0<=r<9 and not (t ==row and r == col):
          if population[t][r] == 'Р':
            s += 1
  return s

population = [[0]*10 for i in range(10)]
neighbors = [[0]*10 for i in range(10)]
fish = 'Р'
rock = 'С'
nothing = 'Н'
shrimp = 'К'
population[4][6] = rock
population[3][4] = fish
population[4][5] = fish
population[5][3] = fish
population[5][4] = fish
population[5][5] = fish
for i in range(10):
  for j in range(10):
    print(population[i][j], end=' ')
  print()
print()
s = 0
t=True
while t:
  for i in range(10):
    for j in range(10):
      neighbors[i][j] = size(i,j)
      #print(neighbors[i][j], end=' ')
    #print()
  for i in range(10):
    for j in range(10):
      if population[i][j] == 'С':
        pass
      elif population[i][j] == 0 and neighbors[i][j] == 3:
        population[i][j] = 'Р'
      elif population[i][j] == 'Р' and 2<= neighbors[i][j] <= 3:
        population[i][j] = 'Р'
      else:
        population[i][j] = 0  
      print(population[i][j], end=' ')
    print()
  print()
  print()
  s+=1
  neighbors = [[0]*10 for i in range(10)]
  if s==4:
    t=False"
