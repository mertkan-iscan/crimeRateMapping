import folium
from folium.plugins import HeatMap
from werkzeug.utils import secure_filename
from report import Report
from flask import Flask, request, flash, redirect, url_for, render_template
import os

app = Flask(__name__, static_folder='static')
app.config["UPLOAD_FOLDER"] = "C:/Users/merti/PycharmProjects/example/uploaded_files"

heatmapData = []
reportList = []


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/new-report')
def new_report():
    return render_template('NewReport.html')


@app.route('/create-route')
def create_route():
    return render_template('createRoute.html')


@app.route('/heatmap_crime.html')
def load_heatmap():
    return render_template('heatmap_crime.html')


@app.route('/logout-page')
def logout_page():
    return render_template('login.html')


@app.route('/create-report', methods=['POST'])
def create_report():
    # check if the post request has the file part
    if 'fileToUpload' not in request.files:
        # This part will execute if no file was uploaded.
        flash('No file part')
        return redirect(url_for('index'))

    file = request.files['fileToUpload']

    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # verify reports
        verify_reports()

        # Additional processing or saving the report
        report_list_to_heatmap_data()

        # recreate heatmap
        create_heatmap()
        return redirect(url_for('index'))

    # handle the text report if any
    if 'textReport' in request.form:
        text_report = request.form['textReport']
        # do something with text_report

    # handle the reportType if any
    if 'reportType' in request.form:
        report_type = request.form['reportType']
        # do something with report_type

    # after handling the data

    return redirect(url_for('index'))


@app.route('/location', methods=['POST'])
def handle_location():
    # take location data from html
    data = request.get_json()

    # set coordinates to variables
    latitude = data['latitude']
    longitude = data['longitude']

    # Pass the latitude and longitude
    create_report_obj(latitude, longitude)

    return 'coordinates retrieved'


def create_report_obj(latitude, longitude):
    # reformat coordinates
    latitude = float(latitude)
    longitude = float(longitude)

    # create new report
    newReport = Report("x", latitude, longitude)

    # Calculate intensity
    newReport.calculate_report_intensity()

    # convert report coordinates to address
    newReport.coordinates_to_address()

    # add new report to not verified list
    reportList.append(newReport)

    return 'report created'


def verify_reports():
    for report in reportList:
        report.set_verified()

    return 'all reports verified'


def report_list_to_heatmap_data():
    for report in reportList:
        if report.is_verified():
            # each list item should be in the format [lat, long, value]
            reportData = [report.latitude, report.longitude, report.intensity]

            # append reports to heatmap data
            heatmapData.append(reportData)

    return 'reports added heatmapData'


def select_reports_by_date(date_from, date_to):
    selected_reports = []

    for report in reportList:
        if date_from <= report.date.date() <= date_to:
            selected_reports.append(report)

    return selected_reports


def create_heatmap():
    # create a map object
    mapObj = folium.Map([41.0082, 28.9784], zoom_start=13)

    # create heatmap from the heatmap_data and add to map
    HeatMap(heatmapData).add_to(mapObj)

    # save the map object as html
    mapObj.save("templates/heatmap_crime.html")

    # show html file in browser
    # open_new_tab("example/templates/heatmap_crime.html")


if __name__ == '__main__':
    app.run()
