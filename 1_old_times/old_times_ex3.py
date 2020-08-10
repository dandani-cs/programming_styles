#!/usr/bin/env python3

# readline
# if len line + len (readline) < 1024
#   seek to start of file
#   seek(len(line), 0)
#   line + readline
# else
#   seek to start of file
#   seek(len(line), 0)

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

data.append(["", ""])     # data[1] stores line
data.append(None)   # data[2] stores starting index of word
data.append(0)      # data[3] is index on characters; the i
data.append(False)  # data[4] is flag if word was found
data.append("")     # data[5] is the word
data.append("")     # data[6] is word, frequency from secondary memory
data.append(0)      # data[7] is frequency

word_freqs = touchopen('word_freqs', 'rb+')

f = open(sys.argv[1])
while True:
    data[1][0] = ""
    while len(data[1][0]) + len(data[1][1]) < 1024:
        data[1][0] = data[1][0] + data[1][1]
        data[1][1] = f.readline()

        if data[1][1] == "":
            break

    if data[1][0] == "":
        break

    if data[1][0][len(data[1][0]) - 1] != "\n":
        data[1][0] += "\n"
    data[2] = None
    data[3] = 0

    for c in data[1][0]:
        if data[2] == None:
            if c.isalnum():
                data[2] = data[3]

        else:
            if not c.isalnum():
                data[4] = False
                data[5] = data[1][0][data[2]:data[3]].lower()

                if len(data[5]) > 2 and data[5] not in data[0]:
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


while True:
    data[25] = word_freqs.readline().strip()
    if data[25] == b"":
        break;

    data[26] = int(data[25].decode().split(",")[1])
    data[25] = data[25].decode().split(",")[0].strip()

    for i in range(25):
        if data[i] == [] or data[26] > data[i][1]:
            data.insert(i, [data[25], data[26]])
            del data[26]
            break # break for only

for tf in data[0:25]:
    if len(tf) == 2:
        print(f"{tf[0]} - {tf[1]}")

word_freqs.close()
