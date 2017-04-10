## Exercise 1: Getting ready for training

### Step 1:
Create a tensorflow constant with value 3.6 and assign it to **input**.

### Step 2:
Create a tensorflow Variable with initial value 2.0 and assign it to **weight** ([documentation](https://www.tensorflow.org/api_docs/python/tf/Variable)). 

### Step 3:
Multiply weight by input and assign it to **output** ([documentation](https://www.tensorflow.org/api_docs/python/tf/matmul)).

### Step 4:
Print out the multiplication op in the graph. What are its inputs?

### Step 5:
Create an op that will initialize all variables (in this case, we have only one variable, [documentation](https://www.tensorflow.org/versions/r0.10/api_docs/python/state_ops/variable_helper_functions#initialize_all_variables)).

### Step 6:
Create a session and run the op that you created in **Step 5**. The **weight** variable is now initialized to the value we specified in **Step 2** (namely, 2.0).

### Step 7:
Run the op to produce the multiplication result.

(Make sure to copy the successful steps you performed to a file for submission)