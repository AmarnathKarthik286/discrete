import matplotlib.pyplot as plt

# Function to generate geometric progression
def geometric_progression(first_term, common_ratio, n):
    terms = [first_term * common_ratio ** i for i in range(n)]
    return terms

# Parameters
x_0 = -3
r = -3
n = 8

# Generate geometric progression
progression = geometric_progression(x_0, r, n)

# Plotting the stem plot
plt.stem(range(n), progression, linefmt='b-', markerfmt='bo', basefmt='k-')

# Marking the seventh term with a different color
plt.stem(n - 2, progression[-2], linefmt='r-', markerfmt='ro', basefmt='k-')

# Adding labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot of Geometric Progression')

# Display the plot
plt.show()

