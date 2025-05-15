
DATASET NA POROVNAVANIE
- Priemerne 15 bodov na rotacnu periodu
- Celkovo aspon 100 merani
- Aspon 75% pokrytia foldnutej krivky

DATASET NA VYSKUM
- Kniznica
- volitelne parametre
- menej ako 100 merani
## TODO

- [ ] Normalizacia
	- [ ] Amplitude / Max amplitude 
- [ ] Vyskusat modely
	
- [ ] aka je licencia na data

## CLASSES

| Name                | Objects | Tracks |     |
| ------------------- | ------- | ------ | --- |
| CZ-3B R/B           | 62      | 2448   | ✔   |
| ATLAS 5 CENTAUR R/B | 36      | 1265   | ✔   |
| FALCON 9 R/B        | 41      | 916    | ✔   |
| H-2A R/B            | 15      | 776    | ✔   |
| ARIANE 5 R/B        | 74      | 741    | ✔   |
| DELTA 4 R/B         | 18      | 398    | ✔   |

--- 

## LENGTH OF TRACKS

### Gap sizes in seconds between measurements
- looks like 0.1 second is a typical frequency of measurements

![[projects/Uni/Teaching/svk2025/mmt-sampling.png]]


| Max         | Min        | Mean                | Median | Std               |
| ----------- | ---------- | ------------------- | ------ | ----------------- |
| 807.996<br> | 0.00099968 | 0.13229693390446304 | 0.1    | 1.451504439134846 |

### Removing gaps bigger than the rotational period

#### Original track lengths in 0.1 seconds

|               | Max    | Min | Mean     | Median | Std      |
| ------------- | ------ | --- | -------- | ------ | -------- |
| Original      | 301001 | 1   | 12017.46 | 7157   | 15936.59 |
| Split by gaps | 62539  | 1   | 3384.18  | 1909   | 4042.38  |

- if track contains a gap larger than its rotational period the track is split into multiple examples

#### Percentages of tracks with maximum length after splitting

| Max length | Percentage |
| ---------- | ---------- |
| 0          | 0.000 %    |
| 1000       | 39.795 %   |
| 2000       | 50.920 %   |
| 3000       | 59.870 %   |
| 4000       | 67.569 %   |
| 5000       | 73.477 %   |
| 6000       | 78.482 %   |
| 7000       | 82.940 %   |
| 8000       | 86.359 %   |
| 9000       | 90.243 %   |
| 10000      | 95.904 %   |
| 11000      | 96.526 %   |
| 12000      | 97.135 %   |
| 13000      | 97.573 %   |
| 14000      | 97.901 %   |

## FILTRATION

#### Stats of filtration

| RB                  | Before | After |
| ------------------- | ------ | ----- |
| Ariane 5         | 875    | 831   |
| Delta 4          | 608    | 273   |
| CZ-3B            | 3327   | 2595  |
| Atlas 5 Centaur | 1590   | 1237  |
| Falcon 9        | 1325   | 963   |
| H-2A            | 981    | 756   |

#### + Uniform size split

| RB                  | Before | After |
| ------------------- | ------ | ----- |
| CZ-3B R/B           | 3675   | 2814  |
| ATLAS 5 CENTAUR R/B | 1659   | 1276  |
| FALCON 9 R/B        | 1525   | 1081  |
| H-2A R/B            | 1009   | 773   |
| ARIANE 5 R/B        | 879    | 833   |
| DELTA 4 R/B         | 684    | 303   |

Number of measurements per track

| Mean    | Median  | Std     | Max      | Min    |     |
| ------- | ------- | ------- | -------- | ------ | --- |
| 4687.10 | 4170.50 | 3028.14 | 20483.00 | 140.00 |     |

![[projects/Uni/Teaching/svk2025/robo_split.png]]

Lengths

| Mean    | Median  | Std     | Max     | Min    |
| ------- | ------- | ------- | ------- | ------ |
| 5746.39 | 5773.00 | 2711.87 | 9999.99 | 171.01 |

![[projects/Uni/Teaching/svk2025/robo-length-final.png]]

