import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample customer interaction data
data = pd.DataFrame({
    'customer_id': [1, 2, 3, 1, 2, 3],
    'ad_action': ['view', 'click', 'view', 'purchase', 'purchase', 'click']
})

# Define states
states = ['view', 'click', 'purchase']
transition_matrix = pd.DataFrame(np.zeros((3,3)), index=states, columns=states)

# Calculate transition probabilities
for i in range(len(data) - 1):
    current_state = data.loc[i, 'ad_action']
    next_state = data.loc[i + 1, 'ad_action']
    transition_matrix.loc[current_state, next_state] += 1

transition_matrix = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)
print("Transition Matrix:\n", transition_matrix)

# Mock Accuracy Plot
iterations = [1, 2, 3, 4, 5, 6]
accuracy = [72, 76, 79, 82, 84, 86]
plt.plot(iterations, accuracy, marker='o')
plt.title('Model Accuracy Over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Accuracy (%)')
plt.ylim(70, 90)
plt.grid(True)
plt.show()

# Mock API Efficiency Plot
queries = ['Query 1', 'Query 2']
rest_queries = [120, 100]
graphql_queries = [80, 60]
x = np.arange(len(queries))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, rest_queries, width, label='REST')
rects2 = ax.bar(x + width/2, graphql_queries, width, label='GraphQL')
ax.set_ylabel('Number of Queries')
ax.set_title('REST vs GraphQL Query Efficiency')
ax.set_xticks(x)
ax.set_xticklabels(queries)
ax.legend()
plt.show()