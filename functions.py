import numpy as np

def fn_to_eval(x):
    return np.log(x)/(np.sin(2*x)+1.5) + x/5

def calculate_matrix(n, x_range, y_range):
  matrix = [[0] * n for i in range(n)]
  for i in range(n):
    print(i)
    for j in range(n):
      matrix[i][j] = x_range[i]**j
  return np.linalg.solve(matrix,y_range)

def approximate(n, x_range, y_range, row):
  print(n)
  print(row)
  matrix = [[0] * row for i in range(n)]
  for i in range(n):
    for j in range(row):
        matrix[i][j] = x_range[i]**j
  numpyArrayX = np.array(matrix)
  numpyArrayY = np.array(y_range)
  transposedMatrixX = np.transpose(numpyArrayX).dot(numpyArrayX)
  transposedMatrixY = np.transpose(numpyArrayX).dot(numpyArrayY)
  return np.linalg.solve(transposedMatrixX,transposedMatrixY)

def interpolate(result, x):
  count = 0
  total = 0
  for value in result:
    total = total + value * x**count
    count+=1
  return total

def loss(result, x):
  return abs(fn_to_eval(x)-interpolate(result,x))

def chebyshev_range(count, start, end):
    range_x = []
    for i in range(count):
        temp = (end + start) / 2 + (end - start) / 2 * np.cos((2 * i + 1) * np.pi / (2 * count))
        range_x.append(temp)
    return range_x