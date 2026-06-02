### Load Necessary Libraries
"""

# Import a Python package/module: import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Import a Python package/module: import numpy as np
import numpy as np
# Import a Python package/module: import pandas as pd
import pandas as pd

"""### Basic Graph"""

# Create x-values as a simple Python list
x = [0, 1, 2, 3, 4]

# Create y-values as a simple Python list (here: y = 2x)
y = [0, 2, 4, 6, 8]

# Create a new figure (canvas) with a specific size and resolution (dpi)
plt.figure(figsize=(8, 5), dpi=100)

# (Optional) Example showing full keyword-argument styling (kept commented out)
# plt.plot(x, y, label='2x', color='red', linewidth=2, marker='.',
#          linestyle='--', markersize=10, markeredgecolor='blue')

# Plot the first line using shorthand style:
# 'b^--' means: blue ('b') + triangle marker ('^') + dashed line ('--')
plt.plot(x, y, 'b^--', label='2x')

# Create a NumPy array from 0 up to 4.5 in steps of 0.5 (more points than x)
x2 = np.arange(0, 4.5, 0.5)

# Plot the first part of y = x^2 as a solid red line (slice first 6 points)
plt.plot(x2[:6], x2[:6] ** 2, 'r', label='X^2')

# Plot the remaining part of y = x^2 as a dashed red line (from index 5 onward)
plt.plot(x2[5:], x2[5:] ** 2, 'r--')

# Add a plot title with font settings (fontdict controls font properties)
plt.title(
    'Our First Graph!',
    fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20}
)

# Label the x-axis
plt.xlabel('X Axis')

# Label the y-axis
plt.ylabel('Y Axis')

# Set the tick marks (shown values) on the x-axis
plt.xticks([0, 1, 2, 3, 4])

# (Optional) Example of controlling y-axis ticks (kept commented out)
# plt.yticks([0, 2, 4, 6, 8, 10])

# Add a legend using the 'label=' values from plot() calls
plt.legend()

# Save the current figure to a PNG file (high dpi makes it sharper)
plt.savefig('mygraph.png', dpi=300)

# Display the figure on screen
plt.show()

"""### Bar Chart"""

# Category labels for the bars
labels = ['A', 'B', 'C']

# Heights for each bar category
values = [1, 4, 2]

# Create a new figure for the bar chart
plt.figure(figsize=(5, 3), dpi=100)

# Draw the bar chart and keep the BarContainer so we can style each bar
bars = plt.bar(labels, values)

# Define hatch patterns to visually distinguish bars
patterns = ['/', 'O', '*']

# Loop through each bar object and apply a hatch pattern
for bar in bars:
    # Pop removes and returns the first pattern each time (so each bar gets a different hatch)
    bar.set_hatch(patterns.pop(0))

# Save the bar chart as a PNG
plt.savefig('barchart.png', dpi=300)

# Display the bar chart
plt.show()

"""# Real World Examples
Download data from my Github (gas_prices.csv & fifa_data.csv)

### Line Graph
"""

# Read the gas price dataset from a CSV into a DataFrame
gas = pd.read_csv('gas_prices.csv')

# Create a new figure for the gas price line graph
plt.figure(figsize=(8, 5))

# Title with bold font weight and larger size
plt.title(
    'Gas Prices over Time (in USD)',
    fontdict={'fontweight': 'bold', 'fontsize': 18}
)

# Plot USA gas prices vs Year (blue dots with lines), and label it for legend
plt.plot(gas.Year, gas.USA, 'b.-', label='United States')

# Plot Canada gas prices vs Year (red dots with lines)
plt.plot(gas.Year, gas.Canada, 'r.-')

# Plot South Korea gas prices vs Year (green dots with lines)
plt.plot(gas.Year, gas['South Korea'], 'g.-')

# Plot Australia gas prices vs Year (yellow dots with lines)
plt.plot(gas.Year, gas.Australia, 'y.-')

# Another approach (kept commented out): loop through columns and plot selected countries
# countries_to_look_at = ['Australia', 'USA', 'Canada', 'South Korea']
# for country in gas:
#     if country in countries_to_look_at:
#         plt.plot(gas.Year, gas[country], marker='.')

# Show x-ticks every 3 years, and force-add 2011 at the end
plt.xticks(gas.Year[::3].tolist() + [2011])

# Label the x-axis
plt.xlabel('Year')

