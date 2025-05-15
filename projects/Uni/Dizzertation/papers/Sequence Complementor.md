# Sequence Complementor: Complementing Transformers For Time Series Forecasting with Learnable Sequences

Author: Xiwen Chen1, Peijie Qiu, Wenhui Zhu, Huayu Li, Hao Wang , Aristeidis Sotiras , Yalin Wang , Abolfazl Razi 
Link: [arXiv](https://arxiv.org/pdf/2501.02735)
Tags: #ARCHITECTURE #TRANSFORMER #TIMESERIES #LOSS_FUNCTION
Date: 2025-01-06

---

- **Empirical Analysis of Transformer Limitations**: Shows a strong correlation between forecasting performance and representation richness (measured by entropy).
- **Introduction of Sequence Complementors**: Learnable sequences that enrich the model’s input, enhancing feature diversity and improving forecasting accuracy.
	- Concatenates *learnable sequences* to the original input sequences.
	- The positional encoding is done only on the original sequence to maintain the temporal information.
	
		![[Pasted image 20250226132011.png]]
		
- **Theoretical Justification**: Proves that adding complementary sequences lowers forecasting error by increasing entropy and reducing uncertainty.
- **Diversification Loss**: Introduces a novel loss function to ensure complementary sequences remain diverse and non-redundant.
	1. MSE Loss
	2. Divesification Loss - encourages complementary sequences to be diverse using *volume maximization of sub-matrices* to ensure that each learnable sequences caries unique information.
		$$ L =  L_{MSE} + \lambda L_{dcs} $$
		$$ L_{dcs}(S) = - \sum_{i=1}^K 2 \text{log}((\sigma_S)_i + \epsilon$$
		
- **Model-Agnostic Design**: Sequence Complementors can be seamlessly integrated into existing transformer architectures for time series forecasting.








