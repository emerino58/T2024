import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.SLATE],
    title="TFM Dashboard"
)
server = app.server

app.layout = html.Div([
    html.Div([
        html.H2("🏟️ Panel de Aplicaciones", style={"textAlign": "center", "color": "white", "marginBottom": "40px"}),
        dbc.Row([
            dbc.Col(dbc.Button("🔍 Clasificación de Jugadores", href="/ml", size="lg", color="primary", className="w-100 mb-4")),
            dbc.Col(dbc.Button("🌟 Promesas Sub-23", href="/promesas", size="lg", color="success", className="w-100 mb-4")),
        ], justify="center", className="px-5"),
    ], style={
        "padding": "4rem",
        "backgroundColor": "#1e1e2f",
        "minHeight": "100vh"
    }),
    dash.page_container
])

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
