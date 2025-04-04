import pandas as pd
import matplotlib.pyplot as plt
data = {
    'nth_number': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'facecream': [250, 263, 270, 300, 310, 350, 380, 400, 420, 450, 470, 490],
    'facewash': [150, 160, 180, 200, 210, 220, 230, 240, 250, 260, 270, 280],
    'toothpaste': [520, 510, 495, 480, 500, 520, 530, 550, 560, 580, 600, 620],
    'bathingsoap': [800, 810, 820, 830, 840, 860, 870, 880, 890, 900, 910, 920],
    'shampoo': [200, 220, 210, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'moisturizer': [300, 310, 320, 330, 340, 360, 370, 380, 390, 400, 410, 420]}
df = pd.DataFrame(data)
print("1) Toothpaste sales data for each month shown using scatter plot:")
plt.scatter(df['nth_number'], df['toothpaste'], color='green')
plt.title('Toothpaste Sales per Month')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.grid(True)
plt.show()
print("2) Face Cream and Face Wash Sales Data shown using bar chart:")
labels = df['nth_number']
x = range(len(labels))
bar_width = 0.4
plt.bar(x, df['facecream'], width=bar_width, label='Face Cream', color='red')
plt.bar([p + bar_width for p in x], df['facewash'], width=bar_width, label='Face Wash', color='green')
plt.xticks([p + bar_width/2 for p in x], labels)
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Face Cream and Face Wash Sales')
plt.legend()
plt.show()
print("3) Total yearly sales of each product shown using pie chart:")
total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=140)
plt.title('Total Sales of Each Product (Yearly)')
plt.axis('equal')
plt.show()
