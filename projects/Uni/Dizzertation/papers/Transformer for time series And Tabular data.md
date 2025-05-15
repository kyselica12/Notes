## Transformer for time series And Tabular data. ArXiv, 2024.

Author: "G. Cabrera-Vives, D. Moreno-Cartagena, N. Astorga, I. Reyes-Jainaga, F. Förster, P. Huijse, J. Arredondo, A. M. Muñoz Arancibia, A. Bayo, M. Catelan, P. A. Estévez, P. Sánchez-Sáez, A. Álvarez, P. Castellanos, P. Gallardo, A. Moya and D. Rodriguez-Mancini: ATAT: Astronomical"
Link: [arXiv]((https://arxiv.org/pdf/2405.03078)
Tags: #ARCHITECTURE #TRANSFORMER #FOURIER

---

- Transformer for Timeseries and tabular data
	![[Pasted image 20250204095617.png|700]]
- Input: light-curve (6 bands) (fluxes instead of magnitudes), meta-data, computed features
- Fixes size - the maximum length
	- zero padding
- Time Modulation using Fourier Series for time series
	- ![[Pasted image 20250204100011.png|500]]
- Quantile Feature Tokenizer for tabular data
	- $QT$ - quantile transformation transforms features into a desired distribution (a normal distribution in this work) by mapping the cumulative distribution function of the features to the quantile function of the desired distribution. 
	- Then Tokenized to desired shape
	 $$QFT_k(f_k) = W_k \times QT_k(f_k) + b_k$$
	- Custom encoding helps
		 ![[Pasted image 20250204101711.png|500]]
- Training details:
	- Adam
	- Early stopping $2 . 10^{-4}$
	- Batch size:  256
	- Class balanced batches
	- Nans and infs replaces with $-9999$
- Outperformes RF (MD + Features) with input LC + MetaData + Features (But not a huge difference considering that RF does not have LC as input)
	- With the same data performance is similar




