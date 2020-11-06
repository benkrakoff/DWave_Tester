#reference documentation
#https://docs.ocean.dwavesys.com/en/stable/docs_dimod/reference/sampler_composites/samplers.html

from dimod import ExactSolver

Q = {}
h = {}
for i in range(10):
    Q[(i, i+1)] = -1
    h[i] = 0
sampleset = ExactSolver().sample_ising(h, Q)
print(sampleset.first.sample)