# TODO 

## Sigma - Change Detection

1. [ ] Jetson Stats
	- Benchmark model inference
		- ResNet18/50
		- ViT-S16
2. Knowledge distillation repository setup
	- [x] GitHub repo na KD
	- [x] Loading of Foundation Models
		- Using Terratorch for weights
		- Combination of Terratorch as SMP
	- [ ] Finetuning of FM
		- AutoEncoder style for Image reconstruction
	- [ ] Student architecture
		- ResNet backbone
		- AE ? VaE ?
		- Adapters ?
	- [ ] Knowledge distillation pipeline
		- [ ] one teacher one student
		- [ ] hierarchical with two students (Bigger and smaller ResNet)
		- [ ] different loss functions
	- [ ] Experiments
		1. [ ] Input Bands
			- Full (13 Sentinel 2) / Sentinel 
			- RGB + NIR
			- RGB
		2. [ ] Memory requirements for storage 
			- 3-4 embeddings in time
		3. [ ] Domain adaptation
			- Honza uz robil research a implementoval nieco
			- Adapters??
		
---
## *Questions*


---
# Work Log

## Sigma - Change Detection

2025-05-15
-  Loading of Foundation Models
	- Using Terratorch for weights
	- Combination of Terratorch as SMP

2025-05-05
- GitHub repo na KD
	- https://github.com/zaitra/sigma-knowledge-distillation


