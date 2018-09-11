from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

#an api works with a resource and each resource must e a classs

items = []


'simply creating a Student class that is actually inheriting the properties of resource class'
class Item(Resource):
    def get(self,name):
        '''
        here i am replacing for loop used in previous version by
        using filter() method and lambda function
        but since filter() returns a filter object,we use next() method
        to fetch the first item returned by this filter function
        '''
        item=next(filter(lambda x:x['name']==name ,items),None) #we used none to ensure that if no item is found,default value to be passed is none
        return {'item':item},200 if item is not None else 404
        #'''above return statement responds with status code:200 if item is found else with 404'''

    def post(self,name):
        'making sure that item being inserted ,does not already exists in the itemlist'
        if next(filter(lambda x:x['name']==name,items),None) is not None: #is not none can e=be omitted
            return {'message':'An item with name {} already exists in the itemlist'.format(name)} , 400
        else:
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

if __name__ == '__main__':
    app.run(port=5000,debug=True)