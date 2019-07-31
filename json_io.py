# Use flask as the API
from flask import Flask

# Configure flask
app = Flask(__name__)
app.config.update(DEBUG=True)


# End point for the url 
@app.route("/output")


# Using inner HTML as a form of json to prouduce HTML and intenal javascript if needed
# Currently dumps the return statement into the body
def output():


    # Change the color of the svg
    SpinningCircleColor = '#00C1E3'

    # The body of the HTML
    body = '<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 1000 1000" style="enable-background:new 0 0 1000 1000;" xml:space="preserve"><circle class="st0" cx="500" cy="500" r="302.8"><animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 500 500" to="360 500 500" dur="100s" repeatCount="indefinite" /></circle><circle class="st1" cx="500" cy="500" r="237.7"><animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 500 500" to="360 500 500" dur="40s" repeatCount="indefinite" /></circle><circle class="st2" cx="500" cy="500" r="366.8" transform="rotate(0 500 500)" ;><animateTransform attributeType="xml" attributeName="transform" type="rotate" from="0 500 500" to="-360 500 500" dur="50s" repeatCount="indefinite" /></circle><circle class="st3" cx="500" cy="500" r="385.1" /></circle></svg></div>'


    # intenal style sheet
    style = '<style>.h{ border-radius: 200px; background: #FFFFFF; text-align: center; position: absolute; top: 36.7%; left: 41.7%; margin-top: -50px; margin-left: -50px; } p{ font-size: 250%; text-align: center; color: white; }</style><style type="text/css">body {background-color: #232323;}svg {height: 95vh;width: 95vw;}.st0 {fill: none;stroke: ' + SpinningCircleColor + ';stroke-width: 42;stroke-miterlimit: 10;}.st1 {fill: none;stroke: ' + SpinningCircleColor + ';stroke-width: 42;stroke-miterlimit: 10;}.st2 {fill: none;stroke: ' + SpinningCircleColor + ';stroke-width: 42;stroke-miterlimit: 10;}.st3 {fill: none;stroke: ' + SpinningCircleColor + ';stroke-width: 42;stroke-miterlimit: 10;}.st0 {stroke-dasharray: 12.1947, 12.1947, 12.1947, 12.1947, 12.1947, 12.1947;}.st1 {stroke-dasharray: 50, 90, 200, 30, 40, 0;}.st2 {stroke-linecap: square;stroke-dasharray: 120, 20, 110, 20, 140;}.st3 {stroke-width: 16;stroke-linecap: square;<style>'

    # Concatination of body and stlye sheet
    whole = body + '</br>' + style

    # Return this to the output route
    return whole


