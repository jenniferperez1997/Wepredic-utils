import json
import requests

class Product:
    def __init__(self):
        self.api_url = "https://dev-prod-eurosafe.wepredic.com/"

    def all(self):
        r = requests.get(self.api_url + "/products")
        return r.json()
    
    def getBy(self, params):
        r = requests.get(self.api_url + "/products", params=params)
        return r.json()

    def create(self, params):
        print(params)
        r = requests.post(
            self.api_url + "/products",
            headers={"Content-Type": "application/json"},
            data=json.dumps(params),
        )
        return r.json()

    def update(self, id, params):
        r = requests.put(
            self.api_url + "/products/" + str(id),
            headers={"Content-Type": "application/json"},
            data=json.dumps(params),
        )
        return r.json()


class Category:
    def __init__(self):
        self.api_url = "https://dev-prod-eurosafe.wepredic.com"

    def all(self):
        r = requests.get(self.api_url + "/product-categories")
        return r.json()
    
    def isExist(self, params):
        r = requests.get(self.api_url + "/product-categories", params=params)
        if len(r.json()) == 0:
            return False
        else:
            return True
            
    def getBy(self, params):
        '''
        Get product categories by params
        category.getBy({"number": 1})
        '''
        r = requests.get(self.api_url + "/product-categories", params=params)
        return r.json()
    
    def create(self, params):
        print(params["name"], params["description"], params["number"])
        r = requests.post(
            self.api_url + "/product-categories",
            headers={"Content-Type": "application/json"},
            data=json.dumps(params),
        )
        return r.json()


    def update(self, id, params):
        r = requests.put(
            self.api_url + "/product_category/" + str(id),
            headers={"Content-Type": "application/json"},
            data=json.dumps(params),
        )
        return r.json()
    
class Commanditary:
    def __init__(self):
        self.api_url = "https://dev-prod-eurosafe.wepredic.com"

    def all(self):
        r = requests.get(self.api_url + "/commanditaires")
        return r.json()
    
    def isExist(self, params):
        r = requests.get(self.api_url + "/commanditaires", params=params)
        if len(r.json()) == 0:
            return False
        else:
            return True
            
    def getBy(self, params):
        '''
        Get product categories by params
        category.getBy({"number": 1})
        '''
        r = requests.get(self.api_url + "/commanditaires", params=params)
        return r.json()
    
    def create(self, params):
        r = requests.post(
            self.api_url + "/commanditaires",
            headers={"Content-Type": "application/json"},
            data=json.dumps(params),
        )
        return r.json()


    def update(self, id, params):
        r = requests.put(
            self.api_url + "/commanditaires/" + str(id),
            headers={"Content-Type": "application/json"},
            data=json.dumps(params),
        )
        return r.json()



class Session:
    def __init__(self):
        self.api_url = "https://dev-prod-eurosafe.wepredic.com"

    def all(self):
        r = requests.get(self.api_url + "/sessions")
        return r.json()
    
    def isExist(self, params):
        r = requests.get(self.api_url + "/sessions", params=params)
        if len(r.json()) == 0:
            return False
        else:
            return True
            
    def getBy(self, params):
        '''
        Get product categories by params
        category.getBy({"number": 1})
        '''
        r = requests.get(self.api_url + "/sessions", params=params)
        return r.json()
    
    def create(self, params):
        r = requests.post(
            self.api_url + "/product-categories",
            headers={"Content-Type": "application/json"},
            data=json.dumps(params),
        )
        return r.json()


    def update(self, id, params):
        r = requests.put(
            self.api_url + "/sessions/" + str(id),
            headers={"Content-Type": "application/json"},
            data=json.dumps(params),
        )
        return r.json()