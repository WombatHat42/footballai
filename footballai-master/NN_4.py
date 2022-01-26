import random
import math
import Matrix
import numpy as np

class NeuralNetwork:

    def __init__(self, scenarioLen, inputSize, hiddenSize, playbook):
        """creates a neural network and its layers as long as a
        few extra variables"""
        self.input = []
        self.hidden = []
        self.output = []
        self.variation = 1
        self.playbook = playbook
        self.learning_rate = .2

        for num in range(inputSize):
            self.input.append(Perceptron(scenarioLen, self.learning_rate))

        for num in range(hiddenSize):
            self.hidden.append(Perceptron(inputSize, self.learning_rate))

        for num in range(len(playbook)):
            self.output.append(Perceptron(hiddenSize, self.learning_rate))
            
    def newLearnRate(self, learning_rate):
        self.learning_rate = learning_rate
        for p in self.input:
            p.newLearnRate(learning_rate)

        for p in self.hidden:
            p.newLearnRate(learning_rate)

        for p in self.output:
            p.newLearnRate(learning_rate)

    def sigmoid_values(self):
        print('Input Sigmoid:')
        print(self.inputSigmoid)
        print('Hidden Sigmoid:')
        print(self.hiddenSigmoid)
        print('Output Sigmoid:')
        print(self.outputSigmoid)

    def current_weights(self):
        print('Input Weights:')
        for p in self.input:
            print(p.weights)
        print('Hidden Weights:')
        for p in self.hidden:
            print(p.weights)
        print('Output Weights:')
        for p in self.output:
            print(p.weights)

    def feedforward(self, scenario):
        """Feed forward a scenario through each layer using sigmoid calculation"""

        self.inputSigmoid = []
        self.hiddenSigmoid = []
        self.outputSigmoid = []
        """input layer"""
        wgt = []
        for w in scenario:
            wgt.append(w * .01)
        for pi in self.input:
            self.inputSigmoid.append(pi.sig_calc(wgt))
    
        """hidden layer"""
        for ph in self.hidden:
            self.hiddenSigmoid.append(ph.sig_calc(self.inputSigmoid))
        
        for po in self.output:
            self.outputSigmoid.append(po.sig_calc(self.hiddenSigmoid))

            
        play = Football.playCall(self)

        return play

    def backprop(self, offense, defense, scenario):
        self.loss = 0
        self.prevInput = self.input
        self.prevHidden = self.hidden
        self.prevOutput = self.output
        self.outputError = []
        self.hiddenError = []
        self.inputError = []
        scenarioLower = []
        for s in scenario:
            scenarioLower.append(s * .01)
        self.scenario = scenarioLower

        '''Output Layer'''
        self.feedforward(scenario)
        
        computedList = []
        targetList = []
        
        computed = self.outputSigmoid
        for value in computed:
            computedList.append(value)
        target = Matrix.expected(offense)
        
        index = 0
        for grade in target:
            if index == self.play:
                targetList.append(0)
            else:
                if grade == 4:
                    targetList.append(1)
                else:
                    targetList.append(computed[index])
            index += 1

        self.loss = self.total_loss(targetList)

        self.output_learn(targetList)
        self.hidden_learn()
        self.input_learn()

        self.variation += 1

    def total_loss(self, target):
        totalLoss = 0
        for index in range(len(target)):
            if (target[index] - self.outputSigmoid[index]) < 0:
                totalLoss += (target[index] - self.outputSigmoid[index]) * -1
            else:
                totalLoss += (target[index] - self.outputSigmoid[index])

        return totalLoss
        
    
    def output_learn(self, target):
        
        index = 0
            
        for perceptron in self.output:
            self.outputError.append(perceptron.epochOutput(target[index], self.outputSigmoid[index], self.hiddenSigmoid))
            index += 1
    
    def hidden_learn(self):

        
        totalError = NeuralNetwork.error(len(self.hidden), self.outputError)

        index = 0

        for perceptron in self.hidden:
            self.hiddenError.append(perceptron.epochHI(totalError[index], self.inputSigmoid))
            index += 1

    def input_learn(self):

        totalError = NeuralNetwork.error(len(self.input), self.hiddenError)
        
        index = 0

        for perceptron in self.input:
            self.inputError.append(perceptron.epochHI(totalError[index], self.scenario))
            index += 1

    def error(layerLength, errorLayer):
        totalError = []
        for percCount in range(layerLength):
            totalError.append(0)
            
        for layer in errorLayer:
            for num in range(len(layer)):
                
                totalError[num] += layer[num]

        return totalError
        

        
