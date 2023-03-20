import json

def selectComparison(json_data):
    compa = json_data['i']['condition1']+'__vs__'+json_data['i']['condition2']
    return compa


def json2Dict(json_file):
    with open(json_file) as json_info:
        data = json.load(json_info)
        return data

def getOverAllInfo(json_data,compa):
    info = dict()
    info['genes_number'] = json_data['alldeseqres'][compa]['counts']
    info['go_number'] = json_data['alldeseqres'][compa]['countsGo']
    info['kegg_number'] = json_data['alldeseqres'][compa]['countsKegg']

    return info

def getFoldChange(json_data,compa):
    return json_data['alldeseqres'][compa]['fc']

def getGenes(json_data,compa):
    genes = []
    deg = json_data['alldeseqres'][compa]['genes']
    for gene in deg:
        gene_info = dict()
        gene_info['baseMean'] = gene['baseMean']
        gene_info['log2FC'] = gene['log2FC']
        gene_info['lfcSE'] = gene['lfcSE']
        gene_info['pvalue'] = gene['pvalue']
        gene_info['padj'] = gene['padj']
        gene_info['meanInComp'] = gene['meanInComp']
        gene_info['name'] = gene['Gene'].split('>')[2].replace('</a','')
        genes.append(gene_info)
    
    return genes

def run(json_file):
    compa_dict = dict()
    json_data = json2Dict(json_file)
    print(json_data['i']['condition1'])
    compa = selectComparison(json_data)
    compa_dict['name'] = compa
    compa_dict['fc'] = getFoldChange(json_data,compa)
    compa_dict['overview'] = getOverAllInfo(json_data,compa)
    compa_dict['genes'] = getGenes(json_data,compa)

    return compa_dict

file_test = 'tests/J0T0C0__vs__J1T1C6.json'
test = run(file_test)

print(test)