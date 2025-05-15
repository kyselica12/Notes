
# LORA: LOW-RANK ADAPTATION OF LARGE LAN- GUAGE MODELS
authors : Edward Hu, Yelong Shen,Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhu Li, Hean Wang, Lu Wang, Weizhu Chen
link    : [arXiv](https://arxiv.org/pdf/2106.09685)
year    : 2021

- Freeze the big Transformer model and train only small "adapters"

> [!quote]
> ...at the pre-trained language models have a low “instrisic dimension” and can still
learn efficiently despite a random projection to a smaller subspace. Inspired by this, we hypothesize the updates to the weights also have a low “intrinsic rank” during adaptation.

- Using this insight then the fully connected MLP in transformer can be written as follows:

	$$ W_0 + \Delta W  = W_0 + BA $$
	where $A,B$ are low-rand matrices $B\in \mathbb{R}^{d\times r}$, $A\in \mathbb{R}^{r\times k}$. Then the forward pass is:
	$$ h = W_ox + \Delta Wx = W_0x + BA x $$

- Only $A,B$ are trained while the original model is frozen
	- resulting in less trainable parameters - lower GPU requirements 


# Lightweight Adapter Learning for More Generalized Remote Sensing Change Detection
authors : Dou Quan, Rufan Zhou, Shuang Wang, Ning Huyan, Dong Zhao, Yanan Li, Licheng Jiao
link    : [arXiv](https://arxiv.org/pdf/2504.19598)
year    : 2025

- Use Dataset specific adapters on encoder-decoder architecture
- Base network for general understanding + adapters finetuned for specific task/dataset
	- Adapters use attention mechanism to incorporate low-resolution and high-resolution features

![[canet.png]]


# Fine-tune Smarter, Not Harder: Parameter-Efficient Fine-Tuning for Geospatial Foundation Models
authors : Francesc Marti Escofet, Benedikt Blumenstiel, Lunus Scheibenreif, Paolo Fraccaro, Konran Schindler
link    : [arXiv](https://arxiv.org/pdf/2504.17397)
code    : [GitHub](https://github.com/IBM/peft-geofm/)
year    : 2025


- Comparison of different fine-tunning methods for foundational models (transformer based)
	- LoRa
	- VPT (learnable input tokens)
	- Adapters (to be compatible with various types of decoders)
	![[finetuning.png]]
- These methods does not necessary guarantee better performance than fully fine-tuned model - depends on the model, dataset ....
- Sometimes better hidden representation for out of distribution data
- UNet performing quite well on the tasks
- Prithvi performance with different decoders
	1. FCN (Fully Convolutional Decoder) 
	2. UNet (close) - best for other models like Clay
	3. Linear Decoder (close) - quite surprising as it is very simple
	4. UpperNet (not very good)



# Remote Sensing Imagery for Flood Detection: Exploration of Augmentation Strategies

authors : Vladyslav Polushko, Damjan Hatic, Ronald Rosch, Thomas Marz, Markus Rauhut and Andreas Weinmann
link    : [arXiv](https://arxiv.org/pdf/2504.20203)
year    : 2025

- Comparison of augmentation techniques for change detection on Remote sensing
- Best performing *Distortion* and *Blur & Noise*
	![[augmentations.png|700]]
- *Distortion* 
	- OpticalDistortion - warps the image by applying barrel or pincushion distortion
	- ElasticTransform - alters an image according to a displacement map using random deformation
	- GridDistortion - randomly shift pixels in an image 
	- GridDropout - removing pixels in a structural manner 
	- GridElasticDeform - applies deformation over a grid to create a complex and elastic transformation 
	- Perspective - alters the perspective view of the image, as if taken from a different viewpoint 
	- RandomScale - randomly scale the image within a set range 
	- CropAndPad - crops the image and pads the remaining part
- *Blur & Noise*
  - GaussianBlur - blurs the image using a Gaussian kernel
  - MotionBlur - simulates motion blur by applying a linear kernel
  - MedianBlur - blurs the image using a median filter
  - GaussianNoise - adds Gaussian noise to the image
  - Zoom 


# Earth-Adapter: Bridge the Geospatial Domain Gaps with Mixture of Frequency Adaptation
authors : Xiaoxing Hu, Ziyang Gong, Yupei Wang, Yuru Jia, Gen Luo, Xue Yang
link    : [arXiv](https://arxiv.org/pdf/2504.06220)
year    : 2025
code    : [GitHub](https://github.com/VisionXLab/Earth-Adapter)

- Use DTF (Discrete Fourier transform) to divide signal into low and high frequency features
- Mixture of Adapters (MoA) 
	- 3 adapters for low frequency, high frequency and spatial features
		- Spatial adapter takes the original features
- Report best results for cross-domain adaptation

![[earthadapter.png]]

# A Sensor Agnostic Domain Generalization Framework for Leveraging Geospatial Foundation Models: Enhancing Semantic Segmentation via Synergistic Pseudo-Labeling and Generative Learning
authors : Anan Yaghmour, Melba M. Crawford, Saurabh Prasad
link    : [arXiv](https://arxiv.org/pdf/2505.01558)
code    : [GitHub](https://github.com/anan0110692/GeoAI-FoundGen)
year    : 2025

- Traines the source domain together with the target domain (with limited samples)
	- Computes $\mathcal{L}_{seg}$  for both domains
	- Generates pseudo labels for the target domain + Shanon Entropy in $\mathcal{L}_{DA}$, to make more confident predictions
	- Use Masked AutoEncoder (MAE) to reconstruct masked image from the target domain $\mathcal{L}_{MAE}$
	 ![[yaghmour.png|600]]


# ChangeAnywhere: Sample Generation for Remote Sensing Change Detection via Semantic Latent Diffusion Model
authors : Kai Tang, Jin Chen
link    : [arXiv](https://arxiv.org/pdf/2404.08892)
code    : [GitHub](https://github.com/tangkai-RS/ChangeAnywhere)
year    : 2024

- Trained difusion model in latent space to generate samples for change detection
- Samples are generated using the "change mask" and segmentation mask of the input image

![[changeanywhere.png|900]]


# Parameter Efficient Self-Supervised Geospatial Domain Adaptation
authors : Linus Scheibenreif, Michael Mommert, Damian Borth
link    : [OpenAccess](https://openaccess.thecvf.com//content/CVPR2024/papers/Scheibenreif_Parameter_Efficient_Self-Supervised_Geospatial_Domain_Adaptation_CVPR_2024_paper.pdf)
code    : [GitHub](https://github.com/HSG-AIML/GDA)
year    : 2024


- Following on LoRa it is adding trainable scaling parameters which scale the activations of the frozen model

	![[slr.png|400]]

- Good performance on domain adaptation
	![[slr-results.png|400]]



# Efficient Adaptation of Deep Neural Networks for Semantic Segmentation in Space Applications
authors : Leonardo Olivi, Edoardo Santero Mormile, and Enzo Tartaglione
link    : [arXiv](https://arxiv.org/pdf/2504.15991)
year    : 2025

- Demonstrated use of adapters for training ResNet18/34/50, VGGNet, Mobilenet... for parameter efficient finetuning
- Instead of updating the whole model on the device just send the lightweight adapters
- Little performance drop 


# Towards a Unified Copernicus Foundation Model for Earth Vision
authors : Yi Wang, Zhitong Xiong, Chenying Liu1, Adam J. Stewart, Thomas Dujardin, Nikolaos Ioannis Bountos, Angelos Zavras, Franziska Gerken, Ioannis Papoutsis, Laura Leal-Taixé, Xiao Xiang Zhu
link    : [arXiv](https://arxiv.org/html/2503.11849v1)
code    : [GitHub](https://github.com/zhu-xlab/Copernicus-FM)
year    : 2025

- **Copernicus-Pretrain**:
	- A massive-scale dataset with 18.7 million aligned images from all major Copernicus Sentinel missions (Sentinel-1 to Sentinel-5P).
	    - Includes Sentinel-1 (SAR), Sentinel-2 (multispectral reflectance), Sentinel-3 (multispectral radiance), Sentinel-5P (atmospheric variables), and Copernicus DEM GLO-30 elevation data.
	- Aligned with ERA5 reanalysis dataset for EO and weather/climate data consistency.
	- Organized in 0.25° × 0.25° grid cells (~28 km surface area).
- **Copernicus-FM**:
	- A unified foundation model processing any spectral or non-spectral sensor modality.
	- Utilizes dynamic hypernetworks and metadata encoding for versatile applications.
- **Copernicus-Bench**:
	- A benchmark with 15 datasets across three task levels: preprocessing (e.g., cloud detection), base applications (e.g., land cover classification), and specialized applications (e.g., air quality estimation).
	    - Level-1: Two cloud detection tasks (Sentinel-2/3).
	    - Level-2: Eight land use/land cover classification/segmentation tasks (Sentinel-1/2/3).
	    - Level-3: Five specialized tasks (Sentinel-1/2/3/5P).
	- Includes nine existing datasets with permissive licenses and six newly curated for Sentinel-3 and Sentinel-5P.
    - Provides linear regression results on 10-year climate parameter means and variability, reporting RMSE scores.


# TiMo: Spatiotemporal Foundation Model for Satellite Image Time Series

authors : Xiaolei Qin, Di Wang, Jing Zhang, Fengxiang Wang, Xin Su, Bo Du, Liangpei Zhang
link    : [arXiv](https://arxiv.org/html/2505.08723v1)
code    : [GitHub](https://github.com/MiliLab/TiMo) 
year    : 2025

- **Architecture**:
    - **Hierarchical Vision Transformer**: TiMo employs a hierarchical vision transformer architecture tailored for capturing multiscale spatiotemporal patterns in SITS data.
    - **Spatiotemporal Gyroscope Attention (STGA)**: Introduces a novel attention mechanism that dynamically captures evolving patterns across both spatial and temporal dimensions.
    - **Differential STGA (D-STGA)**: Enhances the model's ability to detect subtle changes by focusing on differences across time.
- **Pre-training Dataset - MillionST**:
    - **Scale and Diversity**: A large-scale dataset comprising one million images from 100,000 geographic locations, each with 10 temporal phases over five years, encompassing various geospatial changes and seasonal variations.
    - **Self-Supervised Learning**: Utilizes masked image modeling to pre-train TiMo, enabling it to learn generalizable spatiotemporal representations without reliance on labeled data.
- **Superior Results**: demonstrates state-of-the-art performance across multiple tasks, including deforestation monitoring, land cover segmentation, crop type classification, and flood disaster assessment - *Surpassing models like Prithvi*

> [!warning] weights / code not available yet!! 2025-05-15




# Matryoshka Pruning??

---

COSPAR 
9999 blbost
5000 7000 - kratky signal
6000 - stabilny














