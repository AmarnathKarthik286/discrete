import matplotlib.pyplot as plt

# Function to generate the terms of the geometric progression
def geometric_progression(first_term, common_ratio, num_terms):
    terms = [first_term * common_ratio**i for i in range(num_terms)]
    return terms

# Parameters for the geometric progression
first_term = -3
common_ratio = -3
num_terms = 8

# Generate the terms
terms = geometric_progression(first_term, common_ratio, num_terms)

# Create a stem plot
plt.stem(range(num_terms), terms, basefmt='b-', linefmt='r-', markerfmt='ro')

# Set labels and title
plt.xlabel('n')
plt.ylabel('x(n) ')
plt.title('Stem Plot of Geometric Progression')
# Show the plot
plt.show()
plt.savefig("stemplotfinal.jpeg")