@app.route('/voicetts')
def voicetts():
    mic = '<div class="micStyle"><svg xmlns="http://www.w3.org/2000/svg" id="Layer_35" enable-background="new 0 0 64 64" height="512" viewBox="0 0 64 64" width="512"><path d="m23 52.12c5.18.45 9 2.08 9 4.88 0 3.31-5.37 5-12 5s-12-1.69-12-5c0-2.8 3.82-4.43 9-4.88v5.88h6z" fill="#fcd770"/><path d="m23 52.12v5.88h-6v-5.88-6.16c.33.03.66.04 1 .04h4c.34 0 .67-.01 1-.04z" fill="#838f9b"/><path d="m6 29v1c0 1.1-.9 2-2 2s-2-.9-2-2v-4c0-1.1.9-2 2-2 .55 0 1.05.22 1.41.59.37.36.59.86.59 1.41z" fill="#fcd770"/><path d="m38 26v4c0 1.1-.9 2-2 2s-2-.9-2-2v-1-3c0-1.1.9-2 2-2 .55 0 1.05.22 1.41.59.37.36.59.86.59 1.41z" fill="#fcd770"/><path d="m10 28v2h-4v-1-3h4z" fill="#fcd770"/><path d="m34 26v3 1h-4v-2-2z" fill="#fcd770"/><path d="m30 32v2c0 4.42-3.58 8-8 8h-4c-4.42 0-8-3.58-8-8v-2z" fill="#838f9b"/><path d="m30 32h-20v-2-2h20v2z" fill="#ff826e"/><path d="m10 16c0-4.42 3.58-8 8-8h4c4.42 0 8 3.58 8 8v10 2h-20v-2z" fill="#969faa"/><path d="m62 47v2c0 4.42-3.58 8-8 8h-12c-4.42 0-8-3.58-8-8v-2c0-2.21.9-4.21 2.34-5.66 1.45-1.44 3.45-2.34 5.66-2.34v-4l6 4h6c4.42 0 8 3.58 8 8z" fill="#e6e9ed"/><path d="m62 10v2c0 4.42-3.58 8-8 8h-6l-6 4v-4c-2.21 0-4.21-.9-5.66-2.34-1.44-1.45-2.34-3.45-2.34-5.66v-2c0-4.42 3.58-8 8-8h12c4.42 0 8 3.58 8 8z" fill="#e6e9ed"/><g fill="#b4dd7f"><circle cx="56" cy="11" r="2"/><circle cx="48" cy="11" r="2"/><circle cx="40" cy="11" r="2"/><circle cx="40" cy="48" r="2"/><circle cx="48" cy="48" r="2"/><circle cx="56" cy="48" r="2"/></g><path d="m24 51.222v-4.392c6.219-.967 11-6.343 11-12.83v-1.184c.314.112.648.184 1 .184 1.654 0 3-1.346 3-3v-4c0-1.654-1.346-3-3-3-1.302 0-2.402.839-2.816 2h-2.184v-9c0-4.962-4.037-9-9-9h-4c-4.963 0-9 4.038-9 9v9h-2.184c-.414-1.161-1.514-2-2.816-2-1.654 0-3 1.346-3 3v4c0 1.654 1.346 3 3 3 .352 0 .686-.072 1-.184v1.184c0 6.487 4.781 11.863 11 12.83v4.393c-5.732.662-9 2.743-9 5.777 0 3.701 4.981 6 13 6s13-2.299 13-6c0-3.034-3.268-5.115-9-5.778zm11-25.222c0-.551.448-1 1-1s1 .449 1 1v4c0 .551-.448 1-1 1s-1-.449-1-1v-1zm-2 1v2h-2v-2zm-22 2h18v2h-18zm0 4h18v1c0 3.86-3.141 7-7 7h-4c-3.859 0-7-3.14-7-7zm2-21.889v1.889h2v-2h-1.889c1.262-1.235 2.987-2 4.889-2h4c1.902 0 3.627.765 4.889 2h-1.889v2h2v-1.889c1.235 1.263 2 2.988 2 4.889v11h-18v-11c0-1.902.765-3.627 2-4.889zm-4 17.889h-2v-2h2zm-5 2c-.552 0-1-.449-1-1v-4c0-.551.448-1 1-1s1 .449 1 1v3 1c0 .551-.448 1-1 1zm3 3v-3h2v3c0 4.962 4.037 9 9 9h4c4.963 0 9-4.038 9-9v-3h2v3c0 6.065-4.935 11-11 11h-4c-6.065 0-11-4.935-11-11zm15 13v10h-4v-10zm-2 14c-6.477 0-11-1.645-11-4 0-1.819 2.655-3.226 7-3.764v5.764h8v-5.764c4.345.539 7 1.945 7 3.764 0 2.355-4.523 4-11 4z"/><path d="m54 1h-12c-4.963 0-9 4.038-9 9v2c0 4.625 3.506 8.446 8 8.945v4.924l7.303-4.869h5.697c4.963 0 9-4.038 9-9v-2c0-4.962-4.037-9-9-9zm7 11c0 3.86-3.141 7-7 7h-6.303l-4.697 3.131v-3.131h-1c-3.859 0-7-3.14-7-7v-2c0-3.86 3.141-7 7-7h12c3.859 0 7 3.14 7 7z"/><path d="m25 23h2v2h-2z"/><path d="m21 23h2v2h-2z"/><path d="m17 23h2v2h-2z"/><path d="m13 23h2v2h-2z"/><path d="m25 19h2v2h-2z"/><path d="m21 19h2v2h-2z"/><path d="m17 19h2v2h-2z"/><path d="m13 19h2v2h-2z"/><path d="m25 15h2v2h-2z"/><path d="m21 15h2v2h-2z"/><path d="m17 15h2v2h-2z"/><path d="m13 15h2v2h-2z"/><path d="m21 11h2v2h-2z"/><path d="m17 11h2v2h-2z"/><path d="m56 8c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.552 0-1-.449-1-1s.448-1 1-1 1 .449 1 1-.448 1-1 1z"/><path d="m48 8c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.552 0-1-.449-1-1s.448-1 1-1 1 .449 1 1-.448 1-1 1z"/><path d="m40 8c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.552 0-1-.449-1-1s.448-1 1-1 1 .449 1 1-.448 1-1 1z"/><path d="m54 38h-5.697l-7.303-4.869v4.924c-4.494.499-8 4.32-8 8.945v2c0 4.962 4.037 9 9 9h12c4.963 0 9-4.038 9-9v-2c0-4.962-4.037-9-9-9zm7 11c0 3.86-3.141 7-7 7h-12c-3.859 0-7-3.14-7-7v-2c0-3.86 3.141-7 7-7h1v-3.131l4.697 3.131h6.303c3.859 0 7 3.14 7 7z"/><path d="m56 45c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.552 0-1-.449-1-1s.448-1 1-1 1 .449 1 1-.448 1-1 1z"/><path d="m48 45c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.552 0-1-.449-1-1s.448-1 1-1 1 .449 1 1-.448 1-1 1z"/><path d="m40 45c-1.654 0-3 1.346-3 3s1.346 3 3 3 3-1.346 3-3-1.346-3-3-3zm0 4c-.552 0-1-.449-1-1s.448-1 1-1 1 .449 1 1-.448 1-1 1z"/></svg></div>'


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    # STYLING

    # Padding on the mic svg
    micDivPadding = '75px'

    # Margin Top of the mic SVG
    micDivMarginT = '15%'

    # BGC
    BGC = 'grey'

    style_voicetts = '<style>.micStyle{padding: ' + micDivPadding + ';margin-top: ' + micDivMarginT + ';background-color: ' + BGC + '; display: inline-block;}</style>'

    return mic + style_voicetts

if __name__ == "__main__":
    app.run()


