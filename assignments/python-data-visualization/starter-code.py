import os

sales_data = {
    'January': 1200,
    'February': 1500,
    'March': 1700,
    'April': 1600,
    'May': 1800,
    'June': 2100,
    'July': 2400,
    'August': 2200,
    'September': 2000,
    'October': 2300,
    'November': 2600,
    'December': 2800
}

months = list(sales_data.keys())
values = list(sales_data.values())

# Task 1: Matplotlib charts
try:
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 4))
    plt.plot(months, values, marker='o', label='Monthly Sales')
    plt.title('Monthly Sales (Matplotlib)')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig('sales_line.png')
    plt.close()

    plt.figure(figsize=(10, 4))
    plt.bar(months, values, color='skyblue')
    plt.title('Monthly Sales Bar Chart (Matplotlib)')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sales_bar.png')
    plt.close()

    print('Matplotlib charts saved as sales_line.png and sales_bar.png')
except ImportError:
    print('matplotlib is not installed. Run pip install matplotlib')

# Task 2: Plotly interactive chart
try:
    import plotly.graph_objects as go

    fig = go.Figure(data=[go.Bar(x=months, y=values, name='Monthly Sales')])
    fig.update_layout(title='Monthly Sales (Plotly)', xaxis_title='Month', yaxis_title='Sales')
    fig.write_html('sales_interactive.html')
    print('Plotly interactive chart saved as sales_interactive.html')
except ImportError:
    print('plotly is not installed. Run pip install plotly')

# Task 3: Summary statistics

total_sales = sum(values)
avg_sales = total_sales / len(values)
max_month = months[values.index(max(values))]
min_month = months[values.index(min(values))]

print('\nSales Summary:')
print(f'  Total sales: ${total_sales}')
print(f'  Average monthly sales: ${avg_sales:.2f}')
print(f'  Highest month: {max_month} (${max(values)})')
print(f'  Lowest month: {min_month} (${min(values)})')
