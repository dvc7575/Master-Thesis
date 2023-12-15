from SALib.analyze import morris
from SALib.sample.morris import sample

from SALib.util import read_param_file
from SALib.plotting.morris import (
    horizontal_bar_plot,
    covariance_plot,
    sample_histograms,
)
import matplotlib.pyplot as plt
import numpy as np


problem = read_param_file(r"C:\Users\daovi\Documents\data\Morris\BDL4\parameter_file.txt")
problem.pop('groups')
# print(problem_g)
print(problem)

param_values = np.loadtxt(r"C:\Users\daovi\Documents\BDL4_final_1190\model_input.txt")

# param_values = sample(problem, N=100, num_levels=4, optimal_trajectories=32)

# with open(r"C:\Users\daovi\Documents\data\Morris\BDL3\model_input.txt", 'w') as mi:
#     np.savetxt(mi,param_values)

data = np.loadtxt(r"C:\Users\daovi\Documents\BDL4_final_1190\model_output.txt")

# print("sample shape: ", param_values.shape)
# print("data shape:", data.shape)
# print("data size: ", data.size)


#Total Load
Y_0 = data[:,0]

Si_0 = morris.analyze(
    problem,
    param_values,
    Y_0,
    conf_level=0.95,
    print_to_console=True,
    num_levels=4,
    num_resamples=100,
)

# print(Si_0["sigma"])
# print(Si_0["mu_star"])
fig1, (ax1,ax2) = plt.subplots(1,2)

colors = ["blue", "orange", "red", "purple", "brown", "pink", "gray", "cyan", "olive"]
names = Si_0["names"]
sigma = Si_0["sigma"]
mu_star = Si_0["mu_star"]

Si_0["color"] = colors

for i in range(0,len(names)):
        out = ax1.scatter(mu_star[i], sigma[i], c=colors[i], marker="o", label = names[i])

ax1.set_ylabel(r"$\sigma (kWh/m^2)$", fontsize = 16)
ax1.set_xlabel(r"$\mu^\star (kWh/m^2)$", fontsize = 16)
# ax1.set_title('Covariance Plot', fontsize=20)


ax1.set_xlim(0,)
ax1.set_ylim(0,)
x_axis_bounds = np.array(ax1.get_xlim())
(line1,) = ax1.plot(x_axis_bounds, x_axis_bounds, "k-", label = r"$\sigma / \mu^{\star} = 1.0$")
(line2,) = ax1.plot(x_axis_bounds, 0.5 * x_axis_bounds, "k--", label = r"$\sigma / \mu^{\star} = 0.5$")
(line3,) = ax1.plot(x_axis_bounds, 0.1 * x_axis_bounds, "k-.", label = r"$\sigma / \mu^{\star} = 0.1$")
        
fig1.legend(loc = 'lower center', ncol =4, fontsize = 12)
ax1.tick_params(axis='both', which='major', labelsize=12)


# define a color sorting function
def sort_Si(Si, key, sortby="mu_star"):
    return np.array([Si[key][x] for x in np.argsort(Si[sortby])])

colors_sorted = sort_Si(Si_0, "color", sortby = "mu_star")
print(colors_sorted)


# fig2, (ax2) = plt.subplots()
horizontal_bar_plot(ax2, Si_0, {"color" : colors_sorted}, sortby='mu_star')
ax2.set_xlabel(r"$\mu^\star (kWh/m^2)$", fontsize = 16)
ax2.tick_params(axis='both', which='major', labelsize=12)






fig1.suptitle("Total Load Intensity $(kWh/m^2)$", fontsize=20)






# fig2 = plt.figure()

# sample_histograms(fig2, param_values, problem, {"color": "y"})
plt.show()

# #Cooling Load
# Y_1 = data[:,1]

# Si_0 = morris.analyze(
#     problem,
#     param_values,
#     Y_1,
#     conf_level=0.95,
#     print_to_console=True,
#     num_levels=4,
#     num_resamples=100,
# )

# #Heating Load
# Y_2 = data[:,2]

# Si_0 = morris.analyze(
#     problem,
#     param_values,
#     Y_2,
#     conf_level=0.95,
#     print_to_console=True,
#     num_levels=4,
#     num_resamples=100,
# )

# #Lighting Load
# Y_3 = data[:,3]

# Si_0 = morris.analyze(
#     problem,
#     param_values,
#     Y_3,
#     conf_level=0.95,
#     print_to_console=True,
#     num_levels=4,
#     num_resamples=100,
# )

# #Elec Load
# Y_4 = data[:,4]

# Si_0 = morris.analyze(
#     problem,
#     param_values,
#     Y_4,
#     conf_level=0.95,
#     print_to_console=True,
#     num_levels=4,
#     num_resamples=100,
# )