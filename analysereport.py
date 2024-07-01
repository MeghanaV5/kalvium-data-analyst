import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the election results data
df = pd.read_csv('all_table_data.csv')

# Ensure the 'reports' folder exists
import os
if not os.path.exists('reports'):
    os.makedirs('reports')

# Total Seats Won by Each Party
party_seats = df['Party'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=party_seats.values, y=party_seats.index, palette='viridis')
plt.title('Total Seats Won by Each Party')
plt.xlabel('Number of Seats')
plt.ylabel('Party')
plt.savefig('reports/total_seats_won.png')
plt.close()