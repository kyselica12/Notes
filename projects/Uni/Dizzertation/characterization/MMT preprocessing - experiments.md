---
height: "540" 
theme: white
css: [css/layout.css,css/custom_layout.css]
---

## XGBoost - Baseline

- Best performance using Fourier Series coefficients
- Data split by Track ID - normal scenario (1 object can be observed multiple times)
- 6 classes

| Validation acc | Test acc |
| -------------- | -------- |
| 75.18 %        | 57.26%   |

--

#### Evaluation set (MMT)

| prediction \\ actual | CZ-3 | falcon 9 | atlas V | H2-A | Globalstar |
| -------------------- | ---- | -------- | ------- | ---- | ---------- |
| CZ-3                 | 1805 | 373      | 276     | 27   | 12         |
| falcon 9             | 74   | 53       | 11      | 6    | 2          |
| atlas V              | 73   | 9        | 197     | 7    | 10         |
| H2-A                 | 30   | 3        | 18      | 409  | 20         |
| Globalstar           | 52   | 4        | 50      | 34   | 841        |

|           | CZ-3 | falcon 9 | atlas V | H2-A | Globalstar | Avg. |
| --------- | ---- | -------- | ------- | ---- | ---------- | ---- |
| precision | 0.72 | 0.36     | 0.67    | 0.85 | 0.86       | 0.69 |
| recall    | 0.89 | 0.12     | 0.36    | 0.85 | 0.95       | 0.63 |
| f1        | 0.80 | 0.18     | 0.46    | 0.85 | 0.90       | 0.64 |



#### Test set (SDLCD)

| prediction \\ actual | CZ-3 | falcon 9 | atlas V | H2-A |
| -------------------- | ---- | -------- | ------- | ---- |
| CZ-3                 | 61   | 39       | 0       | 1    |
| falcon 9             | 2    | 6        | 0       | 5    |
| atlas V              | 0    | 1        | 0       | 1    |
| H2-A                 | 0    | 0        | 0       | 6    |



|           | CZ-3  | falcon 9 | atlas V | H2-A  |
| --------- | ----- | -------- | ------- | ----- |
| precision | 0.604 | 0.75     | ---     | 1     |
| recall    | 0.968 | 0.130    | ---     | 0.75  |
| F1 score  | 0.744 | 0.222    | ---     | 0.857 |

#### <span style="color:#ff0000">!!! Bad F1 score for Falcon and Atlas 5 !!!</span>

--

#### Hyperparameter tuning optimizing F1 score

- hyperparameter tuning using Bayesian optimization over >40 runs

| Class    | Best F1 score | learning rate | max depth | num. estimators |
| -------- | ------------- | ------------- | --------- | --------------- |
| Falcon 9 | 0.348         | 0.996         | 14        | 86              |
| Atlas V  | 0.605         | 0.135         | 18        | 8               |

---

## Neural Network

Best performing models for each data type, optimizing validation accuracy
- Resnet20
- 25 epochs
- 32 batch size
- 6 classes

---

### Light curve vs. Reconstructed LC using Fourier series coeficients
| DataType         | Cyclic shift | MixUp | Label smoothing | Val accuracy | Test accuracy |
| ---------------- | ------------ | ----- | --------------- | ------------ | ------------- |
| Light curve      | ✔            | X     | X               | 78.06%       | 65.63%        |
| Reconstructed LC | ✔            | X     | ✔<br>           | 74.54%       | 64.58%        |

Better F1 score (precision and accuracy) for harder classes as Falcon 9  and Atlas V

--
### LC

| predicted / actual | CZ-3 | Falcon 9 | Atlas V | H2-A | Globalstar |
| ------------------ | ---- | -------- | ------- | ---- | ---------- |
| CZ-3               | 1734 | 272      | 183     | 13   | 12         |
| Falcon 9           | 140  | 132      | 25      | 0    | 0          |
| Atlas V            | 110  | 24       | 258     | 12   | 3          |
| H2-A               | 41   | 11       | 25      | 448  | 5          |
| Globalstar         | 19   | 3        | 61      | 9    | 880        |

|           | CZ-3 | falcon 9 | atlas V | H2-A | Globalstar | Avg. |
| --------- | ---- | -------- | ------- | ---- | ---------- | ---- |
| precision | 0.78 | 0.44     | 0.63    | 0.85 | 0.91       | 0.72 |
| recall    | 0.85 | 0.30     | 0.47    | 0.93 | 0.98       | 0.70 |
| f1        | 0.81 | 0.36     | 0.54    | 0.89 | 0.94       | 0.71 |

