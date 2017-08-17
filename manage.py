#!/usr/bin/env python
#coding: utf-8
from flask import Flask,request,jsonify
from flask_script import Manager
import datetime

app  = Flask(__name__)
manager = Manager(app)

def alert_data(post_data):
  import json
  data = json.loads(post_data)
  #print data
  data = data['alerts']
  contents = []
  for item in data:
    content = {
      'status': item['status'],
      'module': item['labels']['job'],
      'annotations': item['annotations'],
    }
    contents.append(content)
  contents.append({
    'time': datetime.datetime.now().strftime("%Y-%m-%d:%H:%M:%S")
  })
  import requests

  url = 'yoururl'
  send_data = {
    "msgtype": "text",
    "text": {
      "content": contents
    }
  }
  headers = {
    'Content-Type':'application/json'
  }
  r =  requests.post(url,headers=headers,data=json.dumps(send_data))
  return jsonify({'status':r.ok,'mesg':r.text})

@app.route('/dingding',methods=['POST'])
def alert_send():
  if request.method == 'POST':
    post_data = request.get_data()
    return alert_data(post_data)
  return 

if __name__ == '__main__':
  manager.run()
