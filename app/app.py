import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Loading the Data
df = pd.read_csv("../data/cleaned_data.csv")

# Preprocessing Data: Adding 'World' data as the average of all countries
numeric_columns = df.select_dtypes(include='number').columns.tolist()
world_avg = df.groupby("year")[[col for col in numeric_columns if col != "year"]].mean().reset_index()
world_avg["country"] = "World"
df = pd.concat([df, world_avg], ignore_index=True)

# Initializing the Dash App
app = dash.Dash(__name__)
server = app.server  # For deployment

# Dropdown Options for country
countries = df['country'].unique()

# App Layout
app.layout = html.Div([
    html.Div(style={
        'background-color': '#f9f9f9',
        'width': '100%',
        'max-width': '2012px',  
        'height': '96%',  
        'margin': '0 auto',
        'padding': '10px',
        'padding-bottom': '0',
        'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)',
        'border-radius': '8px'
    }, children=[
        html.H1("Comprehensive Energy Dashboard", style={
            'textAlign': 'center',
            'font-family': 'Arial',
            'font-size': '24px',
            'color': '#2c3e50',
            'margin-bottom': '10px'
        }),


        html.Div([
            html.Label("Select Country:", style={
                'font-weight': 'bold',
                'font-size': '16px',
                'margin-right': '10px',
                'color': '#34495e',
                'display': 'inline-block',
                'vertical-align': 'middle'
            }),
            dcc.Dropdown(
                id="country-dropdown",
                options=[{"label": country, "value": country} for country in countries],
                value=["World"],
                multi=True,
                placeholder="Select countries...",
                searchable=False,
                style={
                    'width': '40%',
                    'font-size': '12px',
                    'border-radius': '5px',
                    'display': 'inline-block',
                    'vertical-align': 'middle'
                }
            )
        ], style={'textAlign': 'center', 'margin-bottom': '20px'}),

        html.Div([
            html.Div([dcc.Graph(id="line-chart", style={'height': '400px'})],
                     style={'width': '32%', 'display': 'inline-block', 'padding': '10px'}),
            html.Div([dcc.Graph(id="scatter-plot", style={'height': '400px'})],
                     style={'width': '32%', 'display': 'inline-block', 'padding': '10px'}),
            html.Div([dcc.Graph(id="heatmap", style={'height': '400px'})],
                     style={'width': '32%', 'display': 'inline-block', 'padding': '10px'}),
        ], style={'display': 'flex', 'justify-content': 'space-between', 'margin-bottom': '10px'}),

        html.Div([
            html.Div([dcc.Graph(id="bar-chart", style={'height': '400px'})],
                     style={'width': '32%', 'display': 'inline-block', 'padding': '10px'}),
            html.Div([dcc.Graph(id="pie-chart", style={'height': '400px'})],
                     style={'width': '32%', 'display': 'inline-block', 'padding': '10px'}),
            html.Div([dcc.Graph(id="histogram", style={'height': '400px'})],
                     style={'width': '32%', 'display': 'inline-block', 'padding': '10px'}),
        ], style={'display': 'flex', 'justify-content': 'space-between'})
    ])
], style={
    'background-color': '#ecf0f1',
    'margin': '0',
    'padding': '0',
    'box-sizing': 'border-box',
    'display': 'flex',
    'justify-content': 'center',
    'align-items': 'center',
    'height': '100vh'
})


@app.callback(
    [
        Output("line-chart", "figure"),
        Output("scatter-plot", "figure"),
        Output("heatmap", "figure"),
        Output("bar-chart", "figure"),
        Output("pie-chart", "figure"),
        Output("histogram", "figure")
    ],
    [Input("country-dropdown", "value")]
)
def update_graphs(selected_countries):
    filtered_df = df[df['country'].isin(selected_countries)]

    # Line Chart
    line_chart = px.line(filtered_df, x="year", y=["primary_energy_consumption", "renewables_share_energy"],
                         color="country", title="Energy Consumption and Renewables Share",
                         template="plotly_white")
    line_chart.update_traces(line=dict(width=2.5))
    line_chart.update_layout(font=dict(size=12))

    # Scatter Plot
    scatter_plot = px.scatter(filtered_df, x="renewables_share_energy", y="energy_per_capita",
                              color="country", title="Energy Per Capita vs Renewables Share",
                              template="plotly_white")
    scatter_plot.update_traces(marker=dict(size=10))  # Enlarged markers
    scatter_plot.update_layout(font=dict(size=12))

    # Heatmap
    heatmap_data = filtered_df.select_dtypes(include='number').corr()
    heatmap = px.imshow(heatmap_data, color_continuous_scale='Viridis', title="Correlation Heatmap")
    heatmap.update_layout(font=dict(size=10))

    # Bar Chart
    bar_chart = px.bar(filtered_df, x="year", y="fossil_fuel_consumption", color="country",
                       title="Fossil Fuel Consumption Over Time", template="plotly_white")
    bar_chart.update_layout(font=dict(size=12))

    # Pie Chart
    renewables_avg = filtered_df.groupby("country")["renewables_share_energy"].mean().reset_index()
    pie_chart = px.pie(renewables_avg, names="country", values="renewables_share_energy",
                       title="Average Renewables Share", template="plotly_white")
    pie_chart.update_traces(textfont_size=12)

    # Histogram
    histogram = px.histogram(filtered_df, x="population", nbins=20, title="Population Distribution",
                             template="plotly_white")
    histogram.update_layout(font=dict(size=12))

    return line_chart, scatter_plot, heatmap, bar_chart, pie_chart, histogram


if __name__ == "__main__":
    app.run_server(debug=True)
