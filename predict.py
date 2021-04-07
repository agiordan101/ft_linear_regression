weights_file = open("weights.txt", "r")
weights = weights_file.read().split('\n')[:-1]
print("Weights :", weights)

mileage = float(input("Enter a mileage : "))
print("The model predict a price of", str(float(weights[0]) * mileage + float(weights[1])), "for cars with mileage of", mileage)

weights_file.close()