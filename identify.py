#!/usr/bin/python3

import math
import MeCab
mecab = MeCab.Tagger()


def main():
    test_Dir = "./list/test.list"
    output_Dir = "./output"

    sgml = open(test_Dir)
    test_lines = sgml.readlines()

    sgml = open(output_Dir)
    output_lines = sgml.readlines()

    count = -1
    for a_output in output_lines:
        count += 1
        a_output = a_output.split(' ')
        a_output = float(a_output[1])

        if a_output < 0.9:
            continue

        test = test_lines[count]
        test = test.split(" ")
        txt = test[2].split("。")
        txt = txt[0]

        print("1 "+test[1]+" "+txt)


if __name__ == '__main__':
    main()
