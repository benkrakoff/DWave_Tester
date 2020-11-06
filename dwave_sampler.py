from dwave.system import DWaveSampler
import time

sampler = DWaveSampler()
Q = {}
qubits = [sampler.nodelist[0]]

for i in range(10):
    qubits.append(next(iter(sampler.adjacency[qubits[-1]])))
    Q[(qubits[-2], qubits[-1])] = -1

t_1 = time.time()
sampleset = sampler.sample_ising({}, Q, num_reads = 100)
t_2 = time.time()

print((sampleset.first.sample, t_2-t_1))