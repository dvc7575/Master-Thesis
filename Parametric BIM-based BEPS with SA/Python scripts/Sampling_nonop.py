from SALib.sample.morris import sample

from SALib.util import read_param_file
import numpy as np


problem1 = read_param_file(r"C:\Users\daovi\Documents\data\BDL3_m\parameter_file.txt")
param_values1 = sample(problem1, N=240, num_levels=4, optimal_trajectories=None)
print(param_values1.shape)

with open(r"C:\Users\daovi\Documents\data\Morris_nonop\BDL3\model_input.txt", 'w') as mi1:
     np.savetxt(mi1,param_values1)

problem2 = read_param_file(r"C:\Users\daovi\Documents\data\BDL4_m\parameter_file.txt")
param_values2 = sample(problem2, N=240, num_levels=4, optimal_trajectories=None)
print(param_values2.shape)

with open(r"C:\Users\daovi\Documents\data\Morris_nonop\BDL4\model_input.txt", 'w') as mi2:
     np.savetxt(mi2,param_values2)