import falcon
import json

"""
 # list comprehension for later
 # [{'entry':entry, '_self':f'/report/{entry}', 'data':data} for entry, data in db.items()]

"""

class Entries():
    def on_get(self, req, resp):
        resp.media = db


class Entry():
    def on_put(self, req, resp, _id):
        data = json.load(req.stream)

        print(id)
        db[id] = data 
        write_on_json()
        resp.media = {'id': _id, '_self':f'/entry/{_id}', 'data':data} # instead of data db[_id]


def write_on_json():

    with open('data.json', 'w') as f:
        json.dump(db, f)
try:
    with open('data.json') as f:
        db = json.load(f)
except (FileNotFoundError):
    db = {}

# from falcon_cors import CORS
# cors = CORS(allow_all_origins=True, allow_methods_list=['GET'])

# app = falcon.API(middleware=[cors.middleware])

app = falcon.API()
app.add_route('/entry', Entries())


# gunicorn name:app -b 0:80 --reload
