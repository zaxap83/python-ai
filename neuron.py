class Neuron:
    weight = 0.5 # random weight, it will be corrected in train
    lastError = 1 # random value, it must be > correctionStep to start the train
    correctionStep = 0.0001 # smaller correction will give better result but will take more time

    def processInputData(self, inputValue):
        return inputValue * self.weight

    def restoreInputData(self, outputValue):
        return outputValue / self.weight

    def train(self, inputValue, expectedResult):
        actualResult = inputValue * self.weight
        self.lastError = expectedResult - actualResult
        correction = (self.lastError / actualResult) * self.correctionStep
        self.weight = self.weight + correction
