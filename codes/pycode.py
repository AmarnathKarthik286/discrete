import matplotlib.pyplot as plt

# Read data from the file
with open("coordinates.txt", "r") as file:
    lines = file.readlines()
    data = [tuple(map(float, line.split())) for line in lines]

# Separate x and y data
x_values, y_values = zip(*data)

# Create a stem plot
plt.stem(x_values, y_values, basefmt="b-", linefmt="r-", markerfmt="ro")

# Customize the plot
plt.title('Stem Plot: Geometric Progression')
plt.xlabel('Term (n)')
plt.ylabel('Value')

# Show the plot
plt.show()

plt.savefig("pycode.png")
