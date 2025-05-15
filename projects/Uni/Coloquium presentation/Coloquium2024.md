---
height: "540" 
theme: white
css: [css/layout.css,css/custom_layout.css]
---

<!-- slide template="[[title-slide]]" -->

::: title
Processing of light curves of satellites and space debris for the purpose of their identification 
:::

::: event
PhD colloquium
:::

::: author
Daniel Kyselica <!-- element style="font-size: 1.4em" -->
:::

::: date
28.10.2024
:::

<grid drag="50 10" drop="3 80"  align="left" pad="0 0px" class="footer">
**Supervisor**: Roman Ďurikovič<br>
**Advisor**:      Jiří Šilha
</grid>

::: footer
:::

---

Space Debris <!-- element  class="title" style="font-size=3em;"-->

---

<!-- slide template="[[basic-slide]]" -->

::: title
ESA Space Environment Report 2024
:::

::: subTitle
Space Debris
:::

<grid drag="100 60" drop="0 25"  align="left" pad="0 0px" class="footer">
![[esa_numbers.png]]
</grid>
<grid drag="100 60" drop="4 74"  align="left" pad="0 0px" class="footer">
Number of tracked objects in Earth orbit over time
</grid>
<grid drag="100 80" drop="55 15"  align="left"  pad="0 0px" class="footer">
![[esa2.png]]
</grid>
<grid drag="100 60" drop="54 74"  align="left" pad="0 0px" class="footer">
Number of tracked objects in Earth orbit over time
</grid>

::: footer
:::

---

Reentry Event<!-- element  class="title" style="font-size=3em;"-->

---

<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Reentry event
:::

<grid drag="40 100" drop="0 1"  align="center" pad="0 0px">
1) Partial fragmentation
2) Main fragmentation - explosion
3) **Light flight**
4) Dark flight
5) Impact
</grid>
<grid drag="50 100" drop="45 1"  align="left" pad="0 0px" class="footer">
![[reentry.png]]
</grid>
<grid drag="50 100" drop="45 50"  align="center" pad="0 0px" class="footer">
Reentry event stages[^1]
</grid>

::: footer
[1]: Space safety 2023
:::

---
<!-- slide template="[[basic-slide]]" -->
::: title
Salsa Reentry
:::

::: subTitle
Reentry
:::
<grid drag="20 40" drop="0 20" align="left" >
![[projects/Uni/Coloquium presentation/images/astros_logo.png]]
</grid>
<grid drag="20 40" drop="0 50" align="left" >
![[projects/Uni/Coloquium presentation/images/FMFI_logo_black 1.png]]
</grid>
<grid drag="100 115" drop="0 0" align="right">
![[projects/Uni/Coloquium presentation/images/reentry3.png]]
</grid>

::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->
::: title
Salsa Reentry - Plane observation
:::

::: subTitle
Reentry
:::

::: footer
:::

<grid drag="100 110" drop="0 1"  align="center" pad="0 0px">
![[reentry2.png]] 
</grid>
<grid drag="100 110" drop="0 1"  align="center" pad="0 0px">
![[reentry2_2.PNG]]<!-- element class="fragment fade-in" -->
</grid>

---
<!-- slide template="[[basic-slide]]" -->

::: title
CZ-3B reentry on $25^{th}$ October 2020 
:::

::: subTitle
Reentry
:::

<grid drag="46 100" drop="2 1"  align="left" pad="0 0px">
![[reentry_hk.png]]
</grid>
<grid drag="50 10" drop="0 95"  align="center"  pad="0 0px" class="footer">
Composite Image from AMOS-HK [^1]
</grid>
<grid drag="46 100" drop="50 1"  align="left" pad="0 0px" class="footer">
![[reentry_mk.png]]
</grid>
<grid drag="50 10" drop="46 95"  align="center"  pad="0 0px" class="footer">
Composite Image from AMOS-MK [^1]
</grid>

