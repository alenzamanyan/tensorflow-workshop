## Exercise 1: Setting up the data

### Step 0:
The first thing you might want to do is create a tensorflow Graph ([documentation](https://www.tensorflow.org/api_docs/python/tf/Graph)). You can then use a context manager to make sure that all operations are added to this graph (and not the default graph, [documentation](https://www.tensorflow.org/api_docs/python/tf/Graph#as_default)).

### Step 1:
Create a Python list to encode the input features (study time, sleep time) described in the README file. The dimensions of the list should be 10x2 (10 examples and 2 features). In other words, you need to use nesting to make the list look like a matrix.

### Step 2:
Create a Python list to encode the output values (test scores) described in the README file. The dimensions of the list should be 10x1 (10 examples and 1 test score per example).

### Step 3:
Create a tensorflow placeholder to hold float32 **input** data ([documentation](https://www.tensorflow.org/versions/r0.11/api_docs/python/io_ops/placeholders)).

### Step 4:
Create another tensorflow placeholder to hold float32 **output** data.

### Step 5:
We're going to use these placeholders to feed data into our neural network. We do this by using a Python dictionary ([documentation](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)). Look for the feed_dict parameter of the tf.Session's run() function ([documentation](https://www.tensorflow.org/api_docs/python/tf/Session#run)). Define a dictionary (call it **feed_dict**) and store two elements in it.
* The key for the first element is the **input** tensor we defined in **Step 3**. The value for the first element is the raw input data we defined in **Step 1**.
* The key for the second element is the **output** tensor we defined in **Step 4**. The value for the second element is the raw output data we defined in **Step 2**.

We'll use this feed_dict dictionary later when we are training and evaluating the results.

### Step 6:
For the **input** and **output** tensors, we need to prepare the data by normalizing it (so that the values are between 0 and 1). This is because we are not interested in the units (i.e., hours, points on a test), but rather the relative values of these observations. For each feature, we will determine the maximum value and divide all observations by that value.

* First, you can use reduce_max() to compute the max per feature ([documentation](https://www.tensorflow.org/api_docs/python/tf/reduce_max)). This will generate a 1x2 tensor.

* Now, you can divide your **input** tensor from **Step 3** by the output of reduce_max() to get the normalized input. Note that dividing a 10x2 tensor by a 1x2 tensor results in element-wise division across all rows of the 10x2 tensor.

### Step 7:
Perform the same steps that you did in **Step 6** to normalize the **output** tensor.