# -*- coding: utf-8 -*-
"""
Question 4:
Implement the Forward propagation & Backward propagation for a three 
layers Neural Network. X,W and b can be random.
"""

from random import random
from random import seed
from math import exp


# Consider a three layers neural network
# count_in is the number of inputs
# n_hidden is the number of neurons in the hidden layer
# count_out is the number of outputs

# Neural Network Initialization
def neunet_init(count_in, n_hidden, count_out):
    neunet = list()
    layer_hidden = [{'weights':[random() for i in range(count_in + 1)]} for i in range(n_hidden)]
    neunet.append(layer_hidden)
    layer_out = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(count_out)]
    neunet.append(layer_out)
    return neunet

#Neuron Activation
def neuact(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation

# Use Sigmoid Activation Function - Transfer Neuron Activation
def tranact(activation):
	return 1.0 / (1.0 + exp(-activation))

# Forward Propagation
def forw_prop(neunet, row):
    inputs = row
    for layer in neunet:
        new_inputs = []
        for neuron in layer:
            activation = neuact(neuron['weights'], inputs)
            neuron['output'] = tranact(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

# Derivative of neuron output
def tranderv(output):
	return output * (1.0 - output)

# Backward Propagation
def back_prop(neunet, eout):
	for i in reversed(range(len(neunet))):
		layer = neunet[i]
		errors = list()
		if i != len(neunet)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in neunet[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(eout[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * tranderv(neuron['output'])
            
# Update weights with error
def upweights(neunet, row, LR):
	for i in range(len(neunet)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in neunet[i - 1]]
		for neuron in neunet[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += LR * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += LR * neuron['delta']
            

# Train network for epochs
def train_neunet(neunet, train, LR, count_epoch, count_out):
	for epoch in range(count_epoch):
		sum_error = 0
		for row in train:
			outputs = forw_prop(neunet, row)
			eout = [0 for i in range(count_out)]
			eout[row[-1]] = 1
			sum_error += sum([(eout[i]-outputs[i])**2 for i in range(len(eout))])
			back_prop(neunet, eout)
			upweights(neunet, row, LR)
		print('--> epoch=%d, LR=%.3f, error=%.3f' % (epoch, LR, sum_error))

        
# Predict using the network
def predict_neunet(neunet, row):
	outputs = forw_prop(neunet, row)
	return outputs.index(max(outputs))

# Training the network with a sample dataset
seed(1)
dataset = [[1,1,0],
	[2.5,1,2,0],
	[1.7,3,7,0],
	[4.3,3,5,0],
	[5.5,2,0],
	[6,2.3,1],
	[5.7,6.8,1],
	[8.7,1,1],
	[9.8,2.1,1],
	[4,9,1]]
count_in = len(dataset[0]) - 1
count_out = len(set([row[-1] for row in dataset]))
neunet = neunet_init(count_in, 3, count_out)   #Considering 3 neurons for the hidden layer
train_neunet(neunet, dataset, 0.6, 25, count_out)
print()
print("Following are the layers with corresponding weights: ")
for layer in neunet:
	print(layer)

# Making prediction for a new dataset    
new_dataset = [[1.5,2],
	[3,4.5],[6,2],
    [1,2.2],[6,7],
    [5.4,5.9]]

print()
print("Predictions for the new dataset are: ")
for row in new_dataset:
	prediction = predict_neunet(neunet, row)    
	print('Prediction = ', prediction)
    



    

