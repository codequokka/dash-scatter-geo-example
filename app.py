# You can run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import sys
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import data

if len(sys.argv) >= 2:
    debug = True
else:
    debug = False

tabs_styles = {"height": "44px"}

tab_style = {
    "borderBottom": "1px solid #d6d6d6",
    "padding": "6px",
    "fontWeight": "bold",
}

tab_selected_style = {
    "borderTop": "1px solid #d6d6d6",
    "borderBottom": "1px solid #d6d6d6",
    "backgroundColor": "#119DFF",
    "color": "white",
    "padding": "6px",
}

colors = {"background": "#111111", "text": "#7FDBFF"}


pop_data = data.get_pop_data(
    population_src_file="./data/WPP2019_TotalPopulationBySex.csv",
    locations_src_file="./data/WPP2019_F01_LOCATIONS.XLSX",
    debug=debug,
)

app = dash.Dash(__name__)

app.layout = html.Div(
    dcc.Tabs(
        id="tabs",
        style=tabs_styles,
        children=[
            dcc.Tab(
                label="Dashboard-1",
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div(
                        html.H1(
                            "World Population Prospects", style={"textAlign": "center"}
                        )
                    ),
                    dcc.Dropdown(
                        id="scatter-geo-dropdown-for-projection",
                        options=[
                            {"label": i, "value": i}
                            for i in [
                                "equirectangular",
                                "mercator",
                                "orthographic",
                                "natural earth",
                                "kavrayskiy7",
                                "miller",
                                "robinson",
                                "eckert4",
                                "azimuthal equal area",
                                "azimuthal equidistant",
                                "conic equal area",
                                "conic conformal",
                                "conic equidistant",
                                "gnomonic",
                                "stereographic",
                                "mollweide",
                                "hammer",
                                "transverse mercator",
                                "albers usa",
                                "winkel tripel",
                                "aitoff",
                                "sinusoidal",
                            ]
                        ],
                        value="orthographic",
                    ),
                    dcc.RadioItems(
                        id="scatter-geo-radioitems-for-poptype",
                        options=[
                            {"label": i, "value": i}
                            for i in pop_data["PopType"].unique()
                        ],
                        value="PopTotal",
                    ),
                    dcc.Graph(
                        id="scatter-geo",
                    ),
                ],
            ),
            dcc.Tab(
                label="Dashboard-2",
                style=tab_style,
                selected_style=tab_selected_style,
                children=[
                    html.Div(
                        html.H1(
                            "World Population Prospects", style={"textAlign": "center"}
                        ),
                    ),
                    dash_table.DataTable(
                        id="dash-table",
                        columns=[
                            {"name": i, "id": j}
                            for i, j in zip(
                                pop_data,
                                pop_data.columns,
                            )
                        ],
                        data=pop_data.to_dict("records"),
                        page_size=30,
                        filter_action="native",
                        sort_action="native",
                    ),
                ],
            ),
        ],
    )
)


@app.callback(
    dash.dependencies.Output("scatter-geo", "figure"),
    [
        dash.dependencies.Input("scatter-geo-radioitems-for-poptype", "value"),
        dash.dependencies.Input("scatter-geo-dropdown-for-projection", "value"),
    ],
)
def update_graph(pop_type, projection):
    pop_data_filterd = pop_data.query("PopType == @pop_type")
    figure = px.scatter_geo(
        pop_data_filterd,
        locations="Location",
        locationmode="country names",
        color="GeoRegName",
        hover_name="Location",
        size="Population",
        opacity=0.5,
        animation_frame="Time",
        projection=projection,
    )

    return figure


if __name__ == "__main__":
    if not debug:
        app.run_server(host="0.0.0.0", port=8050)
    else:
        app.run_server(host="0.0.0.0", port=8050, debug=True)
