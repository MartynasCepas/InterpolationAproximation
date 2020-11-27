import matplotlib.pyplot as plt
from scipy import interpolate
from spline import hermite_interpolation_spline, np

x_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_range = [-8.9003,-15.417,-0.6314,1.93806,7.63665,13.1566,15.3685,15.025,8.08982,4.60416,-3.4688,-2.1801]

interpolation_f = hermite_interpolation_spline(x_range, y_range)

plt.scatter(x_range, y_range, label='Month`s avg. temp')
plt.plot(np.arange(x_range[0], x_range[-1], 0.01),
         [interpolation_f(_x) for _x in np.arange(x_range[0], x_range[-1], 0.01)],
         'r', label='Spline')

plt.xlabel('Month')
plt.ylabel('Temp. avg.')
plt.title('Hermite interpolation spline 2007 Finland temperature')

plt.grid(True)
plt.legend()
plt.show()