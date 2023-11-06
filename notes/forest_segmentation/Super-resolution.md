### Spatial Resolution Enhancement for Large-Scale Land Cover Mapping via Weakly Supervised Deep Learning
([link](https://www.ingentaconnect.com/content/asprs/pers/2021/00000087/00000006/art00009)/[[bibliography#Spatial Resolution Enhancement for Large-Scale Land Cover Mapping via Weakly Supervised Deep Learning|citation]])

- Use Sentinel 1 and Sentinel 2 data to improve *MODIS* land cover data
- *MODIS* data is low resolution (500m) and Sentinel 2 is high resolution (10m)
- **Workflow**:
    - Denoise Sentinel 1 data
    - Data augmentation
    - Tran DeepLabV3+ on Semantic segmentation task using MODIS labels
    - After 5 epoch use *Refine Label* process:
        - Compare MODIS labels with predicted labels of DeepLabV3+ model checkpoint
        - Pixels in the difference are masked out
        - Only inter section of the masks is used for following training
        - Checkpoint is updated each 5 epochs

![Workflow](modis_enhancement.png)

### Super-resolution land cover mapping by deel learning
([link](https://www.tandfonline.com/doi/abs/10.1080/2150704x.2019.1587196)/[[bibliography#Super-resolution land cover mapping by deel learning|citation]])

1. Input land cover map is divided into maps containing only one class
1. For each class CNN is trained to upsample the map
1. Resulting maps are merged into one map by miximizing the following equation
    $$ \text{max: } E = \sum_{v=1}^{z\times z}\sum_{k=1}^K x_k(v) \times p_k(v) $$

    where:

    $$ x_k(v) =  
    \begin{cases}
    1 ,& \text{if } v \text{ is member of class } k \text{ in the input map}\\
    0, & \text{otherwise}
    \end{cases}  
    $$

    $p_k(v)$ is the probability of pixel $v$ belonging to class $k$ in the output map for class $k$.

![Results](deep_SRM.png)

### Enhancing Land Cover Mapping and Monitoring: An Interactive and Explainable Machine Learning Approach Using Google Earth Engine
([link](https://www.mdpi.com/2072-4292/15/18/4585)/[[bibliography#Enhancing Land Cover Mapping and Monitoring: An Interactive and Explainable Machine Learning Approach Using Google Earth Engine|citation]])

- Interactive tool for land cover mapping using Google Earth Engine
- Uses Sentinel 2 data
![Diagram](gee_colab_tool.png)

### SEG-ESRGAN: A Multi-Task Netwoek for Super-Resolution and Semantic Segmentation of Remote Sensing Images
([link](https://www.mdpi.com/2072-4292/14/22/5862)/[[bibliography#SEG-ESRGAN: A Multi-Task Netwoek for Super-Resolution and Semantic Segmentation of Remote Sensing Images|citation]])

- Performing two tasks at once:
	1. Super resolution of Sentinel 2 Imagery
	1. Semantic segmentation
- WorlView imagery used as *gound truth*
- Manually anotated labels
- Target resolution 2m/px
- Modified ESRGAN
	- added branch which uses output of blocks at different depth to as input 
	- this branch is *Encoder-Decoder* architecture for semantic segmentation
- Loss function contains three terms:
	1. $L_{CE}$ - weighted Cross-Entropy loss for semantic segmentatio
	1. $L_1$ - L1 loss between target high resolution image and genereted image
	1. $L_{FA} - Affinity loss - Absolute difference between similarity matrices calculated from high-resolution feature maps of Super-resolution task and segmentation task

	$$L = L_{CE} + w_1 L_1 + w_2 L_{FA}$$

![results](segesrgan.png) 

*(a) is the Sentinel 2 input image, (b) is the target high resolution, (c) output high resolution, (d) target land cover map, (e) output land cover map*

