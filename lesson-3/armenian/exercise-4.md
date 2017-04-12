## Առաջադրանք 4: Tuning and Evaluation

**Note: Don't forget about feed_dict in the steps below. The network doesn't have any built-in data, so you need to feed in data every time you try to fetch a result that depends on the input.**

### Քայլ 1:
Compare the normalized output (**actual**) to the output that our neural network now computes based on the learned weights. Are the results close?

### Քայլ 2:
It may be hard to visually compare all the 10 values and have a good feel for how well we did. Thankfully, we already defined a loss function. So we can just fetch that value. What's the loss?

### Քայլ 3:
Let's tune some parameters to see if we can improve the results. Here's a list of the parameters that you can change to see the effects:
* Number of neurons in the hidden layer.
* How you initialize the weights - i.e., tf.zeros, tf.random_normal, or values from some other distribution.
* The learning rate for our stochastic gradient descent algorithm.
* You can even swap out GradientDescentOptimizer for another optimizer ([documentation](https://www.tensorflow.org/api_guides/python/train)).
* Play around with the number of epochs. Are 1000 steps enough? How long does 10000 steps take?

Once you've found a set of parameters that minimize the loss, we can move on to the last stage of evaluation.

### Note:
You might say that of course our neural network performs well on this data - after all, this is the same data that we trained on. Well, that's a very astute observation. In fact, that's a common problem in machine learning. If we train and evaluate using the same data, we're bound to have success. The real test is being able to do well on data we haven't seen yet. So a common approach is to separate our data into train and test datasets.

### Քայլ 4:
Split the data into two sets (with say, 5 examples in each). Use one of the sets for training and the other set for testing. Do you see a difference in the loss for the **train** set versus the loss for the **test** set?

### Քայլ 5:
If you have time, see if you can run the model on new data to gain some insight about how you should plan for your future tests. For instance, if it's 11pm, you have a test tomorrow at 8am, and you haven't studied at all, what should you do?