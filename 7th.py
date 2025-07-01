import numpy as np

# Input data (features) and actual output (target)
X = np.array([[2, 9], [1, 5], [3, 6]], dtype=float)
y = np.array([[92], [86], [89]], dtype=float)

# Normalize data
X = X / np.amax(X, axis=0)  # Scale input
y = y / 100                 # Scale output between 0 and 1

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid (for backpropagation)
def derivatives_sigmoid(x):
    return x * (1 - x)

# Hyperparameters
epoch = 5000                  # Number of iterations
lr = 0.1                      # Learning rate
inputlayer_neurons = 2       # Number of input features
hiddenlayer_neurons = 3      # Number of hidden neurons
output_neurons = 1           # Output neuron

# Weight and bias initialization
wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))  # weights for input -> hidden
bh = np.random.uniform(size=(1, hiddenlayer_neurons))                   # bias for hidden layer
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))    # weights for hidden -> output
bout = np.random.uniform(size=(1, output_neurons))                      # bias for output layer

# Training the ANN
for i in range(epoch):
    # Forward propagation
    hinp1 = np.dot(X, wh)
    hinp = hinp1 + bh
    hlayer_act = sigmoid(hinp)

    outinp1 = np.dot(hlayer_act, wout)
    outinp = outinp1 + bout
    output = sigmoid(outinp)

    # Backpropagation
    EO = y - output                # Error at output
    outgrad = derivatives_sigmoid(output)
    d_output = EO * outgrad

    EH = d_output.dot(wout.T)      # Error at hidden layer
    hiddengrad = derivatives_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddengrad

    # Updating weights and biases
    wout += hlayer_act.T.dot(d_output) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

# Display the results
print("Input: \n", X)
print("Actual Output: \n", y)
print("Predicted Output after training: \n", output)