::: footer
[1,2] : Šilha, Jiří, et al. "Analysis of re-entry event of CZ-3B R/B observed by all-sky meteor cameras AMOS." _2nd NEO and Debris Detection Conference_ 2023.
:::

---

<!-- slide template="[[basic-slide]]" -->

::: title
Towards image processing of reentry event[^1]
:::


::: subTitle
Reentry
:::

**Pipeline** <!-- element style="font-size:1.5em"-->
1. Preprocessing: denoising, background subtraction, thresholding;
2. Fragment segmentation;
3. Fragment tracking;
4. Fragment association by descriptors


::: footer <!-- element style="font-size:0.1em"-->
[1]: Kyselica, D., et al. "Towards image processing of reentry event." _JAMSI_ 19.1 (2023): 47-60.
:::

---
<!-- slide template="[[basic-slide]]" -->

::: title
Association
:::
::: subTitle
Image processing pipeline
:::
<grid drag="100 150" drop="0 20" align="top" >
![[projects/Uni/Coloquium presentation/images/pipeline1.png]]
</grid>
<grid drag="90 10" drop="5 10" align="center" class="">
Visualization of association between summary frames corresponding to frames 240-280 in original video recordings.
</grid>

::: footer
:::


---

<!-- slide template="[[basic-slide]]" -->

::: title
Results
:::
::: subTitle
Image processing pipeline
:::

<grid drag="50 100" drop="-53 0"  align="left" pad="0 0px">
![[result2.PNG]]
</grid>
<grid drag="50 100" drop="46 6"  align="left" pad="0 0px">
![[result1_1.png]]
</grid> 
<grid drag="50 10" drop="-53 -95"  align="top"  pad="0 0px" class="footer">
Human association[^1]
</grid>
<grid drag="50 10" drop="46 -95"  align="top" pad="0 0px" class="footer">
Automated association[^2]
</grid>

::: footer
[1] : Šilha, Jiří, et al. "Analysis of re-entry event of CZ-3B R/B observed by all-sky meteor cameras AMOS." _2nd NEO and Debris Detection Conference_ 2023.<br>
[2]: Kyselica, D., et al. "Towards image processing of reentry event." _JAMSI_ 19.1 (2023): 47-60.
:::

---

Light Curves<!-- element  class="title" style="font-size=3em;"-->

---
<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Light Curve
:::

<grid drag="50 100" drop="0 1"  align="left" pad="0 0px">
- Sequence of consecutive measurements 
- Result of objects shape, reflection properties, geometry, surface, rotation ...
- Observation conditions have high impact on quality
</grid>
<grid drag="50 100" drop="50 1"  align="left" pad="0 0px" class="footer">
![[lc1.png]]
</grid>
<grid drag="50 10" drop="50 98"  align="center" pad="0 0px" style="font-size:0.8em">
Objec, sun and observer scene ^1
</grid>


::: footer
[1]: Nussbaum, Max, et al. "Spectral light curve simulation for parameter estimation from space debris." _Aerospace_ 9.8 (2022): 403.
:::

---

<!-- slide template="[[basic-slide]]" -->

::: title
Example: Atlas V Centaur
:::

::: subTitle
Light Curves
:::

<grid drag="50 100" drop="0 1"  align="center" pad="0 0px">
![[scatter.png]]
</grid>
<grid drag="50 100" drop="50 1"  align="center" pad="0 0px" class="footer">
![[projects/Coloquium presentation/images/Atlas_V_PHS_30_OBS_30.gif]]
</grid>

::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->

::: title
Databases
:::
::: subTitle
Light Curves
:::
<grid drag="50 10" drop="2 0"  align="left" pad="0 0px">
**Mini Mega Tortora (MMT)**[^1]
</grid>
<grid drag="50 40" drop="2 10"  align="left" pad="0 0px">
- 15 560 objects;
- 2 923 objects with apparent period;
- 525 122 tracks.
</grid>
<grid drag="50 10" drop="2 43"  align="left" pad="0 0px">
**Catalogue SDLCD**
</grid>
<grid drag="50 40" drop="2 58"  align="left" pad="0 0px">
- Maintained by Astronomical and geophysical observatory in Modra;
- 759 objects;
- 1 925 tracks;
- Folded light curves.
</grid>
<grid drag="50 100" drop="50 1"  align="center" pad="0 0px">
![[projects/Uni/Coloquium presentation/images/mmt1.png|300]]
</grid>
<grid drag="50 10" drop="50 92"  align="center" pad="0 0px" class="footer">
Falcon 9 light curve[^1]
</grid>


