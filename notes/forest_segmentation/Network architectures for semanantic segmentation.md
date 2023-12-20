### Benchmarking and scaling of deep learning models for land cover image classification
([link](https://www.sciencedirect.com/science/article/pii/S0924271622003057)/[[notes/forest_segmentation/bibliography#Benchmarking and scaling of deep learning models for land cover image classification|citation]])


- BigEarthNet dataset
- 19 LULC classes
- Tested multiple architectures:
- ResNet
- VGG
- ViT
- MLPMixes (not the worst performace + low number of parameters)
- CNN
- WRN (wide residual network) + EfficientNet with attention (best performance)
### Fully Convolutional Networks for Semantic Segmentation
[[notes/forest_segmentation/bibliography#Fully Convolutional Networks for Semantic Segmentation|citation]]


- Fully Convolutional network for pixel-vise semantic segmentation from CNN for image classification
- Uses modified CNN for image classification like ImageNet, LeNet, GoogleNet - in the final experiments VGG-16 layer net used
- Introduced **updampling convolution** - using bilinear convolution with learnable parameters (to be able to learn nonlinear upsampling)
- 1x1 convolution added to cast the output to the number of channels identical to the number of segmentation classes
- Added skipped connections to address the issue of low details

![Fully CNN](FCN_1.png)

Skipped connections are used to preserve more information about details in the image in output (large upsampling strides tends to loose information about small details in the input image)

![Fully CNN architecture with skipped connections](FCN_architecture.png)
### U-Net: Convolutional Networks for Biomedical Image Segmentation
([link](https://link.springer.com/chapter/10.1007/978-3-319-24574-4_28)/[[notes/forest_segmentation/bibliography#U-Net: Convolutional Networks for Biomedical Image Segmentation|citation]])

- Full CNN network reminding U-shape
- Output is the same size as image containing one output channel for one segmentation class
- Uses down and upsampling blocks
- Do not use padding in convolutions rather it mirrors the image around the edges.

![Unet architecture](Unet.png)


### Semantic image segmentation with deep convolutional nets and fully connected CRFs
([link](https://arxiv.org/abs/1412.7062)/[[notes/forest_segmentation/bibliography#Semantic image segmentation with deep convolutional nets and fully connected CRFs|citation]])

- Use of **atrous algorithm** or altrous convolution.

Basic convolution can be computed as:

$$I \star K (i) =  \sum_{-\Delta < a < \Delta} I(i+a)K(i) $$

Astrous convolution can be written as:

$$I \star K (i) =  \sum_{-\Delta < a < \Delta} I(i+\mathbf{r} a)K(i) $$

where $\mathbf{r}$ is the rate parameter or initial stride. It represents how many pixels in the original image are skipped between each pixel of the kernel.

![Atrous convolution](atrous_convolution.png)

It is used to broater the field of view quicker without increasing the number of parameters.

This helped to reduce number of parameters and widen the field of view so keep information about local details.

- **CRF** Conditional random fields - to smooth noisy segmentation maps. Pixels class is assigned based on the assigned probability to itself and to its neighbors (close in space, close in color). Model employs the enrgy function

$$
E(x)=\sum_{i}\theta_{i}(x_{i})+\sum_{i j}\theta_{i j}(x_{i},x_{j})
$$

$$
w_{1}\exp\left(-\,{\frac{||p_{i}-p_{j}||^{2}}{2\sigma_{\alpha}^{2}}}-{\frac{||I_{i}-I_{j}||^{2}}{2\sigma_{\beta}^{2}}}\right)+w_{2}\exp\left(-\,{\frac{||p_{i}-p_{j}||^{2}}{2\sigma_{\gamma}^{2}}}\right)
$$

where $p$ is the position, $I$ is color (RGB) vector and $\sigma$ are hyper parameters.
### Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation
([link](https://openaccess.thecvf.com/content_ECCV_2018/html/Liang-Chieh_Chen_Encoder-Decoder_with_Atrous_ECCV_2018_paper.html)/[[notes/forest_segmentation/bibliography#Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation|citation]])

- Encoder-Decoder architecture for better reconstruction
- Xception network with depthwise-separable convolutions (convolution is done by channels separatly and processed by 1x1 convolution at the end to reduce number of computations)
- atrous separable convolutions
- resulting model is faster and stronger on PASCAL VOC2012 dataset than state of the art

![DeepLabV3+](DeepLabV3+.png)

### Swin Transformer: Hierarchical Vision Transformer using Shifted Windows
([link](https://openaccess.thecvf.com/content/ICCV2021/html/Liu_Swin_Transformer_Hierarchical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper)/[[notes/forest_segmentation/bibliography#Swin Transformer: Hierarchical Vision Transformer using Shifted Windows|citation]])

- Transformer achitecture adapted on vision tasks to become an universal backbone architecture
- Introduced:
- Hierarchical feature maps by merging patches (in contrast to ViT - Visual transformer)
- Shifted Windows approach for computing self attention -> every other block shifftes patches from previous block to get overlaps

![[swin_sw.png]]



- State of the art performance on various computer vision tasks including semantic segmentation

### Segment Anything
([link](https://arxiv.org/abs/2304.02643)/[[notes/forest_segmentation/bibliography#Segment Anything|citation]])

- Promt based segmentation
- trained with over 1 billion masks
- Promts:
- Point
- Box
- Mask
- Free-form text
- Model:
- Image encoder - pretrained ViT
- Prompt encoder - point and boxes (position embedding), masks (cnn + sum)m text (off-the-shelf from CLIP)
![SAM](SAM.png)
- Aplications:
- Zero-shot Transfer learning
- Zero-shot Edge detection
- Zero-shot Instance segmentation
- Automatic labeling system
- Publicly available pretained version
