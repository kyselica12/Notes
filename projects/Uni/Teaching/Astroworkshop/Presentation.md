---
height: "540" 
theme: white
css: [css/layout.css,css/custom_layout.css]
---

<!-- slide template="[[title-slide]]" -->

::: title
Machine learning in astronomy
:::

::: event
Astroworkshop 2024
:::

::: author
Daniel Kyselica
:::

::: date
19.4.2024
:::

---

<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Why machine learning?
:::

<grid drag="50 100" drop="0 0">

- Fast
- No instructions needed
- No bias
- Able to find hidden connections
- Lot of available data

</grid>
<grid drag="50 80" drop="50 10">

![[robot.png]]
</grid>

::: footer
:::

---
<!-- slide template="[[basic-nosubtitle]]" -->
::: title
Demystifying machine learning
:::

<grid drag="100 100" drop="0 5" align="center" >
![[Pasted image 20240418201604.png]]
</grid>

::: footer
:::

--
<!-- slide  template="[[basic-slide]]" -->

::: title
Supervised learning
:::
::: subTitle
Demystifying machine learning
:::


<grid drag="40 100" drop="5 5">
- Good definition of a problem
- Labaled data
- Problems:
	- Classification
	- Segmentation
</grid>
<grid drag="60 100" drop="40 5" style="font-size:1.4em">
![[Pasted image 20240418202918.png]]
</grid>


::: footer

:::

--

<!-- slide template="[[basic-slide]]" -->

::: title
Segmentation
:::
::: subTitle
Supervised learning
:::

<grid drag="40 100" drop="0 10">
- Find all stars and galaxies
- Mask R-CNN neural network
</grid>

<grid drag="60 80" drop="40 10">
![[Pasted image 20240418193840.png]]
</grid>
::: footer
[1]: Colin J. Burke et. al. Deblending and Classifying Astronomical Sources with Mask R-CNN Deep Learning
:::

--

![[Pasted image 20240418193355.png]] 

--
<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Segmentation in python
:::
<grid drag="100 50" drop="0 30" style="font-size:1.4em">
```python
#-------------- Create model object in inference mode------------------------
print("loading mask R-CNN model")
model = modellib.MaskRCNN(mode="inference", config=config, model_dir=ROOT_DIR)
#-------------- Load weights trained on MS-COCO -------------------------------
model.load_weights(COCO_MODEL_PATH, by_name=True)

os.chdir('../')

sample_image = "11.jpg"
image = skimage.io.imread(os.path.join("../input/data-images/", sample_image))
results = model.detect([image], verbose=1)

# Visualize results
r = results[0]
print( class_names[r['class_ids'][0]])

visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], class_names, r['scores'])
```
</grid>
::: footer
:::

--
<!-- slide template="[[basic-slide]]" -->
::: title
Results
:::
::: subTitle
Segmentation
:::

<grid drag="50 100" drop="0 0" style="font-size:1.4em">
![[Pasted image 20240418195240.png]]
</grid>
<grid drag="50 100" drop="50 0" style="font-size:1.4em">
![[Pasted image 20240418195303.png]]
</grid>

::: footer
:::

--
<!-- slide template="[[basic-slide]]"  -->

::: title
Light curve classification
:::
::: subTitle
Supervised learning
:::

<grid drag="100 20" drop="0 5" align="center" pad="0px 20px">
**Atlas V Centaur** <!-- element style="font-size:0.8em" --> 
</grid>
<grid drag="50 80" drop="0 20" align="center" pad="0px 20px">
![[atlas_V_lc.png]]
</grid>

<grid drag="50 80" drop="50 20" align="center" pad="0px 20px">
![[Atlas_V_PHS_30_OBS_30.gif]]
</grid>

::: footer
https://www.sdlcd.space-debris.sk/
:::

--

<!-- slide template="[[basic-slide]]" -->

::: title
Results
:::
::: subTitle
Light curve classification
:::

<grid drag="80 100" drop="10 0" align="center"  pad="0px 20px">
|           | CZ-3 | falcon 9 | atlas V | H2-A | Globalstar | Avg. |
| --------- | ---- | -------- | ------- | ---- | ---------- | ---- |
| precision | 0.83 | 0.31     | 0.76    | 0.93 | 0.91       | 0.75 |
| recall    | 0.74 | 0.54     | 0.55    | 0.87 | 0.99       | 0.74 |
| f1        | 0.79 | 0.40     | 0.64    | 0.90 | 0.95       | 0.73 |

</grid>
::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->

::: title
Unsupervised learning
:::

::: subTitle
Demystifying machine learning
:::

<grid drag="50 100" drop="0 0">
- Big Data without labels
- Clustering
- Data mining
- Dimensionality reduction
- Forecasting
- Denoising
</grid>
<grid drag="50 100" drop="50 5" style="font-size:1.4em">
![[Pasted image 20240418203949.png]]
</grid>

::: footer
:::

--
<!-- slide template="[[basic-slide]]" -->

::: title
Dimensionality reduction
:::
::: subTitle
Unsupervised learning
:::

<grid drag="50 100" drop="0 10">
![[Pasted image 20240418204420.png|200]]
![[Pasted image 20240418204452.png|200]]
![[Pasted image 20240418204531.png|200]]
</grid>
<grid drag="50 100" drop="22 0" style="font-size:2em">
$$\rightarrow$$
</grid>
<grid drag="50 100" drop="50 5" style="font-size:1.4em">
![[Pasted image 20240418204302.png]]
</grid>



::: footer
:::

--
<!-- slide template="[[basic-slide]]" -->
::: title
Dimensionality reduction
:::
::: subTitle
Unsupervised learning
:::

::: footer
:::

<grid drag="100 50" drop="0 20" style="font-size:1.4em">
```python
XX = np.concatenate([X["cz_3"], X["atlas_V"], X["h2a"], X["globalstar"]], axis=0)

reduced_data = TSNE(n_components=2,
					learning_rate='auto', 
					init='random', 
					perplexity=5).fit_transform(XX)
for l in np.unique(labels):
    ok = labels == l
    plt.scatter(reduced_data[ok, 0],
	         reduced_data[ok, 1],
	         label=class_names[l])

plt.legend()
```
</grid>

--

<!-- slide template="[[basic-slide]]"  -->
::: title
SuperResolution
:::

::: subTitle
Unsupervised learning
:::

<grid drag="100 100" drop="0 5" style="font-size:1.4em">
![[Pasted image 20240418205825.png]]
</grid>
::: footer
S2DR3: Effective 12-Band 10x Single Image Super-Resolution for Sentinel-2
:::

--

<!-- slide template="[[basic-slide]]" -->
::: title
Space weather forecasting
:::

::: subTitle
Unsupervised learning
:::
<grid drag="50 100" drop="0 0" style="font-size:2em">
![[Pasted image 20240418211627.png|400]]
</grid>
<grid drag="50 100" drop="50 0" style="font-size:1.4em">
![[Pasted image 20240418211723.png|400]]
</grid>

::: footer
Vishal Upendran el. al. Solar Wind Prediction Using Deep Learning
:::

--
<!-- slide template="[[basic-slide]]" -->

::: title
LSTM
:::
::: subTitle
Solar weather forecasting
:::

<grid drag="100 100" drop="0 5">
![[Pasted image 20240418212117.png]]
</grid>

::: footer
Sepp Hochreiter and Jürgen Schmidhuber, Long Short-term Memory
:::

---

<!-- slide bg="[[Pasted image 20240419083915.png]]" data-background-opacity="0.5" -->

Thank you for your attention! <!-- element class="title" -->

---