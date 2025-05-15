---
height: "540" 
maxScale: "2"
theme: white
---
![[Pasted image 20240410105009.png]]

--

1. Ukážeme, že vždy existuje optimálne riešenie, v ktorom je pomocou malých mincí (5, 10, 20, 25) zaplatených menej ako 50 centov. To sa dalo napr. pozorovaním, že v optimálnom riešení je najviac jedna 5-centovka, (dve by sa dali nahradiť 10-centovkou), najviac jedna 10-centovka, dve 20-centovky (3 by sa nahradili pomocou 50+10) a najviac jedna 25-centovka, takže určite nikdy neplatíme viac ako 25+20+20+10+5 = 80 centov pomocou malých mincí, a prípady medzi 50 a 80 sa dajú manuálne rozobrať.  <!-- element style="font-size:0.8em" -->
--

::: block <!-- element style="font-size:0.8em" -->
2. Pomocou veľkých mincí (50, 100, 200) sa dajú zaplatiť práve násobky 50 centov.
3. Z krokov 1 a 2 vyplýva, že vždy existuje optimálne riešenie, kde je pomocou veľkých mincí zaplatený najväčší násobok 50 centov neprevyšujúci cieľovú sumu.
4. Ukážeme, že greedy riešenie má rovnakú štruktúru, teda že pomocou veľkých mincí vždy zaplatí najväčší násobok 50 neprevyšujúci cieľovú sumu. Navyše, greedy algoritmus vždy najprv vybaví celú časť s veľkými mincami a až potom začne riešiť malé mince.
:::
--
::: block <!-- element style="font-size:0.8em" -->
5. Ukážeme, že greedy použije rovnako veľa veľkých mincí ako optimálne.
6. Ukážeme, že greedy použije nanajvýš o jednu malú mincu viac, než optimálne (napr. manuálnym rozborom prípadov, keďže vieme, že obe riešenia platia malými mincami menej ako 50).  
:::

---

![[Pasted image 20240410114856.png]]

--

b) 

::: block <!-- element style="font-size:0.8em" -->
Jeden birokrat moze mat max 2 pridelene ulohy -> pridelime zoradene od najvacsej prvu ulohu a potom druhu v opacnom poradi
:::

--

c) 

::: block <!-- element style="font-size:0.8em" -->
Algoritmus nemoze priradit viac ako 4/3 t*, znamenalo by to ze priradil byrokratovi ktory mal uz prirade ulohy  za t* a zaroven ma pridenych najmenej uloh. Ta situacia nemoze nastat.
:::

---
## Hash tables
::: block <!-- element style="font-size:0.8em" -->
- Dynamic data structured
	- search
	- insert
	- delete
- Comparing two files ...
:::

--

#### Hash function

::: block <!-- element style="font-size:0.6em" -->
- $K$ set of all keys
- $U$ set of all possible keys
- $T$ size of the table
- $f$ hash function

$$ f(x) : U \rightarrow T $$
$$ |U| >> |K| $$


> [!question]
>1. How to solve collisions?
>2. What is the worst-case time complexity of search?
>3. What is the expected time complexity of search?
:::

--

::: block <!-- element style="font-size:0.8em" -->
Collisions
- chaining
- linear probing
:::

--

Worst-case time complexity for search is O(n) 

--

3. What is the expected time complexity of search?

::: block <!-- element style="font-size: 0.6em" -->
> [!Assumptions:]
>- Good hashing function
>	- $P(h(k_i) = x) = \frac{1}{m}$
>	- O(1)
>- Linear probing 
>	- $n_j$ is the size of $j$-th entry
>- $\alpha = \frac{n}{m}$

  $\implies$ search time for key $k$ is proportional to the $T_{h(k)}$
:::

--

![[Pasted image 20240410121607.png]]


--

![[Pasted image 20240410121746.png]]
![[Pasted image 20240410121759.png]]

--

#### Universal hashing function

::: block <!-- element style="font-size: 0.8em" -->
$$ h_i(x) = x i \text{ mod } p  \text{ mod } M$$
- $P$ prime number $> 2^{64}$
- $M$ size of the table


> [!question]
> What is the probability of collision?
:::

--
::: block <!-- element style="font-size: 0.8em" -->
$$
P(h(x)=h(y)) \leq \frac{c}{M} \leftarrow \text{ our target}\\\\
$$
$$
\begin{align*}
h(x) = h(y) \\\\
	x i \text{ mod } p  \text{ mod } M =  y i \text{ mod } p  \text{ mod } M \\\\
	x i \text{ mod } p  \text{ mod } M - y i \text{ mod } p  \text{ mod } M =& 0 \\\\
	x i \text{ mod } p   - y i \text{ mod } p  =& qM \\\\
	(x i \text{ mod } p  - y i \text{ mod } p) \text{ mod } p =& qM \\\\
	i(x-y) \text{ mod } p =& qM \\\\
\end{align*}
$$

- $i(x-y) \in [-P, P]$ $\rightarrow$ $2P$ possibilities

Leads to $\frac{2P}{M}$ collision points
:::


---

### Rabin-Karp string search

```python
# version for multiple strings of size m
def RabinKarpSet(string s[1..n], set of string subs, m):
    set hsubs := emptySet
    foreach sub in subs
        insert hash(sub[1..m]) into hsubs
    hs := hash(s[1..m])
    for i from 1 to n-m+1
        if hs ∈ hsubs and s[i..i+m-1] ∈ subs
            return i
        hs := hash(s[i+1..i+m])
    return not found
```

--


### Rolling hash

::: block <!-- element style="font-size: 0.8em" -->

$H = c_1a^{k-1}+c_2a^{k-2}+c_2a^{k-2}+\dots + c_1a^0$

- $\alpha$ i a constant
- $c_1,\dots , c_k$ are input characters


<br>
$s[i+1..i+m] = s[i..i+m-1] - s[i] + s[i+m]$
:::


