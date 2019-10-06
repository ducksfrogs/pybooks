import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
plt.style.use('seaborn-darkgrid')

mu_paramus = [-1, 0, 1]
sd_paramus = [0.5, 1, 1.5]

x = np.linspace(-7, 7, 100)
f, ax = plt.subplots(len(mu_paramus), len(sd_paramus), sharex=True, sharey=True)

for i in range(3):
    for j in range(3):
        mu = mu_paramus[i]
        sd = sd_paramus[j]
        y = stats.norm(mu, sd).pdf(x)
        ax[i, j].plot(x, y)
        ax[i, j].plot(0, 0, label="$\\mu$ ={:3.2f}\n$\\sigma$ = {:3.2f}".format(mu, sd), alpha=0)
        ax[i, j].legend(fontsize=8)
ax[2,1].set_xlabel('$x$', fontsize=14)
ax[1,0].set_ylabel('$pdf(x)$', fontsize=14)

plt.tight_layout()
plt.savefig('img101.png')
plt.show()
