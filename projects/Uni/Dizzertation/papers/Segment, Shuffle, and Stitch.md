# Segment, Shuffle, and Stitch: A Simple Layer for Improving Time-Series Representations

Author: Shivam Grover, Amin Jalali, Ali Etemad
Link  : [NeurIPS](https://papers.nips.cc/paper_files/paper/2024/file/0898f05f6c1d247be3eab8da93d33da1-Paper-Conference.pdf)
Tags  : #ARCHITECTURE #TIMESERIES


---

## S3 layer

1. **Segment**
	- Splits the input sequence $x_i$ into $n$ non-overlapping segments $s_i$ of length $l$.
2. **Shuffle**
	- Shuffles the segments $s_i$ - Generates shuffle vector $P = \{p_1,p_2,\dots,p_n\} \in \mathbb{R}^n$ using learnable weights
3. **Stitch**
	- Concatenates the shuffled segments into a single sequence. Then perform weighted sub between the original $x_i$ and shuffled $\widetilde{x_i}$ sequence with learnable weights $w_1$ and $w_2$.


![[Pasted image 20250206093959.png]]

## Stacking layers

For $\phi$ layers, the input sequence $x_i$ is transformed as follows:
$$
n_{\ell}=n \times \theta^{\ell-1} \quad \text { for } \ell=1,2, \ldots, \phi
$$
where $n$ is the number of segments. We can then define the output of layer $l$ as:
$$
\mathbf{x}_{\ell}^{\prime}=\operatorname{Stitch}\left(\operatorname{Shuffle}\left(\operatorname{Segment}\left(\mathbf{x}_{\ell-1}^{\prime}, n_{\ell}\right), \mathbf{P}_{\ell}\right),\left(\mathbf{w}_{\ell, 1}, \mathbf{w}_{\ell, 2}\right)\right), \text { for } \ell=1,2, \ldots, \phi,
$$
