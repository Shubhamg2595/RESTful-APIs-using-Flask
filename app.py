from flask import Flask,jsonify,request

app=Flask(__name__)


'CREATING A SIMPLE STORE LIST'
stores=[
    {
        'name':'My wonderful store',
        'items':[
            {
                'name':'My Item',
                'price' :15.99
            }
        ]
    }

]

'route to get list of all the stores'
@app.route("/store")
def get_stores():
    return jsonify({'stores':stores})


'route to create a new store name'
@app.route("/store",methods=['POST'])
def create_store():
    request_data=request.get_json()
    new_store={
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

'route to get data of store,when there name is provided'
@app.route("/store/<string:name>",methods=['GET'])
def get_store(name):
    #iterate over stores to find store name in stores list
    #IF NAME MATCHES,RETURN IT
    #IF NONE,RETURN AN ERROR MESSAGE
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'This store is not available in this region'})



'route to add a new item in store'
@app.route("/store/<string:name>/item",methods=['POST'])
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        if store['name']==name:
            new_item_in_store={
                'name':request_data['name'],
                'price':request_data['price']
                }
            store['items'].append(new_item_in_store)
            return jsonify(new_item_in_store)
    return jsonify({'message':'return not found'})

'route to get details of a specific item in store'
@app.route("/store/<string:name>/item")
def get_item_from_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})


if __name__ == '__main__':
    app.run(port=5000,debug=True)