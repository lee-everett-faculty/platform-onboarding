import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash

import mlflow
import faculty_models


app = dash.Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1(children="Predict Sales"),
        html.Label("Spent on TV ads: "),
        dcc.Input(id="input-div"),
        html.Div(id="output-div", children=[]),
    ]
)

# CHANGE ME: Copy-paste the code snippet from the model registry below.
#
# Something like:
#   model = faculty_models.load_mlmodel(
#         project_id="YOUR PROJECT ID",
#         model_id="YOUR MODEL ID"
#   )


@app.callback(
    Output(component_id="output-div", component_property="children"),
    [Input(component_id="input-div", component_property="value")],
)
def update_output(input_value):
    if input_value is None or not input_value:
        return ["Missing input"]
    try:
        spent_on_tv = int(input_value)
    except ValueError:
        return ["Invalid input"]
    model_input = [[spent_on_tv]]
    [predicted_sales] = model.predict(model_input)
    predicted_sales
    return [f"Predicted sales: {predicted_sales} $"]


if __name__ == "__main__":
    app.run_server(host="127.0.0.1", port=8888, debug=True)
