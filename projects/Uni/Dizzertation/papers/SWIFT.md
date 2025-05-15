# SWIFT: Mapping Sub-series with Wavelet Decomposition Improves Time Series Forecasting

Author: Wenxuan Xie, Fanpu Cao
Link  : [arXiv](https://arxiv.org/pdf/2501.16178)
Tags  : #ARCHITECTURE #WAWELETS #TIMESERIES 

---

- Lightweight model for long-term time series forecasting

![[Pasted image 20250206111812.png|500]]

1. **Instance Normalization**
	- Subtracting samples mean / two instance norm approaches [^1]
2. **DWT**
	- Using DWT with Haar Wavelet perform $1^{st}$-order decomposition to approximation coefficients / *low-pass filter* and detail coefficients / *high-pass filter* 
	- Both filters are concatenated along new dimension : 1xN 1xN -> 2xN
3. **Aggregating & Filtering**
	- Both *low-pass* and *high-pass* filters are concatenated along new dimension : 1xN 1xN -> 2xN
	- 1D-CNN layer used as filter on the result  
	- CNN does not changes size of the input
	- DWT is used to widen the receptive field with better scaling. Each order of decomposition widens it by a factor of $2$
		![[Pasted image 20250206112559.png]]
4. **Linear layer / MLP -> Sub-series mapping**
	- shared weights for mapping both *low* and *high* frequency components -> more robust, less sensitive to noise, enccourages to learn generalized features aplicable to both frequency ranges
	- Efficient Computation
5. **IDWT**
	- Inverse DWT for obtaining final prediction


[^1]: Taesung Kim, Jinhee Kim, Yunwon Tae, Cheonbok Park, Jang-Ho Choi, and Jaegul Choo. Reversible instance nor malization for accurate time-series forecasting against dis tribution shift. In International Conference on Learning Representations, 2021.]