::: footer
[1-2]: Karpov, S et al. (2016). “Massive photometry of low-altitude artificial satellites on
Mini-Mega-TORTORA”. _Revista Mexicana de Astronomia y Astrofisica_ 48,
pp. 112–113.
:::

---

<!-- slide template="[[basic-slide]]" -->

::: title
Shape classification from light curves
:::
::: subTitle
Light Curves
:::

<grid drag="33 100" drop="0 0" align="center" >
Box-wing
![[jason2.png|250]]
::: block<!-- element style="font-size:0.8em" -->
Jason-2 satellite[^1] 
:::
</grid>
<grid drag="33 100" drop="33 0" align="center" >
Rocket body
![[falcon9.png|250]]
::: block<!-- element style="font-size:0.8em" -->
Falcon 9 second stage 
:::
</grid>
<grid drag="33 100" drop="66 0" align="center" >
Asymmetrical
![[EOS.png|250]]
::: block<!-- element style="font-size:0.8em" -->
Earth Observing-1 satellite[^1]<!-- element style="font-size:0.8em" -->
:::
</grid>

::: footer
[1]: Re-entry of the Jules Verne (n.d.). https://nasa3d.arc.nasa.gov/models.
Accessed: 2023-12-06.
:::

---

<!-- slide template="[[basic-slide]]" -->

::: title
Allworth et al 2021[^1]
:::

::: subTitle
Shape classification from light curves
:::

<grid drag="96 10" drop="2 0" align="top" style="font-size:1.3em">
**A transfer learning approach to space debris classification using observational light curve data**
</grid>
<grid drag="50 10" drop="2 40" align="left" style="font-size:1.1em" >
**Model**
</grid>
<grid drag="50 100" drop="2 20" align="left" >
- 1D CNN network;
- Pretrained on synthetic data;
- Finetuning using real data.
</grid>

<grid drag="50 10" drop="50 40" align="left" style="font-size:1.1em" >
**Data**
</grid>
<grid drag="50 100" drop="50 20" align="left" >
- MMT database;
- At least 500 measurements per rotational period;
- Samples are rescaled to 1200 points
</grid>

::: footer
[1]:Allworth, James et al. (2021). “A transfer learning approach to space debris
classification using observational light curve data”. In: Acta Astronautica 181,
pp. 301–315.
:::

---

<!-- slide template="[[basic-slide]]" -->

::: title
Results
:::
::: subTitle
Allworth et al 2021
:::
<grid drag="90 90" drop="2 10" align="center" >
![[projects/Uni/Coloquium presentation/images/allworth_results.png]]
</grid>

::: footer
[1]:Allworth, James et al. (2021). “A transfer learning approach to space debris
classification using observational light curve data”. In: Acta Astronautica 181,
pp. 301–315.
:::

---
<!-- slide template="[[basic-slide]]" -->
::: title
Generalization on other databases
:::
::: subTitle
Shape classification from light curves
:::

- SDLCD database contains __folded light curves__
- MMT light curves can be divided into individual rotational periods with enough measurements $\rightarrow$ more training data
- Different preprocessing for better generalization

---
<!-- slide template="[[basic-slide]]" -->
::: title
Classification from individual periods
:::
::: subTitle
Generalization on other databases
:::

<grid drag="50 10" drop="2 10" align="left" style="font-size:1.1em" >
**Model**
</grid>
<grid drag="50 100" drop="2 10" align="left" >
- Two architectures
	- 1D CNN;
	- 1D ResNet-18;
