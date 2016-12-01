#!/usr/bin/python
## #!flask/bin/python

""" 
This script requieres bfabric python module installed
http://fgcz-svn.uzh.ch/repos/scripts/trunk/linux/bfabric/apps/python

This scripts runs on localhost by executing:
$ python flax.py

it provides a REST TO WSDL wrapper

the INPUT is a workunit ID given as URL:
http://localhost:5000/bfabric/api/projectid/1000


this script can be used as a bfabric <-> shiny wrapper

Christian Panse <cp@fgcz.ethz.ch
Witold E. Wolski <wew@fgcz.ethz.ch>
2016-07-05 1700

"""


import json
from flask import Flask, jsonify, request
from bfabric import bfabric

app = Flask(__name__)
bfapp = bfabric.Bfabric(login='pfeeder')

def wsdl_extract(sampleid):

    try:
        return map(lambda x: {'sampleid': sampleid, 'name': x.name, 'id': x._id},
            bfapp.read_object(endpoint='extract', obj={'sampleid': sampleid}))
    except:
        pass

def wsdl_sample(projectid):

    try:
        return map(lambda x: {'id': x._id, 'name': x.name},
            bfapp.read_object(endpoint='sample', obj={'projectid': projectid}))
    except:
        pass

def wsdl_user(projectid):
    try:
        res =  bfapp.read_object(endpoint='user', obj={'projectid': projectid})
        res = map(lambda x:x.login, res)
        print res
        # user_ids =  map(lambda x: x._id, res[0].member)
        # rrr = map(lambda x:  bfapp.read_object(endpoint='user', obj={'id': x})[0].login, user_ids)
        return res
    except:
        pass
        

def wsdl_sample_extract(projectid):
    try:
        return map(lambda x: wsdl_extract(x._id), 
            bfapp.read_object(endpoint='sample', obj={'projectid': projectid}))
    except:
        pass

@app.route('/add_dataset/<int:projectid>', methods=['GET', 'POST'])
def add_dataset(projectid):
    try:
        queue_content = json.loads(request.data)
    except:
        return jsonify({'error': 'could not get POST content.'})

    try:
        obj = {}
        obj['name'] = 'autogenerated dataset by http://fgcz-s-028.uzh.ch:8080/queue_generator/'
        obj['projectid'] = projectid
        obj['attribute'] = [ {'name':'File Name', 'position':1, 'type':'String'},
            {'name':'Path', 'position':2},
            {'name':'Position', 'position':3},
            {'name':'Inj Vol', 'position':4, 'type':'numeric'},
            {'name':'ExtractID', 'position':5, 'type':'extract'} ]

        obj['item'] = list()

        for idx in range(0, len(queue_content)):
            obj['item']\
            .append({'field': map(lambda x: {'attributeposition': x + 1, 'value': queue_content[idx][x]}, range(0, len(queue_content[idx]))), 'position': idx + 1})

            print obj

    except:
        return jsonify({'error': 'composing bfabric object failed.'})

    try:
        res = bfapp.save_object(endpoint='dataset', obj=obj)[0]
        print "added dataset {} to bfabric.".format(res._id)
        return (jsonify({'id':res._id}))

    except:
        print res
        return jsonify({'error': 'beaming dataset to bfabric failed.'})



@app.route('/user/<int:projectid>', methods=['GET'])
def get_user(projectid):
    res = wsdl_user(projectid)

    if len(res) == 0:
        return jsonify({'error': 'no resources found.'})
        # abort(404)

    return jsonify({'user': res})


@app.route('/sampleid/<int:sampleid>', methods=['GET'])
def get_extract(sampleid):
    res = wsdl_extract(sampleid)

    if len(res) == 0:
        return jsonify({'error': 'no resources found.'})
        # abort(404)

    return jsonify({'extract': res})


"""
# running in R
res.sample <- as.data.frame(fromJSON("http://localhost:5000/projectid/1000"))
View(res.sample)
res.extract <- as.data.frame(fromJSON("http://localhost:5000/sampleid/30160"))
View(res.extract)
"""
@app.route('/projectid/<int:projectid>', methods=['GET'])
def get_sample(projectid):
    res = wsdl_sample(projectid)

    if len(res) == 0:
        return jsonify({'error': 'no resources found.'})
        # abort(404)

    return jsonify({'sample': res})

if __name__ == '__main__':
    #wsdl_user(1000)
    app.run(debug=True, host="0.0.0.0")
