def readHistoryFile():
    """Reads the history file and returns the list of patches that have been"""
    history = []
    with open('eurosafe_patch_history.txt', 'r') as f:
        for line in f:
            #split the line into a list of words by \t (tab)
            line = line.split('\t')
            
            #create PATCH,COMMANDITAIRE,NPRODUIT,DILUTION,SOO,NOM,PRODUIT,NV,CAT,COSM,RESULTAT,Scorage variables from split line
            #if PATCH empty, Get previus value of PATCH
            if line[0] == '':
                PATCH = line[0]
            else:
                PATCH = line[0]


            COMMANDITAIRE = line[1]
            NPRODUIT = line[2]
            DILUTION = line[3]
            SOO = line[4]
            NOM = line[5]
            PRODUIT = line[6]
            NV = line[7]
            CAT = line[8]
            COSM = line[9]
            RESULTAT = line[10]
            Scorage = line[11]

            history.append(line.strip())
    return history


