---
height: "540"
theme: white
css:
  - css/layout.css
  - css/custom_layout.css
---
<!-- slide template="[[mol-slide2]]" -->

::: title
Attittude
:::

<grid drag="50 100" drop="0 1" align="left" >
![[Pasted image 20240528110109.png]]
</grid>
<grid drag="50 100" drop="50 1" align="left" >
**Known**
- Phase angle (Sun - object - observer)
**Unknown**
- Incident angle (Rotation axis - line of sight)
</grid>

---

<!-- slide template="[[mol-slide2]]" -->

::: title
Project of dissertation
:::

We will investigate what is the smallest amount of additional information about
an object, except for its light curve, needed for models to perform well. Additional
information is objects’ model information, phase angle and shape...

![[Pasted image 20240528112404.png]]


---
<!-- slide template="[[mol-slide2]]" -->

::: title
Classification approach
:::

![[Pasted image 20240528112720.png]] <!-- element  style="margin:auto"-->

---
![[Pasted image 20240528112837.png]]

---
<!-- slide template="[[mol-slide2]]" -->

::: title
Regression approach
:::

![[Pasted image 20240528112201.png]] <!-- element  style="margin:auto"-->

---
<!-- slide template="[[mol-slide2]]" -->
::: title
Artificial data
:::

<split even gap="3" style="margin:auto">

![[Pasted image 20240528112941.png|300]]
![[Pasted image 20240528112957.png|300]]
</split>

::: block <!-- element style="font-size:0.6em"-->
**Attitude inversion of space debris based on the laboratory-tested photometry dataset**
:::

---

<!-- slide template="[[mol-slide2]]" -->
::: title
Artificial data
:::

- Chinese laboratory dataset - CZ-4B
- Our generator (Blender / NVISII)
	- 3D objects
	- no colors
	- no specular reflections
- ESA (YOTA)
	- 3D objects
	- highly accurate

---

<!-- slide template="[[mol-slide2]]" -->
::: title
Artificial data
:::

<split even gap="3" style="margin:auto">

![[Pasted image 20240528112941.png|300]]
![[Pasted image 20240528112957.png|300]]
</split>

::: block <!-- element style="font-size:0.6em"-->
**Attitude inversion of space debris based on the laboratory-tested photometry dataset**
:::

---

<grid drag="100 100" drop="0 0" align="left" >

> [!faq] What to do
> Validate synthetic light curve generator on Chinese dataset 
> Task ? 
> - Preferred way is direct prediction / classification without a need for generating synthetic LCs
> Model ?
> Data
> - YOTA
> - Chinese dataset
> - One real object with laser measurements for validation

</grid>

---

---

> [!Vedecky ciel]
> Vytvorit model na CZ-4C
> 	- natrenovat na YOTE
> 	- validovat na cinskom datasete
> Potom vytvorit model pre CZ-3 a validova na skutocnom resp inom datasete 

- nieco ako pomocna aplikacia pre astronomov (zapojit cloveka / experta)
- analyza vplyvu material / geometria na LC  ??

> [!faq] Architektura modelu
> - Mozno genrativny model na generovanie kriviek??
> 	- generovanie novych cilindrov ktore nevidelo?? (rozne pomery stran)
> 	- vyuzitie YOTA na generovanie trenovacic dat
> - RL na odhad skrytych parametrov

---


> [!todo]
> - [ ]  Skontrolovat krivky MMT lebo skakali nejake pri vizualizacii 
> - [ ]  Dohodnut si konzultaciu ohladom architekturi   

---

- 3 charakteristicke rotacie ( podla 3 osi ) a pozriet sa na fourierku


---

Viktor konzultacia

