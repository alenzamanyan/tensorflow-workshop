## Exercise 1: Setting up the data

### Step 1:
Create a Python list to encode the input features (study time, sleep time) described in the README file. The dimensions of the list should be 7x2. In other words, you need to use nested to make the list look like a matrix.

### Step 2:
Create a Python list to encode the output values (test scores) described in the README file. The dimensions of the list should be 7x1.

### Step 3:
Use the raw **input** data to create a constant TensorFlow operation. Pass dtype=tf.float32 to the constant constructor to ensure that the values are read in as floats. Otherwise, we will have data type incompatibility issues later.

### Step 4:
Use the raw **output** data to create a constant TensorFlow operation. This should look a lot like what you do in **Step 3**.

### Step 5:
For each of these tensors, we need to prepare the data by normalizing it (so that the values are between 0 and 1). This is because we are not interested in the units (i.e., hours, points on a test), but rather the relative values of these observations. For each feature, we will determine the maximum value and divide all observations by that value.

* First, you can use reduce_max() to compute the max per feature ([documentation](https://www.tensorflow.org/api_docs/python/tf/reduce_max)). This will generate a 1x2 tensor.

* Now, you can divide your input tensor from **Step 3** by the output of reduce_max() to get the normalized input. Note that dividing a 7x2 tensor by a 1x2 tensor results in element-wise division across all rows of the 7x2 tensor.

### Step 6:
Perform the same steps that you did in **Step 5** to normalize the output tensor.