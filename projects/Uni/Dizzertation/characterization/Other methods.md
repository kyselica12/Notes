
# Allworth 2021 
[[Atransfer learning approachtospacedebrisclassification using.pdf]]

1. Light curve simulation
	- TLE data
	- 3D model - NASA website
	- Blender rendering (Cycles)
	- Extract apparent magnitude from image
		- apparent magnitude  -> Ashikhmin-Shirley BRDF applied to FFM
	- Different sampling rates and lenghts
2. Model
	- Grid search for optimal parameters
	- Architecture
		- Layer 1
			- input size 100
			- 64 filters
			- Stride 3
		- MaxPool
		- BatchNorm
		- Layer 2
			- input size 50
			- 64 filters
			- Stride 3
		- MaxPool
		- BatchNorm
		- Flatten
		- FC 1 (512) ReLU
		- FC 2 (128) ReLU
		- FC 3 (n_classes) Softmax

3. Dataset
	1. EOS dataset
		- 900 lc 
		- 22 objects
	2. MMT
		- satellites, rocket bodies, space debris
		- determined rotation,>= 500 observations
		- 40 000 lc
		- 153 objects
		- unbalanced dataset
		- sub dataset
			- 500 lc per 8 classes
4. Traininng
	- K-fold cross validation (k=5)
	- Sampler for imbalanced datasets

5. Results
	- higher 80% accuracy
	![[Pasted image 20240602154923.png]]

	
> [!quote]	
> The majority of misclassifications appear to be between classes that are similar.
> 
> Blender dataset, there are a number of misclassifications between similarly shaped objects such as the three different rocket body classes (CZ-3B, ARIANE 5, FALCON 9).


> [!faq]
> Same objects in validation and training
> Possible same tracks in the training and validation??
> What normalization was chosen ?


## Suvey
[[Survey_Mode__A_Review_of_Machine_Learning_in_Resident_Space_Object_Detection_and_Characterization.pdf]]

- Chaudhary, A. et al [43] - wavelets
```
Chaudhary, A., Payne, T., Gregory, S., and Dao, P., “Fingerprinting of Non-resolved Three-axis Stabilized Space Objects Using
a Two-Facet Analytical Model,” 2011.
```


Shape classification
- [46] Linares, R et al 2019
```
Furfaro, R., Linares, R., and Reddy, V., “Shape Identification of Space Objects via Light Curve Inversion Using Deep Learning
Models,” Advanced Maui Optical and Space Surveillance Technologies Conference, edited by S. Ryan, 2019, p. 17.
```
	- simulation
	- CNN
	- 4 classes roxket bodies
- [47] Yao, L. et al
```
Yao, L., and Chang-yin, Z., “The Basic Shape Classification of Space Debris with Light Curves,” , Apr. 2021. https:
//doi.org/10.1016/j.chinastron.2021.05.005, URL http://dx.doi.org/10.1016/j.chinastron.2021.05.005.
```
	- 1D CNN
	- simulated data
	- MMT

## Yao, L. 2021
[[The Basic Shape Classification of Space Debris.pdf]]

- folding MMT lcs
- accuracy around 80
- overall features be 0 and 1, respectively - classic normalization

> [!note] Architecture
> 64 filters , kernel size 5
> input dimension 200
> 500 and 100 Fully connected at the end
> 15 layers

> [!quote]
> If the combination of two convolutional layers, one dropout layer, and one pooling layer is seen as a group of convolutional layers, the 3, 4, and 5 groups of convolutional layers correspond to the network structure with depth of 15, 19, and 23, respectively.

> [!faq]
> Validation on same objects?
> Same tracks?




