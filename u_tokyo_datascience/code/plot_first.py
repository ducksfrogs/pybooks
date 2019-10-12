import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
student_math = pd.read_csv('../data/student-mat.csv')

x = np.random.randn(1000)

plt.plot(x, np.sin(x), 'o')
plt.grid(True)
plt.show()