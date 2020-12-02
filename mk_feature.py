#!/usr/bin/python3

#import glob
import math
import MeCab
mecab = MeCab.Tagger()


def main():
    Dir="./list/train.list"
    sgml = open(Dir)
    txt_list = sgml.readlines()
    kind_list = []
    kind_file = []

    #------------------STAGE1--------------------#
    hash={} # Positive記事とNegative記事を区別して、形態素NのTF値を算出する
    file_hash={} #単語 -> filename,filename2,....
    count=0
    for txt in txt_list:
        count += 1
        segment = txt.split(" ")
        pos_nega = segment[0]
        lines = segment[2].split("。")
        for line in lines:
            mecab_result = mecab.parse(line)
            results = mecab_result.split("\n")
            for result in results:
                if "名詞" not in result and "動詞" not in result and "形容詞" not in result:
                    continue
                result_list = result.split("\t")
                word = result_list[0]
                if len(word)<2:
                    continue

                if word in file_hash:# idf編集用に..
                    list = file_hash[word].split(",")
                    if str(count) not in list:
                        file_hash[word] += ","+str(count)
                else:
                    file_hash[word] = str(count)

                if (pos_nega+":"+word) in hash:# sigma_tf 編集
                    hash[pos_nega+":"+word] += 1
                else:
                    hash[pos_nega+":"+word] = 1
    #--------------- STAGE1 : hash & idf_hash作成 <END>  -------------------#


    #--------------- STAGE2: ans_hash(単語毎の出現確率辞書)の作成 --------------------#
    ans_hash={}#各記事毎に形態素の集計後,STAGE1のhashを参照し「ans_hash[単語:1or-1]->出現確率Pを算出
    #1「記事」毎に
    for txt in txt_list:
        segment = txt.split(" ")
        sub_hash={}
        pos_nega = segment[0]
        filename = segment[1]
        kind_file.append(filename)
        lines = segment[2].split('。')
        #2「行」毎に
        for line in lines:
            mecab_result = mecab.parse(line)
            results = mecab_result.split("\n")
            #3「形態素」毎に
            for result in results:
                if "名詞" not in result and "動詞" not in result and "形容詞" not in result:
                    continue
                result_sep = result.split("\t")
                word = result_sep[0]
                if len(word)<2:
                    continue

                if (pos_nega+":"+word) in sub_hash:
                    sub_hash[pos_nega+":"+word] += 1
                else:
                    sub_hash[pos_nega+":"+word] = 1
                    kind_list.append(word)
        #1に属する
        for key in sub_hash.keys():
            ans_hash[filename+':'+key] = sub_hash[key]/hash[key]

    #------------- STAGE2：単語毎の出現確率辞書の作成 <END>-----------#



    kind_list = set(kind_list) #単語の種類(kind)リスト
    kind_file = set(kind_file) #ファイル名のリスト
    #print(len(kind_list))
    #------------- STAGE3：STOPワードをkind_listから抜いておく-----------#
    stop_file = "./list/stopword.list"
    txt = open(stop_file)
    stop_list = txt.readlines()
    for a_stop in stop_list:
        a_stop = a_stop.replace('\n','')
        if a_stop in kind_list:
            kind_list.remove(a_stop)
    #------------- STAGE3：<END>-----------#

    D=3560
    #------- STAGE4: 単語(kind_list)とファイル名(kind_file)をループさせ、Positive記事＆Negative記事区別してエントロピーを算出---------#
    HP_hash = {}
    idf_hash = {}
    for a_kind  in kind_list:
        #---idfの計算
        sep = file_hash[a_kind].split(',')
        idf_hash[a_kind] = math.log2(D/len(sep))

        pos_HP = 0
        nega_HP = 0
        for file in kind_file:
            if (file+':'+'1'+':'+a_kind) in ans_hash:
                pos_HP -= ans_hash[file+':'+'1'+':'+a_kind]*math.log2(ans_hash[file+':'+'1'+':'+a_kind])
            elif (file+':'+'-1'+':'+a_kind) in ans_hash:
                nega_HP -= ans_hash[file+':'+'-1'+':'+a_kind]*math.log2(ans_hash[file+':'+'-1'+':'+a_kind])

        #大きい方を採用する
        if pos_HP > nega_HP:
            HP_hash[a_kind] = pos_HP
        else:
            HP_hash[a_kind] = nega_HP
    #-------- STAGE4:  <END>  ----------------------------------------#



    #ソート＆条件付きで表示
    sorted_list = sorted(HP_hash.items(), key=lambda x:x[1], reverse=True)
    count=0
    for key,entropy in sorted_list:
        if entropy <= 2 or idf_hash[key] <= 1:
            continue
        count += 1
        print(str(count)+" "+key+" "+str(entropy))

if __name__ == '__main__':
    main()
