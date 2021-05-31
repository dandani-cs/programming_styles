import sys, re, string

def extract_words(path_to_file):
    words = re.findall('[a-z]{2,}',
                        open(path_to_file).read().lower())

    stop_words - set(open('../stop_words.txt').read().split(','))

    return [w for w in words if not w in stop_words]
