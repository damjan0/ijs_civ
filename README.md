# IJS Civilizations
Sandberg paper:
https://arxiv.org/abs/1806.02404

`generateData3DLongevity.py`  Generates points for each Lmax and saves it to a file

`3DLongevity.py`  Plots a 3DGraph from files created from before

---------
### Clustering and Boxplots
Manualy read from a graph for different clusters. For each cluster draw a boxplot for each parameter

### Flipping N and L
Generate points and plot a 3Dgraph where N and L are changed.. calulating L for different Nmax points
Using `generateData3DN.py` to generate points and `3DN.py` to plot it

### Machine Learning
Using Machine Learning to get clusters for generated points
- dAE - Deep Autoencoder
- VAE - Variational autoencoder
- tSNE

### Different models
Model 2: https://arxiv.org/ftp/arxiv/papers/1510/1510.08837.pdf
Model 2 opposite to original Drake equation (calculates how many int.civs are out there now), this model caluclates how many int.civs. were ever out there.
We used Sandberg distributions for astrophysics probabilities, Papers lower bound for biotechnical probabilities and L so we can calculate similar results to Model 1
Useable files:  `generateDataModel2.py` to generate points and `plotDataModel2.py` to plot it

Model 3: http://adsabs.harvard.edu/full/1983QJRAS..24..283B
...
Useable files:  `generateDataModel3_3DLongevity.py` to generate points and `Model3_3DLongevity.py` to plot it
---------
`points4.csv`  480000 points generated from an old code (2019-01-13)

`Sfinga.jpg`  Latest version of Sphynx (2019-02-28) /Bokal update

![alt text](https://github.com/damjan0/ijs_civ/blob/master/Sfinga.png?raw=true "Sfinga")