const chart = document.getElementById('alt-chart');

var embedOpt = {
    "mode": "vega-lite",
    "actions": false // https://github.com/vega/vega-embed#options
};
function showError(el, error){
    el.innerHTML = ('<div class="error" style="color:red;">'
                    + '<p>JavaScript Error: ' + error.message + '</p>'
                    + "<p>This usually means there's a typo in your chart specification. "
                    + "See the javascript console for the full traceback.</p>"
                    + '</div>');
    throw error;
}
vegaEmbed("#alt-chart", spec, embedOpt)
    .catch(error => showError(el, error));