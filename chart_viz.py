import seaborn as sns
import main as sales_data
import matplotlib.pyplot as plt


x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
y = sales_data.sales


ax = sns.barplot(x, y)
ax.set(xlabel="Months", ylabel="Sales (£) ")

ax.figure.savefig("static/sales_chart.png")
plt.show()
