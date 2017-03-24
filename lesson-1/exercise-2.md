## Exercise 2: Simple arithmetic

### Step 1:
Define a tensorflow constant and store the integer 2 in it ([documentation](https://www.tensorflow.org/versions/r0.10/api_docs/python/constant_op/constant_value_tensors#constant)). Assign it to the Python variable **x**.

### Step 2:
Define a second constant and store the integer 3 in it. Assign it to the Python variable **y**.

### Step 3:
Multiply x and y and store the result in z. Use the conventional * operator for multiplication.

### Step 4:
Take a look at what’s stored in each Python variable. You can do this by typing the variable name and pressing enter or using the print function. What is the information stored in x, y, and z?

### Step 5:
As you can see, we don’t have the result of 2 * 3 yet. In order to evaluate the expression, we need to run the graph. Use the same approach from Exercise 1 to run the graph. What should you use as the fetch value?

### Step 6:
The * operator is translated into the tensorflow multiply operation. Perform the same multiplication as you did in Step 3, but do so using the multiply operation explicitly ([documentation](https://www.tensorflow.org/api_docs/python/tf/multiply)). Store the operation in a Python variable called **tf_z**.

### Step 7:
Run the graph again as you did in **Step 5** to verify the result.