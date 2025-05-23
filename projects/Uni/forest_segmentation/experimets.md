# Experiments

## 1. Experiment - Different network architectures

- mobilnet backbone
- trained for 10 epochs
- one season dataset

### Results

Most of the models are training in the save fashion except for the 'LinkNet' with slow start.

Results in [experiment1.csv](experiment1.csv)

![Experiment1](experiment1.png)


## 2. Experiment - RGB vs. Sentinel2 Multispectral

- backbones ResNet18, ResNet50 
- two set of weights, pretrained 
    1. Imagenet
    2. SSL4EO-S12
- 10 epochs

### Results

The models pretrained on Sentine2 data are performing better than the models pretrained on Imagenet after 10 epochs. However the convergence was not reached so the results are not conclusive. We can say that the learning should be quicker with the pretrained weights on Sentinel2 data.  

Results in [experiment2.csv](experiment2.csv)

![Experiment2](experiment2.png)



## 3. Experiment - Normalization

In original SSL4EO-S12 paper the authors clip the Sentinel2 data do values between 0 and 1 by dividing the data by 10000.

In this experiment we will compare the result of the pretrained models on data:
    1. Clippped to 0-1
    2. Clipped to 0-1 and normalized with mean and std of the training set

- 20 epochs

### Results

The results shows that the normalization helps quite a lot for the fine-tuning for both Imaget and SSL4OEO-S12 pretrained models. Probably bigger dataset and mini-baches would help to overcome this problem.


| Model | Training accuracy | Validation accuracy |
| ---   | --- | --- |
| ResNet18 pretrained on Imagenet | ![Training accuracy](experiment3_train_acc.png) | ![Validation accuracy](experiment3_val_acc.png) |
|  | [csv](experiment3_train_acc.csv) | [csv](experiment3_val_acc.csv) |
| ResNet18 pretrained on SSL4EO-S12 | ![Training accuracy](experiment3_train_acc_S2.png) | ![Validation accuracy](experiment3_val_acc_S2.png) |
|  | [csv](experiment3_train_acc_S2.csv) | [csv](experiment3_val_acc_S2.csv) |

## 4. Experiment - Finetuning

Finetuning of 4 Unet networks with different backbones pretrained on either SSL4EO-S12 or IMAGENET dataset. All models were trained on SATURN (FMFI UK) server.

Training configurations:
* `batch_size = 10` - due to GPU memory limit
* `num_workers = 0`
* `early stopping`
    * `monitor` -> validation loss
    * `stop criterion` -> no improvement in `5` epochs
* `dataset` 
    * 3 seasons of the year 2021 (spring, summer, autumn)
    * validation split `0.1` based on location

### Results

Backbones pretrained on the SSL4EO-S12 dataset performed better with margin $ \approx1\%$ over models pretrained using Imagenet. For the specific backbone architecture both *Resnet 18* and *Resnet 50* performed similarly - possibly due to small mini batch size and other hyperparameters.

**BEST MODEL ==> Resnet 18 (SSL4EO-S12 pretrained)**

| | |
| --- | --- |
| Validation loss | ![Val loss](finetuned_val_loss.png) |
| Validation accuracy | ![Val loss](finetuned_val_acc.png) |
| Validation dice score | ![Val loss](finetuned_dice_score.png) |


## 5. Experiment - Finetuning / masked data

Data in previous experiments contained examples in which the input image did not contained much information. There are two scenarios when pixel value is set to Nan or 0:
    
- Pixel is occluded by clouds and cloud mask is set for this pixel -> Nan
- Pixel is looking at position outside of the region of interest (in this example Belgium) and set to 0

To remove examples with too little information a preprocessing step filters out all input images with $\geq 30\%$  NaN or zero pixels.

Loss function is modified so it doesnt count positions which in the original image are NaN or zero values.

Two models have been trained both using ResNet18 SSL4EO-S12 pretrained backbone. Dataset consits of three seasons (summer, autumn, spring) in the year 2021.

### Results

Unet model performs slightly better on the validation set. Training was performed using smaller batch size (16) than for the DeepLab (32) due to size of the model and GPU memory limitations.

|            |              Train              |         Validation          |
| :--------: | :-----------------------------: | :-------------------------: |
|    Loss    | ![Train loss](train_loss_2.png) | ![Val loss](val_loss_2.png) |
|  Accuracy  |  ![Train acc](train_acc_2.png)  |  ![Val acc](val_acc2.png)   |
| Dice score | ![Train dice](train_dice_2.png) | ![Val dice](val_dice_2.png) |
|            |                                 |                             |
|            |                                 |                             |


| Model | Val accuracy | Val dice score | Val loss | Val wIoU ($\alpha=1$) |
| --- | ---: | ---: | ---: | ---: | 
| Unet | 0.9337 | 0.9250 | 0.1443 | 0.8152 |
| DeepLabV3+ | 0.9313 | 0.9217 | 0.1502 |  0.8093 |

**Checkpoints**
- Unet:  `Finetuning_masked_data-Unet-epoch=48-val_loss=0.14.ckpt`
- DeepLabV3+: `Finetuning_masked_data-DeepLabv3+-epoch=71-val_loss=0.15.ckpt`


