def readHistoryFile():
    """Reads the history file and returns the list of patches that have been"""
    history = []
    PATCH=''
    COMMANDITAIRE=''
    with open('Eurosafe_historique-format.csv', 'r') as f:
        for line in f:
            #split the line into a list of words by ;
            print(line)
            line = line.split(';')
            
            #create PATCH,COMMANDITAIRE,NPRODUIT,DILUTION,SOO,NOM,PRODUIT,NVCATCOSM,RESULTAT,SCORAGE variables from split line
            #Skip line if SOO is empty
            if line[2] == '':
                continue
            #if PATCH empty, Get previus value of PATCH
            if line[0] != '':
                PATCH = line[0]
            #if COMMANDITAIRE empty, Get previus value of COMMANDITAIRE
            if line[1] != '':
                COMMANDITAIRE = line[1]

            COMMANDITAIRE = line[1]
            NPRODUIT = line[2]
            DILUTION = line[3]
            SOO = line[4]
            NOMPRODUIT = line[5].replace('\n','')
            NVCATCOSM = line[6]
            RESULTAT = line[7]
            SCORAGE = line[8].replace('\n','')
            
            #Print all variables
            print(PATCH,COMMANDITAIRE,NPRODUIT,DILUTION,SOO,NOMPRODUIT,NVCATCOSM,RESULTAT,SCORAGE)
            #history.append(line.strip())
    #return history

readHistoryFile()
