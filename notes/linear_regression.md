# Linear Regression

# Model form
* y = Bx + a
* Sum of squared error (SSE) is not robust to outliers because it tends to over-respond to them.
* Absolute value is not differentiable.
* Norm = length of a vector

# Analytic solving vs gradient descent

# Hyperparameter
* Hyperparameters are parameters of your learning rather than your prediction

# Learning Rate
* There is no way without knowing the particular function what the ideal learning rate is. Has to be derived experimentally.
* But can be discovered for a particular function.
* The perfect step for a quadratic function is 2.
* (Take current derivative and divide by the 2nd derivative, provided that the 2nd derivative is constant.)

# Gradient calculation
* If you have 1M samples, then you can sample <i.e., 128> examples per gradient calculation.
  * This is a noisy but unbiased estimate of the gradient.
  * This is known as minibatch gradient descent.
  * Divide this learning rate by the batch size proportion.
  * (Normal is called batch gradient descent.)
  * Also known as stochastic gradient descent (SGD).
    * Can also mean just 1 example.

# Epochs
* Going through all of the data.
* Training the learning rate and changing the batch size effectively increase the resolution in later epochs (sensitivity to gradient).

# When to Batch vs Minibatch
* Different people use different amounts—you can use vector operations to parallelize 64+ gradient computations in parallel, which makes things much more efficient.
* Would be a waste to just give it one, which downweights the strength of stochastic gradient descent.
* If you have 500 examples, might as well just batch GD. But if you have significantly more, minibatch makes more sense. Also consider the amount of memory you're consuming.

# Stochastic gradient descent
* Because it learns on one example at a time, it is sometimes used for online learning.

# Overfitting
* Overfitting is enabled by capacity
  * Capacity: ~ # features
* Linear models are not very complex so it's harder to overfit them (though with enough features, it's quite possible)

# Bias-variance tradeoff
* Linear models have high bias
  * Very rigid assumption about the relationship between the variables. (I.e., the relationship is only linear and we'll only consider linear relationships.)
  * Low variance—i.e., lower likelihood to capture spurious relationships.
  * Variance allows to fit not just the true relationship, but also the noise of the model.

# Ways to minimize variance
* Regularization
  * Penalty methods — some penalty of model complexity. I.e., I'll let you be more complex if you're proportionally more accurate.
    * For linear regression, you can get an L2 penalty (take length of weights vector times a penalty factor)
    * This penalizes large coefficients (which would claim that a single factor has a large effect on the outcome)
* Model averaging ("bagging")
  * Take subsets of the training data and train the same structure model on different subsets of the training data, and have ten models on ten different subsets. Each will have some variance and fit some of the noise. But if you average the answers, you'll get lower variance.
* Dropout
  * A bagging technique for neural nets.
* "Same model"
  * The same model type with the same hyperparameters.

# Maximum A Posteriori
  * Choosing the model that is most likely given the probability distribution times the probability of the data given that model.
  * Different from the Maximum Likelihood Estimate (MLE).
  * This assumes that the most likely situation is that the variation is the data is noise.

# Validation Error
* Choose a training / validation split
* 80/20 for training/validation. Train on training data.

# L2 Penalty

# Feature Reach
* A feature may have predictive value, but is very uncommonly expressed in the population.
  * I.e., a slam-dunk feature if present, but usually not present.

# Overtraining
* Linear regression will easily overtrain since it only responds to immediate snapshots of the gradient. It does not consider how altering any coefficients will affect the overall prediction.
* It is very difficult for linear regression to not overtrain if it contains a lot of irrelevant variables.
* L2 regularization compels you to equally distribute the weights, rather than weight a single feature highly.

# L1 Regularization ("LASSO")
* Also known as LASSO — least actual shrinkage optimization something something.
* Take the sum of ABS(weights) as the penalty
* This increases model sparsity
  * Increases the interpretability of the model
  * If you train without L2 or L1 regularization, you will always have each feature receive some weight
  * It also selects out only relevant features, and finds the distracting features for you
* If you believe that all features are relevant to the problem, then you'd probably not want to do L1 regularization.
* Regularizations tend to cause the model to "fall short."

# Feature Selection
* There are a number of algorithms to select meaningful features, over and above linear regression with L1 Regularization.
* First eliminate features with extremely low reach.
* Then eliminate features where conditioning on the feature, it doesn't predict the class at all—then throw out the feature. Any pairwise effects will not get picked up by a linear regression anyway since it's a linear model.

# When to use L2 Regularization
* When there's multi-colinearity in the data
  * I.e., when relevant features are replicated or highly correlated.
  * In that case, you'd like the spread out the weight to the many variables that are involved.
* Learned features are encouraged to be general, or learned features are used in synthesis.
  * I.e., in complicated models, you can essentially learn a feature like "is_example1," in which case it would turn it into a 100% accurate classification based on the model.
  * I.e., it encourages generalization and not just memorizing the training set (by applying maximum weight to ungeneralizable features).
