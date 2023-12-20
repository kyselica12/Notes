
1. [ ] Mask Improvement using SAM -> refactoring 
1. [ ] Annotation system [[https://cvat.multitel.be/|CVAT]] -> to create jop / annotate 
1. [ ] Documentation -> SAM mask improvement
1. [ ] Check documentation for modules
	1. [ ] Semantic segmentation
	2. [ ] Satlas super-resolution
	3. [ ] Download-sentinel

# Done

2023-12-01
- [x] Itterative mask improvement [[Super-resolution#Spatial Resolution Enhancement for Large-Scale Land Cover Mapping via Weakly Supervised Deep Learning]]

2023-11-29
- [x] Compare performance of models:
	- Trained on High resolution
	- Trained on lower resolution

2023-11-29
- [x]  <span style="color:#ff0000">Retrain LR to HR model !!!</span>

2023-11-28
- [x] Test Loss functions
	- HR model

2023-11-27
- [x] Resume Super-Resolution for Wallonie spring 2018

2023-11-24
- [x] Copy `2021_months` images to `DATA/Sequences/Protected/IADAS/segmentation_forest/sentinel_Belgium`

2023-11-24
- [x] Implement Loss functions:
	- [x] Focal loss [[https://paperswithcode.com/method/focal-loss|link]] -> check if the implementation is correct
	- [x] IoU loss
	- [x] CE loss -> already used
	- Implementation
		- [x] Add Loss function to Configuration
		- [x] Add weight map to the computation of loss functions
  
2023-11-21
 - [x] Fix mapping between LR images and HR images  for comparison
 
2023-11-21
- [x] Slides for Matthieu
	1. topic
	2. methods
	3. results
	4. problems & perspectives

2023-11-21
- [x] Found bug in resize mask -> <span style="color:#ffc000">bool conversion to uint8 lead to the resulting map of almost all False  values</span>
							-> <span style="color:#00b050">just straight resize Bool array is good</span>
		  
2023-11-20
- [x]  FIX DATASETS -> WRONG NUMBERS
	- [x] HR -> HR dataset: `a9ede607cb8d23d2101beb0fae2`  #DONE
		 -> shift all indices +1
		 -> remove prefixes from names `mask_t_x_y.tif` -> `t_x_y.tif`
	- [x] LR -> HR dataset: `1b08783e7301e59b662e2de892c57944`
		  -> remove prefixes 