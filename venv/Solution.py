import csv
import matplotlib.pyplot as plt;
import numpy as np
import matplotlib.pyplot as plt

ratesDictionnary = {} #Dictionnary that holds all the interest rates by purpose
averageRateDictionnary = {} #Dictionnary that holds the average interest rates by purpose

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    purposeIndex = -1
    int_rateIndex = -1
    for row in csv_reader:
        # Find the index of the purpose and the int_rate within each row by using the titles' row
        if line_count == 0:
            line_count += 1
            purposeIndex = row.index("purpose")
            int_rateIndex = row.index("int_rate")
        else:
            # If there is an entry with the current purpose, add the current interest to the existing list
            if row[purposeIndex] in ratesDictionnary:
                ratesDictionnary[row[purposeIndex]].append(float(row[int_rateIndex]))
            # Create a new list for a new purpose with the current interest rate
            else:
                ratesDictionnary[row[purposeIndex]] = [float(row[int_rateIndex])]

            line_count += 1

# Set the average interest rate for all the purposes
for key, val in ratesDictionnary.items():
    averageRateDictionnary[key] = sum(val) / float(len(val))

plt.rcdefaults()
objects = averageRateDictionnary.keys()
# Generate an array with the x coordinates of every bar
xPositions = np.arange(len(objects))
# Use the average interests as the height of every bar
averageInterests = averageRateDictionnary.values()
plt.bar(xPositions, averageInterests, align='center')
# Rotate the xticks by 90 degrees to avoid overlaps between titles
plt.xticks(xPositions, objects, rotation = 90)
# Set titles for the axes and the plot
plt.ylabel('Average Interest Rate')
plt.xlabel('Loan Purpose')
plt.title('Average Interest Rate vs Loan Purpose')
# Display the plot
plt.show()