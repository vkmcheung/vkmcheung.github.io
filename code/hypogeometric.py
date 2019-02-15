# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:37:38 2019

Demonstrating the hypogeometric distribution:

"If I draw 10 cards at random from a deck of 52 cards, what are my chances of getting 2 aces and 3 kings?"

@author: Vincent Cheung
"""
import numpy
from scipy.special import comb

sample = 10 #number of cards to randomly sample in total
a = 2 #number of aces needed
k = 3 #number of kings needed

n = 10000 #number of trials per experiment
perm = 10 #number of experiment replications


deck = range(1,52+1)

allcount = []
for p in range(perm):
    count = 0
    
    for i in range(n):
            l = numpy.random.choice(deck, sample , replace = False)
            
            ca = 0
            ck = 0
            for j in range(sample):
                if l[j] <= 4: #if ace
                    ca += 1
                if l[j] >= 49: #if king
                    ck += 1                
    
            if  ca == a and ck == k:
                count += 1                
    allcount.append(count)

print 'the empiracal probability is: \t', numpy.mean(allcount)/n
print 'the theoretical probability is:\t', comb(44,sample-a-k)*comb(4,a)*comb(4,k)/comb(52,sample)
