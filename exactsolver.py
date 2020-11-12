#reference documentation
#https://docs.ocean.dwavesys.com/en/stable/docs_dimod/reference/sampler_composites/samplers.html

from dimod import ExactSolver

Q = {}
h = {}
for i in range(10):
    Q[(i, i+1)] = -1
    h[i] = 0

data = ExactSolver().sample_ising(h, Q).to_pandas_dataframe()

data.to_csv("Data_1.csv")