import os
import sys
sys.path.append(os.path.split(os.path.realpath(__file__))[0])

from lightnlp.tc.re.tool import re_tool

train_path = '../data/re/train.sample.txt'
dev_path = '../data/re/test.sample.txt'
vec_path = 'D:/Data/NLP/embedding/word/sgns.zhihu.bigram-char'

# data_set = re_tool.get_dataset(train_path)
#
# print(len(data_set))
#
# item = data_set[0]
# print(item.text)
# print(item.label)

from lightnlp.tc import RE

re = RE()

re.train(train_path, dev_path=train_path, vectors_path=vec_path, save_path='./re_saves',
         log_dir='E:/Test/tensorboard/')

re.load('./re_saves')
# re.test(dev_path)
# # # 钱钟书	辛笛	同门	与辛笛京沪唱和聽钱钟书与钱钟书是清华校友，钱钟书高辛笛两班。
print(re.predict('钱钟书', '辛笛', '与辛笛京沪唱和聽钱钟书与钱钟书是清华校友，钱钟书高辛笛两班。'))
