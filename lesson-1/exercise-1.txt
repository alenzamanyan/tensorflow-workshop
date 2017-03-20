Exercise 1: Hello, TensorFlow!

As is customary, let’s start with a basic “Hello, world!” example.
Step 1:
Import TensorFlow library.

Step 2:
Create a constant TensorFlow operation to store your “Hello, world!” string ([documentation](https://www.tensorflow.org/versions/r0.10/api_docs/python/constant_op/constant_value_tensors#constant)).

Step 3:
Create a TensorFlow session (documentation).

Step 4:
Run the session, passing it the constant as a fetch (documentation).

Step 5:
Open up a file (name it hello_world.py), and copy what you did in steps 1-4 into the file. You should be able to run the file from terminal using the following command:
> python hello_world.py
Hello, TensorFlow!

Step 6:
Use “with” statement (context management) to define session in your script (documentation). Re-run your script to make sure it still works.

Step 7:
Use special __name__ variable to only run the code in your script when the script is directly invoked (i.e., not imported as a library, documentation). Re-run your script to make sure it still works.
