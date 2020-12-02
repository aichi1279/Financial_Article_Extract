#!/usr/bin/python3

import math
import MeCab
mecab = MeCab.Tagger()


def main():
    result_Dir = "./result.txt"
    correct_Dir = "./list/correct.list"

    sgml = open(result_Dir)
    result_lines = sgml.readlines()

    sgml = open(correct_Dir)
    correct_lines = sgml.readlines()

    #Precision_phase
    count = 0
    correct = 0
    for line in result_lines:
        count += 1
        line = line.split(' ')
        re_polar = line[0]
        re_id  = line[1]

        for one in correct_lines:
            one = one.split(' ')
            co_polar = one[0]
            co_id  = one[1]
            if re_id == co_id and re_polar == co_polar:
                correct += 1
                break

    Precision = correct / count

    #recall_phase
    count = 0
    correct = 0
    for one in correct_lines:
        one = one.split(' ')
        co_polar = one[0]
        co_id  = one[1]
        if int(co_polar) != 1:
            continue

        count += 1
        for line in result_lines:
            line = line.split(' ')
            re_polar = line[0]
            re_id  = line[1]
            if re_id == co_id:
                correct += 1
                break

    recall = correct / count

    print("Precision : "+str(Precision))
    print("Recall : "+str(recall))
    print("F値 : "+str((2*recall*Precision)/(Precision+recall)))


if __name__ == '__main__':
    main()
