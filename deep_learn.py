#!/usr/bin/python3

import argparse
from sklearn.datasets import load_svmlight_files

# TensorFlow from Keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras import optimizers
# import keras.backend as K

# 設定したサンプル数ごとに勾配を更新
b_size = 128

# エポック数
n_epoch = 20

def main():
    # コマンドライン引数の読み込み
    args = readArgs()

    # データの読み込み
    svm_train = [args.train]
    train, trainTag = load_svmlight_files(svm_train)
    train = train.toarray()

    # 素性数
    num_feature = train.shape[1]
    
    # Create model
    model = create_model(num_feature)

    model.fit(train, trainTag, batch_size=b_size, epochs=n_epoch, 
              verbose=1, validation_split=0.3, shuffle=True, initial_epoch=0)

    # テストデータの読み込み
    svm_test = [args.test]        # svm_test
    num_f = model.input_shape[1]  # 素性数
    test, testTag = load_svmlight_files(svm_test, n_features=num_f)
    test = test.toarray()

    results = model.predict_proba(test, batch_size=b_size, verbose=1)
    
     # create output
    fp = open("output", mode='w')
 
    for res in results:
        
        for r in res:
            fp.write(str(r)+" ")
        fp.write("\n")


# コマンドライン引数の処理関数
# 引数: なし
# 返値: 処理した引数の辞書
def readArgs():
    parser = argparse.ArgumentParser(description='deep learn ver.5')
    
    parser.add_argument('train', type=str, default='deep_train', help='train file')
    parser.add_argument('test', type=str, default='deep_test', help='test file')
    
    return parser.parse_args()


# モデルを設計
def create_model(max_features):
    model = Sequential()

    # 入力層
    model.add(Dense(max_features, input_dim=max_features, activation='relu'))

    # 中間層
    lap = 3

    for var in range(0, lap):
        model.add(Dense(1000, activation='relu'))

    for var in range(0, lap):
        model.add(Dense(500, activation='relu'))
    
    for var in range(0, lap):
        model.add(Dense(200, activation='relu'))

    for var in range(0, lap):
        model.add(Dense(100, activation='relu'))

    # 出力層（0,1の２値分類 0:negative 1:positive）
    model.add(Dense(2, activation='sigmoid'))

    # 最適化関数
    opt = optimizers.Adadelta(lr=1.0, rho=0.95, decay=0.0)

    # 学習モデルのコンパイル
    model.compile(loss='sparse_categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

    return model


if __name__ == '__main__':
    main()

