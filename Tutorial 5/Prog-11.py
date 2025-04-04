import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales_a = [150, 200, 250, 300, 280]
sales_b = [100, 180, 220, 260, 310]
plt.plot(months, sales_a, label='Product A', color='blue', marker='o')
plt.plot(months, sales_b, label='Product B', color='green', marker='s')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales of Product A and B')
plt.legend()
plt.show()
