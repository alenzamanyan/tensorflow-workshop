## Exercise 3: Inspect the graph

### Step 1:
Loop over all the operations in the default graph ([documentation](https://www.tensorflow.org/api_docs/python/tf/get_default_graph)) and print them in full ([documentation](https://www.tensorflow.org/api_docs/python/tf/Graph#get_operations)). You can use the Python built-in print command ([documentation](https://docs.python.org/2/library/functions.html#print)). What do the operations look like? Make sure to understand all the parts of the [proto buffer](https://developers.google.com/protocol-buffers/?hl=en) that is printed out.

### Step 2:
Add another operation and give it a name (use the **name** parameter). Print out all the operations again and find the named operation in the list.

### Step 3:
Create a summary file writer object