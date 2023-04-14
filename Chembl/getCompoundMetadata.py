import pubchempy as pcp

def cas_to_properties(cas):
    """
    Convert a CAS number to a dictionary of chemical properties using the PubChem API.
    """
    cas_number = cas['cas']
    name = cas['name']
    print('Processing CAS number ' + cas_number)
    try:
        # Search PubChem for the compound with the given CAS number
        compound = pcp.get_compounds(cas_number, 'name')[0]
        # Retrieve the desired properties for the compound
        properties = {
            'name': name,
            'cas': cas_number if cas_number is not None else '',
            'formula': compound.molecular_formula if compound.molecular_formula is not None else '',
            'smiles': compound.isomeric_smiles if compound.isomeric_smiles is not None else '',
            'inchi_key': compound.inchikey if compound.inchikey is not None else '',
            'alogp': compound.xlogp if compound.xlogp is not None else '',
            'mw': compound.molecular_weight if compound.molecular_weight is not None else '',
        }
        return properties
    except:
        properties = {
            'name': name,
            'cas': cas_number,
            'formula': '',
            'smiles': '',
            'inchi_key': '',
            'alogp': '',
            'mw': '',
        }
        print(f"Error retrieving properties for CAS number {cas_number}.")
        return properties

def write_properties_to_tsv(properties_list, filepath):
    """
    Write a dictionary of chemical properties to a tab-separated values (TSV) file.
    """
    with open(filepath, 'a') as f:
        f.write('name\tcas\tformula\tsmiles\tinchi_key\talogp\tmw\n')
        for properties in properties_list:
            if properties is not None:
                f.write(f"{properties['name']}\t{properties['cas']}\t{properties['formula']}\t{properties['smiles']}\t{properties['inchi_key']}\t{properties['alogp']}\t{properties['mw']}\n")

def getCaslist(filepath):
    """
    Read a list of CAS numbers from a text file.
    """
    CAS_list = []
    with open(filepath) as f:
        for line in f:
            l=line.split('\t')
            name = l[0].replace('\n','')
            CAS=l[1].replace('\n','')
            CAS_list.append({'name':name,'cas':CAS})
    return CAS_list

# Example usage
CAS_list = getCaslist('ChemicalList.txt')
properties_list = []
for CAS in CAS_list:
    properties = cas_to_properties(CAS)
    properties_list.append(properties)
write_properties_to_tsv(properties_list, 'compound_properties.tsv')