class Perceptron:

    def __init__(self, no_of_inputs, learning_rate):
        self.learning_rate = learning_rate
        self.weights = []
        for i in range(no_of_inputs + 1):
            self.weights.append(np.random.uniform(0, .2))

    def newLearnRate(self, learning_rate):
        self.learning_rate = learning_rate

    def sig_calc(self, inputs):
        weight = 0
        index = 0
        
        """calculates sigmoid value. input equals prev layer sigmoid values"""
        for i in inputs:
            weight += i * self.weights[index]
            index += 1
    
        s = Activation.sigmoid(weight - self.weights[-1])
        
        return s

    def epochOutput(self, T, O, prevSig):
        LR = self.learning_rate
        errorFrac = []

        error = T - O

        totalWeight = 0

        for weightIndex in range(len(self.weights) - 1):
            if self.weights[weightIndex] < 0:
                totalWeight += (self.weights[weightIndex] * -1)
            else:
                totalWeight += self.weights[weightIndex]

        for weightIndex in range(len(self.weights) - 1):
            I = prevSig[weightIndex]
            
            if error != 0:
                if weightIndex < (len(self.weights) - 1):
                    prevNode = (self.weights[weightIndex] / totalWeight) * error
                    errorFrac.append(prevNode)
                    self.weights[weightIndex] = self.weights[weightIndex] + LR * I * error
                else:
                    self.weights[weightIndex] = self.weights[weightIndex] + LR * (-1) * error
            else:
                errorFrac.append(0)
                
        return errorFrac
    
    def epochHI(self, error, prevSig):
        LR = self.learning_rate
        errorFrac = []
        totalWeight = 0

        for weightIndex in range(len(self.weights) - 1):
            if weightIndex < (len(self.weights) - 1):
                if self.weights[weightIndex] < 0:
                    totalWeight += (self.weights[weightIndex] * -1)
                else:
                    totalWeight += self.weights[weightIndex]

        for weightIndex in range(len(self.weights) - 1):
            I = prevSig[weightIndex]
            
            if error != 0:
                
                if weightIndex < (len(self.weights) - 1):
                    prevNode = (self.weights[weightIndex] / totalWeight) * error
                    errorFrac.append(prevNode)
                    self.weights[weightIndex] = self.weights[weightIndex] + LR * I * error
                else:
                    self.weights[weightIndex] = self.weights[weightIndex] + LR * (-1) * error
            else:
                errorFrac.append(0)
        return errorFrac
    
class Activation:

    def sigmoid(x):

        if x >= 0:
            z = math.exp(-x)
            sig = 1 / (1 + z)
            return sig
        else:
            z = math.exp(x)
            sig = z / (1 + z)
            return sig
            if x >= 0:
                z = math.exp(-x)
                sig = 1 / (1 + z)
                return sig
            else:
                z = math.exp(x)
                sig = z / (1 + z)
                return sig

class Football:

    def playCall(self):
        playIndex = 0
        playPredict = -9999999999
        self.play = 0
        
        for value in self.outputSigmoid:

            if value > playPredict:
                playPredict = value
                self.play = playIndex
                
            playIndex += 1
                
        return self.playbook[self.play]
            
    
        
        
