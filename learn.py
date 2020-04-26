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
lr = 1

print("Km :", km)
print("Price : ", price)
print("Weights : ", weights[0], " / ", weights[1])
print("Learning rate : ", lr)


#Compute new weights
for j in range(0, 10):
	errorW0 = 0
	errorW1 = 0
	for i in range(len(km)):
		errorW0 += (predict(km[i]) - price[i]) * km[i]
		errorW1 += (predict(km[i]) - price[i]) * 1
	errorW0 /= len(km)
	errorW1 /= len(km)

	print("Errors : ", errorW0, " / ", errorW1)

	weights[0] = weights[0] - lr * errorW0
	weights[1] = weights[1] - lr * errorW1

	print("New weights : ", weights[0], " / ", weights[1])

#Write new weights
"""
weights_file = open("weights", "w")
weights_file.write(str(w0) + "\n")
weights_file.write(str(w1) + "\n")
weights_file.close()
"""
