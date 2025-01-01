import neuron

usd = 1
uah = 42.26

neuron = neuron.Neuron()

i = 0
while neuron.lastError > neuron.correctionStep or neuron.lastError < -neuron.correctionStep:
    i = i + 1
    neuron.train(usd, uah)
    print('Iteration', i, ' inaccuracy ', neuron.lastError)

print('Result: ', neuron.processInputData(100))