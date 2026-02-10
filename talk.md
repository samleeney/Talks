# Slide 1
Hi guys, I've discussed cNBRE's in some form with most of you here at different stages. My main goal today for the hour (or however long that takes) is to discuss prospective new ideas, but I thought it might be useful to briefly go over what cNBRE's are, what they may be useful for, etc first so have prepared a short 5 min talk to start with, which will hopefully stimulate discussion.

# Slide 2
So first, loosely what is a cNBRE? Lets start with evidence networks. Nial Jeffrey, Ben Wandelt showed that a properly optimised classiffier network trained to predict/distinguish between data simulated from two competing models can predict the Bayes factor of model a vs model B. So looking at the figure, ignore the orange box for now. 

Thomas and Will extended this result to be used for *forecasting* see Gessey Jones and Handley. IE, using evidence networks (or 'Neural Bayes Ratio Estimators') for * sensitivity forecasting*. So this allows us to ask questions like, given some physics parameters, what are our chances of detecting some signal?

Here, we extend this idea to *experimental optimisation*. We add an additional 'design parameter' as an input to our neural network, allowing us to forecast 'given some range of design parameters, how likely are we to detect some signal'. 

# Slide 3
So lets look at a very simple example for REACH, where the 'design variable' is observation time. We all know the answer here, but it is a nice demonstration of the method. We see that our probability of detection *marginalised over some prior range of possible signals, and nuisense parameters* gets better as we observe for longer, up to some noise floor.

# Slide 4
Whats nice about this is that by approaching a problem like this with cNBRE's rather than samplers, we learn an amortized representation of our parameter space. We train then network once, then we can slice the data down axis of interest. Here on the left we see the same design example (observation time) plotted against signal amplitude. We see, obviously, bigger signal and more time = higher chance of detection. Again, we are now marginalising over all other parameters in the reach simulator.

Looking at a slightly more complex example on the right, we look at *antenna orientation*. How does antenna orientation affect our chance of detecting the global 21cm signal? We see a 20% variance, over a single night.

# Slide 5 (not yet written)
A note on cost - GPU's are not cheap, but large physics experiments spend millions and in some cases billions for percentage point gains in sensitivity. When compared to the cost of physical sensors, lossless cables, new antennas, etc etc, this is an EXTREMELY cost effective way of improving instrument sensitivity. 

# Slide 6
So I have explained how these things work, now lets go over some potential future use cases. Mostly tuned to radio astronomy/REACH, but open to any suggestions.

# Slide 7
Another idea that came up in discussions with Jacob etc was using these for Null testing. Looking at the plot here we logK predicteed by our cNBRE vs Nested Sampling. Any X's or O's beyond here or here are **FALSE POSITIVES**. Notice that Nested Sampling creates more false positives than cNBRE's. 