# Label the y-axis
plt.ylabel('US Dollars')

# Show legend (only USA line has a label in this version)
plt.legend()

# Save the gas price figure
plt.savefig('Gas_price_figure.png', dpi=300)

# Display the gas price line graph
plt.show()

"""### Load Fifa Data"""

# Read the FIFA dataset from a CSV into a DataFrame
fifa = pd.read_csv('fifa_data.csv')

# Display the first 5 rows (useful in notebooks; in scripts it prints a table if run interactively)
fifa.head(5)

"""### Histogram"""

# Define bin edges for the histogram (each interval becomes a bar)
bins = [40, 50, 60, 70, 80, 90, 100]

# Create a new figure for the histogram
plt.figure(figsize=(8, 5))

# Plot a histogram of the "Overall" column using the bins specified
plt.hist(fifa.Overall, bins=bins, color='#abcdef')

# Set x-axis tick marks to match the bin edges
plt.xticks(bins)

# Label y-axis as counts of players
plt.ylabel('Number of Players')

# Label x-axis as the rating scale
plt.xlabel('Skill Level')

# Add a title
plt.title('Distribution of Player Skills in FIFA 2018')

# Save the histogram
plt.savefig('histogram.png', dpi=300)

# Display the histogram
plt.show()

"""### Pie Chart"""

# Count how many rows have Preferred Foot == 'Left'
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]

# Count how many rows have Preferred Foot == 'Right'
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

# Create a new figure for the pie chart
plt.figure(figsize=(8, 5))

# Labels for the pie slices
labels = ['Left', 'Right']

# Slice colors
colors = ['#abcdef', '#aabbcc']

# Draw a pie chart; autopct formats percentages displayed on the chart
plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')

# Add a title
plt.title('Foot Preference of FIFA Players')

# Display the pie chart
plt.show()

"""### Pie Chart #2"""

# Create a new figure for the second pie chart
plt.figure(figsize=(8, 5), dpi=100)

# Apply a Matplotlib style preset (affects grid/spacing/colors, etc.)
plt.style.use('ggplot')

# Convert Weight strings like "150lbs" into integers.
# If the value is already numeric/non-string, keep it as-is.
fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]

# Count players in each weight range
light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa[fifa.Weight >= 200].count()[0]

# Put the counts into a list (slice sizes)
weights = [light, light_medium, medium, medium_heavy, heavy]

# Labels matching the weight ranges
label = ['under 125', '125-150', '150-175', '175-200', 'over 200']

# Explode separates slices outward (to emphasize certain groups)
explode = (.4, .2, 0, 0, .4)

# Add a title
plt.title('Weight of Professional Soccer Players (lbs)')

# Draw the pie chart:
# - pctdistance controls where percent text is placed (closer to center)
# - autopct formats percent labels
plt.pie(weights, labels=label, explode=explode, pctdistance=0.8, autopct='%.2f %%')

# Display the pie chart
plt.show()

"""### Box and Whiskers Chart"""

# Create a new figure for the box plot
plt.figure(figsize=(5, 8), dpi=100)

# Reset style back to default (so this plot isn't affected by ggplot style)
plt.style.use('default')

# Select the "Overall" ratings for specific clubs (each becomes a dataset in boxplot)
barcelona = fifa.loc[fifa.Club == "FC Barcelona"]['Overall']
madrid = fifa.loc[fifa.Club == "Real Madrid"]['Overall']
revs = fifa.loc[fifa.Club == "New England Revolution"]['Overall']

# Create the boxplot:
# - labels name each dataset
# - patch_artist=True allows filled boxes
# - medianprops styles the median line
bp = plt.boxplot(
    [barcelona, madrid, revs],
    labels=['FC Barcelona', 'Real Madrid', 'NE Revolution'],
    patch_artist=True,
    medianprops={'linewidth': 2}
)

# Add a title
plt.title('Professional Soccer Team Comparison')

# Label y-axis (the values being summarized)
plt.ylabel('FIFA Overall Rating')

# Loop through each box (rectangle) to style outline and fill colors
for box in bp['boxes']:
    # Set the outline color and width
    box.set(color='#4286f4', linewidth=2)
    # Set the fill color for the box
    box.set(facecolor='#e0e0e0')
    # (Optional) add hatch patterns if desired
    # box.set(hatch='/')

# Display the box plot
plt.show()

