import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def perceptron(myinput, weight):
    bias = weight[-1]
    print(bias)
    mysum = bias
    for i in range(len(myinput)-1):
        mysum += myinput[i]* weight[i]
        print(mysum)
    output = activationfunction(mysum)
    print(output)
    return output


def activationfunction(Sum):
    result = sigmoid(Sum)
    return result


def sigmoid(value):
    return 1 / (1 + np.exp(-value))


def weights(rows, columns):
    weightarray = np.random.rand(rows+1, columns)
    weightmatrix= weightarray.transpose()
    return weightmatrix


def main():
    myinputs = []
    networklayers = int(input("How many layers does the neural network have, apart from input layer?"))
    for layer in range(networklayers):
        if layer==0:
            print("This is input layer \n ")
            neurons = int(input("How many neurons does layer " + str(layer + 1) + "have"))
            columns = int(input("How many inputs does each neuron have?"))
           # Entering the inputs into a matrix
            for i in range(0,neuron):
                print("Entering input values for neuron " + str(i+1) + " now....")
                myinputs.append([])
                for j in range(0,columns):
                    myinputs[i].append(int(input("Enter the " + str(j+1) + " input")))
            # Printing the inputs
            print("Inputs: ")
            print(np.matrix(myinputs))
        else:
            print("....This is  Hidden layer no. "+ str(layer)+ "....")
        # Building a weight matrix with random numbers, +1 for bias
        myweights = weights(rows, columns)
        print("Weights are: " )
        print(np.matrix(myweights))
        output=[]
        for i in range(rows):
            print(myinputs[i][:])
            print(myweights[:][i])
            output.append(perceptron(myinputs[i][:], myweights[i][:]))
        myinputs=output
        print("Output of layer:")
        print(myinputs)
main()
