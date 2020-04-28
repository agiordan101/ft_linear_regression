"""
from plotly.offline import plot
import plotly.graph_objs as plgraph
import numpy as np
x = np.arange(250000)
"""

#Function to predict price with mileage
def	predict(mileage):
	return weights[0] * mileage + weights[1]

#Read data
weights_file = open("weights", "r")
weights = weights_file.read().split('\n')
weights_file.close()

dataset_file = open("data.csv", "r")
lines = dataset_file.read().split('\n')
dataset_file.close()

#Parse data
weights[0] = float(weights[0])
weights[1] = float(weights[1])

del lines[0]
del lines[-1]
km = []
price = []
for i in lines:
	line = i.split(",")
	km.append(float(line[0]))
	price.append(float(line[1]))

#lr = float(input("Enter a learning rate (default: 1) : "))
lr0 = 0.0000000001
lr1 = 0.1

print("Km :", km)
print("Price : ", price)
print("Weights : ", weights[0], " / ", weights[1])
#print("Learning rate : ", lr)
"""
#fig = plgraph.Figure(data=plgraph.Scatter(x=x, y=weights[0] * x + weights[1]))
#fig.add_trace(plgraph.Scatter(x=km, y=price, mode='markers', name='markers'))
fig = plgraph.Figure()
fig.add_scatter(x=km, y=price, mode='markers', name='markers')
"""
#Compute new weights
for k in range(10000):
	deltaWeight0 = 0
	deltaWeight1 = 0
	for i in range(len(km)):
		error = price[i] - predict(km[i])
		deltaWeight0 += error * km[i];
		deltaWeight1 += error * 1;
	deltaWeight0 /= len(km)
	deltaWeight1 /= len(km)
	weights[0] += lr0 * deltaWeight0
	weights[1] += lr1 * deltaWeight1
	#fig.update_traces(patch=dict(x=x, y=weights[0] * x + weights[1]), selector=dict(type="scatter", mode="lines"))
"""
fig.add_scatter(x=x, y=weights[0] * x + weights[1])
plot(fig)
"""
print("New weights : ", weights[0], " / ", weights[1])

#Write new weights
"""
weights_file = open("weights", "w")
weights_file.write(str(w0) + "\n")
weights_file.write(str(w1) + "\n")
weights_file.close()
"""
