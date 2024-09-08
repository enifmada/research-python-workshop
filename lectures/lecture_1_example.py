import numpy as np
import matplotlib.pyplot as plt

def forward_one_gen(p, s):
    return p + s * p * (1 - p)

N = 5000
s = 0.01
num_gens = 500
p_init = .25
allele_freqs = np.zeros(num_gens)

allele_freqs[0] = p_init
for i in np.arange(1,num_gens):
    allele_freqs[i] = forward_one_gen(allele_freqs[i - 1], s)

plt.plot(allele_freqs)
plt.show()