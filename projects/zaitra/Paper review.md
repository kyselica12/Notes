
---
# Table of content

1. [Foundational Models](#foundational-models)
	- [Awesome Remote Sensing Foundation Models](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models?tab=readme-ov-file#awesome-remote-sensing-foundation-models) 
		- A collection of papers, datasets, benchmarks, code, and pre-trained weights for Remote Sensing Foundation Models (RSFMs)
	- [NASA & IBM Prithvi](#nasa--ibm-prithvi)
	- [SSL4EO](#ssl4eo)
	- [MIMRS: A Survey on Masked Image Modeling in Remote Sensing](#mimrs-a-survey-on-masked-image-modeling-in-remote-sensing)
2. [Knowledge distilation](#knowledge-distilation)
	- [Semantic Knowledge Distillation for Onboard Satellite Earth Observation Image Classification](#semantic-knowledge-distillation-for-onboard-satellite-earth-observation-image-classification)
	- [Exploring Model Compression Limits and Laws: A Pyramid Knowledge Distillation Framework for Satellite-on-Orbit Object Recognition](#exploring-model-compression-limits-and-laws-a-pyramid-knowledge-distillation-framework-for-satellite-on-orbit-object-recognition)
2. [Datasets](#datasets)
	- [SSL4EO Datasets and Foundation Models for Landsat Imagery](#ssl4eo-datasets-and-foundation-models-for-landsat-imagery)
	- [Terra A Multimodal Spatio-Temporal Dataset Spanning the Earth](#terra-a-multimodal-spatio-temporal-dataset-spanning-the-earth)
	- [M3LEO A Multi-Modal Multi-Label Earth Observation Dataset](#m3leo-a-multi-modal-multi-label-earth-observation-dataset)
3. [Change detection methodologies](#change-detection-methodologies)
	- [Graph Neural Network based Scene Change Detection Using Scene Graph Embedding with Hybrid Classification Loss](#graph-neural-network-based-scene-change-detection-using-scene-graph-embedding-with-hybrid-classification-loss)
	- [RaVÆn unsupervised change detection of extreme events using ML on‑board satellites](#ravæn-unsupervised-change-detection-of-extreme-events-using-ml-onboard-satellites)
	- [A Transformer-based Siamese Network for Change Detection](#a-transformer-based-siamese-network-for-change-detection)
	- [TransUNetCD: a hybrid transformer network for change detection in optical remote-sensing images](#transunetcd-a-hybrid-transformer-network-for-change-detection-in-optical-remote-sensing-images)
	- [Adapting Segment Anythong Model for Change Detection in VHR Remote Sensing Images](#adapting-segment-anythong-model-for-change-detection-in-vhr-remote-sensing-images)
	- [Unsupervised flood detection on SAR time series using variatinal autoencoder](#unsupervised-flood-detection-on-sar-time-series-using-variatinal-autoencoder)
	- [Deep-Learing-Based System for Change Detection Onboard Earth Observation Small Satellites](#deep-learing-based-system-for-change-detection-onboard-earth-observation-small-satellites)
	- [Domain knowledge-driven variational recurrent networks for drought monitoring](#domain-knowledge-driven-variational-recurrent-networks-for-drought-monitoring)
	- [Mamba Architecture with a Semantic Transformer for Efficient Real-Time Remote Sensing Semantic Segmentation](#mamba-architecture-with-a-semantic-transformer-for-efficient-real-time-remote-sensing-semantic-segmentation)
	- [Geographic Location Encoding with Spherical Harmonics Wnd Sinusoidal Representation Networks](#geographic-location-encoding-with-spherical-harmonics-wnd-sinusoidal-representation-networks)
3. [Adder Networks For FPDA Inference Speed](#adder-networks-for-fpda-inference-speed)
	- [AdderNet: Do We Really Need Multiplications in Deep Learning?](#addernet-do-we-really-need-multiplications-in-deep-learning)
	- [High-speed convolutional neural networks using parallel prefix adders](#high-speed-convolutional-neural-networks-using-parallel-prefix-adders)
	- [Kernel Based Progressive Distillation for Adder Neural Networks](#kernel-based-progressive-distillation-for-adder-neural-networks)
	- [An Empirical Study of Adder Neural Networks for Object Detection](#an-empirical-study-of-adder-neural-networks-for-object-detection)
	- [Searching for Energy-Efficient Hybrid Adder-Convolution Neural Networks](#searching-for-energy-efficient-hybrid-adder-convolution-neural-networks)
	- [All Adder Neural Networks for On-Board Remote Sensing Scene Classification](#all-adder-neural-networks-for-on-board-remote-sensing-scene-classification)
	- [Q-A2NN: Quantized All-Adder Neural Networks for Onboard Remote Sensing Scene Classification](#q-a2nn-quantized-all-adder-neural-networks-for-onboard-remote-sensing-scene-classification)
4. Complementary sources
	- [SSL4EO](https://github.com/zhu-xlab/SSL4EO-S12?tab=readme-ov-file)
		- 2024 Phd Course [website](https://ankitkariryaa.github.io/ssl4eo/) 
			- videos [youtube](https://www.youtube.com/playlist?list=PLZbT99RJ8DPM2VtPhgWaACm9uiEmRfB6t)
			-  Encoding geospatial data in deep neural networks NEFR
				- spherical harmonics as positional encodings + siren (sinusoidal functions intead of relu)
		- Datasets for EO ([link](https://earthnets.retool.com/embedded/public/676aa812-0dca-4e3b-a596-b043d852571d))
		- Review of the methods ([link](https://github.com/satellite-image-deep-learning/techniques?tab=readme-ov-file#change-detection))
	- [Satellite-image-deep-learning](https://github.com/satellite-image-deep-learning/techniques?tab=readme-ov-file#change-detection)
	- my research for semantic segmentation of forests [GitHub](https://github.com/kyselica12/forest_segmentation/blob/main/research/papers.md)
	- [AI4EO](https://github.com/AI4EO)
	- [TerraTorch](https://github.com/IBM/terratorch?tab=readme-ov-file)
		- finetuning framework for Geospatia FM
		- includes: Prithvi, SatMAE, ScaleMAE ...
	- [TorchGeo](https://github.com/microsoft/torchgeo)


# Foundational Models

## Geospatial Reasoning: Unlocking insights with generative AI and multiple foundation models

Link  : [Google blog](https://research.google/blog/geospatial-reasoning-unlocking-insights-with-generative-ai-and-multiple-foundation-models/)<br>
Year  : 2025<br>

- no code or pretrained model available yet
- multimodal foundation model
	- text
	- image
	- geospatial data
	- time series



## NASA & IBM Prithvi

Link: [HuggingFace](https://huggingface.co/ibm-nasa-geospatial)
Paper: [arXiv](https://arxiv.org/pdf/2412.02732)

- NASA’s Harmonized Landsat and Sentinel-2 data archive at 30m resolution
- MAE (masked autoencoder)
	- ViT backbone
	- 3D positional embedding for space-temporal relations
	- second encoding for lat-lon and time
	- training input 4x256x256 (time,w,h)
	- patch size 16x16 (600M version)
	
	 <img src="/sigma/prithvi.png" width=800>

- Evaluation for *Disaster response*
	- Used with [UperNet](https://huggingface.co/docs/transformers/model_doc/upernet)  head decoder

## SSL4EO

paper : [arXiv](https://arxiv.org/pdf/2306.09424)
link  : [Github](https://github.com/zhu-xlab/SSL4EO-S12?tab=readme-ov-file)

- Various backbones pretrained for combination of bands
	- MoCo-v2 method [arXiv](https://arxiv.org/pdf/2003.04297v1)
		- ResNet 18 / 50
		- ViT
	- MAE 
		- ViT only

## FlexiMo: A Flexible Remote Sensing Foundation Model

authors: Xuyang Li, Chenyu Li, Pedram Ghamisi, Senior Member, Danfeng Hong, Senior Member
paper  : [arXiv](https://arxiv.org/pdf/2503.23844)
year   : 2025

- supports arbitrary:
	- input resolution
	- size
	- channel count
	- channel wavelength
- Input:
	1. Input Image
	2. spatial patch size parameter
	3. wavelengths
- wavelength  -> dynamic convolution kernels
- spatial resolution-aware scaling module based on pseudo-inverse bilinear interpolation
- no code or pretrained model available yet


## MIMRS: A Survey on Masked Image Modeling in Remote Sensing

authors: Shabnam Choudhury, Akhil Vasim, Michael Schmitt, Biplap Banerjee<br>
paper  : [arXiv](https://arxiv.org/pdf/2504.03181)<br>
year   : 2025<br>

- 2 approaches:
	1. Making the input -> Reconstruction loss
	2. Augmenting the input -> Contrastive loss

| Model | Backbone | Params (M) | Scene Classification |  | Object Detection |  | Semantic Segmentation |  |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  |  |  | $\begin{gathered}\text { AID } \\\text { TR=50\% }\end{gathered}$ | $\begin{aligned}& \text { RESISC-45 } \\& \text { TR=20\% }\end{aligned}$ | $\begin{gathered}\text { DIOR } \\\text { mAP }_{50}\end{gathered}$ | DIOR-R $\mathrm{mAP}_{50}$ | LoveDA mIoU | $\begin{aligned}& \text { SpaceNetV1 } \\& \mathrm{mF} 1\end{aligned}$ |
| Contrastive - based |  |  |  |  |  |  |  |  |
| SeCo [1] | ResNet-50 | 26 | 95.99 | 92.91 | - | - | 43.63 | 77.09 |
| GASSL [2] | ResNet-50 | 26 | 95.92 | 93.06 | 67.40 | 65.65 | 48.76 | 78.51 |
| CaCo [3] | ResNet-50 | 26 | 95.05 | 91.94 | 66.91 | 64.10 | 48.89 | 77.94 |
| MAE-based |  |  |  |  |  |  |  |  |
| SatMAE [4] | ViT-L | 307 | 96.94 | 94.10 | 70.89 | 65.66 | - | 78.07 |
| ScaleMAE [5] | ViT-L | 307 | 97.58 | 95.04 | 73.81 | 68.17 | - | - |
| [SSL4EO](#ssl4eo) | ViT-S | 22 | 94.82 | 91.21 | 67.91 | 61.23 | - | - |
| RingMo [6] | Swin-B | 88 | 95.06 | 95.06 | 75.90 | 67.59 | - | - |
| RVSA [7] | ViT-B+RVSA | - | 98.50 | 95.69 | 75.80 | 70.51 | 54.00 | 54.00 |
| SelectiveMAE [8] | ViT-L | 307 | 98.48 | 95.77 | 77.80 | 77.80 | 54.31 | 79.46 |

[^1]: Manas, Oscar, et al. "Seasonal contrast: Unsupervised pre-training from uncurated remote sensing data." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.<br>
[^2]: Ayush, Kumar, et al. "Geography-aware self-supervised learning." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.<br>
[^3]: Mall, Utkarsh, Bharath Hariharan, and Kavita Bala. "Change-aware sampling and contrastive learning for satellite images." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.<br>
[^4]: Cong, Yezhen, et al. "Satmae: Pre-training transformers for temporal and multi-spectral satellite imagery." Advances in Neural Information Processing Systems 35 (2022): 197-211.<br>
[^5]: Reed, Colorado J., et al. "Scale-mae: A scale-aware masked autoencoder for multiscale geospatial representation learning." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.<br>
[^6]: Sun, Xian, et al. "RingMo: A remote sensing foundation model with masked image modeling." IEEE Transactions on Geoscience and Remote Sensing 61 (2022): 1-22.<br>
[^7]: Wang, Di, et al. "Advancing plain vision transformer toward remote sensing foundation model." IEEE Transactions on Geoscience and Remote Sensing 61 (2022): 1-15.<br>
[^8]: Wang, Fengxiang, et al. "OpticalRS-4M: Scaling Efficient Masked Autoencoder Learning on Large Remote Sensing Dataset." arXiv preprint arXiv:2406.11933 (2024).<br>

---

# Knowledge distillation

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


---

# Datasets

## SSL4EO: Datasets and Foundation Models for Landsat Imagery

paper : [arXiv](https://arxiv.org/pdf/2306.09424)<br>
link  : [MediaTUM](https://mediatum.ub.tum.de/1660427)<br>

- unlabeled patch triplets 
	1. Sentinel-1 dual-pol SAR
	2. Sentinel-2 top-of-atmosphere multispectral
	3. Sentinel-2 surface reflectance multispectral
- 251079 locations 
- 2640m x 2640m per patch  
- four seasonal time stamps

## Terra: A Multimodal Spatio-Temporal Dataset Spanning the Earth

paper : [OpenReview](https://openreview.net/pdf?id=I0zpivK0A0)
link  : [HuggingFace](https://huggingface.co/datasets/onedean/Terra)

- multimodal dataset 
	- (spatial) time-series
	- images
	- text

## M3LEO: A Multi-Modal Multi-Label Earth Observation Dataset

paper : [arXiv](https://arxiv.org/abs/2406.04230)
link  : [HuggingFace](https://huggingface.co/M3LEO)

- bigger than SSL4EO 1.05M tiles
- no change detecetion labels
	 <img src="/sigma/m3leo.png" width=800>

## Efficient Self-Supervised Learning for Earth Observation via Dynamic Dataset Curation

authors: Thomas Kerdreux, Alexandre Tuel, Quentin Febvre, Alexis Mouche, Bertrand Chapron
paper  : [arXiv](https://arxiv.org/pdf/2504.06962)
year   : 2025
link   : **NO CODE AVAILABLE YET 5/15/2025**[GitHub](github.com/galeio-research/nereus-sar-models/)

- Sentinel 1
- Automatic dataset curation
	- itterative process
		1. train a model for few epochs
		2. use models embeddings to cluster the dataset
		3. sample the clusters


---
# Change detection methodologies


## Graph Neural Network based Scene Change Detection Using Scene Graph Embedding with Hybrid Classification Loss

authors: Soyeon Kim, Kyung-no Joo, Chan-Hyun Youn <br>
year   : 2021 <br>
paper  : [IEEE](https://ieeexplore.ieee.org/document/9621009) <br>
#### Method

1. Construct *Scene graph*
	- Faster RCNN -> object detection (GloVe for the features)
	- Edges - based on relative distance in the image
2. GNN for change detection
	- Compare two graphs 
		- Binary classifier (change yes/no), categorical classification head

<img src="/sigma/graph-generation.png" width=800>

## RaVÆn: unsupervised change detection of extreme events using ML on‑board satellites
authors: Vít Růžička, Anna Vaughan , Daniele De Martini , James Fulton , Valentina Salvatelli  , Chris Bridges , Gonzalo Mateo‑Garcia & Valentina Zantedeschi <br>
year   : 2022 <br>
paper  : [Nature](https://www.nature.com/articles/s41598-022-19437-5) <br>


- 32x32 px tiles (normalize between -1,1)
- trained VAE (variational auto encoder) to learn embeddings
- cosine distance to compare the embedings


## A Transformer-based Siamese Network for Change Detection 

authors: Wele Gedara Chaminda Bandara, Vishal M. Patel <br>
paper  : [IEEE](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9883686)<br>
year   : 2022<br>

- siamese transformer networks *ChangeFormer*
- difference computed at multiple scales
	- learnable metric $\rightarrow$ CNN + ReLU + BN
- differences are psampled to binary change map


<img src="/sigma/changeformer.png" widht=800>


## TransUNetCD: a hybrid transformer network for change detection in optical remote-sensing images

authors: Qungyang Li, Rofei Zhong, Xin Du, and Yu Du <br>
paper  : [IEEE](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9761892) <br>
year   : 2022<br>

- TransUNetCD
	- Unet architecture with Transformer in the middle
- Dice loss + Weighted binary cross entropy
	
<img src="/sigma/transunetcd.png" width=900>


## Adapting Segment Anythong Model for Change Detection in VHR Remote Sensing Images

authors: Lei Ding Kun Zhu, Daifeng Peng, Hao Tang, Kuiwu Yang, and Lorenzo Bruzzone<br>
paper  : [IEEE](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10443350)<br>
year   : 2024<br>
code   : [GitHub](https://github.com/ggsDing/SAM-CD)<br>

- adapting SAM for change detection
	- FastSAM frozen encoder
	- Learnable adaptor to extract features
		- Pyramid structure
	- UNet-like decoder
- cosine distance to learn similar patches
- change map -> $conv ( \sigma (conv (l_1 + l_2)) f_c)$
	- $l_1, l_2$ are concatenated
	- $f_c$ is attention computed using softmax
- better performance with FastSAM than SAM

<img src="/sigma/samcd.png" width=800>


## Unsupervised flood detection on SAR time series using variatinal autoencoder

authors: Ritu Yadav, Andrea Nascetti, Hossein Azizpour, Yifang Ban <br>
paper  : [ELSEVIER](https://www.sciencedirect.com/science/article/pii/S1569843223004594)<br>
year   : 2024<br>

- VAE architecture with LSTM and 3D convolutions to extract temporal and spatial features
	- archietcture is not clear from the publication
- Uses VAE loss + contrastive learning (comparing two different locations)
- Reports better performance than [Raven](#ravæn-unsupervised-change-detection-of-extreme-events-using-ml-onboard-satellites)

## Deep-Learing-Based System for Change Detection Onboard Earth Observation Small Satellites

authors: Chahira Serief, Youcef Ghelamallah, and Youcef Bentoutou<br>
paper  : [IEEE](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10148624&tag=1#page=3.69)<br>
year   : 2023<br>

### Method

1. *coregistration* 
	- to mitigate geometric misalignments (using optical flow)
2. feature extraction with pretrained CNN (as black box) 
3. upsampling
4. compute the difference between inputs
5. feature maps with the highest variance are selected 
6. k-means clustering to cluster change/no change pixels
7. combine all changes

## Domain knowledge-driven variational recurrent networks for drought monitoring

authors: Mengxue Zhang, Miduel-Angel Fernandex-Torres, and Camps-Valls<br>
paper  : [Elsevier](https://www.sciencedirect.com/science/article/pii/S0034425724002700)<br>
year   : 2024<br>

- LSTM + VAE
- computing posteriori | domain knowledge prior distribution
- Loss function
	- KL divergence loss 
	- reconstruction loss
	- Classification loss


## Mamba Architecture with a Semantic Transformer for Efficient Real-Time Remote Sensing Semantic Segmentation

authors: Hao Ding, Bo Xia, Weilin Liu, Zekai Zhang, Jinglin Zhang, Xing Wang and Sen Xu<br>
paper  : [MDPI](https://www.mdpi.com/2072-4292/16/14/2620)<br>
year   : 2025<br>

- real-time semantic segmentation
	- 1024x1024 input, ONNX, fp32, 59 fps
	- Jetson AGX Orin
- Mamba architecture together with CNN for feature extraction
	- linear scaling compared to transformers
- Semantic Transformer during training to help learn better hidden representations

<img src="/sigma/mamba.png" width=800>


## Geographic Location Encoding with Spherical Harmonics Wnd Sinusoidal Representation Networks

authors: Marc Rußwurm, Konstantin Klemmer, Esther Rolf, Robin Zbinden and Devis Tuia<br>
paper  : [arXiv](https://arxiv.org/pdf/2310.06743)<br>
year   : 2024<br>
GitHub : [link](https://github.com/marccoru/locationencoder)<br>


- Spherical Hacmonic coordinate embeddings
	- weighted sum of spherical harmonics
	- no artifacts near the poles
- Uses SirenNets (Sinusoidal Representation Networks)
	- sinusoidal activation function
- Can be used together with other neural networks representing priors - for example land/ocean 

![test](/sigma/inaturalist.png)


# Adder Networks For FPDA Inference Speed

## AdderNet: Do We Really Need Multiplications in Deep Learning?

authors: Hanting Chen, Yunhe Wang, Chunjing Xu, Boxin Shi, Chao Xu, Qi Tian, Chang Xu<br>
paper  : [CVPR](https://openaccess.thecvf.com/content_CVPR_2020/papers/Chen_AdderNet_Do_We_Really_Need_Multiplications_in_Deep_Learning_CVPR_2020_paper.pdf)<br>
year   : 2020<br>
GitHub : [link](https://github.com/huawei-noah/AdderNet)<br>

- Computational cost of multiplication is higher than addition
- $\ell_1$ distance instead of convolution 
 $$ Y(m,n,t) = - \sum_{i=0}^{d}\sum_{j=0}^{d}\sum_{k=0}^{c_{in}} | X(m+i, n+j, k) - K(i,j,k,t) |  $$
- Implementation details
	- $\ell_2$ norm at the start as it produce better gradients
	- Bath normalization after each adder layer
	- Gradient clipping [-1,1]
	- Adaptive learning rate for each filter - gradient for filters are much smaller compared to CNN and differ greatly between filters

| Model | Method | #Mul. | #Add. | XNOR | Top-1 Acc. | Top-5 Acc. |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  | BNN | 0 | 1.8 G | 1.8 G | $51.2 \%$ | $73.2 \%$ |
| ResNet-18 | AddNN | 0 | 3.6 G | 0 | $67.0 \%$ | $87.6 \%$ |
|  | CNN | 1.8 G | 1.8 G | 0 | $69.8 \%$ | $89.1 \%$ |
| ResNet-50 | BNN | 0 | 3.9 G | 3.9 G | $55.8 \%$ | $78.4 \%$ |
|  | AddNN | 0 | 7.7 G | 0 | $74.9 \%$ | $91.7 \%$ |
|  | CNN | 3.9 G | 3.9 G | 0 | $76.2 \%$ | $92.9 \%$ |


## High-speed convolutional neural networks using parallel prefix adders

authors: Butchi Babu Sarnala, Siva Ramakrishna Pillutla<br>
paper  : [ELSEVIER](https://www.sciencedirect.com/science/article/abs/pii/S1434841125001323)<br>
year   : 2025<br>

- Implementation of parrallel prefix adders for CNNs on FPGA
	- Optimized for LeNet
	- Clasic CNN - optimizing the sum of products in the convolutional layer

## Kernel Based Progressive Distillation for Adder Neural Networks

authors: Yixing Xu, Xinghao Chen, Chang Xu, Minjing Dong, Chunjing XU, Yunhe Wang<br>
paper  : [NeurIPS](https://proceedings.neurips.cc/paper/2021/hash/37693cfc748049e45d87b8c7d8b9aacd-Abstract.html)<br>
year   : 2021<br>

- The problem of KD from CNN to AdderNet is in the lattent space distributions
	- CNN weight distribution is Gaussian
	- AdderNet weight distribution is Laplace
- Using the kernel trick to transform the inputs and weights to the common distribution
	- For CNN
	$$ h\left(\mathbf{x}_c^m, \mathbf{f}_c^m\right)=e^{-\frac{\mathbf{x}_c^m * f_c^m}{2 \sigma_c^c}}, $$
	- For AdderNet
	$$ g\left(\mathbf{x}_a^m, \mathbf{f}_a^m\right)=e^{-\frac{\mathbf{x}_a^m \odot \mathscr{f}_a^m}{\sigma_a}} $$
- ResNet50 Adder version achieved better accuracy on ImageNet than the original ResNet50

![alg](/sigma/kd_adder.png)


## An Empirical Study of Adder Neural Networks for Object Detection

authors: Xinghao Chen, Chang Xu, Minjing Dong, Chunjing Xu, Yunhe Wang<br>
paper  : [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2021/file/37693cfc748049e45d87b8c7d8b9aacd-Paper.pdf#page=5.11)<br>
year   : 2021<br>

- Trying to solve the proble of sparce feature maps compared to CNN -> not good for object detection
- Proposed new decoder architecture using top-down and down-top connections to propagate low-level features up 

![decoder](/sigma/adder_decoder.png)


## Searching for Energy-Efficient Hybrid Adder-Convolution Neural Networks

authors: Wenshuo Li, Xinghao Chen, Jinyu Bai, Xuefei Ning, Yunhe Wang<br>
paper  : [IEEE](https://ieeexplore.ieee.org/document/9857279/authors#authors)<br>
year   : 2022<br>

- Modified GhostNet with Adder layers
- Using evolutionary algorithm to search for the best architecture
- Power consumption is the main metric without a loss in accuracy
- Final netowork achieve comparable accuracy to GhostNet on the Imagenet while saving some power ()


## All Adder Neural Networks for On-Board Remote Sensing Scene Classification

authors: Ning Zhang, Guoqing Wang, Jue Wang, He Chen, Wenchao Liu, and Liang Chen<br>
paper  : [IEEE](https://ieeexplore.ieee.org/abstract/document/10105644?casa_token=2xpIpkW5Z48AAAAA:NAkh7_V_JfbZC3bFGssK_IwXNeAZBeMOErqTJP85Kkoq8MhBkQvWnzTyNUMuh6SKsj0_8x_Zp51ZSyo)<br>
year   : 2023<br>

- All Adder Neural Network for scene classification
- KD using two teachers
	- CNN teacher
	- AdderNet teacher
- Using generated images (generator) for training
- Few % worse than CNN


## Q-A2NN: Quantized All-Adder Neural Networks for Onboard Remote Sensing Scene Classification

authors:  Ning Zhang, He Chen, Liang Chen, Jue Wang, Guoqing Wang and Wenchao Liu <br>
paper  : [MDPI](https://www.mdpi.com/2072-4292/16/13/2403#FD10-remotesensing-16-02403)<br>
year   : 2024<br>

- Q-A2NN - quantized All-Adder Neural Network
- Novel  quantization for A2NN 
	- POT-Based Shared Scaling Factor Quantization Scheme
	- weight debiasing (because the orriginal weight distribution is skewed)
	- feature debiasin - KD with original A2NN
- Comparable performance to CNNs 
	- not a big drop in accuracy
