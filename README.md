markdown
# Interactive Visualization and Analysis of SAIFI Data

## Overview
This project provides an interactive dashboard to visualize and analyze the System Average Interruption Frequency Index (SAIFI) data from 2013 to 2025. The SAIFI dataset measures the average number of power interruptions experienced by customers and is a critical indicator of power supply reliability.

## Features
- **Interactive Visualizations:** View SAIFI trends using line graphs and other visual tools.
- **Data Filtering:** Filter data based on specific years or regions.
- **Data Export:** Download filtered data in CSV format.
- **Informative Metadata:** Detailed metadata and contextual information to aid understanding.

## Prerequisites
- Python 3.7 or above.
- Required Python libraries: `pandas`, `matplotlib`, `seaborn`, `plotly`.

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/example/saifi-visualization.git
   cd saifi-visualization
   
2. Install the required libraries:
   bash
   pip install -r requirements.txt
   

## Usage
1. Run the script:
   bash
   python saifi_analysis.py
   
2. View the generated visualizations in your browser.
3. To export filtered data:
   - Open `saifi_analysis.py`.
   - Modify the `export_filtered_data` function parameters with your desired year range.
   - Run the script to generate and save the filtered dataset in CSV format.

## Example
Here is an example usage of the script:
python
# Filter and export data between 2015 and 2020
export_filtered_data(saifi_data, 2015, 2020)

The resulting file, `saifi_filtered_2015_2020.csv`, will be saved in the project directory.

## License
This project is licensed under the Open Data License. See [terms of use](https://opendata.abudhabi/en/terms-of-use) for more details.

## Support
For any questions or support, please contact: [support@energy.abudhabi.ae](mailto:support@energy.abudhabi.ae).
