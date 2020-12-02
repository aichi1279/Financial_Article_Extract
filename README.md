# -記事データから深層学習モデルで業績発表記事を取得する実装 

\n#1.素性リストの生成--------------------------

-プログラム名：mk_feature.py

-参照：train.list

-実行コマンド
python3 mk_feature.py > feature.list


#2.深層学習用トレーニングデータファイルの生成------

-プログラム名：mk_deep_train.py

-参照：train.list & feature.list

-実行コマンド
python3 mk_deep_train.py > deep_train


#3.深層学習用テストデータファイルの生成-----------

-プログラム名：mk_deep_test.py

-参照：test.list & feature.list

-実行コマンド
python3 mk_deep_test.py > deep_test

#4.深層学習の実装-----------------------------

-プログラム名：deep_learn.py

-実行コマンド
python3 deep_learn.py deep_train deep_test

-生成物: output

#5.outputに記述された尤度が0.9以上の記事を業績発表記事として識別

-プログラム名：identify.py

-実行コマンド
python3 identify.py > result.txt

#6.本学習における精度の確認(精度＆再現度＆F値)--------

-プログラム名: precision_recall_F.py

-実行コマンド
python3 precision_recall_F.py

※精度がターミナルに表示されます


以上！
