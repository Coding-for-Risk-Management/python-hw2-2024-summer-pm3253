#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 05:37:27 2024

@author: mupeiyao
"""

import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = m * ppy
    period_rate = y / ppy
    coupon_payment = face * couponRate / ppy
    t = np.arange(1, n + 1)
    cf = np.full(n, coupon_payment)
    cf[-1] += face
    pv_factors = (1 + period_rate) ** -t
    pvcf = cf * pv_factors
    weighted_pvcf = pvcf * t
    duration = weighted_pvcf.sum() / pvcf.sum()
    return duration

# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1


