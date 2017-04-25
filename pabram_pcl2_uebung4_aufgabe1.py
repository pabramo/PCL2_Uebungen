import codecs
import sys
#from glob import glob
from lxml import etree
from xml.etree import ElementTree as et


filename = sys.argv[1]

def freqwords(indir, outfile):

    with open(filename, 'rt') as src, open('gigaunique.txt', 'w') as trg:
        tree = et.parse(filename)

        for node in tree.iter('s'):
            lemmata = []

            if len(node) >= 6:
                for token in node:
                    lemma = token.attrib.get('lemma')
                    if lemma == None:
                        pass

                    else:
                        lemmata.append(lemma)

            dedupl_hashes = set()
            counter = 0

            for sentence in lemmata:
                
                dedupl_hash = hash(sentence)

                if dedupl_hash  not in dedupl_hashes:
                    dedupl_hashes.add(dedupl_hash)

                else:
                    counter += 1

                    trg.write(sentence)

freqwords('testfile.xml', 'gigaunique.txt')


