import random
import lxml.etree as et
import bz2

def gettitles(infile, testfile, trainfile, k):

    article_titles = []
    
    with bz2.open(infile) as in_file, open(testfile, 'w') as test_file, open(trainfile, 'w') as train_file:
        for article_title in et.iterparse(in_file, tag='{http://www.mediawiki.org/xml/export-0.10/}title'):)
            article_titles.append(article_title)

            article_title.clear()

            for anc in elpath ('anc-or-self::*'):
                while anc.getprevious() is not None:
                    del anc.getparent()[0]


    sample(in_file, test_file, k)

    for article_title in article_titles:
        if artile_title in reservoir:
            testfile.write("%s\n" % article_title)
        else:
            train_file.write("%s\n" % article_title)


def sample(infile, k):
"""
Returns @param k random items from @param iterable.
"""
    reservoir = []

    for t, item in enumerate(in_file):

        if t < k:
            reservoir.append(item)

        else:
            m = random.randint(0,t)

            if m < k:
                reservoir[m] = item

    return reservoir

gettitles(dewiki-latest-pages-articles.xml.bz2, testfile.txt, trainfile.txt, 3)

