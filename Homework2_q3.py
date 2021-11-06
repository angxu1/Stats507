# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Packages

import os
import sys
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Homework1 import mean_est, prop_est
from scipy.stats import norm, ttest_ind, chi2_contingency
from IPython.core.display import display, HTML

# # Question 0 - Topics in Pandas

# ##  Window Functions
# * Provide the calculation of statistics 
# * Primarily used in signal processing and time series data
# * Perform desired mathematical operations on consecutive values at a time

# ## Rolling Functions
# * Can apply on Series and Dataframe type
# * For DataFrame, each function is computed column-wise
# * Here is an example for calculation of rolling sum
# * Similar way to calculate the mean, var, std ...

series = pd.Series(range(5))
df = pd.DataFrame({"A": series, "B": series ** 3})
df.rolling(3).sum()

# ## Parameters
# * **win_type** changes the window function (equally weighted by default)
# * You can set the minimum number of observations in window required to have a
# value by using **min_periods=k**
# * Set the labels at the center of the window by using **center==True** 
# (set to the right edge by default)

print(df.rolling(3, win_type='gaussian').sum(std=3))
print(df.rolling(3, win_type='gaussian', center=True).sum(std=3))
print(df.rolling(3, win_type='gaussian', min_periods=2, 
                 center=True).sum(std=3))

# ## Expanding Functions
# * Calculate the expanding sum of given DataFrame or Series
# * Perform desired mathematical operations on current all previous values
# * Similar way to calculate the mean, var, std...

df.expanding(min_periods=2).sum()

# # Question 1 - NHANES Table 1

# part a
demo_g = pd.read_sas('DEMO_G.XPT')
demo_g['cohort'] = '2011-2012'
demo_h = pd.read_sas('DEMO_H.XPT')
demo_h['cohort'] = '2013-2014'
demo_i = pd.read_sas('DEMO_I.XPT')
demo_i['cohort'] = '2015-2016'
demo_j = pd.read_sas('DEMO_J.XPT')
demo_j['cohort'] = '2017-2018'
demo_data = pd.concat([demo_g,demo_h,demo_i,demo_j], ignore_index=True)
demo_data = demo_data[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2',
                       'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA',
                       'WTMEC2YR', 'WTINT2YR', 'cohort', 'RIAGENDR']]
demo_data = demo_data.rename(columns={'SEQN': 'id', 'RIDAGEYR': 'age', 
                                      'RIDRETH3': 'race_and_ethnicity',
                                      'DMDEDUC2': 'education',
                                      'DMDMARTL': 'marital_status',
                                      'RIDSTATR': 'survey_weighting_var1',
                                      'SDMVPSU': 'survey_weighting_var2',
                                      'SDMVSTRA': 'survey_weighting_var3',
                                      'WTMEC2YR': 'survey_weighting_var4',
                                      'WTINT2YR': 'survey_weighting_var5',
                                      'RIAGENDR': 'gender'})
demo_data = demo_data.astype({'id': 'int32', 'age': 'int32',
                              'education': 'category',
                              'marital_status': 'category',
                              'race_and_ethnicity': 'category',
                              'survey_weighting_var1': 'category',
                              'survey_weighting_var2': 'category',
                              'survey_weighting_var3': 'int32',
                              'cohort': 'category',
                              'gender': 'category'})
demo_data.to_pickle('demo_data_gender_2011-2018.pkl')



