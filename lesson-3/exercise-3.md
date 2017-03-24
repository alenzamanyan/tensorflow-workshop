## Exercise 3: Learning the weights

**Python tip: In the interactive shell, you can import a library once. Subsequent imports will not reload your code. For that, you can use the **reload** function ([documentation](https://docs.python.org/2/library/functions.html#reload).**

We've prepared the data and built the neural network. There's not much left to do! We just have to define the loss function and the optimization technique and we're off to the races!

### Step 1:
The loss function is going to be the sum of squared differences between the actual and predicted value for each example. Here is the formula:

**loss = (1/num_examples) * Σ(actual - predicted)<sup>2</sup>**

In our case, the **actual** is the normalized output we set up in **Exercise 1**. The **predicted** output is the same as **activation_2** from **Exercise 2**. **num_examples** is the number of examples in our dataset.

Now, you may be thinking, "what's that Σ symbol?" This is sum over all examples. An easy way to compute this in tensorflow is using tf.reduce_sum ([documentation](https://www.tensorflow.org/api_docs/python/tf/reduce_sum)).

### Step 2:
We have the loss function, which tells us how far we are from the actual output. So we need an optimizer that can modify the variables of the system (namely, the **weights** and **biases**) and to minimize the loss. Create a GradientDescentOptimizer and call its minimize() function, passing it the **loss** we defined in **Step 1**. You can go back to **Lesson 2 - Exercise 3** to refresh your memory on how to do this. What learning rate did you choose?

### Step 3:
Create a context for the session. Don't forget to tab-indent for the next few steps.

```python
with tf.Session() as sess:
```

### Step 4:
Initialize all the tensorflow variables.

### Step 5:
Before we train, let's take a look at the output of the neural network based on the zeroed or random weights we've assigned as initial values. It should be nothing near the actual output.

```python
  print(sess.run(activation_2, feed_dict = feed_dict))
```

Note: Remember the **feed_dict** dictionary that we defined in **Exercise 1**. That's what we're using here to feed data into the network.

### Step 6:
An **epoch** is a single run of the optimization method. Use a for loop to run 10000 epochs of the training step that we defined in **Step 2**. Don't forget to feed our data into the network.

**Congratulations! You've built and trained your first neural network.**
