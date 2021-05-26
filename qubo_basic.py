## Hybrid solver
#from dwave.system import LeapHybridSampler
#sampler_manual = LeapHybridSampler()

## Quantum solver
from dwave.system import DWaveSampler, EmbeddingComposite
sampler_manual = EmbeddingComposite(DWaveSampler())

## Encode the self-parameters
qbit_biases = {(0, 0) : 0.1, (1, 1) : 0.1}

## Define the coupling strengths
coupler_strengths = {(0, 1) : -0.2}

## Initialize the Q object
Q = {**qbit_biases, **coupler_strengths}

## Sample the problem
sampled_space = sampler_manual.sample_qubo(Q, num_reads = 5000)

print(sampled_space)
