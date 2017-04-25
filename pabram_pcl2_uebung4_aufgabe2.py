import random
import lxml.etree as et
import bz2
##def sample(iterable, k):
##"""
##Returns @param k random items from @param iterable.
##"""
##reservoir = []
##for t, item in enumerate(iterable):
##    if t < k:
##        reservoir.append(item)
##    else:
##        m = random.randint(0,t)
##        if m < k:
##            reservoir[m] = item
##    return reservoir


def gettitles(infile, testfile, trainfile, k):
    with bz2.open(infile) as in_file, open(testfile, 'w') as test_file, open(trainfile, 'w') as train_file:
        for _, article_title in et.iterparse(in_file, tag='{http://www.mediawiki.org/xml/export-0.10/}title'):
            print(article_title.text)
            article_title.clear()

gettitles('dewiki-latest-pages-articles.xml.bz2', 'testfile.txt', 'trainfile.txt', 3)
