from flask import Flask, render_template
import main as sales

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template(
        'index.html',
        title = "Dashboard",
        subtitle = "Sales Reporting",
        year = 'Jan - Dec 2018',
        total_sales=sales.total_sales,
        average_sales = sales.average_yearly,
        highest_month = sales.highest_month,
        lowest_month = sales.lowest_month,
        highest_value = sales.highest_sales_val,
        lowest_value = sales.lowest_sales_val
    )

app.run(debug=True)

