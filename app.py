from topicmodeller import TopicModeller
from topicdiscoverer import TopicDiscoverer
from flask import Flask, request
import pandas as pd
import json

app = Flask(__name__)
tm = None
td = None

@app.route('/topics', methods=['POST'])
def uploadFileForTopics():
    if request.method == 'POST':
        f = request.files['file']
        artifacts = pd.read_csv(f)
        vs = tm.CSV2Topics(artifacts)
        return json.dumps(td.discover(vs))

@app.route('/count', methods=['POST'])
def uploadFileForWordCount():
    if request.method == 'POST':
        f = request.files['file']
        artifacts = pd.read_csv(f)
        return json.dumps(tm.CSV2TermAmount(artifacts))

if __name__ == '__main__':
    shouldUseDump = True
    tm = TopicModeller(shouldUseDump)
    td = TopicDiscoverer()
    #artifacts = pd.read_csv('./complete_data.csv')
    #vs = tm.CSV2Topics(artifacts)
    #print(json.dumps(td.discover(vs)))
    app.run(debug=True)
    