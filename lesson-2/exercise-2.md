## Exercise 2: Visualizing the graph using TensorBoard.

### Step 1:
Create a summary file writer ([documentation](https://www.tensorflow.org/api_docs/python/tf/summary/FileWriter)) and name it **graph_writer**.

### Step 2:
Add to the default graph to graph_writer.

### Step 3:
Run TensorBoard in a separate terminal ([documentation](https://www.tensorflow.org/get_started/summaries_and_tensorboard#launching_tensorboard)). Here’s the command (replace the bolded part with your subdirectory name):
`> tensorboard --logdir=**[REPLACE-THIS-WITH-SUBDIRECTORY-NAME]**`

### Step 4:
The terminal will start up TensorBoard on your machine and will make it accessible via port 6006. It should print out the following:

```Starting TensorBoard 39 on port 6006
(You can navigate to http://127.0.1.1:6006)
```

Go to http://127.0.1.1:6006/ to view the graph in the TensorBoard console. Go to the Graphs tab to see the simple network that you just built.
