import json
import requests

class Product:
    def __init__(self):
        self.api_url = "https://dev-prod-eurosafe.wepredic.com/api"

    def all(self):
        r = requests.get(self.api_url + "/products")
        return r.json()['data']
    
    def getBy(self, attribute, value):
        r = requests.get(self.api_url + "/products?filters[%s][$eq]=%s"%(attribute, value))
        return r.json()['data']
    
    def isExist(self, attribute, value):
        r = requests.get(self.api_url + "/products?filters[%s][$eq]=%s"%(attribute, value))
        if len(r.json()['data']) == 0:
            return False
        else:
            return True

    def create(self, params):
        print(json.dumps(params))
        r = requests.post(
            self.api_url + "/products",
            headers={"Content-Type": "application/json"},
            data=json.dumps({'data':params}),
        )
        return r.json()['data']

    def update(self, id, params):
        r = requests.put(
            self.api_url + "/products/" + str(id),
            headers={"Content-Type": "application/json"},
            data=json.dumps({'data':params}),allow_redirects=True
        )
        return r.json()['data']


class Category:
    def __init__(self):
        self.api_url = "https://dev-prod-eurosafe.wepredic.com/api"

    def all(self):
        r = requests.get(self.api_url + "/categories")
        return r.json()['data']
    
    def isExist(self, attribute, value):
        r = requests.get(self.api_url + "/categories?filters[%s][$eq]=%s"%(attribute, value))
        if len(r.json()['data']) == 0:
            return False
        else:
            return True
            
    def getBy(self, attribute, value):
        '''
        Get product categories by params
        category.getBy({"number": 1})
        '''
        r = requests.get(self.api_url + "/categories?filters[%s][$eq]=%s"%(attribute, value))
        return r.json()['data']
    
    def create(self, params):
        r = requests.post(
            self.api_url + "/categories",
            headers={"Content-Type": "application/json"},
            data=json.dumps({'data':params}),
        )
        return r.json()['data']


    def update(self, id, params):
        r = requests.put(
            self.api_url + "/category/" + str(id),
            headers={"Content-Type": "application/json"},
            data=json.dumps({'data':params}),
        )
        return r.json()['data']
    
class Commanditary:
    def __init__(self):
        self.api_url = "https://dev-prod-eurosafe.wepredic.com/api"

    def all(self):
        r = requests.get(self.api_url + "/commanditaries")
        return r.json()
    
    def isExist(self, attribute, value):
        r = requests.get(self.api_url + "/commanditaries?filters[%s][$eq]=%s"%(attribute, value))
        if len(r.json()['data']) == 0:
            return False
        else:
            return True
            
    def getBy(self, attribute, value):
        '''
        Get product categories by params
        category.getBy({"number": 1})
        '''
        r = requests.get(self.api_url + "/commanditaries?filters[%s][$eq]=%s"%(attribute, value))
        return r.json()['data']
    
    def create(self, params):
        r = requests.post(
            self.api_url + "/commanditaries",
            headers={"Content-Type": "application/json"},
            data=json.dumps({'data':params}),
        )
        return r.json()['data']


    def update(self, id, params):
        r = requests.put(
            self.api_url + "/commanditaries/" + str(id),
            headers={"Content-Type": "application/json"},
            data=json.dumps({'data':params}),
        )
        return r.json()['data']



class Session:
    def __init__(self):
        self.api_url = "https://dev-prod-eurosafe.wepredic.com/api"

    def all(self):
        r = requests.get(self.api_url + "/sessions")
        return r.json()['data']
    
    def isExist(self, attribute, value):
        r = requests.get(self.api_url + "/sessions?filters[%s][$eq]=%s"%(attribute, value))
        if len(r.json()['data']) == 0:
            return False
        else:
            return True
            
    def getBy(self, attribute, value):
        '''
        Get product categories by params
        category.getBy({"number": 1})
        '''
        r = requests.get(self.api_url + "/sessions?filters[%s][$eq]=%s"%(attribute, value))
        return r.json()['data']
    
    def create(self, params):
        r = requests.post(
            self.api_url + "/sessions",
            headers={"Content-Type": "application/json"},
            data=json.dumps({'data':params}),
        )
        return r.json()['data']


    def update(self, id, params):
        r = requests.put(
            self.api_url + "/sessions/" + str(id),
            headers={"Content-Type": "application/json"},
            data=json.dumps({'data':params}),
        )
        return r.json()['data']