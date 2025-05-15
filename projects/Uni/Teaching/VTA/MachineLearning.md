---
height: "540" 
theme: white
css: [css/layout.css,css/custom_layout.css]
---

<!-- slide template="[[title-slide]]" -->

::: title
Introduction to Machine learning
:::

::: event
VTA
:::

::: author
Daniel Kyselica
:::

::: date
6.5.2024
:::

::: footer

:::

---

![[0_bCJPtB21nMDve83N.png]]

---

<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Tasks
:::

<grid drag="30 100" drop="33 0" align="center" pad="0px 20px">
**Classification**
![[classification.png]]
</grid>
<grid drag="30 100" drop="0 0" align="center" pad="0px 20px">
**Regression**
![[regression2.png]]
</grid>
<grid drag="30 100" drop="66 0" align="center" pad="0px 20px">
**Clustering**
![[Drawing 2024-05-03 09.51.24.excalidraw]]
</grid>

::: footer
:::

---

<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Regression
:::

<grid drag="50 100" drop="0 0" align="left" pad="20px 0px">
- Supervised learning
- Learn relationship between variables
- Prediction of continous outcomes
	- stellar mass
	- luminosity
- Data : $[(x_1,y_1),(x_2,y_2)\dots (x_n,y_n)]$ 
	- $x_i$ input variables
	- $y_i$  target variable
</grid>

<grid drag="45 100" drop="55 0" align="left" pad="20px 0px">
**Linear Regression**
$$ y = a_0 + a_1 x_1 + a_2 x_2 + \dots + a_n x_n $$


**Polynomial Regression**
$$ y = a_0 + a_1 x_1 + b_2 x^2_{1} + \dots $$

```python
from sklearn.linear_model import LinearRegression
```
</grid>

::: footer

:::

---


<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Classification
:::

<grid drag="50 100" drop="0 0" align="left" pad="20px 0px">
- Supervised learning
- Task: Classify data into predefined class
- Data : $[(x_1,y_1),(x_2,y_2)\dots (x_n,y_n)]$ 
	- $x_i$ input variables
	- $y_i$  target class
</grid>

<grid drag="45 100" drop="55 0" align="left" pad="20px 0px">
- Shape classification
- Galaxy classification
- ...
</grid>

::: footer

:::

---

<!-- slide template="[[basic-slide]]" -->

::: title
SVM - Support Vector Machines
:::

::: subTitle
Classification
:::

<grid drag="50 100" drop="0 0" align="left"  pad="20px 20px" style="">
- Finds the hyperplane that best separates classes in high-dimensional space.


</grid>

<grid drag="50 100" drop="50 0" align="center" pad="20px 20px" style="">
![[Pasted image 20240503104523.png]]
</grid>

::: footer
:::

---
<!-- slide template="[[basic-slide]]" -->

::: title
Decision trees and Random Forests
:::

::: subTitle
Classification
:::

<grid drag="50 100" drop="0 0" align="left"  pad="20px 20px" style="">
- Decision tree partition the feature space into regions
- Random forests combine multiple trees

</grid>

<grid drag="47 100" drop="50 0" align="left" pad="20px 20px" style="">
![[Pasted image 20240503104918.png]]
</grid>


::: footer
:::

---

<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Clustering
:::

<grid drag="50 100" drop="0 0" align="topleft"  pad="20px 20px" >
**Definition**
- Unsupervised learning
- Group similar data together
- No knowledge about labels
- Data : $[x_1,x_2,\dots x_n]$ 
	- $x_i$ input variables
</grid>

<grid drag="47 100" drop="50 0" align="topleft" pad="20px 20px" >
**Purpose**
- Hidden structure
- Image compression
</grid>

::: footer
:::

---


<!-- slide template="[[basic-slide]]" -->

::: title
K-Means
:::
::: subTitle
Clustering
:::

<grid drag="50 100" drop="0 0" align="left"  pad="0px 20px" >
- Iteratively updates $k$ cluster centers 
- Assumes spherical clusters and equal variance
- Sensitive to the choice of $k$

</grid>

<grid drag="47 100" drop="50 0" align="topleft" pad="20px 20px" >
![[kmeans.gif]]
</grid>

::: footer
:::

---
<!-- slide template="[[basic-nosubtitle]]" -->

::: title
Dimensionality reduction
:::

<grid drag="50 100" drop="0 0" align="left"  pad="20px 20px" >
**Definition**
- reduce the number of input variable, while conserving some property of the data
	$$ X\in  \mathbb{R}^n \rightarrow Z \in \mathbb{m}, n > m $$
**Purpose**
- Simplifying data representation
- Improving model performance and interpretability.
</grid>
<grid drag="45 100" drop="55 0" align="center" pad="20px 20px" >
![[Pasted image 20240503112730.png]]
</grid>


::: footer

:::

---

<!-- slide template="[[basic-slide]]" -->

::: title
PCA
:::
::: subTitle
Dimensionality reduction
:::

- Linear dimensionality reduction technique.
- Identifies orthogonal axes (principal components) that capture the maximum variance in the data.
- Useful for reducing high-dimensional data to a lower-dimensional subspace.

- Transformation matrix $U$ is constructed from $p$ eigenvectors corrensponding to largest eigenvalues of covariance matrix $X^TX$

<grid drag="100 50" drop="0 80" align="center" pad="20px 20px" >
$Z = XU$
</grid>

::: footer

:::

---

<!-- slide template="[[basic-slide]]" -->

::: title
PCA - Eigen faces 
:::
::: subTitle
Dimensionality reduction
:::
<grid drag="50 100" drop="0 0" align="center" pad="20px 20px" >
![[Pasted image 20240503114932.png]]
</grid>
<grid drag="50 100" drop="50 0" align="center" pad="20px 20px" >
![[Pasted image 20240503114846.png]]
</grid>
<grid drag="50 100" drop="50 0" align="center" pad="20px 20px" frag="2" >
![[Pasted image 20240503115337.png]]
</grid>

::: footer

:::

---


Neural networks <!-- element class="title"-->

---
<!-- slide template="[[basic-slide]]" -->

::: title
Artificial Neuron
:::
::: subTitle
Neural networks
:::
<grid drag="100 100" drop="0 0" align="center" pad="20px 20px" >
![[Pasted image 20240503110843.png]]
</grid>

::: footer
:::

---
<!-- slide template="[[basic-nosubtitle]]" -->
::: title
Neural network
:::
![[Pasted image 20240503112412.png]] 
::: footer
[Playground](https://playground.tensorflow.org/) ; [Colab1 - Neural networks](https://colab.research.google.com/drive/135jh55nDXdrj4BpcVhbW_MdJeieZSfSj?usp=classroom_web|Colab1)
;[Colab2 - SVM & RF](https://colab.research.google.com/drive/1QmftrmpAddk2nA62i_V4ch9aarHZeTyt?usp=classroom_web#scrollTo=2-D2kPITctdi)

:::


