from functions import fn_to_eval, approximate, interpolate, loss, np
import matplotlib.pyplot as plt

x_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_range = [-8.9003,-15.417,-0.6314,1.93806,7.63665,13.1566,15.3685,15.025,8.08982,4.60416,-3.4688,-2.1801]
n = len(x_range)
row = 12
result = approximate(n, x_range, y_range, row)
plt.scatter(x_range, y_range, label='Month`s temp. avg.')
plt.plot(x_range, [interpolate(result,x) for x in x_range], 'r', label='Temp. interpolation')
plt.grid(True)
plt.legend()
plt.xlabel('Month')
plt.ylabel('Temp. avg.')
plt.title("2007 Finland temperature")
plt.show()