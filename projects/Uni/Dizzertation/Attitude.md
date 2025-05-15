## Classification of Low Earth Orbit (LEO) Resident Space Objects' (RSO) Light Curves Using a Support Vector Machine (SVM) and Long Short-Term Memory (LSTM)
([[https://www.mdpi.com/1424-8220/23/14/6539|link]]/[[projects/Uni/Dizzertation/bibliography#Classification of Low Earth Orbit (LEO) Resident Space Objects' (RSO) Light Curves Using a Support Vector Machine (SVM) and Long Short-Term Memory (LSTM)|citation]])

- Preprocessing:
	- Set sampling frequency signal length, low pass filter threshold
	- Wavelet scattering trnsformation (WST) -> itterative convolution with wavelet transformation and low-pass filtering
	- Padd or truncate the data to choosen length 
	- Add mean WST features to the input -> 2D set of features from 3D array
- Class prediction into Three classes (shown in the figure)

- Better class separation (Fig. t-SNE reduction)
	![[WST.png]]
 