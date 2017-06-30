# Naive Bayes
* P(C | F1, F2, F3, F4...)
  * = P(C) * P(F1, F2, ... Fn | C) / P(F1 ... Fn)
  * = P(C) * P(Fi | C) / P(Fi)
  * P(C = 0 | Fi) / P(C = 1 | Fi)
    * = P(C = 0) / P(C = 1) * P(Fi = fi | C = 1) / P(Fi = fi | C = 1)
* Assumes conditional independence

# Generative model
* Naive Bayes can be used generatively.
* In a generative model, we capture the full joint distribution. I.e., we have uncovered the probability of P(C = c1, F1 = f1, Fn = fn).
* I.e., for any e-mail we can determine the probability of that e-mail.
* We are able to "factor" the joint distribution into each of its probabilistic components.
* By assuming conditional independence, the model is very easy to create.
* Any graphical model is dominated by the node with the most incoming edges (i.e., low in-degree).
* You cannot learn a model without sufficient data points.

# Joint distributions
* Any queries can be answered from the joint distribution.
* If you're missing features, you can still apply missing models thanks to the joint distribution / graphical models.
* Graphical models find a lot of use in the medical field (sometimes you have a test as a feature, sometimes you don't)

# Other Graphical Models
* Topic models or clustering models
* LDA (or mixture models)
* Hidden Markov Models
* Probabilistic graphical models to learn Markov Models, Bayes Nets, etc.

# Expert Models vs Expert Systems
* Domain specific knowledge that's being injected into a system which is not learned, but simply learned by a system.

# Smoothing
* Add one smoothing or additive smoothing
* n + 1 == pseudocount
* Fits into Bayesian inference

# Confidence region
* F(Dataset) => Region of parameter space
* 95% confidence region has the property that no matter the true theta, theta is in F(Dataset) with probability >= 95%

# Decision Theory
* How expert systems deal with updating via frequentist statistics
* Statistics by Casella and Berger
* Different expectations / cost functions associated with mispredicting true parameters

# Penalty methods
* Way to incorporate priors (Bayesian statistics)
  * The penalty function generally corresponds with our prior beliefs on the parameters
* P(theta) = prior probability, P(theta | data) = posterior probability
  * P(theta | data) = P(theta) * P(data | theta) / P(data)
  * P(data) is a normalizing constant, can be ignored for maximization purposes
* MAP (maximum a posteriori) — choosing the model that is most likely given the probability distribution times the probability of the data given that model.

# How to choose a prior probability
* Sometimes priors can be uniform—expressing total ignorance.
* Probability density function
  * Integrating under the curve of probability
    * For a continuous probability, any point probability will be 0
  * Integral of a density function — measures a relative likelihood

# Beta distribution  
* Used for defining prior probabilities for a Bernoulli variable (0 or 1)
* The pseudocounts feature in the beta function, great cameo
  * 5 stars
*
