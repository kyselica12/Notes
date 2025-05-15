Authors: Randa Qashoa, Regina Lee [link](file://C:\Users\danok\Documents\clanky)

#LSTM #SVM #RSO #CLASSIFICATION #WAWELETS

- Ukrainan LC database (http://oap.onu.edu.ua/article/view/117655)
- Wavelet scattering trasform (WST) for preprocessing (better clusters in t-SNE visualisation)
		![[Pasted image 20240221104457.png]]
- Classification task
	- stable satellite
	- tumbling satellite
	- rocket body
- SVM
	- Window based approach -> classify smaller patches then combine results
		- $60\%$  test accuracy
	- Mean Features -> Reducing input size from $m\times n \times o$ to $m \times o$ adding mean of columns as input parameter 
		- $87\%$ test accuracy
		- training time 7s
- LSTM
	- Bayesian Optimization for hyperparameters $\rightarrow$ took over one week (30 epochs per model)
	- $92\%$ test accuracy
		
