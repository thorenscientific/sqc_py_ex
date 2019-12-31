import matplotlib.pyplot as plt

# Based on Matplotlib example:
# https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# There are only a few data points so we will enter them manualy. For larger
# data sets, it is better to read data in from a separate file (CSV, etc.)
labels = 'Init. Cutoff', 'Turning', 'Drilling', 'Assembly'
sizes = [80, 170, 73, 37]

fig1, ax1 = plt.subplots()
plt.title
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("Pie Chart for Data in Table 3.5")
plt.show()