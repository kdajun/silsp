# -*- coding: utf-8 -*-
"""실습과제2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BfT__bxUSBEp3c7ylXC5j3uju5Z-NMKj
"""

words = ["knowledge", "hardwork", "attitude"]
words = list(map(len,words))
words

import random
def dongjeon(k) :
  adj = ['head','tail']
  s = random.choice(adj)
  if s == k :
    print('당신이 승리했습니다!')
  else :
    print('당신이 패배했습니다.')
k_ = str(input("head(앞면)과 tail(뒷면) 중 하나를 입력하십시오. : "))
dongjeon(k_)

en = str(input("영어문자열을 입력하십시오 : "))
eng = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big= []
for i in range(0,len(en)) :
  if en[i] in eng :
    big.append(en(i).upper)
  else :
    big.append(en(i).lower)
print(big)