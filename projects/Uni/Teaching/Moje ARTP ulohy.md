
# HW 1

[Zadanie](<file:C:\Users\danok\Documents\teaching\artp\a1-en.pdf>)
[Suba - dobre riesenie](<file:C:\Users\danok\Documents\teaching\artp\artp_du1_suba.pdf>)
[Moje zle riesenie](<file:C:\Users\danok\Documents\teaching\artp\hw1.pdf>)
[Kometare](<file:C:\Users\danok\Documents\teaching\artp\kyselica.pdf>)

Hodnotenie
1.1. Clumsy Coins
	a) 8/8
	b) 2/12
1.2. Bureaucrats
	a) 5/5
	b) 5/8
	c) 7/7

Typický dôkaz mal zhruba tieto kroky:
  

1. Ukážeme, že vždy existuje optimálne riešenie, v ktorom je pomocou malých mincí (5, 10, 20, 25) zaplatených menej ako 50 centov. To sa dalo napr. pozorovaním, že v optimálnom riešení je najviac jedna 5-centovka, (dve by sa dali nahradiť 10-centovkou), najviac jedna 10-centovka, dve 20-centovky (3 by sa nahradili pomocou 50+10) a najviac jedna 25-centovka, takže určite nikdy neplatíme viac ako 25+20+20+10+5 = 80 centov pomocou malých mincí, a prípady medzi 50 a 80 sa dajú manuálne rozobrať. 
2. Pomocou veľkých mincí (50, 100, 200) sa dajú zaplatiť práve násobky 50 centov.
3. Z krokov 1 a 2 vyplýva, že vždy existuje optimálne riešenie, kde je pomocou veľkých mincí zaplatený najväčší násobok 50 centov neprevyšujúci cieľovú sumu.
4. Ukážeme, že greedy riešenie má rovnakú štruktúru, teda že pomocou veľkých mincí vždy zaplatí najväčší násobok 50 neprevyšujúci cieľovú sumu. Navyše, greedy algoritmus vždy najprv vybaví celú časť s veľkými mincami a až potom začne riešiť malé mince.
5. Ukážeme, že greedy použije rovnako veľa veľkých mincí ako optimálne.
6. Ukážeme, že greedy použije nanajvýš o jednu malú mincu viac, než optimálne (napr. manuálnym rozborom prípadov, keďže vieme, že obe riešenia platia malými mincami menej ako 50).  

Kroky 2 a 3 sú dostatočne triviálne na to, aby som nevyžadoval ich explicitné spomenutie v dôkaze. Krok 5 je dosť jasný na to, aby mi stačilo iba ho spomenúť (bez dôkazu).

Tvoje riešenie obsahovalo v princípe len krok 6, za ten som dával 2 body. 

Argument, že len sumy, kde greedy vyberie ako prvú 25-centovku, sú nebezpečné, je podľa mňa nekorektný. Čo ak pre nejakú sumu bolo v optimálnom riešení treba zobrať 25-centovku, ale greedy ju nezoberie?  

## Programovacia uloha

```python
import sys
from _collections import defaultdict

def read_Graph():
    N = int(sys.stdin.readline().strip())
    G = defaultdict(set)

    for i in range(round((N*(N-1)/2))):
        line = sys.stdin.readline().strip().split()
        v_from, v_to = int(line[0]), int(line[1])
        G[v_from].add(v_to)

    return N, G

def find_cycle(G):
    for v1 in G:
        for v2 in G[v1]:
            for v3 in G[v2]:
                if v1 in G[v3]:
                    return True, v1, v2, v3

    return False, None, None, None

def solve():
    N, G = read_Graph()
    removed = set()

    while True:
        ok, v1,v2,v3 = find_cycle(G)
        if not ok:
            break
            
        removed.add(v1)
        removed.add(v2)
        removed.add(v3)

        del G[v1]
        del G[v2]
        del G[v3]

        for v in G:
            G[v] -= {v1,v2,v3}

    print(len(removed))
    print(' '.join(list(map(str,removed))))

solve()
```


# HW2

[Kometare](<file:C:\Users\danok\Documents\teaching\artp\kyselica (1).pdf>)

2.1. Super hra
	a) 10/10
	b) 10/10
2.2. Vrcholové pokrytie, nezávislá množina a klika
	a) 7/8
	b) 1/12


