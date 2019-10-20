from dotenv import load_dotenv
load_dotenv()

import os
accesstoken = os.getenv("accesstoken")

from groupy import Client
client = Client.from_token(accesstoken)

def create_group(groupname):
    new_group = client.groups.create(name=groupname)
    new_group.update(share=True)
    for group in client.groups.list_all():
        if group.name == groupname:
            new_group = group
            break
    return new_group.data["share_url"]


from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "hello_world"
    
@app.route('/<group>', methods=['POST'])
def main(group):
    print(group)
    link = create_group(group)
    result = {}
    result["group_link"] = link
    return jsonify(result)



### curl -X POST localhost:5000/testtest

