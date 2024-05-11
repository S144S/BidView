import dash
import dash_bootstrap_components as dbc
from dash import html

# Initialize Dash app with the Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define layout with Bootstrap utility classes
app.layout = html.Div([
    html.H1("Hello, World!", className="mt-5 text-center text-primary"),
    dbc.Button("Click Me", color="danger", className="mt-3 text-center"),
], className="d-flex")

if __name__ == "__main__":
    app.run_server(debug=True)
