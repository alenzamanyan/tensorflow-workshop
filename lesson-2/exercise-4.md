## Exercise 4: Visualize the training steps.

Printing out the result of each training step was a nice way to see the progression of the weight. But another great way to see this is by using a plot.

### Step 1:
Create a summary operation that will output a protocol buffer with a single scalar entry (documentation). More specifically, the entry that you want to track is **output** from the previous exercise. Assign it to **summary_y**.

### Step 2:
Like you did in Step 1, create another summary operation, but this one should track the **weight** variable. Assign it to **summary_w**.

### Step 3:
Create a file writer that will write the summary values to a file (documentation). The logdir parameter can be anything that is valid unix filename. It will be used to create a subdirectory which will contain the event files that we will load into TensorBoard. Assign the file writer to a Python variable named **summary_writer**.

### Step 4:
Let’s re-run the training, but this time adding summary metrics to a file for subsequent visualization. In your for loop, add the following two lines, before running sess.run(train_step). Note that the variable **i** here is the one that you iterate over in your for loop. Make sure you understand the two lines that you are adding. Ask the instructor if you have questions about it.
summary_writer.add_summary(sess.run(summary_y), i)
summary_writer.add_summary(sess.run(summary_w), i)

### Step 5:
In a separate terminal, navigate to the directory where we are running Python. You can use the *ls* unix command to verify that this directory contains the subdirectory that we specified in Step 3. Run the following command (replacing the bolded part with your subdirectory name):
`> tensorboard --logdir=**[REPLACE-THIS-WITH-SUBDIRECTORY-NAME]**`

### Step 6:
The terminal will startup TensorBoard on your machine and will make it accessible via port 6006. It should print out the following:

Starting TensorBoard 39 on port 6006
(You can navigate to http://127.0.1.1:6006)

Navigate to http://127.0.1.1:6006 to see the TensorBoard interface. You should see a summary metric for output and another one for weight. Examine the graphs to see the step-by-step updating of the weight during each iteration of training.
