# -*- coding: utf-8 -*-
import requests
import json
from flask import Flask
from setting import SLACK_URL

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
    response = requests.get(url)
    text = ''

    for whether_data in response.json()['forecasts']:
        text += whether_data['dateLabel'] + ' ' + whether_data['date'] + 'は、' + whether_data['telop'] + ' です。\n'

    print(text)

    url = SLACK_URL
    payload = json.dumps({'text': '{}'.format(text)})
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=payload, headers=headers)

    """Return a friendly HTTP greeting."""
    return 'Hello World!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=False)
# [END gae_python37_app]

