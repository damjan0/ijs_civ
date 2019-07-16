import matplotlib.pyplot as plt
import numpy as np

probability_sum = [0.28593, 0.34593357466451924, 0.36775687133224694, 0.3987490989891018, 0.5062728030788688, 0.9311251609429948, 1]
probability_without = [0.3594014265946795, 0.4278684553541246, 0.460365756562534, 0.5037349858166346, 0.6132700807513045,
                       0.9507559547042704, 1]

median_brez = [5.41,255.47,2.06]
median_rezanje = [64.19,261.87,31.12]
Ln = [66933.04,495.38,65357.38]

plt.ion()

labels = ['Model1','Model2','Model3']
cut = ['no cut', '-8', '-6', '-4', '-2', '0', '2']

x = np.array([0, 1, 2])
fig = plt.figure()
# fig.add_subplot()

fig, ax = plt.subplots()
ax.set_title('Median without cut R, with cut B')
ax.set_xlabel('Model')
ax.set_ylabel('Median')
ax.set_xticks(x)
#ax.set_xticklabels(('no cut', '-8', '-6', '-4', '-2', '0', '2'))
ax.set_xticklabels(('Model1','Model2','Model3'))

ax.bar(x, median_brez, color='r')
ax.bar(x + 0.2, median_rezanje, width=0.2, color='b')

fig.show()
