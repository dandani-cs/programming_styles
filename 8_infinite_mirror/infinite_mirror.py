import re, sys, operator

RECURSION_LIMIT = 5000
sys.setrecursionlimit(RECURSION_LIMIT+10)


def count(word_list, stopwords, wordfreqs):
    if word_list == []:
        return

    else:
        word = word_list[0]

        if word not in stopwords:
            if word in wordfreqs:
                wordfreqs[word] += 1
            else:
                wordfreqs[word] = 1

        count(word_list[1:], stopwords, wordfreqs)


def wf_print(wordfreq):
    if wordfreq == []:
        return

    else:
        (w, c) = wordfreq[0]
        print(w, '-', c)
        wf_print(wordfreq[1:])


stopwords = set(open('../stop_words.txt').read().split(","))
words = re.findall('[a-z]{2,}', open(sys.argv[1]).read().lower())
wordfreqs = {}

count(words, stopwords, wordfreqs)

wf_print(sorted(wordfreqs.items(), key=operator.itemgetter(1), reverse=True)[:25])
