# Title
Thanks for the introduction. Today I am going to be talking about data curation.

# The first pulsar: found by eye
We've had several talks this week on transient searching and anomaly  
algorithms. The first pulsar was detected by a human anomaly flagger, Jocelyn 
Bell in 1967.

We have come a long way since then, but humans are still at least partially 
involved in data curation and cleaning. This is becoming less and less practical 
as data rates grow to terrabytes and beyond to petabytes.

In this talk I will present a method initially designed for cleaning data, but 
that now can be used for fully automated data curation. No human in the loop. No 
hyperparameters to tune.

# Outline
Overview

# Method
Take a small step back. I am going to explain the underlying method we use here, 
which is have coined as 'Bayesian Anomaly Detection'. After I explain this, I 
will extend to 'automatic data curation'

# Why not just flag first and fit later?
Firsly lets look at what I see as some of the main problems with standard 
anomaly detection frameworks.

1. Anomaly detection and inference seperate. Data thrown away. Really we want 
   the model of the thing we understand to help us inform the model of the thing 
we dont (our anomaly flagger)
2. Humans in the loop prone to bias, even if just tuning hyperparameters.
3. Humans manually inspect edge cases.

# What if the data are contaminents
So im going to start with an oversimplified example. Straight line fitting! You 
can see we have some contaminents, which i want to 'model' alongside my straight 
line fit.

# What if the mast is part of the model
Im going to define some mask, which we will call epsilon, where zero is clean 
and 1 is anomaly.

# How do we find the right mask
Of course, we dont know the correct mask apriori. So, I am going to take a 
bayesian approach *marginalise over all possible masks* to get a probability 
that each point is contaminated.

However, of course, 2^N masks is intractible.

So instead of summing, we maximise at each step of our sampler. Lets look at 
this in a bit more detail.

# What does this look like in practice
We start running our numerical sample and it starts with some guess at the 
parameters that describe our line. They are of course not very accurate. 

For each point, we say 'is its likelihood above or below some threshold'. It 
gets assigned 1 if below 0 if above.

We repeat this throughout our striaght line fitting procedure.

# Weighted average over samples gives probabilities
In the end we weighted average over all the 1s and 0s masks, and get the 
PROBABILITY each point is contaminated. 

A key point to note here is that contaminated points DO NOT have their 
likelihood set to zero, they have it set to the penalta p/Delta. This is an 
OCCAM PENALTY. This is not something we add in manually, it pops out of the 
derivation and prevents the fitter from choosing the simplest model (everything 
flagged!
)

# A familiar activation function
Some of you may have noticed that the left hand side of the comparison we 
evaluate is a logit function. Again, this pops out naturally. A logit function 
is commonly used in machine learning.

# Hard vs soft mixture models
So this image on the top right here is what our likelihood effectively becomes. 
A mixture model where all flagged points are on the 'floor' and the likelihood 
remains above. 

You can effectively apply this method during neural network optimisation by 
adding the condition into the loss function. HOWEVER the corner you see between 
the flat floor and hte likelihood causes problems as it has no gradient.

So, instead of maximising as i described before we can logsumexp over epsilon, 
softening this boundary and allowing and optimiser to move across it. Very cool. 
Neural anomaly detection is a work in progress.

# What is actually being fitted
So the key point that I wanted to get across (this is all you need, if nothing 
lse made sense) is that you give me data and model, i give you probability each 
point is contaminated. Thats all you really need to know for the next stage.

Note that although the method may seem complex, it can be implemented with 2 
lines of code.

# Results on REACH
So lets actually try this method on some real data. Here you can see a year of 
reach data, fit jointly. We get a contamination score per frequency channel per 
observation. However, the plot on the bottom is the score per frequency channel 
marginalised over the year. So we firstly get a 'frequency channel score'.

The channels with panom close to one were excluded. No human needs to go back 
and remove them. They were excliuded automatically.

# What if we slice scores by month?
So now we view our data month by month. I can give you a 'per month' anomaly 
score. We see here that we were having some problems in August.

# What if we slice by day of the year
Similar to before, we now get a score per day. Each dot is the 'score per 
observation'.

# Does the model find instrument problems by itself
So now onto a little more interesting example. The x axis here is the predicted 
noise source temperate. The noise source is a noise diode inside our reciever 
chain that we use to calibrate the instrument. 

We see that where it drifts, the curation score gets markedly worse.

The anomaly flagger does not see TNS. It finds bad data, then after the fact we 
notice this correlates to the temperature of an internal component!

# Does the model recover weather without weather inputs?
We now plot daily rain vs panom. Again, our data curator does something that 
previously a human may have done manually. Removes days where it rained!

Our telescope now doubles as a weather station.

# Results on type Ia superonvae
We also apply our model to type Ia anomaly light curve fitting. We find 
something very interesting.

When observing Ia light curves, astronomers typically observe them with several 
differnet filters (looking in different wavelengths).

On some days, we know certain filters were broken.

Here, we see that our automatic data curator flagged the entire green filter as 
broken. The green filter was broken on that day. Previously this would have been 
done by hand.

# Does this scale to transient searches
We are now using this method to curate transient data. You see here a 
observation of a pulsar, and the anomaly flagger curates each pixel, in the 
marginalised plots we see that it correctly identifies channels with RFI.

c
