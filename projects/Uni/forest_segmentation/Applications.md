### Momentum Contrast for Unsupervised Visual Representation Learning
[[projects/Uni/forest_segmentation/bibliography#Momentum Contrast for Unsupervised Visual Representation Learning|citation]]


- Momentum Contrast (MoCo)
- V3 current leader on BigEarthNet dataset
- Contrastive loss for unsupervised learning
- Encoder computes a query and another a key, query should be similar to ist key and dissimilar to other keys.
- Queue of old keys is stored to compute the loss
- Key encoder is updated with momentum of the query encoder weights
- pseudo code:

![Momentum Contrast](MoCo.png)
### Weakly supervised semantic segmentation of satellite images for land cover mapping - challenges and opportunities
([link](https://arxiv.org/abs/2002.08254)/[[projects/Uni/forest_segmentation/bibliography#Weakly supervised semantic segmentation of satellite images for land cover mapping - challenges and opportunities|citation]])

- *Implemented by previous intern*
- Use of low-resolution training data to train a model for high-resolution data
- Several models trained -> Unet, DeepLabV3+

### Satellite Image Semantic Segmentation
([link](https://arxiv.org/abs/2110.05812)/[[projects/Uni/forest_segmentation/bibliography#Satellite Image Semantic Segmentation|citation]])

- Uses Swin Transformer - Using **S**hifted **WIN**dows makes it robust against scala variability
- 6 classes :
- sparse forest
- dense forest
- moor
- herbaceous formation
- biulding
- road
- open data IGN <a href="https://geoservices.ign.fr/telechargement">test</a>
- BD Ortho for the satellite images
- BD Foret v2 for vegetation data
- <a href="https://github.com/koechslin/Swin-Transformer-Semantic-Segmentation">Github repository</a>

### Satellite Image Segmentation Using Deep Learning for Deforestation Detection
([link](https://ieeexplore.ieee.org/abstract/document/9575783/)/[[projects/Uni/forest_segmentation/bibliography#Satellite Image Segmentation Using Deep Learning for Deforestation Detection|citation]])

- Dataset - 322 Images 512 x 512, PyAutoGiu + Google Earth
- Classes:
- Forest
- Deforestation
- Other
- Traversky + Dice Loss weighted -> deforestation is the most important class
- IOU metric
- standard U-Net architecture

### Semantic segmentation of slums in satellite images using transfer learning on fully convolutional neural networks
([link](https://www.sciencedirect.com/science/article/pii/S0924271619300383)/[[projects/Uni/forest_segmentation/bibliography#Semantic segmentation of slums in satellite images using transfer learning on fully convolutional neural networks|citation]])

- transfer learning for FCNN - pretrained on ImageNet and QuickBird (satellite imagery)
- VGG19 - classification layer is replaced with 1x1 convolutions for correct number of output channels following upsampling layers
![VGG19 architecture](VGG19.png)
- satellite images
- QiuckBird
- Sentinel 2
- TerraSAR-X

- transfer learning to similar types of images (satellite images) helped -> QuickBird to Sentinel 2

### Forest monitoring in guatemala using satellite imagery and deep learning
([link](https://ieeexplore.ieee.org/abstract/document/8899782)/[[projects/Uni/forest_segmentation/bibliography#Forest monitoring in guatemala using satellite imagery and deep learning|citation]])

- Sentinel 2 data for training and high resolution Digital Globe + Planet platforms for validation
- Shallow U shaped CNN to predict difference between images
- No evaluation yet


### Forest Segmentation with Spatial Pyramid Pooling Modules: A Surveillance System Based on Satellite Images
([link](https://www.mdpi.com/1999-4907/14/2/405)/[[projects/Uni/forest_segmentation/bibliography#Forest Segmentation with Spatial Pyramid Pooling Modules: A Surveillance System Based on Satellite Images|citation]])

- Pretrained Unet as backbone
- Spatial Pyramid Pooling added
- authors report good porformance

![Spatial pyramid pooling](SPP.png)

### Global land use / land cover with Sentinel 2 and deep learning
([link](https://ieeexplore.ieee.org/abstract/document/9553499)/[[projects/Uni/forest_segmentation/bibliography#Global land use / land cover with Sentinel 2 and deep learning|citation]])

- Unet trained from scratch
- Sentinel 2 -> 6 bands
- 10 classes (including trees)
- Tested on Belgium region

![Results on Belgium region](Unet_belgium.png)

### Efficient Deep Semantic Segmentation for Land Cover Classification Using Sentinel Imagery
([link](https://www.mdpi.com/2072-4292/15/8/2027)/[[projects/Uni/forest_segmentation/bibliography#Efficient Deep Semantic Segmentation for Land Cover Classification Using Sentinel Imagery|citation]])

- U-TAE model $\rightarrow$ based on lighweight temporal encoder transformer (LTAE) with Unet architecture with modification
- instead of temporal attention a channel attention is used by switching input channels
- Combination of Sentinel 1 and Sentinel 2 data
- Outperforms other models with very low computational cost (better in details)
- Experiments with the number of input parameters , (ndvi, ndbi, ndwi)
- including class Trees


### Self-supervised Vision Transformers for Land-cover Segmentation and Classification
([link](https://openaccess.thecvf.com/content/CVPR2022W/EarthVision/html/Scheibenreif_Self-Supervised_Vision_Transformers_for_Land-Cover_Segmentation_and_Classification_CVPRW_2022_paper.html)/[[projects/Uni/forest_segmentation/bibliography#Self-supervised Vision Transformers for Land-cover Segmentation and Classification|citation]])

- Self-supervised learning using **contrastive** learning -> to embed different images appart from each other and similar closer
- Using Sentinel 1 and Sentinel 2 imagery
- Swin Transformer + U net architecture

![Architecture](SSL.png)


### Deep Learning in the Mapping of Agricultural LandUse Using Sentinel-2 Satellite Data
([link](https://www.mdpi.com/2673-7086/2/4/42)/[[projects/Uni/forest_segmentation/bibliography#Deep Learning in the Mapping of Agricultural LandUse Using Sentinel-2 Satellite Data|citation]])

- using Unet for segmentation
- Sentinel 2 data

### Double-Step U-Net: A Deep Learning-Based Approach for the Estimation of Wildfire Damage Severity trhough Sentine-2 Satellite Data
([link](https://www.mdpi.com/2076-3417/10/12/4332)/[[projects/Uni/forest_segmentation/bibliography#Double-Step U-Net: A Deep Learning-Based Approach for the Estimation of Wildfire Damage Severity trhough Sentine-2 Satellite Data|citation]])

- Architecture containing 2 separate U-net models
- first one for segmentation of the burned area
- second one for classification of the burned area into 4 classes of severity (negligible, low, medium, high, complete destruction)

![Double UNet parallel](double_unet_parallel.png)

![Double UNet sequential](doubel_unet_sequential.png)

### Superpixel-Based Attentio0n Graph Neural Network for Semantic Segmentation in Aerial Images
([link](https://www.mdpi.com/2072-4292/14/2/305)/[[projects/Uni/forest_segmentation/bibliography#Superpixel-Based Attentio0n Graph Neural Network for Semantic Segmentation in Aerial Images|citation]])
 

- Graph neural network
- Modules:
    - superpixel extraction using SLIC (Simple Linear Iterative Clustering)
    - Feature extraction using CNN
    - GANN (Graph Attention Neural Network) - graph neural network
    - Prediction (upsampling) - no imlementation details
- Graph construction:
    - nodes are superpixels
    - edges are constructed using K nearest neighbors
    - node features are (average RGB, x, y, feature vector)
- on some datasets performs better than DeepLabV3+
- no code available

![SAGNN](SAGNN.png)

### SA2-Net: Scale-aware Attention Network for Microscopic Image Segmentation
([link](https://paperswithcode.com/paper/sa2-net-scale-aware-attention-network-for)/[[projects/Uni/forest_segmentation/bibliography#SA2-Net: Scale-aware Attention Network for Microscopic Image Segmentation|citation]])

- Semantic segmentation of medical images the primary focus is precise segmentation of cells boundaries
- CNN bad for distante dependencies and Transformer bad for local dependencies -> Scale-aware attention modules (SA2)
- Unet structure
    - SA2 modules instead of skip connections
    - Adaptive up-attention (AuA) modules used in upscaling to merge skip connections and upsampled features
    - Deep supervision was used to improve the performance

![SA2](SA2.png)

###  SA2 module

1. features at each scale are preprocesed by Local Scale Attentio (LSA) (with depthwise convolution).

2. Attention weights between scales are computed.
   $$Q = \text{Concat}(\hat{F}^1, \hat{F}^2, \hat{F}^3, \hat{F}^4) $$
   $$\{w^1, w^2, w^3, w^4\} = \text{Conv}(Q)$$
   $$\hat{W} = \text{GeLU}(\text{Conv}(Q))$$
   $$ \overline{F}^i = w^i \odot (\hat{F}^i \odot \hat{W})$$

   Following MLP and conv to produce output

3. Adaptive up-attention module
    - takes input from previout stage $P^{i-1}$ and scale-awere attended $O^i$ 
    - process desribed in the image
    - output is compared to the goud truth using deep supervision, during training


### Enhancing USDA NASS Cropland Data Layer with Segment Anything Model
([link](https://ieeexplore.ieee.org/abstract/document/10233404?casa_token=NmyhA-k_YWkAAAAA:2EvjaHOeOusEUiHvhooAj-QsM5V0ye3umO-NFSS3OoXSBl9aFTrJRGYdlN4U-zS7IX2DIcU7aL1A)/[[projects/Uni/forest_segmentation/bibliography#Enhancing USDA NASS Cropland Data Layer with Segment Anything Model|citation]])

- Sentinel 2 imagery
- Using SAM to find better boundaries between individual fields
    - "freground" -> false - to avoid categorizing crops as background
    - "unique" -> true - to avoid merging of similar fields 

    ![SAM - crop fields](sam_crops.png)

### A Novel Hybrid Method for Urban Green Space Segmentation from High-Resolution Remote Sensing Images
([link](https://www.mdpi.com/2072-4292/15/23/5472)/[[projects/Uni/forest_segmentation/bibliography#A Novel Hybrid Method for Urban Green Space Segmentation from High-Resolution Remote Sensing Images|citation]])

- Semantic segmentation of UGS (Urban green space) 
	- 3 Classes : Trees, Low vegetation, Background
 - Architecture
	![MAFANET architecture](MAFANET1.png)

	 - Encoder backbone -> ResNet50
	 - Encoder - Decoder structure 
	 - New Decoder block
	 - BFF (bilateral feature fusion module - not their idea) - connect two consecutive encoder layers (two scales)
	  ![[MAFANET2.png]]
	- MSPA module - Multi Poolong attention module
		   ![[MAFANET3.png]]
		  ![[MAFANET4.png]]
- Data
	- 4 bands - RGB NIR, resolution up to 0.8 m/px
	- Incorporate $NDVI = \frac{NIR - R}{NIR + R}$  into input
- Results
	![[MAFANET5.png]]
	![[MAFANET6.png]]

