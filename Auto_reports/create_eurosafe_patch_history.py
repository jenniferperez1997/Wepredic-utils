from utils import *
from slugify import slugify

def readHistoryFile():
    """Reads the history file and returns the list of patches that have been"""
    SESSION=''
    COMMANDITAIRE=''
    with open('Eurosafe_historique-format.csv', 'r') as f:
        for line in f:
            #split the line into a list of words by ;
            line = line.split(';')
            
            #create PATCH,COMMANDITAIRE,NPRODUIT,DILUTION,SOO,NOM,PRODUIT,NVCATCOSM,RESULTAT,SCORAGE variables from split line
            #Skip line if SOO is empty
            if line[2] == '':
                continue
            #if PATCH empty, Get previus value of PATCH
            if line[0] != '':
                SESSION = line[0]
            #Test if PATCH exist in database
            #If not, create it
            #If yes, get the id
            session = Session()
            if session.isExist({"name": SESSION}):
                session_id = session.getBy({"name": SESSION})[0]["id"]
            else:
                session_id = session.create({"name": SESSION})["id"]

            #if COMMANDITAIRE empty, Get previus value of COMMANDITAIRE
            if slugify(line[1]) != '':
                COMMANDITAIRE = slugify(line[1])

            COMMANDITAIRE = slugify(line[1])

            #Test if COMMANDITAIRE exist in database
            #If not, create it
            #If yes, get the id
            commanditaire = Commanditary()
            if commanditaire.isExist({"name": COMMANDITAIRE}): 
                commanditaire_id = commanditaire.getBy({"name": COMMANDITAIRE})[0]["id"]
            else:
                commanditaire_id = commanditaire.create({"name": COMMANDITAIRE})["id"]

            
            NPRODUIT = line[2]
            DILUTION = line[3]
            #if DILUTION == PUR relpace by 100%
            if DILUTION == 'PUR':
                DILUTION = '100%'
            
            SOO = line[4]
            #If SOO == O replace by occlusive if SO semi_occlusive
            if SOO == 'O':
                SOO = 'occlusive'
            elif SOO == 'S':
                SOO = 'semi_occlusive'
            else:
                SOO = ''
            
            NOMPRODUIT = line[5].replace('\n','')

            NVCATCOSM = line[6]

            #Get the category id from the category number
            category = Category()
            category_id = category.getBy({"number": NVCATCOSM})[0]["id"]
            

            RESULTAT = line[7]
            #Translate RESULTAT from french to english:
            # Très légèrement irritant -> very_slightly_irritant
            # Légèrement irritant -> slightly_irritant
            # Irritant -> irritant
            # Non irritant -> non irritant
            # Très irritant -> very_irritant
            # Modérément irritant -> moderately_irritant

            if RESULTAT == 'Très légèrement irritant':
                RESULTAT = 'very_slightly_irritant'
            elif RESULTAT == 'Légèrement irritant':
                RESULTAT = 'slightly_irritant'
            elif RESULTAT == 'Irritant':
                RESULTAT = 'irritant'
            elif RESULTAT == 'Non irritant':
                RESULTAT = 'non irritant'
            elif RESULTAT == 'Très irritant':
                RESULTAT = 'very_irritant'
            elif RESULTAT == 'Modérément irritant':
                RESULTAT = 'moderately_irritant'
            else:
                RESULTAT = ''

            SCORAGE = line[8].replace('\n','')
            
            #Create the product
            product = Product()
            product_id = product.create(
                {
                    "name": slugify(NOMPRODUIT),
                    "product_number": NPRODUIT,
                    "dilution": DILUTION,
                    "soo": SOO,
                    "product_category": int(category_id),
                    "commanditaire": int(commanditaire_id),
                    "result": RESULTAT,
                    "score": float(SCORAGE.replace(',','.')),
                    "session": int(session_id),
                }
            )

    return product_id


def readCategoryFile():
    """Reads the category file and returns the list of categories that have been"""
    with open('Eurosafe_categories.csv', 'r') as f:
        for line in f:
            params={}
            #split the line into a list of words by ;
            line = line.split(';')
            
            #create NUMBER,NAME, DESCRIPTION variables from split line
            params['number'] = int(line[0].replace('\ufeff',''))
            params['name'] = line[1]
            params['description'] = line[2].replace('\n','')
            category = Category()
            print(category.create(
                {
                    "name": slugify(params["name"]),
                    "description": params["description"],
                    "category_number": params["number"],
                }
            ))

#readCategoryFile()
readHistoryFile()
