# Logistic regression
* Naive Bayes is a generative model, and also a linear model.
  * It's linear in that it tries to approximate `z` (the log odds of a class)
  * Log odds = sum(Theta_i * x_i)
* Logistic regression is going to be a **discriminative model**.
  * It will model the P(c = 1 | X = x)
  * Will be linear because it will spit out that f(x) = z (the log odds)
* In logistic regression, we will assume that features are *not independent*.
* It is also a linear function of x, also spits out a z, but the difference is in the Theta_i's.
* We no longer assume Theta_i are the log odds of the class given the feature.
  * If f_i copies f_j, theta_i = log(P(c = 1 | f_i = 1) / P(c = 0 | f_i = 1)) AND that I've already accounted for the variables 1..i - 1
  * We'll set theta_j = 0 (because its signal is already captured by f_i)
  * How do you subtract out value of previous features?
  * Typically done via gradient descent

# Gradient Descent in Logistic Regression
* The step of a gradient descent is naive (it assumes independence)
* But then re-evaluating after each step, this allows it to break the assumption of independence over the long run.

# Newton's Method
* Start a point, look at derivative, use that to step somewhere else, and continue to use that until you hit the minimum.

# Logistic Regression Does Not Learn the Join Distribution
* I.e., if data is missing, there's no guarantee your model will be correct
  * E.g., if there are two correlated features and one of them is missing, you may lose 50% of the predictive value of that feature
  * Or if two features a correlated

# Loss Function
* In regression, we use a squared loss function (due to central limit theorem?)
* What's the error for classification?
  * Bad error functions:
    * Count of misclassifications
      * Problem: that's not differentiable
      * If the decision boundary is `z >= 0 => positive, z < = => negative`, then there's no incentive to make your z marginally better.
    * You might use that to evaluate how good your model is, but you can't train with that loss function.
    * Gradient descent makes you want to make your model as differentiable as possible.
  * What if we use as our loss function `(1 - 1 / (1 + e ^ -z)) ** 2`
    * This does not penalize too far positive or too far negative values, which is kind of perverse. Basically inverts the log odds.
    * This is better, but sort of meaningless
* Most principled loss function is:
  * The cross-entropy loss

# Cross-entropy loss, a.ka. logistic Loss
* Logistic loss is a "binary" version of cross-entropy loss
* Cross-entropy (CE)
  * Cross-entry cost function is: `(1 - y)log(P_theta(y = 0 | x)) + y(log(P_theta(y = 1 | x)))`

# Entropy
* H(x) = Sum_over_all_values_of_x(P(x = x_i) * log(P(x = x_i)))
* This is also the expectation of `-log(P(x = x_i))`
* I.e., the "best code length" for x
  * See Huffman coding

# Differentiate the cross-entropy loss
* x, y = 1: -log(log_prob(Y = 1 | X = x))
  * => -log(1 / (1 + e^-z))
  * => -(log(1) - log(1 + e^-z))
  * => log(1 + e^-z)
  * then take derivative
    * (1 / (1 + e^-z))(e^-z)(derivative of -z)
    * -z = sum(theta_i * x_i)
    * derivative of -z = vector(x)
    * (1 / (1 + e^-z))(e^-z)(-|x|)
    * **P(y = 0 | x) * -x(vector of weights)**
    * Soft explanation: the probability that we mispredict times the entire weights.
* Fundamentally, this function maximizes the likelihood of the dependent variables given the independent variables.
