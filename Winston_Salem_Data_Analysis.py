import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Read CSV file 
data = pd.read_csv('student_scores.csv')

# Strip leading/trailing whitespace from column names
data.columns = data.columns.str.strip()

# Calculate minimum and maximum proficiency for black students
min_black = data['Pct Prof (Black Students)'].min()
max_black = data['Pct Prof (Black Students)'].max()

# Calculate minimum and maximum proficiency for white students
min_white = data['Pct Prof (White Students)'].min()
max_white = data['Pct Prof (White Students)'].max()

# Calculate minimum and maximum proficiency for all groups combined
min_combined = data['Pct Prof (All groups Combined)'].min()
max_combined = data['Pct Prof (All groups Combined)'].max()

# Calculate mean and median proficiency for black students
mean_black = data['Pct Prof (Black Students)'].mean()
median_black = data['Pct Prof (Black Students)'].median()

# Calculate mean and median proficiency for white students
mean_white = data['Pct Prof (White Students)'].mean()
median_white = data['Pct Prof (White Students)'].median()

# Calculate mean and median proficiency for all groups combined
mean_combined = data['Pct Prof (All groups Combined)'].mean()
median_combined = data['Pct Prof (All groups Combined)'].median()

# Define font size for labels
label_font_size = 14

# Set font size globally for all plots
plt.rc('font', size=label_font_size)

# Define colors
blue_color = '#00a4c7'  # Blue
gray_color = '#c0c0c0'  # Gray

# Define groups and corresponding scores for each metric
groups = ['Black Students', 'White Students', 'All Groups Combined']
metrics = ['Maximum', 'Mean', 'Median']
scores = [
    [max_black, max_white, max_combined],
    [mean_black, mean_white, mean_combined],
    [median_black, median_white, median_combined]
]

# Define colors for bars (gray for mean, blue for median)
colors = [blue_color, gray_color, blue_color]

# Create a single figure with three subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # Adjust figure size

# Create bar charts for each metric in the subplots
for i in range(3):
    axs[i].bar(groups, scores[i], color=colors[i])
    axs[i].set_xlabel('Student Group')
    axs[i].set_ylabel('Proficiency Values')
    axs[i].set_title(f'{metrics[i]} Proficiency Values')
    axs[i].set_ylim(0, 100)  # Set y-axis limit to 0-100
    axs[i].tick_params(axis='x', rotation=15)  # Adjust label rotation

    # Display percentage values on top of each bar
    for bar in axs[i].patches:
        height = bar.get_height()
        axs[i].annotate(f'{height:.1f}%', 
                        xy=(bar.get_x() + bar.get_width() / 2, height), 
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

# Adjust margins
plt.subplots_adjust(wspace=0.3)  # Adjust the width between subplots

# Save the combined chart as an image
plt.savefig('Combined_Proficiency_Scores.png', bbox_inches='tight')

# Show the combined chart
plt.show()

# Schools below average for both black and white students
# Calculate the overall average proficiency for all groups combined
overall_mean = data['Pct Prof (All groups Combined)'].mean()

# Find schools where both black and white students have proficiency scores below the overall average
below_average_schools = data[(data['Pct Prof (Black Students)'] < overall_mean) & (data['Pct Prof (White Students)'] < overall_mean)]

print("\nSchools Below Average for Both Black and White Students:")
print(tabulate(below_average_schools[['School Code', 'School Name', 'Pct Prof (Black Students)', 'Pct Prof (White Students)']], headers='keys', tablefmt='psql'))

# Schools with largest gap
# Calculate the difference in proficiency scores between black and white students
data['Score Difference'] = data['Pct Prof (White Students)'] - data['Pct Prof (Black Students)']

# Find schools with the largest gaps between black and white student scores
largest_gaps_schools = data.sort_values(by='Score Difference', ascending=False).head()

print("\nSchools with Largest Gaps Between Black and White Student Scores:")
print(tabulate(largest_gaps_schools[['School Code', 'School Name', 'Score Difference']], headers='keys', tablefmt='psql'))

# Schools with insignificant gaps
# Find schools where the gap between black and white student scores is small (e.g., less than a certain threshold)
threshold = 5  # Adjust the threshold as per your definition of an insignificant gap
insignificant_gap_schools = data[abs(data['Score Difference']) < threshold]

print("\nSchools with Insignificant Gap in Proficiency Scores:")
print(tabulate(insignificant_gap_schools[['School Code', 'School Name', 'Pct Prof (Black Students)', 'Pct Prof (White Students)']], headers='keys', tablefmt='psql'))

# Schools where black students perform better than white students
# Find schools where black students have higher proficiency scores than white students
black_better_schools = data[data['Pct Prof (Black Students)'] > data['Pct Prof (White Students)']]

print("\nSchools Where Black Students Perform Better Than White Students:")
print(tabulate(black_better_schools[['School Code', 'School Name', 'Pct Prof (Black Students)', 'Pct Prof (White Students)']], headers='keys', tablefmt='psql'))