1. Ako funguju vypocty ?
	- Iba pre valcovity objekt
		- Zalozena na amplitude 
		- Vyziva aj synteticke data - zistuje ktore rotacie maju rovnaku amplitudu
		- Co najvacsi rozdiel medzi fazovymi uhlami jednotlivych pozorovani
	- Pre jednu konkretnu raketu H2-A
		- Rozdiel medzi peakmi - ak ho vidis tak je raketa specificky natocena
			- Spekularny odraz nevznika vzdy
		- Pre specificku geometriu
		- Potreba viacerych pozorovani
	- Metoda pre box-wing satelity
		- Tiez na spekularnych odrazoch
		- Potreba viacerych pozorovani

3. Optimalizacia
	- Optimalizacia vypoctov systemu rovnic
		- Jednoduche - nie je moc miesta pre optimalizaciu
	- Odhad vyslednych parametrov z ciastkovych merani
	- Algoritmicka optimalizacia
	- Statisticky aka velka je asi amplituda - z historie dat
	
3. Generovanie random dat na natrenovanie z ich rovnic 

4. Rozbor syntetickych kriviek
	- co ma aky vplyv na vysledok (tvar/material/attitude .....)
	- zistit nejake zmeny pri materialy .....

Simulatori
- Potrebuje 3D model objektu
- Yota - aj pre kratne casove useky
- "Dspose" - pre dlhe casove useky

---

# Stretnutie 29.7.

- efektivne spracovanie attitude
- hladanie spekularov 
	- hlavne stredy peakov
	- odstranenie ich a analyza difuzneho signalu

- Charakterizacia
	- analyza pripadov kde sa nsjcastejsie myli




#### Machine Learning-Based Identification of Contaminated Images in Light Curves Data Preprocessing


- CNN and SVM to indentigfy stellar and cloudy contamination to improve the quality of the data
	- tellar contamination - object is moving through a star
	- cloud contamination - object is ocluded by clouds
- Rorrectly detect / classify samples.
	- For stellar case - custom CNN - test accuracy 92%
	- Cloud case - SVM with test acc 97%

```
@article{Li_2024,
doi = {10.1088/1674-4527/ad339e},
url = {https://dx.doi.org/10.1088/1674-4527/ad339e},
year = {2024},
month = {apr},
publisher = {National Astromonical Observatories, CAS and IOP Publishing},
volume = {24},
number = {4},
pages = {045025},
author = {Hui Li and Rong-Wang Li and Peng Shu and Yu-Qiang Li},
title = {Machine Learning-based Identification of Contaminated Images in Light Curve Data Preprocessing},
journal = {Research in Astronomy and Astrophysics},
}
```

#### Identifying Cislunar Orbital Families via Machine Learning on Light Curves

- Machine learning to constrain potential Initial orbit determination search spaces to specifc cislunar families
- Synthetic data for training using the Digital Imaging and Remote Sensing Image Generation (DIRSIG™) engine. 
- 6 orbital families
-  87.5% test accuracy when combined with light curves captured from the space-based L1 point and from the face of the moon.

```bibtex
@article{badura2024identifying,
  title={Identifying Cislunar Orbital Families via Machine Learning on Light Curves},
  author={Badura, Gregory P and DeBlasio, Dan and Najera, Aryzbe and Chavez-Lopez, Ana C and Velez-Reyes, Miguel and Un, Nathan and Shimane, Yuri and Ho, Koki},
  journal={The Journal of the Astronautical Sciences},
  volume={71},
  number={3},
  pages={27},
  year={2024},
  publisher={Springer}
}
```

#### Attitude motion classification of resident space objects using light curve spectral analysis

- Splin: "Spin-stabilized" , rotating with a stable angular velocity, tumbling 
- The architecture exploits the Lomb-Scargle Periodogram and the Phase Dispersion Minimization algorithms to classify the object’s attitude motion as ‘‘Spin-stabilized”, ‘‘Tumbling” or ‘‘Uncertain”.
- 90 % accuracy


