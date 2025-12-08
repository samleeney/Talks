# Fast, Marginalised Bayesian Transient Searching
# what are transients
Image of FRB, image of Pulsar
Use @frb_example.png and @pulsar_example.jpg here. Probably one slide each.

# what do they actually look like
Image of FRB before de dispersion. Use @real_pulsar.png here

# How do standard search algorithms work
Several slides, first note rfi flagging on 3d plot, then effective GIF of dispersion (will need to simulate from python script), and flagging in compressed 2d SNR plot.

The idea for this slide is that you write a python script that plots a figure with a) on the top the dispersed puls and directly below its SNR plot, showing what happens when averaging in frequency. initially the simple pulse with noise in background is not visible, but as different dispersions are applied it grows in the SNR plot until it is 'flagged'. First example should also have rfi which we just remove manually. So I will say while talking 1) here is a simulated example of what an frb observation might look like 2) step 1 is to flag the rfi (show the plot with rfi gone) 3) Step two is to de disperse (i then scroll through teh several plots with the different dispersion levels until signal flag comes up).

# My idea
1. Data can be lost during compression, better to search on raw data
2. Better to combine anomaly flagging with 'fit' for thing that we are interested in, rather than independant
3. Enable searching based on physics based, prior ranges. IE, lets search for a pulsar dispersed by x.
4. Feels like it will benefit significantly from modern GPU accelleration

# Step 1 (this may be several slides)
- We need to build a model of the *dispersed* pulse on the freq x time x intensity plot. 
- We can do this with 
- Our model is:

\[
I_{ij}
=
\frac{A}{\sqrt{2\pi}\,\sigma_{\mathrm{frb}}'}
\exp\!\left(
  -\frac{\big[t_j - t_0' - K\,\mathrm{DM}'/f_i^2\big]^2}{2\,{\sigma_{\mathrm{frb}}'}^2}
\right)
+ \epsilon_{ij},
\]

- Can use this to formulate likelihood which we sample with nested sampling. Show the likelihood.

# Step one cont
- This will work to fit a pulse like this 
- write a python script here with a simple pulse simulated ontop of some noise. You can do this using the 'simulate' functionality from the dispersion searcher package in the root. You will need to install appropriate packages with uv. The image generated from this python script should be a slide.
- I will say, this works for a pulse like this... but...

# Step one cont
- On a new slide
- But, how do we deal with a more real signal, containing RFI
- Show real_pulsar.png here.

# Bayesian anomaly detection
Give a VERY brief overview of bayesian anomaly detection. You can use anomaly_detection_talk.tex for this. It should be 2 slides max. Then you need to show our new likelihood which includes anomaly detection.

# Run on real data 1
Show real_pulsar_fitted.png

# Run on real data 2
Show real_pulsar_flagged.png

# Flagging 'detections'
- We flag 'detections' by positive Bayes factor on signal model vs no signal model
- Show 1 or two lines of math here

# Problem... TOO SLOW
- Nice model, but too slow. How can we speed it up?
- Takes 3-5 minutes even when jaxified

# Run through analytic bayes factor derivation
- View @analytic_evidence.tex
- Over several slides run through this derivation.
- Start with our model (that we ahve seen before from step 1).
- Mention that all we actually care about is bayes factor, so in theory, we can marginalise everything out.
- Go through each fitted (primed) parameter one by one, showing how we we either a) marginalise it out or b) use conjugate priors or c) brute force (the time index one).

# Speed increase
Show image obs_time_per_gpu_second.png here

# End on QR code

