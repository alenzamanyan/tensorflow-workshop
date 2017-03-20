## Exercise 3: Training a trivial model.

### Step 1:
Assume that we don’t know what the weight should be. But we do know what the end result should be. In other words, we know that this model should take in 3.2 and should produce 10.0. Define a constant with value 10.0, and assign it to the Python variable **output_** (note the underscore).

### Step 2:
Now we need to define a loss function. This tells us how far we are from the correct output value given the current weight value. It will allow us to modify the weight value (initially, 2.0) to get closer to the known output (10.0). Here’s the loss function that we will use:

<center>loss = (output - output_)<sup>2</sup></center>

Stop and make sure you understand this loss function. For one thing, why do we square the difference? Create a Python variable named **loss** and set it equal to the square of the difference, as shown in the formula above.

### Step 3:
Now we will try to learn the weight that will produce the value 10.0 when given the input 3.2. Create a gradient descent optimizer with learning rate 0.025 and store it in variable named **optimizer** ([documentation](https://www.tensorflow.org/api_docs/python/tf/train/GradientDescentOptimizer)).

### Step 4:
Call minimize function on optimizer to generate an operation that we can use for learning the weight ([documentation](https://www.tensorflow.org/api_docs/python/tf/train/GradientDescentOptimizer#minimize)). Assign the op to Python variable **train_step**.

### Step 5:
Run a single training step using session run. Check the value of the weight and the output. Is this a good weight? If not, try running the training step again and check the results again.

### Step 6:
Now, reset the weight to its initial value by running tf.global_variables_initializer(). Verify that the weight is in fact 2.0.

### Step 7:
Write a for loop to iterate on the training step 20 times. You can use the range built-in Python function ([documentation](https://docs.python.org/2/library/functions.html#range)). In each iteration, print out the following three things:
* step number (i.e., 0, 1, 2, 3, 4)
* the value of **weight**
* the value of **output**

### Step 8:
How many steps does it take to get the exact weight (10 / 3.2 = **3.125**)?

(Remember to put all your code into a separate file for submission and for future reference)
