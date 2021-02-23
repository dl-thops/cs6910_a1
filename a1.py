# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import numpy as np


class NeuralNet:
    def __init__(self,input_size,output_size=1):
        self.structure=[input_size,output_size]
        self.weights = []
        self.bias = []
        
    def addlayer(self,layer_size):
        self.structure=self.structure[:-1]+[layer_size]+self.structure[-1]
        
    def train(self,initialization_type="random",activation="sigmoid"):
        self.init_type = initialization_type
        self.activation = activation
        if self.init_type == "random":
            for i in range(1,len(self.structure)):
                self.weights.append(np.random.rand(self.structure[i],self.structure[i-1]))
                self.bias.append(np.random.rand(self.structure[i],1))
        elif self.init_type=="xavier":
            #to do
            pass
        else:
            print("Unidentified initialization type")
    
    def predict(self,X):
        preds = X
        for i in range(len(self.weights)):
            preds = NeuralNet.activate(np.matmul(self.weights[i],preds)+self.bias[i],self.activation)
            
        return preds
    
    def sigmoid(X):
        X = np.clip(X,-700,700)
        return 1/(1.+np.exp(-X))
            
    def tanh(X):
        pass
        
    def relu(X):
        pass
        
    def activate(X,activation):
        if activation == "sigmoid":
            return NeuralNet.sigmoid(X)
        elif activation == "tanh":
            return NeuralNet.tanh(X)
        elif activation == "relu":
            return NeuralNet.relu(X)
            
