import tensorflow as tf

# Let's define our input and output data.
# Note that this is all observed data, so it is defined as constants.
# The data includes 5 examples and 2 features.
# hours studied  |  hours slept  |  test score
# ---------------------------------------------
#       10       |      7        |     97
#        5       |      4        |     71
#        8       |      3        |     74
#        2       |      8        |     78
#        4       |      8        |     90
#        9       |      1        |     68
#        6       |      8        |     95
#        1       |      7        |     65
#        5       |      3        |     70
#        7       |      6        |     82
# ---------------------------------------------
# Define the raw data that we have observed.
train_input_data = [[10, 7], [5, 4], [8, 3], [2, 8], [4, 8]]
train_output_data = [[97], [71], [74], [78], [90]]

# Number of training examples.
NUM_TRAIN_EXAMPLES = len(train_input_data)

# Store the number of features so we can use it in our neural network structure.
NUM_FEATURES = len(train_input_data[0])

test_input_data = [[9, 1], [6, 8], [1, 7], [5, 3], [7, 6]]
test_output_data = [[68], [95], [65], [70], [82]]

# Number of training steps
EPOCHS = 10000
# Number of neurons in the neural network's hidden layer.
NUM_HIDDEN_LAYER_NEURONS = 3
# Learning rate of our gradient descent optimizer.
LEARNING_RATE = 2.0

graph = tf.Graph()
with graph.as_default():
  # Create a placeholder input tensor.
  input = tf.placeholder(dtype=tf.float32)

  # Create a placeholder for the output tensor (the observed test scores).
  output = tf.placeholder(dtype=tf.float32)

  train_data = {input: train_input_data, output: train_output_data}
  test_data = {input: test_input_data, output: test_output_data}

  # Determine the maximum value of each feature. The result is a 1x2 array.
  max_input = tf.reduce_max(input, 0)

  # Now all of our input values are in the range [0.0, 1.0].
  normalized_input = input / max_input

  # Set up the operations that will normalize the output tensor.
  max_output = tf.reduce_max(output)
  normalized_output = output / max_output

  # Now let's describe the structure of the neural network. We have 2 input features,
  # as described by the input dataset, so this corresponds to 2 nodes in the input
  # layer. Now we want to have a single hidden layer with 3 neurons. Finally, the
  # output layer will only have 1 neuron (the test score).
  num_neurons_1 = NUM_FEATURES
  num_neurons_2 = NUM_HIDDEN_LAYER_NEURONS
  num_neurons_3 = 1

  # Define the weights on the synapses between the input layer and the hidden layer.
  weights_1 = tf.Variable(tf.random_normal([num_neurons_1, num_neurons_2]))

  # Model the bias parameter, as well.
  bias_1 = tf.Variable(tf.random_normal([num_neurons_2]))

  # Compute the weighted sum and add in the bias. Note that bias_1 is 1x3, but the 3 
  # values will be element-wise added to each row in weighted_sums_1, which is 7x3.
  weighted_sums_1 = tf.matmul(normalized_input, weights_1) + bias_1

  # Apply the activation function (sigmoid).
  activation_1 = tf.sigmoid(weighted_sums_1)

  # Do the same steps for the second (output) layer.
  weights_2 = tf.Variable(tf.random_normal([num_neurons_2, num_neurons_3]))
  bias_2 = tf.Variable(tf.random_normal([num_neurons_3]))
  weighted_sums_2 = tf.matmul(activation_1, weights_2) + bias_2
  activation_2 = tf.sigmoid(weighted_sums_2)

  # Define the loss function as the sum of squared differences between observed
  # and computed output.
  loss = tf.reduce_sum((activation_2 - normalized_output)**2) / NUM_TRAIN_EXAMPLES

  # Set up the Stochastic Gradient Descient optimizer to minimize the loss.
  train_step = tf.train.GradientDescentOptimizer(learning_rate=LEARNING_RATE).minimize(loss)

  with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Run EPOCHS steps of learning.
    for i in range(EPOCHS):
      sess.run(train_step, feed_dict = train_data)
    
    # Here are the trained weights and biases, in case we're interested.
    print('weights_1 =\n{}'.format(sess.run(weights_1)))
    print('bias_1 =\n{}'.format(sess.run(bias_1)))
    print('weights_2 =\n{}'.format(sess.run(weights_2)))
    print('bias_2 =\n{}'.format(sess.run(bias_2)))

    # Does our trained model perform well on the training data?
    print('train data: normalized_output =\n{}'.format(sess.run(normalized_output, feed_dict = train_data)))
    print('train data: activation_2 =\n{}'.format(sess.run(activation_2, feed_dict = train_data)))

    # A good measure of how well we're doing is how small the loss is.
    print('train data: loss = {}'.format(sess.run(loss, feed_dict = train_data)))

    # Does our trained model perform well on the testing data?
    print('test data: normalized_output =\n{}'.format(sess.run(normalized_output, feed_dict = test_data)))
    print('test data: activation_2 =\n{}'.format(sess.run(activation_2, feed_dict = test_data)))

    # A good measure of how well we're doing is how small the loss is.
    print('test data: loss = {}'.format(sess.run(loss, feed_dict = test_data)))      

    # Run it on a couple of new inputs just to see what the model predicts.
    print('unseen data: activation_2 =\n{}'.format(sess.run(activation_2, feed_dict = {input: [[0, 8], [1, 7], [4, 4], [2, 6], [8, 0]]})))
