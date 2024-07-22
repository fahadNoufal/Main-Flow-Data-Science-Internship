import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 56, 78, 12],
    'Trend': [15, 25, 35, 45, 55]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))
plt.bar(df['Category'], df['Values'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Bar Chart of Values by Category')
plt.legend(['Values'])
plt.show()
# line chart
plt.figure(figsize=(10, 5))
plt.plot(df['Category'], df['Trend'], marker='o', linestyle='-', color='orange')
plt.xlabel('Category')
plt.ylabel('Trend')
plt.title('Line Chart of Trend by Category')
plt.legend(['Trend'])
plt.show()