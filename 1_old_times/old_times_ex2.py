#!/usr/bin/env python3

import os, sys, string

def touchopen(filename, *args, **kwargs):
    try:
        os.remove(filename)
    except OSError:
        pass
    open(filename, "a").close()

    return open(filename, *args, **kwargs)

stop_words = open("..\\stop_words.txt")
data = [stop_words.read(1024).split(",")] # split returns list

data.append([])     # data[1] stores line
data.append(None)   # data[2] stores starting index of word
data.append(0)      # data[3] is index on characters; the i
data.append(False)  # data[4] is flag if word was found
data.append("")     # data[5] is the word
data.append("")     # data[6] is word, frequency from secondary memory
data.append(0)      # data[7] is frequency
data.append(0)      # data[8] is counter replacing for identifiers


word_freqs = touchopen('word_freqs', 'rb+')

f = open(sys.argv[1])
while True:
    data[1] = [f.readline()]
    if data[1] == [""]:
        break
    if data[1][0][len(data[1][0]) - 1] != "\n":
        data[1][0] += "\n"
    data[2] = None
    data[3] = 0

    while data[3] < len(data[1][0]):
        if data[2] == None:
            if data[1][0][data[3]].isalnum():
                data[2] = data[3]

        else:
            if not data[1][0][data[3]].isalnum():
                data[4] = False
                data[5] = data[1][0][data[2]:data[3]].lower()

                if len(data[5]) > 2 or data[5] not in data[0]:
                    while True:
                        data[6] = word_freqs.readline().strip()

                        if data[6] == b"":
                            break

                        data[7] = int(data[6].decode().split(",")[1])

                        data[6] = data[6].decode().split(",")[0].strip()

                        if data[5] == data[6]:
                            data[7] += 1
                            data[4] = True
                            break

                    if not data[4]:
                        word_freqs.seek(0, 1) # stay in the same position; at end of file;
                        word_freqs.write(bytearray("%20s,%04d\n" % (data[5],1), encoding="utf-8"))

                    else:
                        word_freqs.seek(-26, 1)
                        word_freqs.write(bytearray("%20s,%04d\n" % (data[5], data[7]), encoding='utf-8')) # does it replace the next 26 characters?

                    word_freqs.seek(0, 0)

                data[2] = None

        data[3] += 1

f.close()
word_freqs.flush()

del data[:]

data = [[]] * 25
data.append("") # data[25] word, freq from file
data.append(0)  # data[26] freq
data.append(0)  # data[27] counter


while True:
    data[25] = word_freqs.readline().strip()
    if data[25] == b"":
        break;

    data[26] = int(data[25].decode().split(",")[1])
    data[25] = data[25].decode().split(",")[0].strip()

    while data[27] < 25:
        if data[data[27]] == [] or data[26] > data[data[27]][1]:
            data.insert(data[27], [data[25], data[26]])
            data[27] = 0
            break # break while data[27] < 25 only
        data[27] += 1

data[27] = 0

while data[27] < 25:
    if len(data[data[27]]) == 2:
        print(f"{data[data[27]][0]} - {data[data[27]][1]}")
    data[27] += 1


word_freqs.close()
