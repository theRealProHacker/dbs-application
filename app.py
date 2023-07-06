import flask
import pandas as pd
import altair as alt

app = flask.Flask(__name__)

diebstähle = pd.read_csv("data/Fahrraddiebstahl.csv", encoding="ansi")
plr = pd.read_csv("data/lor_planungsraeume_2021.csv", encoding="ansi")
geo = alt.Data(url = "static/bezirksgrenzen.geojson", format=alt.DataFormat(property='features',type='json'))

@app.route("/")
def index():
    return flask.render_template("index.jinja")


@app.route("/presidents")
def presidents():
    presidents = pd.read_csv(
        "http://infovis.fh-potsdam.de/temp/us_presidents.csv",
        parse_dates=["start", "end"],
    )
    bars = (
        alt.Chart(presidents)
        .mark_bar(height=5)
        .encode(
            x=alt.X("start", axis=alt.Axis(tickCount=10)),
            x2="end",
            y=alt.Y("name", sort="x", axis=None),
            # code von https://github.com/altair-viz/altair/issues/268
            color=alt.Color(
                "party",
                scale=alt.Scale(
                    domain=["Democratic", "Republican"], range=["blue", "darkred"]
                ),
            ),
        )
    )

    labels = bars.mark_text(align="right", dx=-5).encode(text="name")
    chart = bars + labels
    return flask.render_template("chart.jinja", chart = chart.to_json())

@app.route("/map")
def map():
    chart = alt.Chart(geo).mark_geoshape(
        stroke = "white"
    ).encode(
        color=alt.Color("properties.Gemeinde_name:N", scale=alt.Scale(scheme="blues")),
        tooltip=['properties.Gemeinde_name:N']
    ).project(
        type='identity', reflectY=True
    )
    return flask.render_template("chart.jinja", chart = chart.to_json())

app.run(debug=True)