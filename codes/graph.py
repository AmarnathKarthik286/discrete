import matplotlib.pyplot as plt

def geometric_progression(n, first_term, common_ratio):
    terms = [first_term * (common_ratio ** i) for i in range(n)]
    return terms

# Parameters
n_terms = 10  # Number of terms in the progression
first_term = -3
common_ratio = -3

# Generate terms
terms = geometric_progression(n_terms, first_term, common_ratio)

# Plotting
plt.plot(range(1, n_terms + 1), terms, marker='o', linestyle='-', color='b')
plt.title('Geometric Progression: First Term = -3, Common Ratio = -3')
plt.xlabel('Term')
plt.ylabel('Value')
plt.grid(True)
plt.show()

