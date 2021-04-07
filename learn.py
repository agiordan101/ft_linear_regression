from plotly.offline import plot
import plotly.graph_objs as plgraph
import numpy as np
import sys

x_axis = np.arange(250000)
lr0 = 0.0000000001
lr1 = 0.1
epochs = range(500)

#Function to predict price with mileage
def	predict(mileage):
	return weights[0] * mileage + weights[1]

#Read data
weights_file = open("weights.txt", "r")
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

print("Actual weights : ", weights[0], " / ", weights[1])
print("Data set :\n")
print("Km :", km)
print("Price : ", price)

losses = []

momentum_w0 = 0
momentum_w1 = 0

if any(["-momentum" in arg for arg in sys.argv]):
	rho = 0.9
else:
	rho = 0


#Compute new weights
for epoch in epochs:
	
	losses.append([])
	
	deltaWeight0 = 0
	deltaWeight1 = 0
	for batch in range(len(km)):
		loss = price[batch] - predict(km[batch])
		losses[-1].append(loss * loss)

		deltaWeight0 += loss * km[batch]
		deltaWeight1 += loss * 1

	losses[-1] = sum(losses[-1]) / len(losses[-1])

	deltaWeight0 /= len(km)
	deltaWeight1 /= len(km)

	momentum_w0 = rho * momentum_w0 + (1 - rho) * deltaWeight0
	momentum_w1 = rho * momentum_w1 + (1 - rho) * deltaWeight1

	weights[0] += lr0 * momentum_w0
	weights[1] += lr1 * momentum_w1


if any(["-plot_model" in arg for arg in sys.argv]):
	# Print dataset & linear predictions
	fig_predict = plgraph.Figure()
	fig_predict.add_scatter(x=km, y=price, mode='markers', name='markers')
	fig_predict.add_scatter(x=x_axis, y=weights[0] * x_axis + weights[1])
	plot(fig_predict)

if any(["-plot_loss" in arg for arg in sys.argv]):
	# Print losses over epochs
	fig_loss = plgraph.Figure()
	print(losses)
	fig_loss.add_scatter(x=list(epochs), y=losses)
	plot(fig_loss)


print("\nNew weights : ", weights[0], " / ", weights[1])

#Write new weights
weights_file = open("weights.txt", "w")
weights_file.write(str(weights[0]) + "\n")
weights_file.write(str(weights[1]) + "\n")
weights_file.close()
