#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:36:44 2020

@author: asierbelazaortega
"""

import numpy as np
import pandas as pd

## Data frame
years = [year for year in range (1900, 2020)]
deads = [(y + np.random.uniform(0,100) -1850) for y in years]

df = pd.DataFrame({
    
    "years": years,
    "deads": deads
    
})
gf = df.plot(x = "years", y = "deads")

print (gf)
