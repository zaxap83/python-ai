import neuron
from datetime import datetime

usd = 1
uah = 42.26
checkValue = 100

neuron = neuron.Neuron()

i = 0
startTime = datetime.now()
while neuron.lastError > neuron.correctionStep or neuron.lastError < -neuron.correctionStep:
    i = i + 1
    neuron.train(usd, uah)
    print('Iteration', i, ' inaccuracy ', neuron.lastError)

print('Result: $', checkValue, ' = ', round(neuron.processInputData(checkValue), 2), 'UAH')
print('Time spent: ', datetime.now() - startTime)