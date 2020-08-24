#!/usr/bin/env python3

import sys, re, operator, string


class TrueStack():
    class_stack = []

    def pop(self):
        return self.class_stack.pop()


    def peek(self):
        return self.class_stack[-1]


    def empty(self):
        return self.class_stack == []


    def append(self, item):
        self.class_stack.append(item)


    def extend(self, item):
        self.class_stack.extend(item)


    def __len__(self):
        return len(self.class_stack)

# ----------------------------------------

stack = TrueStack()
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

    stack.peek().extend(list(string.ascii_lowercase))
    heap['stop_words'] = stack.pop()

    heap["words"] = []
    while len(stack):
        if stack.peek() in heap['stop_words']:
            stack.pop()
        else:
            heap['words'].append(stack.pop())

    # print(heap['words'])
    stack.extend(heap['words'])
    del heap['words']


# ----------------------------------------
def frequencies():
    heap['word_freqs'] = {}

    while len(stack):
        if stack.peek() in heap['word_freqs']:
            stack.append(heap['word_freqs'][stack.peek()])
            stack.append(1)
            stack.append(stack.pop() + stack.pop())

        else:
            stack.append(1)

        heap['word_freqs'][stack.pop()] = stack.pop()

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

    while stack.peek() < 25 and len(stack) > 1:
        heap["i"] = stack.pop()

        (w, f) = stack.pop()
        print(w, "-", f)
        stack.append(heap["i"])
        stack.append(1)
        stack.append(stack.pop() + stack.pop())


# ------------------------------------------------
