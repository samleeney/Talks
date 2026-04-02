# Anomaly model: Bernoulli mask

The idea is simple: we don't know which pixels are RFI and which aren't, so we let the model figure it out. Every pixel gets a hidden label - is it clean data, or is it an anomaly?

Each pixel has a latent binary mask. Zero means 'this pixel is well-described by the signal-plus-noise model', one means 'this pixel is something else - RFI, an instrumental glitch, whatever'.

If a pixel is clean, it's evaluated under the signal model. If it's anomalous, it gets a flat likelihood over the broad scale - we're saying 'I don't care what this pixel is doing, it's not informing the signal fit'.

Now the obvious problem is that we've introduced a binary variable for every pixel - that's 2^N_pix possible mask configurations, which is completely intractable. But because pixels are independent, that enormous sum factorises into a product of per-pixel terms. You just get a log-sum-exp over two possibilities per pixel. It's exact, and it's cheap.

So what this gives you is a single likelihood that simultaneously fits your pulse parameters and figures out which pixels are RFI - no separate flagging step, no manual threshold, fully automatic. And the posterior on p tells you after the fact how much of your data was contaminated.

# Marginalising t0 (discrete time index)

We can't marginalise t0 analytically the way we can the other parameters - it enters the exponential nonlinearly. But we can do something almost as good: condition on it.

t0 is a discrete variable - it's just which time bin the pulse arrives in. So instead of integrating, we evaluate the evidence independently for every possible arrival bin, and then sum the results weighted by the prior on t0 - which is usually just uniform.

The key point here is that this is embarrassingly parallel. Each time bin is completely independent of the others, so this maps perfectly onto a GPU. You evaluate all arrival times simultaneously, and the sum at the end is trivial.

So after this step, the full evidence is just a weighted sum over t0 of all the per-bin evidences, where each per-bin evidence has already had A and sigma marginalised out analytically.

# Marginalising amplitude A

Now A, the amplitude, is the easy one. It sits outside the exponential as a linear scaling of the template. So if we write the model as A times some template shape psi, the likelihood is quadratic in A.

That means if we put a Gaussian prior on A, the integral is just a Gaussian times a Gaussian - which is another Gaussian. This is conjugacy. You get a closed-form posterior on A, and plugging it back in gives you a marginal likelihood that no longer depends on A at all.

The result depends only on the noise variance sigma squared and the track shape parameters DM and pulse width. One parameter gone, analytically, no approximation.

# Marginalising noise sigma^2

Same trick again. After integrating out A, we have a marginal likelihood that depends on sigma squared. If we put an inverse-gamma prior on sigma squared - which is the conjugate prior for the variance of a Gaussian - the integral is again closed form.

What you end up with is this expression involving the residual sum of squares S. It looks like a Student-t distribution - which makes sense, because that's exactly what you get when you marginalise out unknown variance from a Gaussian.

So now both A and sigma squared are gone. No sampler, no numerical integration, just algebra. What's left is the track shape - DM and pulse width - which we handle with the Laplace approximation on the next slide.
