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

import re
import time
import numpy as np
import pandas as pd
from tabulate import tabulate
from collections import defaultdict

# # Question 3

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
                       'WTMEC2YR', 'WTINT2YR', 'cohort']]
demo_data = demo_data.rename(columns={'SEQN': 'id', 'RIDAGEYR': 'age', 
                                      'RIDRETH3': 'race_and_ethnicity',
                                      'DMDEDUC2': 'education',
                                      'DMDMARTL': 'marital_status',
                                      'RIDSTATR': 'survey_weighting_var1',
                                      'SDMVPSU': 'survey_weighting_var2',
                                      'SDMVSTRA': 'survey_weighting_var3',
                                      'WTMEC2YR': 'survey_weighting_var4',
                                      'WTINT2YR': 'survey_weighting_var5'})
demo_data = demo_data.astype({'id': 'int32', 'age': 'int32',
                              'education': 'category',
                              'marital_status': 'category',
                              'race_and_ethnicity': 'category',
                              'survey_weighting_var1': 'category',
                              'survey_weighting_var2': 'category',
                              'survey_weighting_var3': 'int32',
                              'cohort': 'category'})
demo_data.to_pickle('demo_data_2011-2018.pkl')

# part b
ohx_g = pd.read_sas('OHXDEN_G.XPT')
ohx_g['cohort'] = '2011-2012'
ohx_h = pd.read_sas('OHXDEN_H.XPT')
ohx_h['cohort'] = '2013-2014'
ohx_i = pd.read_sas('OHXDEN_I.XPT')
ohx_i['cohort'] = '2013-2016'
ohx_j = pd.read_sas('OHXDEN_J.XPT')
ohx_j['cohort'] = '2017-2018'
ohx_data = pd.concat([ohx_g, ohx_h, ohx_i, ohx_j], ignore_index=True)
tc_cols = [col for col in ohx_data.columns 
           if re.match(r"OHX[0-9][0-9]TC",col)]
ctc_cols = [col for col in ohx_data.columns 
            if re.match(r"OHX[0-9][0-9]CTC",col)]
ohx_data = ohx_data[['SEQN', 'OHDDESTS']+tc_cols+ctc_cols]
for i, tc_col_name in enumerate(tc_cols):
    ohx_data = ohx_data.astype({tc_col_name: 'category'})
    ohx_data = ohx_data.rename(columns={tc_col_name: 'tooth_counts_'+str(i)})
for i, ctc_col_name in enumerate(ctc_cols):
    ohx_data = ohx_data.astype({ctc_col_name: 'category'})
    ohx_data = ohx_data.rename(columns={ctc_col_name:
                                        'coronal cavities_'+str(i)})
ohx_data = ohx_data.rename(columns={'SEQN': 'id',
                                    'OHDDESTS': 'dentition_status_code'})
ohx_data = ohx_data.astype({'id': 'int32',
                            'dentition_status_code': 'category'})
ohx_data.to_pickle('ohxden_2011-2018.pkl')

print("There are {} cases in the dataset in part a".format(demo_data.shape[0]))
print("There are {} cases in the dataset in part b".format(ohx_data.shape[0]))


