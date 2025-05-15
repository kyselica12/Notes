# Knowledge distillation

Research regarding knowledge distillation, with focus on EO and small models.

---
## Table of Content
- [Semantic Knowledge Distillation for Onboard Satellite Earth Observation Image Classification](#semantic-knowledge-distillation-for-onboard-satellite-earth-observation-image-classification)
- [Exploring Model Compression Limits and Laws: A Pyramid Knowledge Distillation Framework for Satellite-on-Orbit Object Recognition](#exploring-model-compression-limits-and-laws-a-pyramid-knowledge-distillation-framework-for-satellite-on-orbit-object-recognition)
  
---


<a name="semantic-knowledge-distillation-for-onboard-satellite-earth-observation-image-classification"></a>

## Semantic Knowledge Distillation for Onboard Satellite Earth Observation Image Classification

authors: Thanh-Dung Le, Vu Nguyen Ha, Ti Ti Nguyen, Geoffrey Eappen, Prabhu Thiruvasagam, Hong-fu Chou, Duc-Dung Tran, Luis M. Garces-Socarras, Jorge L. Gonzalez-Rios, Juan Carlos Merlano-Duncan, Symeon Chatzinotas<br>
paper  : [IEEE](https://arxiv.org/abs/2411.00209)<br>
year   : 2024<br>
code   : [GitHub](https://github.com/ltdung/SnT-SENTRY)<br>

- *Dual Teachers* EfficientViT $T_1$ and MobileViT $T_2$, sudent $S
	- softern probability distribution with temperature $\tau$: 
		$$ P_{T_1}(x) = \text{softmax}(\frac{T_1(x)}{\tau}), P_{T_2}(x) = \text{softmax}(\frac{T_2(x)}{\tau}), P_{S}(x) = \text{softmax}(\frac{S(x)}{\tau}) $$
	- dynamic weighting
		- confidence scores: $C_{T}=\mathbb{E}\left[\max \left(P_{T}(x)\right)\right]$
		- $C_{T_1}$, $C_{T_2}$ -> teacher weights $\alpha,\beta$
		- algorithm:
			1. when $C_{T_1} < 0.4$ and $C_{T_2} < 0.4$ then
				- $\alpha$, $\beta$ ← 0.0, 0.0 // Ignore both teachers
			2. when if $C_{T_1} < \delta$ and $C_{T_2} < \delta$ then
				- $\alpha$ ← max(0.5 − (δ − $C_{T_1}$), wmin)
				- $\beta$ ← max(0.5 − (δ − $C_{T_2}$), wmin)
			3. when if $C_{T_1} < \delta$ then
				- $\alpha$, $\beta$ ← 0.3, 0.7 // Reduce α, prioritize teacher 2
			4. when if $C_{T_2} < \delta$ then
				- $\alpha$, $\beta$ ← 0.7, 0.3 // Reduce β, prioritize teacher 1
			5. else
				- $\alpha$, $\beta$ ← 0.5, 0.5 // Equal weighting for both confident teachers
- KL divergence loss:
	$$D_{\mathrm{KL}}\left(P_S(x) \| P_{T_i}(x)\right)=\frac{1}{\tau^2} \sum_j P_{T_i}(x)_j \log \left(\frac{P_{T_i}(x)_j}{P_S(x)_j}\right)$$
- Loss
	$$\mathcal{L}_{\text {total }}=\left(1-\frac{\alpha+\beta}{2}\right) \cdot \mathrm{CE}_{\text {loss }}+\frac{\alpha+\beta}{2} \cdot \mathrm{KD}_{\text {loss }}$$

<img src="/sigma/dualkd.png" width=600>

- better than single teacher or trained from scratch 

- [EuroSat dataset](https://github.com/phelber/EuroSAT) - Land Cover (10 classes)

	| Model | Accuracy $(\uparrow)$ | Precision $(\uparrow)$ | Recall $(\uparrow)$ |
	| :--- | :---: | :---: | :---: |
	| ResNet8 (Base) | 87.76 | 87.7 | 87.76 |
	| ResNet8 (EfficientViT) | 91.77 | 91.74 | 91.77 |
	| ResNet8 (MobileViT) | 91.06 | 91 | 91.06 |
	| ResNet8 (Dual) | $\mathbf{9 2 . 8 8}$ | $\mathbf{9 3 . 0 7}$ | $\mathbf{9 2 . 8 8}$ |
	| ResNet16 (Base) | 92.9 | 92.91 | 92.9 |
	| ResNet16 (EfficientViT) | 94.49 | 94.52 | 94.49 |
	| ResNet16 (MobileViT) | 93.29 | 93.33 | 93.29 |
	| ResNet16 (Dual) | $\mathbf{9 6 . 4 6}$ | $\mathbf{9 6 . 5 2}$ | $\mathbf{9 6 . 4 6}$ |


<a name="exploring-model-compression-limits-and-laws-a-pyramid-knowledge-distillation-framework-for-satellite-on-orbit-object-recognition"></a>
  
## Exploring Model Compression Limits and Laws: A Pyramid Knowledge Distillation Framework for Satellite-on-Orbit Object Recognition

authors: Yanhua Pang , Graduate Student Member, Yamin Zhang , Yi Wang, Xiaofeng Wei , and Bo Chen<br>
paper  : [IEEE](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10378728&tag=1)<br>
year   : 2024<br>

- Pyramid Knowledge Distillation (PKD)
	- Multi-level knowledge distillation
	- Combination of online and offline distillation
		- *online* - teacher and student are trained together
		- *offline* - teacher is pretrained and used to train the student
	- Multiple couples of teacher and student - Deep Mutual Learning (DML)
	- Final supervised los using compbined features with attention module
	- Up to 26 models with difference of $I=2$ layers between them
		- Task and dataset dependent
- ResNet structure achieved better performance and compression ratio than VGGs
	- VGG baseline usually better than ResNet baseline
	- ResNet distiled better or equal to VGG distiled with better compression and performance
- Report that PKD outperforms other distillation methods
	- Dual knowledge distillation
	- Collaborative consistent knowledge distillation
	- Pairwise similarity knowledge distillation

<img src="/sigma/pkd.png" width=700>

  