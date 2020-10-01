import numpy as np
from random import randint
from keras.preprocessing.sequence import pad_sequences

# ランダム配列格納用空配列
variable_seq_list = []

# 5~20の長さのシーケンスを10個生成
# 配列の要素は1~10(0以外)
for i in range(10):
    arr = [randint(1,9) for i in range(randint(5,20))]
    variable_seq_list.append(arr)

for i,j in enumerate(variable_seq_list):
    print("{} seq_len:{:>2} {}".format(i,len(j),j))

#一番長い配列にあわせてゼロパディング
maxlen = np.max([len(i)for i in variable_seq_list])
print("最大長:{}".format(maxlen))

print()
print(">>> after zero padding")

# padding='pre'で前に, 'post'で後ろに0を加える
padding_seq_list = pad_sequences(variable_seq_list, maxlen=maxlen,padding='post')

for i,j in enumerate(padding_seq_list):
    print(i,j)
