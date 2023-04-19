#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This script extracts the email addresses of the corresponding authors of all articles
author: t.darde@wepredic.com
date: 2020-10-20

Use: python pubmed_corresponding_authors.py "HepaRG"

"""

from Bio import Entrez, Medline
from io import StringIO
import re


def search_pubmed(search_term):
    """
    Search PubMed for articles with the specified term and extract the email of the corresponding author
    search_term: string
    return: list of strings
    for example: search_pubmed("HepaRG")
    """

    Entrez.email = "it.service@wepredic.com"
    # Search PubMed for articles with the specified term
    handle = Entrez.esearch(db="pubmed", term=search_term, retmax=10000)
    record = Entrez.read(handle)
    handle.close()

    # Get a list of the PubMed IDs for the articles
    id_list = record["IdList"]

    # Loop through each article and extract the email of the corresponding author
    x = 1
    output = open("corresponding_authors.txt", "w")
    output.write("Lastname;Firstname;Email;Affiliation")

    for pmid in id_list:
        print(f"Article {x} of {len(id_list)}")
        x += 1
        try:
          handle = Entrez.efetch(db="pubmed", id=pmid, rettype="medline", retmode="text")
          article = handle.read()
          handle.close()
          if "AD" in article and "FAU" in article:
              record_med = Medline.read(StringIO(article))
              fau_ad_list = zip(record_med["AD"], record_med["FAU"])
              for fau_ad in fau_ad_list:
                email_match = re.search("[^\s]+@[^\s]+", fau_ad[0])
                if email_match:
                  email = email_match[0]
                  trimmed_email = email[:-1] if email.endswith(".") else email
                  non_email_ad = fau_ad[0][:email_match.start()]
                  line = f"{fau_ad[1].replace(',',';').replace(' ','')}; {trimmed_email}; {non_email_ad}+\n"
                  print(line)
                  output.write(f"{line}")
        except:
          print("Error")

    output.close()

if __name__ == "__main__":
    import sys
    search_term = sys.argv[1]
    search_pubmed(search_term)