```
@article{ISOLETTA2024,
title = {Attitude motion classification of resident space objects using light curve spectral analysis},
journal = {Advances in Space Research},
year = {2024},
issn = {0273-1177},
doi = {https://doi.org/10.1016/j.asr.2024.10.034},
author = {G. Isoletta and R. Opromolla and G. Fasano},
keywords = {Space Situational Awareness, RSO characterization, Attitude motion classification, Light curve inversion},
}
```



#### Classification of Low Earth Orbit (LEO) Resident Space Objects’ (RSO) Light Curves Using a Support Vector Machine (SVM) and Long Short-Term Memory (LSTM)

- 

```
@article{qashoa2023classification,
  title={Classification of Low Earth Orbit (LEO) Resident Space Objects’(RSO) Light Curves Using a Support Vector Machine (SVM) and Long Short-Term Memory (LSTM)},
  author={Qashoa, Randa and Lee, Regina},
  journal={Sensors},
  volume={23},
  number={14},
  pages={6539},
  year={2023},
  publisher={MDPI}
}
```


### TOOLS

#### - [swagner-astro](https://github.com/swagner-astro)/
- [lightcurves](https://github.com/swagner-astro/lightcurves)

```
@article{wagner2021statistical,
  title={Statistical properties of flux variations in blazar light curves at GeV and TeV energies},
  author={Wagner, Sarah M and Burd, Paul R and Dorner, Daniela and Mannheim, Karl and Buson, Sara and Gokus, Andrea and Madejski, Greg and Scargle, Jeffrey D and Arbet-Engels, Axel and Baack, Dominik and others},
  journal={arXiv preprint arXiv:2110.14797},
  year={2021}
}
```


####  `light-curve` processing toolbox for Python

- Feature extraction library implemented in Python and Rust for optimal performance.
- Most of the classes implement various feature evaluators useful for light-curve based astrophysical source classification and characterisation.
- FIT
	- [VillarFit](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.VillarFit.html "struct light_curve_feature::features::VillarFit") Villar function fit
	- [BazinFit](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.BazinFit.html "struct light_curve_feature::features::BazinFit") Bazin function fit
	- [LinearFit](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.LinearFit.html "struct light_curve_feature::features::LinearFit") Slope, its error and reduced χ2χ2 of the light curve in the linear fit
	- [LinexpFit](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.LinexpFit.html "struct light_curve_feature::features::LinexpFit") Linexp function fit
	
- [Amplitude](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Amplitude.html "struct light_curve_feature::features::Amplitude") Half amplitude of magnitude
- [AndersonDarlingNormal](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.AndersonDarlingNormal.html "struct light_curve_feature::features::AndersonDarlingNormal") Unbiased Anderson–Darling normality test statistic
- [BeyondNStd](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.BeyondNStd.html "struct light_curve_feature::features::BeyondNStd") Fraction of observations beyond n,σmn,σm​ from the mean magnitude ⟨m⟩⟨m⟩
- [Bins](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Bins.html "struct light_curve_feature::features::Bins") Sampled time series meta-feature
- [Cusum](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Cusum.html "struct light_curve_feature::features::Cusum") Cusum — a range of cumulative sums
- [Duration](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Duration.html "struct light_curve_feature::features::Duration") Time-series duration
- [Eta](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Eta.html "struct light_curve_feature::features::Eta") Von Neummann ηη
- [EtaE](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.EtaE.html "struct light_curve_feature::features::EtaE") ηeηe — modification of [Eta](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Eta.html "struct light_curve_feature::features::Eta") for unevenly time series
- [ExcessVariance](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.ExcessVariance.html "struct light_curve_feature::features::ExcessVariance") Measure of the variability amplitude
- [InterPercentileRange](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.InterPercentileRange.html "struct light_curve_feature::features::InterPercentileRange") Inter-percentile range
- [Kurtosis](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Kurtosis.html "struct light_curve_feature::features::Kurtosis") Excess kurtosis of magnitude
- [LinearTrend](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.LinearTrend.html "struct light_curve_feature::features::LinearTrend") The slope, its error and noise level of the light curve in the linear fit
- [MagnitudePercentageRatio](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.MagnitudePercentageRatio.html "struct light_curve_feature::features::MagnitudePercentageRatio") Magnitude percentage ratio
 - [MaximumSlope](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.MaximumSlope.html "struct light_curve_feature::features::MaximumSlope") Maximum slope between two sub-sequential observations
- [MaximumTimeInterval](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.MaximumTimeInterval.html "struct light_curve_feature::features::MaximumTimeInterval") Maximum time interval between consequent observations
- [Mean](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Mean.html "struct light_curve_feature::features::Mean") Mean magnitude
- [MeanVariance](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.MeanVariance.html "struct light_curve_feature::features::MeanVariance") Standard deviation to mean ratio
- [Median](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Median.html "struct light_curve_feature::features::Median") Median magnitude
- [MedianAbsoluteDeviation](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.MedianAbsoluteDeviation.html "struct light_curve_feature::features::MedianAbsoluteDeviation") Median of the absolute value of the difference between magnitude and its median
- [MedianBufferRangePercentage](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.MedianBufferRangePercentage.html "struct light_curve_feature::features::MedianBufferRangePercentage") Fraction of observations inside Median(m)±q×(max⁡(m)−min⁡(m))/2Median(m)±q×(max(m)−min(m))/2 interval
- [MinimumTimeInterval](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.MinimumTimeInterval.html "struct light_curve_feature::features::MinimumTimeInterval") Minimum time interval between consequent observations
- [ObservationCount](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.ObservationCount.html "struct light_curve_feature::features::ObservationCount") Number of observations
- [OtsuSplit](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.OtsuSplit.html "struct light_curve_feature::features::OtsuSplit") Otsu threshholding algorithm
- [PercentAmplitude](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.PercentAmplitude.html "struct light_curve_feature::features::PercentAmplitude") Maximum deviation of magnitude from its median
- [PercentDifferenceMagnitudePercentile](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.PercentDifferenceMagnitudePercentile.html "struct light_curve_feature::features::PercentDifferenceMagnitudePercentile") Ratio of ppth inter-percentile range to the median
- [Periodogram](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Periodogram.html "struct light_curve_feature::features::Periodogram") Peaks of Lomb–Scargle periodogram and periodogram as a meta-feature
- [ReducedChi2](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.ReducedChi2.html "struct light_curve_feature::features::ReducedChi2") Reduced χ2χ2 of magnitude measurements
- [Roms](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Roms.html "struct light_curve_feature::features::Roms") Robust median statistic
- [Skew](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Skew.html "struct light_curve_feature::features::Skew") Skewness of magnitude G1G1​
- [StandardDeviation](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.StandardDeviation.html "struct light_curve_feature::features::StandardDeviation") Standard deviation of magnitude σmσm​
- [StetsonK](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.StetsonK.html "struct light_curve_feature::features::StetsonK") Stetson KK coefficient described light curve shape
- [TimeMean](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.TimeMean.html "struct light_curve_feature::features::TimeMean") Mean time
- [TimeStandardDeviation](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.TimeStandardDeviation.html "struct light_curve_feature::features::TimeStandardDeviation") Standard deviation of time moments
- [Transformed](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.Transformed.html "struct light_curve_feature::features::Transformed") Feature extractor transforming output of other feature extractors
- [WeightedMean](https://docs.rs/light-curve-feature/latest/light_curve_feature/features/struct.WeightedMean.html "struct light_curve_feature::features::WeightedMean") Weighted mean magnitude



```
@ARTICLE{2021MNRAS.502.5147M,
       author = {{Malanchev}, K.~L. and {Pruzhinskaya}, M.~V. and {Korolev}, V.~S. and {Aleo}, P.~D. and {Kornilov}, M.~V. and {Ishida}, E.~E.~O. and {Krushinsky}, V.~V. and {Mondon}, F. and {Sreejith}, S. and {Volnova}, A.~A. and {Belinski}, A.~A. and {Dodin}, A.~V. and {Tatarnikov}, A.~M. and {Zheltoukhov}, S.~G. and {(The SNAD Team)}},
        title = "{Anomaly detection in the Zwicky Transient Facility DR3}",
      journal = {\mnras},
     keywords = {methods: data analysis, astronomical data bases: miscellaneous, stars: variables: general, Astrophysics - Instrumentation and Methods for Astrophysics, Astrophysics - Solar and Stellar Astrophysics},
         year = 2021,
        month = apr,
       volume = {502},
       number = {4},
        pages = {5147-5175},
          doi = {10.1093/mnras/stab316},
archivePrefix = {arXiv},
       eprint = {2012.01419},
 primaryClass = {astro-ph.IM},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021MNRAS.502.5147M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```


#### Atrobase

-Astrobase is a Python package for analyzing light curves and finding variable stars. It includes implementations of several period-finding algorithms, batch work drivers for working on large collections of light curves, and a web-app useful for reviewing and classifying light curves by stellar variability type. This package was spun out of a bunch of Python modules I wrote and maintain for my work with the [HAT Exoplanet Surveys](https://hatsurveys.org/). It’s applicable to many other astronomical time-series observations, and includes support for the light curves produced by Kepler and TESS in particular.

Most functions in this package that deal with light curves (e.g. in the modules [`astrobase.lcfit`](https://astrobase.readthedocs.io/en/latest/astrobase.lcfit.html#module-astrobase.lcfit "astrobase.lcfit"), [`astrobase.lcmath`](https://astrobase.readthedocs.io/en/latest/astrobase.lcmath.html#module-astrobase.lcmath "astrobase.lcmath"), [`astrobase.periodbase`](https://astrobase.readthedocs.io/en/latest/astrobase.periodbase.html#module-astrobase.periodbase "astrobase.periodbase"), [`astrobase.plotbase`](https://astrobase.readthedocs.io/en/latest/astrobase.plotbase.html#module-astrobase.plotbase "astrobase.plotbase"), [`astrobase.checkplot`](https://astrobase.readthedocs.io/en/latest/astrobase.checkplot.html#module-astrobase.checkplot "astrobase.checkplot")) usually require three Numpy ndarrays as input: times, mags, and errs, so they should work with any time-series data that can be represented in this form. If you have flux time series measurements, most functions also take a magsarefluxes keyword argument that makes them handle flux light curves correctly

- lcfit
	- it an arbitrary order Fourier series to a magnitude/flux time series.
	- fit a univariate cubic spline to a magnitude/flux time series with a specified spline knot fraction
	- savgol_fit (Savitzky=Golay smmmothing filter)
	- fit a Legendre function of the specified order to the magnitude/flux time series.
	- Double inverted gaussian exlipsing binary model
	- and more....
	
- lcmath
	- Contains various useful tools for calculating various things related to lightcurves (like phasing, sigma-clipping, finding and filling gaps, etc.)
- lcmodels 
	- This contains various light curve models for variable stars. Useful for first order fits to distinguish between variable types, and for generating these variables’ light curves for a recovery simulation.
- varbase
	- Contains functions to deal with light curve variability, fitting functions, masking signals, autocorrelation, etc.

- plotbase 
	- for plotting
	
- lcproc
	- batch processing 
```
@misc{wbhatti_astrobase,
      author       = {Waqas Bhatti and
                      Luke G. Bouma and
                      Joshua Wallace},
      title        = {\texttt{Astrobase}},
      month        = feb,
      year         = 2018,
      version      = {0.3.8},
      publisher    = {Zenodo},
      doi          = {10.5281/zenodo.1185231},
      url          = {https://doi.org/10.5281/zenodo.1185231}
}
```