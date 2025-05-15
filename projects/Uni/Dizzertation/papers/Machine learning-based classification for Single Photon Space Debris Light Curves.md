Author: Nadine M. Trummer, Amit Reza, Michael A. Steindorfer, Christiane Helling

Link: [ScienceDirect]([Machine learning-based classification for Single Photon Space Debris Light Curves - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0094576524006404?casa_token=u6nLdIQ-wlgAAAAA:vKkyHz6tgKTcrn3MGgd10o9JzeXlCbP16JhOOhenrraH3I9WgZTzns2a2U1t3l9lRaY1AzESQg)
Tags: #PREPROCESSING #DATASET #RSO #FOURIER #RANDOM_FOREST #CLASSIFICATION

----

- Introducing **IWF SPARC** (Single Photon Light Curve And Laser Ranging Catalogue), created as a by-product of laser ranging measurements.
	- from Feb 2015 to Feb 2023
	- $\geq 6500$ LCs 700 objects

## DATA
- Hand picked 872 LCs
- Sliced into 100 second segments (probably the same LC could be in train and test) -> resulting in 1141 samples
- Feature extraction
	- `TSFresh`[link](https://tsfresh.readthedocs.io/en/latest/index.html)
	- 342 feature -> principal components -> 42 
- 10-fold cross-validation
- **NOT PUBLIC**


### CASE I: Uniques - 8 unique object with the largest LC count
	
|  Description   | Label | LCs | % of subset |
| :------------: | :---: | :-: | :---------: |
|    Jason-2     |  JA2  | 214 |    31.7     |
| TOPEX/Poseidon |  TOP  | 132 |    19.5     |
|     AJISAI     |  AJI  | 94  |    13.9     |
|    ENVISAT     |  ENV  | 70  |    10.4     |
|   GLONASS092   |  G92  | 51  |     7.6     |
|   GLONASS067   |  G67  | 49  |     7.3     |
|     LARES      |  LAS  | 36  |     5.3     |
|  ATLAS 5 R/B   |  A05  | 29  |     4.3     |

### CASE II - Families - 5 families 
	
|      Description      |  Label  | Unique Objects | LCs | % of subset |
| :-------------------: | :-----: | :------------: | :-: | :---------: |
|      Jason-1/-2       |  JASON  |       2        | 240 |    31.9     |
|        GLONASS        | GLONASS |       9        | 177 |    23.5     |
|  Geodetic Satellites  | SPHERE  |       4        | 146 |    19.4     |
|    TOPEX/Poseidon     |  TOPEX  |       1        | 132 |    17.6     |
| ATLAS 5 Rocket Bodies |  ATLAS  |       6        | 57  |     7.6     |
	
### CASE III 

|     Description     | Label | Unique Objects | LCs | % of subset |
| :-----------------: | :---: | :------------: | :-: | :---------: |
|    Rocket Bodies    |  R/B  |       73       | 222 |    43.5     |
| Geodetic Satellites |  SPH  |       4        | 146 |    28.6     |
|  Active Satellites  |  SAT  |       20       | 142 |    27.8     |

## Results

| Classifier | Uniques [%] | Families [%] | Types [%] |
| :---: | :---: | :---: | :---: |
| 1-NN+ED | $48.14 \pm 5.85$ | $53.75 \pm 7.08$ | $57.64 \pm 5.56$ |
| 1-NN+DTW | $76.28 \pm 2.68$ | $80.32 \pm 4.27$ | $81.56 \pm 9.43$ |
| RDF | $65.34 \pm 5.34$ | $68.62 \pm 5.12$ | $67.45 \pm 7.03$ |
| XGB | $58.23 \pm 5.32$ | $63.97 \pm 4.59$ | $61.37 \pm 7.80$ |
| Features+RDF | $87.55 \pm 4.99$ | $90.70 \pm 5.42$ | $86.67 \pm 6.43$ |
| Features+XGB | $88.17 \pm 4.82$ | $89.89 \pm 5.30$ | $86.27 \pm 7.44$ |
