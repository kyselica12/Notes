### Self-supervised Learning in Remote Sensing: A review
([link](https://paperswithcode.com/paper/self-supervised-learning-in-remote-sensing-a)/[[bibliography#Self-supervised Learning in Remote Sensing: A review|citation]])

- Review of self-supervised learning methods usable in remote sensing

    ![Self-supervised methods](self_supervised_tree.png)

- Comparison of deep learning models on banchmark datasets

    ![Self-supervised methods](self-supervised_compared.png)


## Metrics & Loss functions

### Weighted Intersection over Union
([link](https://arxiv.org/pdf/2107.09858)/[[bibliography#Weighted Intersection over Union|citation]])

- Proposed new metric for Image segmentation
- Focus more on boundaries -> adjustable with $\alpha$ parameter
- Weights are computed using L2 norm 
    1. $D(p)$ distance to closest pixel of backgound (pixel belonging to other class)
    1. Rescaled distances $\in (0,1)$ -> $\bar{D}(p) = D(p) / \text{max}(D(p))$
    1. $W(p) = e^{-\alpha \bar{D}(p)}$ 


|  |  |
| :---: | :---: |
| Ground truth | ![Ground truth image](wIOU_gt.png) |
| **Alpha** | **Weight map**| 
| $\alpha=0.01$ | ![alpha 0.001](wIOU_alpha_01.png) |
| $\alpha=1$ | ![alpha 0.001](wIOU_alpha_1.png) |
| $\alpha=100$ | ![alpha 0.001](wIOU_alpha_100.png) |


### A survey of loss functions for semantic segmentation
([link](https://arxiv.org/abs/2006.14822)/[[bibliography#A survey of loss functions for semantic segmentation|citation]])

| Type | Loss Function |
| :---: | :---: |
| Distribution-based Loss | Binary Cross Entropy |
| | Weighted Cross Entropy |
| | Balanced Cross Entropy |
| | Focal Loss |
| | Distance map derived loss penalty term |
| Region-based Loss | Dice Loss |
| | Sensitivity-Specificity Loss |
| | Tversky Loss |
| | Focal Tversky Loss |
| | Log-Cosh Dice Loss |
| Boundary-based Loss | Hausdorff Distance loss | 
| | Shape-aware Loss |
| Compounded Loss | Combo Loss |
| | Exponential Logaritmic Loss |

1. **Cross Entropy Loss**
    $$ L_{CE}(y,\hat y) = -y \text{log} \hat y  - (1-y) \text{log} (1 - \hat y)$$
    1.1. **Weighted Cross Entropy Loss**
        - added term $\beta$ to tune false positives / negatives. $\beta > 1$ dicreases the number of FN, $\beta < 1$ decreases the number of FP.
        $$ L_{WCE}(y,\hat y) = -\beta y \text{log} \hat y  - (1-y) \text{log} (1 - \hat y)$$
    1.2. **Balanced Cross Entropy Loss** 
        - weight also for the negative examples 
        $$ L_{BCE}(y,\hat y) = -\beta y \text{log} \hat y  - (1-\beta)(1-y) \text{log} (1 - \hat y)$$
        $$ \beta = 1 - \frac{y}{H \times W}$$
2. **Focal Loss**
    $$ p_t = 
    \begin{cases}
    p ,& \text{if } y = 1\\
    1-p, & \text{otherwise}
    \end{cases} 
    $$
    $$ L_{F}(p_t) = -\alpha_t (1-p_t)^{\gamma}\text{log} (p_t) $$
    - for $\gamma = 1$ it is the same as Cross Entropy. 
    - $\alpha_t$ can be set to inverse class frequency
3. **Dice Loss**
    $$ L_{D}(y, \hat p) = 1 - \frac{2y\hat p + 1}{y + \hat p + 1} $$

    3.1. **Traversky Loss**
        $$ L_{T}(p, \hat p) =1 - \frac{1+ p \hat p}{1+p\hat p + \beta (1-p) \hat p + (1-\beta) p(1- \hat p)} $$
        - $\beta$ is used to tune the loss to focus on FP or FN
        - $\beta = 0.5$ is the same as Dice Loss
        - Traversky index: 
            $$ TI(p, \hat p) =\frac{p \hat p}{p\hat p + \beta (1-p) \hat p + (1-\beta) p(1- \hat p)} $$
    3.2. **Focal Traversky Loss**
        $$L_{FT} = \sum_c (1 - TI_c)^\gamma  $$
        - attempt to focus on hard examples
4. **Sensitivity Specificity Loss**
    - Sensitivity:  $SE = \frac{TP}{TP + FN}$
    - Specificity: $SP = \frac{TN}{TN + FP}$
    $$ L_{SS} = w * SE + (1-w) * SP $$
    - tackle imbalance in the dataset using $w$ parameter
5. **Shape-aware Loss**
    - Shape-aware loss calculates the average point of predicted segmentation to the ground truth 
    $$ E_i = D(\hat C, C) $$
    $$ L_{SA} = - \sum_i \text{CrossEntropy}(y, \hat y) - \sum_i i E_i \text{CrossEntropy}(y, \hat y) $$
    - Using $E_i$ model learns to predict masks with similar shape as the ground truth
6. **Combo Loss**
    - Weighted Dice loss + modified cross entropy
    $$ L_{mce} = -\frac{1}{N} \sum_i \beta (y-log(\hat y)) + (1-\beta)(1-y)log (1-\hat y) $$
    $$ L_{cl} = \alpha L_{mce} - (1-\alpha) L_{D}(y, \hat y) $$

    6.1. **Exponential Logaritmic Loss**
        - exponential smoothing of the loss
        $$ L_{exp} = w_D e^{-ln(L_{D})^{\gamma_D}} + w_c e^{w_l (-ln(p_l))^{\gamma_c}} $$
        - in paper $\gamma_c = \gamma_D$