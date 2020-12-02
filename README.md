# -金融テキストマイニング（業績発表記事）
# - 深層学習を用いて、記事データから業績発表記事を識別する実装

<br>

#1.素性リストの生成--------------------------

-プログラム名：mk_feature.py

-参照：train.list

-実行コマンド<br>
python3 mk_feature.py > feature.list

<br>#2.深層学習用トレーニングデータファイルの生成------

-プログラム名：mk_deep_train.py

-参照：train.list & feature.list

-実行コマンド<br>
python3 mk_deep_train.py > deep_train


<br>#3.深層学習用テストデータファイルの生成-----------

-プログラム名：mk_deep_test.py

-参照：test.list & feature.list

-実行コマンド<br>
python3 mk_deep_test.py > deep_test

<br>#4.深層学習の実装-----------------------------

-プログラム名：deep_learn.py

-実行コマンド<br>
python3 deep_learn.py deep_train deep_test

-生成物: output

<br>#5.outputに記述された尤度が0.9以上の記事を業績発表記事として識別

-プログラム名：identify.py

-実行コマンド<br>
python3 identify.py > result.txt

<br>#6.本学習における精度の確認(精度＆再現度＆F値)--------

-プログラム名: precision_recall_F.py

-実行コマンド<br>
python3 precision_recall_F.py

※精度がターミナルに表示されます


以上！


<環境構築編　Ubuntu(Linux)対応><br>
sudo apt update<br>
sudo apt upgrade<br>
sudo apt install vim<br>
sudo apt install lv<br>
sudo apt install dbus-x11<br>
sudo apt install gconf2<br>
sudo apt install p7zip-full<br>
sudo apt install fonts-ipafont<br>
sudo apt install gcc<br>
sudo apt install g++<br>
sudo apt install make<br>
sudo apt install emacs<br>
sudo apt install emacs-mozc<br>
sudo apt install mecab<br>
sudo apt install mecab-ipadic-utf8<br>
sudo apt install swig<br>

<Pythonの設定編><br>
sudo apt install python3-pip<br>
sudo apt install python3-dev<br>
sudo pip3 install --upgrade pip<br>
sudo pip3 install --upgrade numpy<br>
sudo pip3 install --upgrade scikit-learn<br>
sudo pip3 install --upgrade gensim<br>
sudo pip3 install --upgrade h5py<br>
sudo pip3 install --upgrade joblib<br>
sudo pip3 install --upgrade paramiko<br>
sudo pip3 install --upgrade mecab-python3<br>
sudo pip3 install --upgrade tensorflow<br>
sudo pip3 install --upgrade keras<br>
cd /usr/local/etc/　　<br>
sudo ln -s /etc/mecabrc<br>