- Trained only on real data;
- Weighted loss function. 
</grid>

<grid drag="50 10" drop="50 10" align="left" style="font-size:1.1em" >
**Data**
</grid>
<grid drag="50 100" drop="50 10" align="left" >
- MMT database - light curves split into **individual rotational periods**;
- Rocket Bodies:
	- Falcon 9, Atlas V, CZ-3B, H-2A;
- Heavily unbalanced dataset.
</grid>

::: footer
[1]: Kyselica, Daniel, et al. "Astronomical Objects Classification by Convolutional Neural Network Algorithms Layers." _2022 New Trends in Signal Processing (NTSP)_. IEEE, 2022.
:::

---

<!-- slide template="[[basic-slide]]" -->
::: subTitle
Classification from individual periods
%% Generalization on SDLCD database %%
:::
::: title
Results
:::

<grid drag="45 100" drop="0 -10" align="left" >
- Similar performance to the state of the art;
- Used to identify Lunar impactor WE0913A[^2];
- Partial results presented  [^1];
- Bad generalization to other datasets;
</grid>

<grid drag="50 100" drop="47 -10" align="left" >
| Object | F1  score | Precision | Recall |
| :--: | :---: | :---: | :---: | 
| CZ-3B | 0.880 | 0.895 | 0.865 |
| Atlas V | 0.761 | 0.702 | 0.830 |
| Falcon 9 | 0.670 | 0.641 | 0.702 |
| H-2A | 0.814 | 0.881 | 0.756 |
</grid>

<grid drag="94 10" drop="2 90" align="left" class="footer">
[1]:Šilha, J., et al. "Space Debris Rotation Properties and Characterization Using Rotation Phase Curves Extracted from Public Photometric Catalogues." _LPI Contributions_ 2852 (2023): 6028.<br>
[2]: Kyselica, Daniel, et al. "Astronomical Objects Classification by Convolutional Neural Network Algorithms Layers." _2022 New Trends in Signal Processing (NTSP)_. IEEE, 2022.
</grid>


::: footer
:::

---

<!-- slide template="[[basic-slide]]" -->
::: subTitle
 Generalization on SDLCD database 
:::
::: title
Preprocessing for enhanced generalization  
:::

__Preprocessing method__:
1. __Method 1__: Fourier series coefficients, order 8;
2. __Method 2__: Reconstructed light curve using Fourier series, order 8;
3. __Method 3__: Wavelet transform.

__Models__:
-  __Method 1__:  Gradient boosted decision tree;
-  __Method 2__: 1D ResNet20;
-  __Method 3__: 1D ResNet20.


::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->
::: subTitle
Preprocessing for enhanced generalization  
:::
::: title
Fourier series
:::

<grid drag="50 100" drop="2 10" align="topleft"  >
![[Fourier_series_square_wave_circles_animation.gif]]
</grid>

<grid drag="60 100" drop="35 0" align="center" >
$ f(t) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty}( a_n \cos(k t) + b_n \sin(k t) )$

$$f(t) \approx \frac{1}{2}a_0 + \sum_{n=1}^{N}( a_n \cos(2\pi \frac{n}{P} t) + b_n \sin(2\pi \frac{n}{P} t) )$$
</grid>


::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->
::: subTitle
Preprocessing for enhanced generalization  
:::
::: title
Wavelet transform
:::

<grid drag="100 20" drop="2 10" align="center" >
$$X_{\psi}(a, b) = \frac{1}{|a|^{1/2}} \sum_{t=0}^{T} x(t) \psi(\frac{m-b}{a})$$
</grid>

<grid drag="100 70" drop="2 33" align="center" >
![[Continuous_wavelet_transform.gif]]
</grid>



::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->
::: subTitle
Preprocessing for enhanced generalization  
:::
::: title
Results
:::

<grid drag="100 100" drop="2 3" align="center" >
![[preprocessing_results.png]]
</grid>


::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->
::: title
Problems
:::
::: subTitle
Shape classification from light curves
:::


