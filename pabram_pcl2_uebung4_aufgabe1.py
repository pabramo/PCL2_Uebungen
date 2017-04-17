import codecs



with open('abcd.txt') as src, open('gigaunique.txt', 'w') as trg:
    sentence_hashes = set()
    for sentence in src:
        sentence_hash = hash(sentence)
        if sentence_hash not in sentence_hashes:
            sentence_hashes.add(sentence_hash)
            trg.write(sentence)
