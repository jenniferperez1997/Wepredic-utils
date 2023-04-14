# Thomas Darde
# Project: Starlight mixture


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
    if mol is None:
        print('No molecule found for '+chemical)
        output.write(chemical+'\t'+CAS+'\n')
        continue
    else :
      try:
        xref_name=mol['cross_references'][0]['xref_name']
        if xref_name is None:
          xref_name=chemical
      except:
        xref_name=''
     
      try:
        molecule_id=mol['molecule_chembl_id']
        if molecule_id is None:
          molecule_id=''
      except:
        molecule_id=''

      try:
        full_molformula=mol['molecule_properties']['full_molformula']
        if full_molformula is None:
          full_molformula=''
      except:
        full_molformula=''

      try:
        canonical_smiles=mol['molecule_structures']['canonical_smiles']
        if canonical_smiles is None:
          canonical_smiles=''
      except:
        canonical_smiles=''

      try:
        standard_inchi_key=mol['molecule_structures']['standard_inchi_key']
        if standard_inchi_key is None:
          standard_inchi_key=''
      except:
        standard_inchi_key=''

      try:
        alogp=mol['molecule_properties']['alogp']
        if alogp is None:
          alogp=''
      except:
        alogp=''

      try:
        full_mwt=mol['molecule_properties']['full_mwt']
        if full_mwt is None:
          full_mwt=''
      except:
        full_mwt=''

      out=chemical+'\t'+CAS+'\t'+'https://www.ebi.ac.uk/chembl/compound_report_card/'+molecule_id+'\t'+full_molformula+'\t'+canonical_smiles+'\t'+standard_inchi_key+'\t'+alogp+'\t'+full_mwt  
      output.write(out+'\n')