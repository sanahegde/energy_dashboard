
# **Comprehensive Energy Dashboard**

An interactive data visualization dashboard created using **Dash** and **Plotly** to analyze global energy data.

---

## **1. Prerequisites**

Ensure the following are installed on your system:

- Python (version 3.8 to 3.11 is recommended)  
- Pip (Python package manager)

---

## **2. Clone the Repository**

1. Open your terminal or command prompt.  
2. Clone this repository to your local system:

   ```bash
   git clone https://github.com/sanahegde/energy_dashboard.git

## **3. Create Virtual environment **
Navigate to the project directory:
bash

cd energy_dashboard
Set Up Virtual Environment (Optional but Recommended)
Create a virtual environment:
bash

python -m venv venv
Activate the virtual environment:
On Windows:
bash

venv\Scripts\activate
On macOS/Linux:
bash
source venv/bin/activate

## **4. Install the necessary dependencies**
Install Dependencies
Install the required Python packages:
bash

pip install -r requirements.txt
Add the Dataset
Ensure the dataset cleaned_data.csv is in the data/ directory.
Path: data/cleaned_data.csv
If not, place the dataset in the correct location.
Run the Application
Start the application:
bash

python app/app.py
Open your web browser and navigate to: http://127.0.0.1:8050



## **5. Features of dashboard: **
1. Interactive dropdown to select countries.
Visualizations:
1.Line Chart: Energy consumption vs renewables share.
2.Scatter Plot: Energy per capita vs renewables share.
3.Heatmap: Numeric data correlations.
4.Bar Chart: Fossil fuel consumption.
5.Pie Chart: Average renewables share.
6.Histogram: Population distribution.
5.Fully responsive and fits within an A4 layout.

Troubleshooting
Dependency Issues: If any library is missing, install it manually using pip:
bash

pip install <library_name>
Dataset Path: Ensure the cleaned_data.csv file is in the correct data/ folder.
Port Issues: If port 8050 is busy, specify a different port:
bash

python app/app.py --port 8060 

## **Adding a screenshot of the visualization here**
![Screenshot 2024-12-15 192838](https://github.com/user-attachments/assets/15661fda-8e41-4ff6-8086-2fea24f621e9)


