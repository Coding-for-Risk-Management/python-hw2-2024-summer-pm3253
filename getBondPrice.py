#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 04:55:14 2024

@author: mupeiyao
"""

import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    t=np.arange(0,ppy*m+1)
    cpn=couponRate*face
    df=(1/(1+y/ppy))
    dft=[df**i for i in t]
    bondPrice=cpn*sum(dft)+dft[-1]*face
    return(bondPrice)


# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy=1