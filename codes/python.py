import matplotlib.pyplot as plt

# Function to generate geometric progression
def geometric_progression(first_term, common_ratio, n):
    terms = [first_term * common_ratio ** i for i in range(n)]
    return terms

# Parameters
first_term = -3
common_ratio = -3
n_terms = 8

# Generate geometric progression
progression = geometric_progression(first_term, common_ratio, n_terms)

# Plotting the stem plot
plt.stem(range(n_terms), progression, linefmt='b-', markerfmt='bo', basefmt='k-')

# Marking the seventh term with a different color
plt.stem(n_terms - 2, progression[-2], linefmt='r-', markerfmt='ro', basefmt='k-')

# Adding labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of Geometric Progression')

# Display the plot
plt.show()

