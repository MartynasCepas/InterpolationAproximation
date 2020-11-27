from functions import fn_to_eval, calculate_matrix, interpolate, loss, np, chebyshev_range
import matplotlib.pyplot as plt

# Number of points
n = 5
# Interpolation function range
range_start = 2
range_end = 10
step_size = (range_end - range_start) / n
# X and Y values calculation using chebyshev polynomial
x_range_cheb = chebyshev_range(n, range_start, range_end)
y_range_cheb = [fn_to_eval(x) for x in x_range_cheb]
result = calculate_matrix(n, x_range_cheb, y_range_cheb)

# Shows f(x) and interpolation graphs
plt.plot(np.arange(range_start, range_end, 0.01), [fn_to_eval(x) for x in np.arange(range_start, range_end, 0.01)], 'b',
         label='f(x)')
plt.plot(np.arange(range_start, range_end, 0.01), [interpolate(result,x) for x in np.arange(range_start, range_end, 0.01)], 'r',
label=f'{n} points interpolation function')
plt.plot(np.arange(range_start, range_end, 0.01), [loss(result,x) for x in np.arange(range_start, range_end, 0.01)], 'g', label='Loss')

plt.scatter(x_range_cheb, y_range_cheb, color='g', label='Chebyshev points')

plt.title('f(x) interpolation using Chebyshev x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(top=8, bottom=-1)
plt.grid(True)
plt.legend()
plt.show()