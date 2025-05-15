

| Name                   | SDLCD | MMT   |
| :--------------------: | :---: | :---: |
| ARIANE 5 R/B           | 231   | 98150 |
| CZ-3B R/B              | 154   | 26624 |
| FALCON 9 R/B           | 130   | 5660  |
| DELTA 4 R/B            | 71    | 2751  |
| TITAN 3C TRANSTAGE R/B | 69    | 2841  |
| ATLAS 5 CENTAUR R/B    | 67    | 16704 |
| H-2A R/B               | 35    | 5738  |
| ATLAS CENTAUR R/B      | 16    | 10982 |

---
### $\rightarrow$ with data from SDLCD

|          Name          | Total amount |
| :--------------------: | :----------: |
|       CZ-3B R/B        |     154      |
|      ARIANE 5 R/B      |     218      |
|      FALCON 9 R/B      |     126      |
|      DELTA 4 R/B       |      68      |
| TITAN 3C TRANSTAGE R/B |      57      |
|  ATLAS 5 CENTAUR R/B   |      63      |
|        H-2A R/B        |      33      |

--- 
Probably wont be using  -> ATLAS CENTAUE R/B


#TODO
V nacitani MMT objectID neodpoveda NORAD ID je to iba nejake interne cislo z nazvu suboru

---

> [!error] Bad quality Light curves 
> After filtration MMT -> low number of LC except 4 classe

#### MMT

| LC measurement coverage | CZ-3B | Falcon 9 | Atlas 5 Centaur | H2-A | Ariane 5 | Delta 4 | Titan 3 |
| ----------------------- | ----- | -------- | --------------- | ---- | -------- | ------- | ------- |
| 0%                      | 26624 | 5660     | 16707           | 5863 | 98200    | 2751    | 2841    |
| 10%                     | 25954 | 5449     | 15674           | 5697 | 9647     | 2547    | 50      |
| 20%                     | 24254 | 5200     | 13619           | 5353 | 2566     | 2149    | 30      |
| 30%                     | 22436 | 4821     | 10451           | 4960 | 898      | 1789    | 23      |
| 40%                     | 20445 | 4498     | 7395            | 4527 | 370      | 1396    | 17      |
| 50%                     | 18000 | 4071     | 5522            | 4055 | 216      | 1053    | 6       |
| 60%                     | 15225 | 3412     | 4159            | 3521 | 141      | 793     | 5       |
| 70%                     | 12568 | 2744     | 3389            | 2963 | 95       | 597     | 5       |
| 80%                     | 10172 | 2207     | 2759            | 2412 | 46       | 410     | 5       |
| 90%                     | 7688  | 1688     | 2162            | 1756 | 32       | 287     | 5       |

#### SDLCD

| LC measurement coverage | CZ-3B | Falcon 9 | Atlas 5 Centaur | H2-A | Ariane 5 | Delta 4 | Titan 3 |     |     |
| ----------------------- | ----- | -------- | --------------- | ---- | -------- | ------- | ------- | --- | --- |
| 0%                      | 154   | 126      | 63              | 33   | 218      | 68      | 57      |     |     |
| 10%                     | 143   | 120      | 62              | 31   | 211      | 62      | 48      |     |     |
| 20%                     | 137   | 117      | 57              | 28   | 184      | 58      | 37      |     |     |
| 30%                     | 130   | 108      | 53              | 28   | 172      | 55      | 33      |     |     |
| 40%                     | 128   | 98       | 48              | 27   | 159      | 53      | 21      |     |     |
| 50%                     | 122   | 92       | 47              | 26   | 153      | 49      | 9       |     |     |
| 60%                     | 115   | 85       | 38              | 23   | 136      | 37      | 2       |     |     |
| 70%                     | 98    | 76       | 30              | 16   | 104      | 27      | 0       |     |     |
| 80%                     | 67    | 51       | 19              | 11   | 57       | 11      | 0       |     |     |
| 90%                     | 32    | 21       | 11              | 5    | 21       | 5       | 0       |     |     |

---

Filter parameters
- only bins - test multiple types of bin sizes -> make stats + training results
- Percentage filter 
