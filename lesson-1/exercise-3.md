## Exercise 3: Inspect the graph ([documentation](https://www.tensorflow.org/api_docs/python/tf/multiply))

### Step 1:
Get the default graph and store it in a Python variable. Call it **graph**.

### Step 2:
Print out the names of all the operations in the graph. Note that the TensorFlow name for an operation is different from the Python variable we pointed at it.

### Step 3:
Print out each operation in full ([documentation](https://www.tensorflow.org/api_docs/python/tf/Graph#get_operation_by_name)). You can use the Python built-in print command ([documentation](https://docs.python.org/2/library/functions.html#print)). What do the operations look like? Make sure to understand all the parts of the [proto buffer](https://developers.google.com/protocol-buffers/?hl=en) that is printed out.

### Step 4:
Create a new operation in the default graph and give it a TensorFlow name. Print out the operation.

### Step 5:
How many operations are in the default graph? How many are in **graph**? Is this what you would expect? Explain why.
