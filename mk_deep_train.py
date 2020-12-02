#!/usr/bin/python3

import math
import MeCab
mecab = MeCab.Tagger()


def main():
    train_Dir = "./list/train.list"
    feature_Dir = "./feature.list"

    sgml = open(train_Dir)
    train_lines = sgml.readlines()

    sgml = open(feature_Dir)
    feature_lines = sgml.readlines()

    for one_train in train_lines:
        one_train = one_train.split(' ')
        polar = int(one_train[0])
        if polar < 0:
            polar = 0
        train_txt_lines = one_train[2].split("。")

        #----------記事の形態素TF辞書ーーーー
        Doc_hash = {}
        for txt in train_txt_lines:
            mecab_result = mecab.parse(txt)
            results = mecab_result.split('\n')
            for info in results:
                if "名詞" not in info:
                    continue

                noun = info.split('\t')[0]
                if noun in Doc_hash:
                    Doc_hash[noun] += 1
                else:
                    Doc_hash[noun] = 1
        #-----------------------------------
        s = ""
        #-----素性値の製作----------
        num_hash = {}
        for one_feat in feature_lines:
            feat_num = one_feat.split(' ')[0]
            feat = one_feat.split(' ')[1]
            feat_value =  float(one_feat.split(' ')[2])

            if feat in Doc_hash:
                num_hash[feat_num] = Doc_hash[feat] * feat_value
                s += feat_num+":"+str(num_hash[feat_num])+" "


        print(str(polar)+" "+s)


if __name__ == '__main__':
    main()