<grid drag="50 100" drop="2 10" align="topleft"  >
**Preprocessing**:
- Rescaling;
- Padding / trimming;
- Normalization - standard, by amplitude ...
**Filtration**:
- Number of measurements;
- Coverage of the rotation period;
</grid>

<grid drag="50 100" drop="50 10" align="topleft"   >
**Train - test split by**:
- rotational periods;
- tracks;
- objects;
**Evaluation**:
- accuracy;
- F1 score.
</grid>
::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->
::: title
RoBo6 *
:::
::: subTitle
Light Curve
:::

<grid drag="100 10" drop="0 2" align="center" class="heading-color">
**Standardized MMT Light Curve Dataset for
Rocket Body Classification**
</grid>

<grid drag="50 10" drop="2 10" align="topleft"  >
**Preprocessing**:
- Resampled with frequency 10Hz;
- Split by gaps / size to 10 000 points;
- Zero padding;
- Normalization using mean, std;
**Filtration**:
- At least 100 measurements;
- 75\% coverage of folded LC;
</grid>

<grid drag="50 100" drop="52 10" align="topleft"   >
**Train - test split by**:
- tracks;
**Evaluation**:
- F1 score;
**6 Classes of rocket bodies**:
- CZ-3B, Atlas V, Falcon 9, H-2A, Ariane 5, Delta 4;
</grid>

::: footer
\* Accepted for publication at 
Machine Learning and the Physical Sciences Workshop @ NeurIPS 2024
:::

---
<!-- slide template="[[basic-slide]]" -->
::: title
Benchmark results
:::
::: subTitle
RoBo6
:::

<grid drag="90 50" drop="5 10" align="center"  >
![[Pasted image 20241023135234.png]]
</grid>

<grid drag="95 10" drop="2 85" class="footer">
[5]: Allworth, James, et al. "A transfer learning approach to space debris classification using observational light curve data." 2021<br>
[6]:Furfaro, Roberto, et al. "Space objects classification via light-curve measurements: deep convolutional neural networks and model-based transfer learning." 2018 <br>
[7]: He, Kaiming, et al. "Deep residual learning for image recognition." 2016<br>
[12]: Pan, Jia-Shu, et al. "Astroconformer: The prospects of analysing stellar light curves with transformer-based deep learning models." 2024<br>
[17]: Yao, L. U., et al. "The basic shape classification of space debris with light curves." 2021

</grid>

::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->
::: title
LC toolkit
:::
::: subTitle
Light Curves
:::

Easy to use tool for light curve preprocessing and dataset creation, for ML and research community.

- Preprocessing functionality
- Standard filtrations
- Computation of statistics (Fourier Series, Amplitude...)
- Compatible with  _huggingface datasets_
- MMT database snapshot

::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->
::: title
Example
:::
::: subTitle
LC toolkit
:::
<grid drag="100 100" drop="0 10" align="center" >
```python
preprocessing = Compose(
    SplitByGaps(max_length=dist),
    SplitBySize(max_length=dist, uniform=True),
    FilterFolded(k=100, threshold=0.75),
    FilterMinLength(100)
)

db = DatasetBuilder(
        classes=RB_CLASSES,
        regexes=None,
        directory="./MMT",
        preprocessing=preprocessing,
        mean_std=True,
        split_ratio=0.8,
        lazy=True
)
train_set, test_set = db.build_dataset(["time", "mag"])
train_set.to_dict()
>>> train_set{
	"data": {
		"time":..., "mag":..., "period":..., "amplitude":..., "start_idx":..., "end_idx":..., 
	},
	"mean": {"time": ..., "mag":...},
	"std": {"time":..., "mag":...}
}
```
</grid>

::: footer

:::

---
<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Conclusion
:::

- Developed image processing pipeline for reentry events
- Model for object characterization by its light curves
- Dataset and Benchmark using MMT database for Rocket Body classification
- Development of LC toolkit

::: footer
:::

---

Thank you for your attention! <!-- element class="title" -->

