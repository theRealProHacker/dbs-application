import flask
import pandas as pd
import altair as alt
import db

app = flask.Flask(__name__)

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
    return flask.render_template("chart.jinja", chart = chart.to_json(), title="US-Präsidenten seit 1945")

@app.route("/map")
def map():
    accidents = db.accidents_by_district()
    chart = alt.Chart(geo).mark_geoshape(
        stroke = "white"
    ).encode(
        color=alt.Color("Diebstähle:Q", scale=alt.Scale(scheme="lightgreyred")),
        tooltip=['Bezirk:N', 'Diebstähle:Q']
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(accidents, 'id', list(accidents.columns))
    ).properties(
        width=500,
        height=400
    ).project(
        type='identity', reflectY=True
    )
    return flask.render_template("chart.jinja", chart = chart.to_json(), title="Diebstähle nach Bezirk")

@app.route("/bar")
def bar():
    accidents = db.accidents_by_district()
    chart = alt.Chart(geo).mark_bar().encode(
        x=alt.X("Bezirk:N"),
        y=alt.Y("Diebstähle:Q"),
        tooltip=['Bezirk:N', 'Diebstähle:Q']
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(accidents, 'id', list(accidents.columns))
    ).properties(
        width=500,
        height=400
    )
    return flask.render_template("chart.jinja", chart = chart.to_json(), title="Diebstähle nach Bezirk")

@app.route("/table")
def table():
    df = db.all_accidents()
    table = df.to_html()
    return flask.render_template(
        "table.jinja",
        table=table,
    )

app.run(debug=True)