|           | CZ-3 | falcon 9 | atlas V | H2-A | Globalstar | Avg. |
| --------- | ---- | -------- | ------- | ---- | ---------- | ---- |
\textbf{Precision} & 0.83 & 0.31     & 0.76    & 0.93 & 0.91\\
\textbf{Recall}    & 0.74 & 0.54     & 0.55    & 0.87 & 0.99 \\
\textbf{F1 score}  & 0.79 & 0.40     & 0.64    & 0.90 & 0.95 \\ \hline

---
### Reconstructed

| predicted / actual | CZ-3 | Falcon 9 | Atlas V | H2-A | Globalstar |
| ------------------ | ---- | -------- | ------- | ---- | ---------- |
| CZ-3               | 1827 | 334      | 308     | 25   | 31         |
| Falcon 9           | 92   | 68       | 8       | 0    | 0          |
| Atlas V            | 41   | 23       | 159     | 3    | 28         |
| H2-A               | 68   | 15       | 28      | 445  | 69         |
| Globalstar         | 6    | 2        | 49      | 10   | 745        |


|           | CZ-3 | falcon 9 | atlas V | H2-A | Globalstar | Avg. |
| --------- | ---- | -------- | ------- | ---- | ---------- | ---- |
| precision | 0.72 | 0.40     | 0.63    | 0.71 | 0.92       | 0.68 |
| recall    | 0.90 | 0.15     | 0.29    | 0.92 | 0.85       | 0.62 |
| f1        | 0.80 | 0.22     | 0.39    | 0.80 | 0.88       | 0.62 |

---

### Wavelet transform

--

#### Comparing number of scales used for wavelet transform

- scales from [1..N]

Lower validation accuracy with higher scale

*Best performance of the model though 30 epochs*

| $N$ | validation accuracy | train accuracy |
| --- | ------------------- | -------------- |
| 1   | 80%                 | 90%            |
| 11  | 79.6%               | 90.1%          |
| 21  | 77.3%               | 93.6%          |
| 31  | 73.23%              | 96.8 %         |
| 61  | 77.7%               | 93.8%          |
| 81  | 78.7%               | 96.9%          |


Worse performance with higher number of wavelet scales

--

Confusion matrix for $N=1$ after 30 epochs (val acc 76% test acc 90%)

| predicted / actual | CZ-3 | Falcon 9 | Atlas V | H2-A | Globalstar |
| ------------------ | ---- | -------- | ------- | ---- | ---------- |
| CZ-3               | 1512 | 190      | 105     | 8    | 2          |
| Falcon 9           | 439  | 240      | 71      | 16   | 2          |
| Atlas V            | 58   | 10       | 304     | 29   | 1          |
| H2-A               | 7    | 2        | 21      | 418  | 2          |
| Globalstar         | 18   | 0        | 51      | 12   | 866        |

|           | CZ-3 | falcon 9 | atlas V | H2-A | Globalstar | Avg. |
| --------- | ---- | -------- | ------- | ---- | ---------- | ---- |
| precision | 0.83 | 0.31     | 0.76    | 0.93 | 0.91       | 0.75 |
| recall    | 0.74 | 0.54     | 0.55    | 0.87 | 0.99       | 0.74 |
| f1        | 0.79 | 0.40     | 0.64    | 0.90 | 0.95       | 0.73 |

--

#### Wavelet scale resolution

- CTW on 5 scales
- Choosing the difference between scales

| Step | Best Validation accuracy |
| ---- | :--: |
| 1    | 80.59%                   |
| 2    | 80%                      |
| 8    | 79.79%                   |
| 16   | 76.36%                   |
| 32   | 70.12%                   |


# Synthetic LC using FS histogram

|                 | CZ-3B  | Falcon 9 | Atlas 5 Centaur | H2-A   | Ariane 5 | Delta 4 | Titan 3 |
| --------------- | ------ | -------- | --------------- | ------ | -------- | ------- | ------- |
| CZ-3B           | 262.0  | 61.0     | 30.0            | 30.0   | 0.0      | 3.0     | 0.0     |
| Falcon 9        | 87.0   | 15.0     | 5.0             | 1.0    | 0.0      | 0.0     | 0.0     |
| Atlas 5 Centaur | 5774.0 | 1229.0   | 1613.0          | 1229.0 | 18.0     | 157.0   | 0.0     |
| H2-A            | 0.0    | 0.0      | 2.0             | 0.0    | 0.0      | 0.0     | 0.0     |
| Ariane 5        | 77.0   | 5.0      | 7.0             | 42.0   | 0.0      | 0.0     | 0.0     |
| Delta 4         | 1515.0 | 284.0    | 445.0           | 473.0  | 16.0     | 115.0   | 0.0     |
| Titan 3         | 204.0  | 81.0     | 54.0            | 69.0   | 0.0      | 17.0    | 0.0     |



![[Pasted image 20240426104435.png]]

