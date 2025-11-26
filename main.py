# Basic Python Project - Hello World
# Biomedical Engineering related
# Alberto Rodríguez - @albertorgb21

import random
import matplotlib.pyplot as plt

# Generate a list consisting of 10 random numbers between 60 and 120
# This will be the BPM of an imaginary patient
dataset = [random.randint(60, 120) for i in range(10)]

# Calculate the average BPM of the dataset
avg = sum(dataset) / len(dataset)
# No need to print the average since it is present in the graph
# print("Average BPM: ", avg)

# Show the evolution of the BPM in a simple graph
plt.figure(figsize=(10, 6))
plt.plot(dataset, marker='o', linestyle='-', linewidth=2, markersize=8, label='BPM') # Plotting whole dataset

# Mark tachycardia measurements (BPM > 100)
tachycardia_indices = [i for i, bpm in enumerate(dataset) if bpm > 100] # Mark those measurements above 100BPM (tachycardia)
tachycardia_values = [dataset[i] for i in tachycardia_indices]          # Save the values in another variable
# Mark tachycardia values with a red circle around them
plt.scatter(tachycardia_indices, tachycardia_values, color='red', s=200, 
            facecolors='none', edgecolors='red', linewidths=2, label='Tachycardia (>100)', zorder=5)

plt.axhline(y=avg, color='green', linestyle='--', label=f'Average: {avg:.1f}')      # Draw average line
plt.axhline(y=100, color='orange', linestyle=':', label='Tachycardia threshold')    # Draw tachycardia threshold

# Axis labelling and title
plt.xlabel('Measurement')
plt.ylabel('BPM')
plt.title('BPM Evolution')
# Grid on, Legend on, Show graph
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

