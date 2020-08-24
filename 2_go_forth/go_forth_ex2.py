#!/usr/bin/env python3

import sys, re, operator, string

stack = []
heap = {}


# ----------------------------------------
def read_file():
    f = open(stack.pop())
    stack.append([f.read()])
    f.close()


# -----------------------------------------
def filter_chars():
    stack.append(re.compile('[\W_]+'))
    stack.append([stack.pop().sub(" ", stack.pop()[0]).lower()])


# ------------------------------------------
def scan():
    stack.extend(stack.pop()[0].split())


# ------------------------------------------
def remove_stop_words():
    f = open("..\\stop_words.txt")
    stack.append(f.read().split(","))
    f.close()

    stack[-1].extend(list(string.ascii_lowercase))

    heap["words"] = []
    stack.append([stack.pop(), 0])
    while len(stack) > 1:
        while stack[-1][1] < len(stack[-1][0]):
            heap['values'] = stack.pop()
            if stack[-1] == heap['values'][0][heap['values'][1]]:
                stack.pop()
                stack.append(heap['values'])
                break

            stack.append(heap['values'][1])
            stack.append(1)
            stack.append(stack.pop() + stack.pop())
            heap['values'][1] = stack.pop()

            stack.append(heap['values'])


        if stack[-1][1] == len(stack[-1][0]):
            heap['values'] = stack.pop()
            heap['words'].append(stack.pop())
            stack.append(heap['values'])

        stack.append(0)
        heap['values'][1] = stack.pop()

    # print(heap['words'])
    stack.pop()
    stack.extend(heap['words'])
    del heap['words']


# ----------------------------------------
def frequencies():
    heap['word_freqs'] = {}

    stack.append([list(heap['word_freqs'].keys()), 0])

    while len(stack) > 1:
        while stack[-1][1] < len(stack[-1][0]):
            heap['values'] = stack.pop()

            if stack[-1] == heap['values'][0][heap['values'][1]]:
                stack.append(heap['word_freqs'][stack[-1]])
                stack.append(1)
                stack.append(stack.pop() + stack.pop())
                heap['word_freqs'][stack.pop()] = stack.pop()
                stack.append([list(heap['word_freqs'].keys()), 0])
                break

            stack.append(heap['values'][1])
            stack.append(1)
            stack.append(stack.pop() + stack.pop())
            heap['values'][1] = stack.pop()

            stack.append([list(heap['word_freqs'].keys()), heap['values'][1]])


        if stack[-1][1] == len(stack[-1][0]):
            heap['values'] = stack.pop()
            stack.append(1)
            heap['word_freqs'][stack.pop()] = stack.pop()
            stack.append([list(heap['word_freqs'].keys()), 0])

        stack.append(0)
        heap['values'][1] = stack.pop()


        # if stack[-1] in heap['word_freqs']:
        #     stack.append(heap['word_freqs'][stack[-1]])
        #     stack.append(1)
        #     stack.append(stack.pop() + stack.pop())
        #
        # else:
        #     stack.append(1)
        #
        # heap['word_freqs'][stack.pop()] = stack.pop()

    stack.pop()
    stack.append(heap["word_freqs"])
    del heap["word_freqs"]


# -------------------------------------------
def sort():
    stack.extend(sorted(stack.pop().items(), key=operator.itemgetter(1)))


# -------------------------------------------
if __name__ == '__main__':
    stack.append(sys.argv[1])

    read_file(); filter_chars(); scan();
    remove_stop_words(); frequencies(); sort();

    stack.append(0)

    while stack[-1] < 25 and len(stack) > 1:
        heap["i"] = stack.pop()

        (w, f) = stack.pop()
        print(w, "-", f)
        stack.append(heap["i"])
        stack.append(1)
        stack.append(stack.pop() + stack.pop())
