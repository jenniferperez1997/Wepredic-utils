from chembl_webresource_client.new_client import new_client

output = open("result.txt", "a")
with open("ChemicalList.txt") as file:
  for line in file:
    out=""
    l=line.split('\t')
    chemical=l[0]
    CAS=l[1]
    molecule = new_client.molecule
    mols = molecule.filter(pref_name__iexact=chemical).only(['molecule_chembl_id', 'molecule_properties', 'molecule_structures','cross_references'])
    mol=mols[0]
    print(chemical)
    out = mol['cross_references'][0]['xref_name']+'\t'+'https://www.ebi.ac.uk/chembl/compound_report_card/'+mol['molecule_chembl_id']+'\t'+mol['molecule_properties']['full_molformula']+'\t'+mol['molecule_structures']['canonical_smiles']+'\t'+mol['molecule_structures']['standard_inchi_key']+'\t'+mol['molecule_properties']['alogp']+'\t'+mol['molecule_properties']['full_mwt']

    print(out)

