python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
data_url = "https://opendata.abudhabi/data/saifi-2013-2025.csv"
saifi_data = pd.read_csv(data_url)

# Display the first few rows of the dataset
print(saifi_data.head())

# Convert 'Year' column to datetime
def preprocess_data(data):
    data['Year'] = pd.to_datetime(data['Year'], format='%Y')
    return data

# Plotting
saifi_data = preprocess_data(saifi_data)
plt.figure(figsize=(10, 6))
sns.lineplot(data=saifi_data, x='Year', y='SAIFI')
plt.title('SAIFI Trend Over Years (2013-2025)')
plt.xlabel('Year')
plt.ylabel('SAIFI Value')
plt.grid(True)
plt.savefig('saifi_trend.png')
plt.show()

# Interactive Plot
fig = px.line(saifi_data, x='Year', y='SAIFI', title='Interactive SAIFI Data Visualization')
fig.show()

# Export filtered data
def export_filtered_data(data, start_year, end_year):
    filtered_data = data[(data['Year'] >= str(start_year)) & (data['Year'] <= str(end_year))]
    filtered_data.to_csv(f'saifi_filtered_{start_year}_{end_year}.csv', index=False)
    print(f"Filtered data for years {start_year}-{end_year} saved as saifi_filtered_{start_year}_{end_year}.csv")

# Example of exporting data between 2015 and 2020
export_filtered_data(saifi_data, 2015, 2020)
