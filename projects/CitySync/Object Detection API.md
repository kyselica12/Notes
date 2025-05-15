## Instalation

1. 
```
conda create -n tensorflow pip python=3.8
conda activate tensorflow
```
2. 
```
pip install --ignore-installed --upgrade tensorflow==2.5.0
```
3. 
```
conda install conda-forge::cudatoolkit
conda install conda-forge::cudnn
# CUDA related exports
export PATH=/usr/local/cuda-11.2/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
	- restart bash

4. Verify instalation
	- `python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"`
5. Clone models
	- `git clone https://github.com/tensorflow/models`
6. Install `protoc`
7. 
```bash
# From within TensorFlow/models/research/
protoc object_detection/protos/*.proto --python_out=.`
```

8. Coco API instalation
```bash
git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make
cp -r pycocotools <PATH_TO_TF>/TensorFlow/models/research/
```
9. Object detection API
```bash
# From within TensorFlow/models/research/
cp object_detection/packages/tf2/setup.py .
python -m pip install .
```
10. Protobuf package
	- `pip show protobuf` -> version e.g. 3.20.3
	- `pip install --upgrage protobuf`
		- Find `~/miniconda3/envs/tensorflow/lib/python3.8/site-packages/google/protobuf/runtime_version.py` and save
	- `pip install protobuf==<ORIGINAL VERSION>`
	- copy `runtime_version.py`  to `~/miniconda3/envs/tensorflow/lib/python3.8/site-packages/google/protobuf`
11. Verify all
```bash
# From within TensorFlow/models/research/
python object_detection/builders/model_builder_tf2_test.py
```

# Creating FTRecords

From file structure
```
DIRECTORY
|-- [<PLATE 1>,***,**].jpg
|-- [<PLATE 1],***,**].txt
|-- [<PLATE 2>,***,**].jpg
|-- [<PLATE 2],***,**].txt
|-- ...
|-- [<PLATE N>,***,**].jpg
|-- [<PLATE N],***,**].txt
```

Script `to_records.py` can read this file structure and produce `.record` files for now using only the **plate** class.

```bash
python to_records.py -i DIRECTORY -o <output>.record -l <labels_path>.pbtxt -c <output_csv>.csv
```
- `-i` - the input directory containing `.jpg` and `.txt` files
- `-o` - path to \<OUTPUT\>.record
- `-l` - path to LABELS.pbtxt where all classes are specified. Example:
	```
	item {
	    id: 1
	    name: 'plate'
	}
	item {
		id: 2
		name: 'vehicle'
	}
	...
	```

# Training

## Download pretrained models

[Tensforflow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md)

Model name                                                                                                                                                                  | Speed (ms) | COCO mAP | Outputs
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------: | :----------: | :-----:
[CenterNet HourGlass104 512x512](http://download.tensorflow.org/models/object_detection/tf2/20200713/centernet_hg104_512x512_coco17_tpu-8.tar.gz)                    | 70         | 41.9           | Boxes
[CenterNet HourGlass104 Keypoints 512x512](http://download.tensorflow.org/models/object_detection/tf2/20200711/centernet_hg104_512x512_kpts_coco17_tpu-32.tar.gz)                    | 76         | 40.0/61.4           | Boxes/Keypoints
[CenterNet HourGlass104 1024x1024](http://download.tensorflow.org/models/object_detection/tf2/20200713/centernet_hg104_1024x1024_coco17_tpu-32.tar.gz)               | 197       | 44.5           | Boxes
[CenterNet HourGlass104 Keypoints 1024x1024](http://download.tensorflow.org/models/object_detection/tf2/20200711/centernet_hg104_1024x1024_kpts_coco17_tpu-32.tar.gz)               | 211       | 42.8/64.5          | Boxes/Keypoints
[CenterNet Resnet50 V1 FPN 512x512](http://download.tensorflow.org/models/object_detection/tf2/20200711/centernet_resnet50_v1_fpn_512x512_coco17_tpu-8.tar.gz)     | 27         | 31.2           | Boxes
[CenterNet Resnet50 V1 FPN Keypoints 512x512](http://download.tensorflow.org/models/object_detection/tf2/20200711/centernet_resnet50_v1_fpn_512x512_kpts_coco17_tpu-8.tar.gz)     | 30         | 29.3/50.7         | Boxes/Keypoints
[CenterNet Resnet101 V1 FPN 512x512](http://download.tensorflow.org/models/object_detection/tf2/20200711/centernet_resnet101_v1_fpn_512x512_coco17_tpu-8.tar.gz)     | 34         | 34.2           | Boxes
[CenterNet Resnet50 V2 512x512](http://download.tensorflow.org/models/object_detection/tf2/20200711/centernet_resnet50_v2_512x512_coco17_tpu-8.tar.gz)     | 27         | 29.5           | Boxes
[CenterNet Resnet50 V2 Keypoints 512x512](http://download.tensorflow.org/models/object_detection/tf2/20200711/centernet_resnet50_v2_512x512_kpts_coco17_tpu-8.tar.gz)     | 30         | 27.6/48.2           | Boxes/Keypoints
[CenterNet MobileNetV2 FPN 512x512](http://download.tensorflow.org/models/object_detection/tf2/20210210/centernet_mobilenetv2fpn_512x512_coco17_od.tar.gz)     | 6         | 23.4           | Boxes
[CenterNet MobileNetV2 FPN Keypoints 512x512](http://download.tensorflow.org/models/object_detection/tf2/20210210/centernet_mobilenetv2fpn_512x512_coco17_kpts.tar.gz)     | 6         | 41.7           | Keypoints
[EfficientDet D0 512x512](http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d0_coco17_tpu-32.tar.gz)                                  | 39         | 33.6           | Boxes
[EfficientDet D1 640x640](http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d1_coco17_tpu-32.tar.gz)                                  | 54         | 38.4           | Boxes
[EfficientDet D2 768x768](http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d2_coco17_tpu-32.tar.gz)                                  | 67         | 41.8           | Boxes
[EfficientDet D3 896x896](http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d3_coco17_tpu-32.tar.gz)                                  | 95         | 45.4           | Boxes
[EfficientDet D4 1024x1024](http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d4_coco17_tpu-32.tar.gz)                              | 133         | 48.5           | Boxes
[EfficientDet D5 1280x1280](http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d5_coco17_tpu-32.tar.gz)                             | 222         | 49.7           | Boxes
[EfficientDet D6 1280x1280](http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d6_coco17_tpu-32.tar.gz)                             | 268         | 50.5           | Boxes
[EfficientDet D7 1536x1536](http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d7_coco17_tpu-32.tar.gz)                             | 325         | 51.2           | Boxes
[SSD MobileNet v2 320x320](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz)                                |19         | 20.2           | Boxes
[SSD MobileNet V1 FPN 640x640](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8.tar.gz)                        | 48        | 29.1           | Boxes
[SSD MobileNet V2 FPNLite 320x320](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz)                | 22         | 22.2           | Boxes
[SSD MobileNet V2 FPNLite 640x640](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz)                | 39         | 28.2           | Boxes
[SSD ResNet50 V1 FPN 640x640 (RetinaNet50)](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz)                          | 46         | 34.3           | Boxes
[SSD ResNet50 V1 FPN 1024x1024 (RetinaNet50)](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_1024x1024_coco17_tpu-8.tar.gz)                      | 87         | 38.3           | Boxes
[SSD ResNet101 V1 FPN 640x640 (RetinaNet101)](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet101_v1_fpn_640x640_coco17_tpu-8.tar.gz)                        | 57         | 35.6           | Boxes
[SSD ResNet101 V1 FPN 1024x1024 (RetinaNet101)](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet101_v1_fpn_1024x1024_coco17_tpu-8.tar.gz)                    | 104        | 39.5           | Boxes
[SSD ResNet152 V1 FPN 640x640 (RetinaNet152)](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet152_v1_fpn_640x640_coco17_tpu-8.tar.gz)                        | 80         | 35.4           | Boxes
[SSD ResNet152 V1 FPN 1024x1024 (RetinaNet152)](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet152_v1_fpn_1024x1024_coco17_tpu-8.tar.gz)                    | 111        | 39.6           | Boxes
[Faster R-CNN ResNet50 V1 640x640](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet50_v1_640x640_coco17_tpu-8.tar.gz)                 | 53         | 29.3           | Boxes
[Faster R-CNN ResNet50 V1 1024x1024](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet50_v1_1024x1024_coco17_tpu-8.tar.gz)             | 65         | 31.0           | Boxes
[Faster R-CNN ResNet50 V1 800x1333](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet50_v1_800x1333_coco17_gpu-8.tar.gz)               | 65         | 31.6           | Boxes
[Faster R-CNN ResNet101 V1 640x640](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet101_v1_640x640_coco17_tpu-8.tar.gz)               |    55      | 31.8           | Boxes
[Faster R-CNN ResNet101 V1 1024x1024](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet101_v1_1024x1024_coco17_tpu-8.tar.gz)           | 72         | 37.1           | Boxes
[Faster R-CNN ResNet101 V1 800x1333](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet101_v1_800x1333_coco17_gpu-8.tar.gz)             | 77         | 36.6           | Boxes
[Faster R-CNN ResNet152 V1 640x640](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet152_v1_640x640_coco17_tpu-8.tar.gz)               | 64         | 32.4           | Boxes
[Faster R-CNN ResNet152 V1 1024x1024](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet152_v1_1024x1024_coco17_tpu-8.tar.gz)           | 85         | 37.6           | Boxes
[Faster R-CNN ResNet152 V1 800x1333](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet152_v1_800x1333_coco17_gpu-8.tar.gz)             | 101         | 37.4           | Boxes
[Faster R-CNN Inception ResNet V2 640x640](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_inception_resnet_v2_640x640_coco17_tpu-8.tar.gz)             | 206         | 37.7           | Boxes
[Faster R-CNN Inception ResNet V2 1024x1024](http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_inception_resnet_v2_1024x1024_coco17_tpu-8.tar.gz)             | 236         | 38.7           | Boxes
[Mask R-CNN Inception ResNet V2 1024x1024](http://download.tensorflow.org/models/object_detection/tf2/20200711/mask_rcnn_inception_resnet_v2_1024x1024_coco17_gpu-8.tar.gz) |    301      | 39.0/34.6           | Boxes/Masks
[ExtremeNet (deprecated)](http://download.tensorflow.org/models/object_detection/tf2/20200711/extremenet.tar.gz)                                                                         | --         | --           | Boxes
[ExtremeNet](http://download.tensorflow.org/models/object_detection/tf2/20210507/extremenet.tar.gz)| --         | --           | Boxes
## Modify `pipeline.config`

Get configs in `models/research/object-detection/configs/tf2`


### CenternetMobilenetV2 model setup

Copy config with different backbone then MobilenetV2 and modify it:

```
model{
  center_net {
    num_classes: 1 # <- SET THIS VALUE
    feature_extractor {
      type: "mobilenet_v2_fpn_sep_conv"
    }
	...
}
```

### Input size

```
model{
	center_net{
		image_resizer {
			keep_aspect_ratio_resizer {
			min_dimension: 256 # <- SET THIS VALUE
			max_dimension: 256 # <- SET THIS VALUE
			pad_to_max_dimension: true
		}
		...
	}
	...
}
```

### Batch size and \# steps
```
train_config{
	batch_size: 8 # <- SET THIS VALUE
	num_steps: 140 # <- SET THIS VALUE
	...
}
```

### Training data
```
train_input_reader: {
  label_map_path: "path/to/label_map.pbtxt"
  tf_record_input_reader {
    input_path: "path/to/<TRAIN>.record"
  }
  # for multiple record files
  # tf_record_input_reader {
  #   input_path: ["path/to/000.tfrecord", "path/to/001.tfrecord"]
  # }
}
```

### Validation data
```
eval_input_reader: {
  label_map_path: "path/to/label_map.pbtxt"
  shuffle: false
  num_epochs: 1
  tf_record_input_reader {
    input_path: "path/to/test.record"
  }
}
```

### CHECKPOINT

If using checkpoint

```
# inside 
train_config{
	...
	fine_tune_checkpoint_version: V2
	fine_tune_checkpoint: "PATH_TO_BE_CONFIGURED/ckpt-1"
	fine_tune_checkpoint_type: "detection"
}
```


# TRAINING

1. Copy `models/research/object_detection/model_main_tf2.py` to your working directory
2. 


# USEFUL LINKS

- [Training Custom Object Detector](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html)



# TODO

- zistit ci je problem s GPU iba pre centernet alebo aj pre ine modely ako SSD
- Docker image



