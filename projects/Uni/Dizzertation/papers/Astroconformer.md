# Astroconformer: The Prospects of Analyzing Stellar Light Curves with Transformer-Based Deep Learning Models
#TRANSFORMER #ARCHITECTURE

- [[https://arxiv.org/pdf/2309.16316.pdf|link]]
- To campture also long range and low-range oscillations
- Astroconformer 
	- CNN - short range information
	- MHSA - long-range correlations
- Embedding as first layer
	- MLP
	- Patch embeddings 
		- 1 LC -> 200 patches over 20 timesteps
![[Pasted image 20240129125921.png]]
- Astroconformer Block -> 8-head Multi Head self attention modules and 2 CNN modules (CNN, BN, Swish activation function)
- Rotary Positional Encoding (RoPE) -> multiplication with complex phases proportional to possition
- Preprocessing
	- Sigma-clipping - rolling window of 50 timestamps (3 $\sigma$)
	- Savitzky-Golay filter - to eliminate low-frequency variations
	- Linear interpolation for missing values
	- Normalization of magnitude $\frac{x}{std(x)} \frac{1}{ln(\text{max std}/\text{std}(x)+1}$
		-> std of LC is restrained between 0.1 - 1


