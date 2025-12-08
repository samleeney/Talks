# Title
- Going to be talking about a project I am just starting, rather than (as usual) something at the publication stage.
- Content may be unpolishesd, but hoping that presenting at this stage will lead to interesting comments, useful suggestions, etc!

# Key message
- Very broad idea here is as follows:
1) Typical transient search methods search on compressed data via multi step fit.
2) I want to a) do one single joint fit b) on uncompressed data c) in a bayesian way, allowing us to search based on priors set by physics parameters.

2) So I want to be able to say, for example, search for a pulse consistent with a cold plasma delay, by setting width prior based on scattering laws.

# FRBs
- Bright short bursts
- We still dont really know what they are
- Useful rulers when localised. If we localise enough, they can give a new way to measure H0
- They normally only come once. Once we miss them they are gone. We need more to really lock down H0.

# Pulsars
- Periodic, so give us cosmic clocks
- If we have an accurate cosmic clock, can measure stretch/compression of spacetime -> detect GW's
- Also useful for instrumentation checks, calibration, etc

# What do they look like when recieved by instrument?
- Typically in papers we see transients like in the previous images
- But when they arrive at our telescopes they look like this. They are *dispersed*.
- Also mixed with interference
- Typical detection pipelines compress this data before fitting. We want to operate in this space entirely.

# Standard search algorithms
- Now will give quick demo of how a standard transient search algorithm works.

# Raw observation
- Dispersed pulse with some RFI.
- RFI can be time constant, transient, repeating, etc.

# Step 1.
- Remove RFI via flagging
- Then compress down frequency domain onto S/N plot
- Apply some arb threshold in S/N and see if anything flagged
# Step 2:
- De disperse, check again in S/N plot
- Repeat many times for different DM's, hoping for flag.

# Over correction
- Going too far breaks things.
- Dispersion sweep needs to be precise
- Can also shmeer improperly flagged RFI into signal

# So we want a Bayesian alternative
- Where we:
- 1) select search parameters based on physical priors
- 2) Deal with anomalies and fit itself simultaneously, not throwing away any information
- 3) Avoid irreversible compression and operate directly on time freq cube
- Is fast on GPU

# Step 1 generative model
- Define some physics based model. Already exists. 
- Evaulate model on full cube, sample to obtain posteriors and evidence

# Step 1: simple vs RFI contaminated pulse
- Works fine for simple pulse, not for anomalies
- We need a principle way to handle anomalies

# Bayesian anomaly detection
- Conveniently, we have this...
- Have talked about this a lot in previous talks so will skim over. Ask me or check my slides if you want more info.

# Bernoulli mask
- Each pixel carries latent mask, epsilon one is anomaly epsilon 0 is not anomaly
- Put Bernoulli prior on this mask
- Yields full likelhood

# Marginalising over masks
- Can solve by marginalising over all possible masks, but not computationally tractible
- So we make assumption that 'true' mask is by far the most probable
- Therefore only need to compute the max likelihood.
- Key point here is that occum naturally comes out. This prevents sampler from finding 'simplest model' by flagging everything. 
- We fit the anomaly threshold as free parameter -> anomaly detection fully automated.

# Real data fits
- Here is a real dispersed pulsar. See the pulse, see the interference.
- We run our fit, searching across all possible DM's
- We fit for anomalies simultaneously
- Anomaly model gives is a PROBABILITY that each pixel is contaminated, rather than binary mask. 
- Correctly picks up most RFI.

# Real data fit (fit)
- See the recovered signal 
- Plotted from recovered signal parameters run through the forward model.

# Flagging detections
- So how does this fit into an automated pipeline?
- Bayes factor. Fit model with signal + anomaly, and then model with noise only
- Bayes factor above some number = detection.

# Problem.. too slow
- The problem is this is too slow. Takes minutes to evaluate Bayes factor per ms of data (at common resolutions).

# Goal: closed form Bayes factor
- So all taht we care about from the perspective of a search is the Bayes factor. We can do the inference later on regions with detection flags.
- So from the perspective of a search algorithm, all parameters are nuisance!
- So how do we move towards a closed form bayes factor?

# Signal model (from step 1)
- So this is our model from before
- We need to marginalise each of the following parameters

# t0
- Starting with t0
- t0 is the asymptote of our dispersed pulse
- We can solve for individual t0 at any time.
- So we can essentially condition on t0, and solve sequentially, or, of course in parallel on a GPU.
- So you can either think of this as 'brute force sampling' or some kind of parellised conditioning.

# amplitude A
- We select a gaussian prior on the amplitude A which is conjugate to the gaussian likelihood
- So the posterior over A and its marginalisation are closed form
- So no sampling required.

# Marginalising noise sigma^2
- Inverse gamma distribution on sigma
- Again leads to a closed form posterior and evidence

# Laplace for DM
- So we are now left with two parameters to model which I cannot think of a closed form solution for.
- I got to about here in this project a few months ago, then got stuck and left it, until workshop last week where the laplace approximation came up
- We can resolve the remaining two parameters via a laplace approximation
- Still needs a small optimisation step, but is quite small.
- So we now have a **almost** closed form model we can use to flag transients. 
- This takes GPU runtime on the example above from several minutes to miliseconds.


# Speed up from analytic evidence
- But we can go further. t0 is highly parellisable, so we can increase the width of our data cubes up to the GPU memory limit.
- What we care about here (for a fixed instrument resolution) is observation seconds per GPU second... odd metric.
- We are essentially saying 'how much faster than realtime can our tool search for transients'.
- On my at home GPU, we can push to almost 5x real time. At 5x real time we oom.
- Modern GPUs will take this higher
- At some point I think that memory bandwidth will break this trick.
- State of the art speed is about 10x real time.

