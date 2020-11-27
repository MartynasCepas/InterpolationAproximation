from functions import fn_to_eval, calculate_matrix, interpolate, loss, np
import matplotlib.pyplot as plt

# Number of points + 1
n = 5
step_size_n = n - 1
# Interpolation function range
range_start = 2
range_end = 10
step_size = (range_end - range_start) / step_size_n
# X and Y values calculation
x_range = np.arange(range_start, range_end, step_size)
x_range = np.append(x_range, range_end)
y_range = [fn_to_eval(x) for x in x_range]
result = calculate_matrix(n, x_range, y_range)

#Shows f(x) and interpolation graphs
plt.plot(np.arange(range_start, range_end, 0.01), [fn_to_eval(x) for x in np.arange(range_start, range_end, 0.01)], 'b',label='f(x)')
plt.plot(np.arange(range_start, range_end, 0.01), [interpolate(result,x) for x in np.arange(range_start, range_end, 0.01)], 'r', label=f'{n} points interpolation function')
plt.plot(np.arange(range_start, range_end, 0.01), [loss(result,x) for x in np.arange(range_start, range_end, 0.01)], 'g', label='Loss')

plt.scatter(x_range, y_range, color='g', label='Interpolation points')

#plt.title("f(x) interpolation")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(top=8, bottom=-1)
plt.grid(True)
plt.legend()
plt.show()