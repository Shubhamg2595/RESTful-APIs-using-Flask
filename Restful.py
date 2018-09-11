from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

#an api works with a resource and each resource must e a classs

items = []

'simply creating a Student class that is actually inheriting the properties of resource class'
class Item(Resource):
    def get(self,name):
        for item in items:
            if item['name']==name:
                return item
        return {'message':'this item does not exist'}, 404

    def post(self,name):
        data=request.get_json() #force=True means that we dont need content type header that is even if we dont set content/type to josn. it qwill simple read the data and display it based on it types
        item={
            'name':name,
            'price':data['price']
        }
        items.append(item)
        return item , 201


class ItemList(Resource):
    def get(self):
        return {'item':items}


'accessing the Student Resource'
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
'''
WHEN YOU USE POST METHOD ,WHERE I AM INSERTING A NEW ITEM USING URL DIRECTLY...
http://127.0.0.1:5000/item/chair
OUTPUT WILL BE SOMETHING LIKE THIS...

{
    "name": "chair",
    "price": 12.5
}

'''


'''
USE THE SAME URL WITH GET METHOD ADN CHECK THE OUTPUT
'''

'''
Use status codes and check the difference in postman:
404: not found
201: created
'''

if __name__ == '__main__':
    app.run(port=5000,debug=True)