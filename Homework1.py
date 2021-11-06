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

import math
import time
import numpy as np
from scipy import stats
from tabulate import tabulate


# # Question 0

# + active=""
# This is _question 0_ for [problem set 1](https://jbhender.github.io/Stats507/F21/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/).
# > Question 0 is about Markdown.
#
# The next question is about the **Fibonnacci sequence**, $F_n=F_{n−2}+F_{n−1}$. In part **a** we will define a Python function ```fib_rec()```.
#
# Below is a …
# ### Level 3 Header
# Next, we can make a bulleted list:
# * Item 1
#   * detail 1
#   * detail 2
# * Item 2
#
# Finally, we can make an enumerated list:
#
# 1.  Item 1 
# 1.  Item 2 
# 1.  Item 3 
#
#
# -

# This is _question 0_ for [problem set 1](https://jbhender.github.io/Stats507/F21/ps1.html) of [Stats 507](https://jbhender.github.io/Stats507/F21/).
# > Question 0 is about Markdown.
#
# The next question is about the **Fibonnacci sequence**, $F_n=F_{n−2}+F_{n−1}$. In part **a** we will define a Python function ```fib_rec()```.
#
# Below is a …
# ### Level 3 Header
# Next, we can make a bulleted list:
# * Item 1
#   * detail 1
#   * detail 2
# * Item 2
#
# Finally, we can make an enumerated list:
#
# 1.  Item 1 
# 1.  Item 2 
# 1.  Item 3 
#

# # Question 1

# +
#part a
def fib_rec(n, a=0, b=1):
    """
    Returns the value of Fn in the Fibonnaci sequence.

    Parameters
    ----------
    n: a nonnegative integer
    a: F0 in the Fibonnaci sequence
    b: F1 in the Fibonnaci sequence
     Returns
     -------
     Fn: the nth item in the sequence

    """
    if n == 0:
        return a
    elif n == 1:
        return b
    return fib_rec(n-1)+fib_rec(n-2)

fib_rec(11)


# +
#part b
def fib_for(n, a=0, b=1):
    """
    Returns the value of Fn in the Fibonnaci sequence using a for loop.

    Parameters
    ----------
    n: a nonnegative integer
    
     Returns
     -------
     Fn: the nth item in the sequence

    """
    if n==0:
        return 0
    fa = 0
    Fn = 1
    for i in range(n-1):
        temp = Fn
        Fn = fa + Fn
        fa = temp
    return Fn

fib_for(11)


# +
#part c
def fib_whl(n):
    """
    Returns the value of Fn in the Fibonnaci sequence using a while loop.

    Parameters
    ----------
    n: a nonnegative integer
    
     Returns
     -------
     Fn: the nth item in the sequence

    """
    if n==0:
        return 0
    fa = 0
    Fn = 1
    count = 1
    while count < n:
        temp = Fn
        Fn = fa + Fn
        fa = temp
        count += 1
    return Fn

fib_whl(11)


# +
#part d
def fib_rnd(n):
    """
    Returns the value of Fn in the Fibonnaci sequence using the 
    rounding method.

    Parameters
    ----------
    n: a nonnegative integer
    
     Returns
     -------
     Fn: the nth item in the sequence

    """
    fi = (1+math.sqrt(5))/2
    Fn = round(fi**n/math.sqrt(5))
    return Fn
    
fib_rnd(11)


# +
#part e
def fib_flr(n):
    """
    Returns the value of Fn in the Fibonnaci sequence using the 
    truncation method.

    Parameters
    ----------
    n: a nonnegative integer
    
     Returns
     -------
     Fn: the nth item in the sequence

    """
    fi = (1+math.sqrt(5))/2
    Fn = math.floor(fi**n/math.sqrt(5)+0.5)
    return Fn
    
fib_flr(11)

# +
#part f
num_repeat = 100
num_start = 10
num_end = 30
interval = 5
time_data = [["N\Method","Recursive(ms)","For loop(ms)","While loop(ms)",
              "Rounding(ms)","Truncation(ms)"]]
median_data = np.zeros(5)
for n in range(num_start,num_end+1,interval):
    time_start = time.perf_counter()
    for i in range(num_repeat):
        fib_rec(n)
    time_rec = time.perf_counter()
    for i in range(num_repeat):
        fib_for(n)
        time_for = time.perf_counter()
    for i in range(num_repeat):
        fib_whl(n)
        time_whl = time.perf_counter()
    for i in range(num_repeat):
        fib_rnd(n)
        time_rnd = time.perf_counter()
    for i in range(num_repeat):
        fib_flr(n)
        time_flr = time.perf_counter()
    time_flr -= time_rnd
    time_rnd -= time_whl
    time_whl -= time_for
    time_for -= time_rec
    time_rec -= time_start
    median_data = np.array([time_rec*1000,time_for*1000,time_whl*1000,
                               time_rnd*1000,time_flr*1000])/num_repeat
    time_data.append([n, np.median(median_data[0]),np.median(median_data[1]),
                      np.median(median_data[2]),np.median(median_data[3]),
                      np.median(median_data[4])])

print(tabulate(time_data, tablefmt="grid"))


# -

# # Question 2

# +
# part a
def Pascal_row(n):
    """
    Returns a specified row of Pascal’s triangle.

    Parameters
    ----------
    n: a nonnegative integer
    
     Returns
     -------
     row_n : nth row in the Pascal’s triangle.

    """
    row_n = []
    c = 1
    for i in range(1,n+2):
        row_n.append(c)
        c = int(c*(n+1-i)/i)
    return row_n

print(Pascal_row(10))


# +
# part b
def Pascal_print(n):
    """
    Prints the first n rows of Pascal’s triangle.

    Parameters
    ----------
    n: a positive integer   

    """
    last_row = Pascal_row(n-1)
    max_num_width = len(str(last_row[int(n/2)]))+1
    max_tri_width = max_num_width * len(last_row)
    for i in range(0,n):
        row_i = Pascal_row(i)
        printed_string = ""
        for val in row_i:
            printed_string += str(val)+' '*(max_num_width-len(str(val)))
        print(printed_string.center(max_tri_width))        
    
Pascal_print(15)


# -

# # Question 3

# +
# part a
def check_format(arr):
    """
    Raise an informative exception if not a 1d Numpy array.

    Parameters
    ----------
    arr: input data

    """
    try:
        arr = np.array(arr)
        if arr.ndim != 1:
            raise exception 
    except:
        print('Error: input not a 1d Numpy array or \
              any object coercable to such an array')
    return arr

def mean_est(arr,conf,form = 'string'):
    """
    Return a point and interval estimate or dictionary.

    Parameters
    ----------
    arr: input data
    conf: desired confidence level
    form: 'string' return a string/ None return a dictionary
    
     Returns
     -------
     dictionary : a dictionary with keys est, lwr, upr, and level
     string : a point and interval estimation
    """
    arr = check_format(arr)
    mean = np.mean(arr)
    sig = np.std(arr, ddof=1)/np.sqrt(len(arr))
    conf_int = stats.norm.interval(conf,loc=mean,scale=sig)
    dictionary = {'est': mean, 'lwr':conf_int[0], 
                  'upr':conf_int[1], 'level': conf}
    if form == None:
        return dictionary
    string = '{}[{}%"CI:({},{})]'.format(dictionary['est'],
                                         100*dictionary['level'],
                                         dictionary['lwr'],
                                         dictionary['upr'])
    return string

mean_est([9.9,10,10.1],0.9)


# +
# part b
def prop_est(arr,conf,method,form = 'string'):
    """
    Return a point and interval estimate.

    Parameters
    ----------
    arr: input data (Bernoulli trials)
    conf: desired confidence level
    method: 'Norm', based on the Normal approximation
            'Clop', Clopper-Pearson interval
            'Jeff', Jeffrey’s interval
            'Agre', Agresti-Coull interval
    form: 'string' return a string/
          None return a dictionary
    
     Returns
     -------
     dictionary : a dictionary with keys est, lwr, upr, and level
     string : a point and interval estimation

    """
    arr = check_format(arr)
    n = len(arr)
    x = len(arr[arr==1])
    p = x/n
    alpha = 1-conf
    conf_int = None
    if method == 'Norm':
        if not (n*p>12 and n*(1-p)>12):
            raise Warning("The approximation is not considered adequate")            
        conf_int = stats.norm.interval(conf,loc=p,scale=(p*(1-p)/n)**0.5)
    elif method == 'Clop':
        conf_int = (stats.beta.ppf(alpha/2,x,n-x+1),
                    stats.beta.ppf(1-alpha/2,x+1,n-x))
    elif method == 'Jeff':
        lwr = stats.beta.ppf(alpha/2,x+0.5,n-x+0.5) if x != 0 else 0
        upr = stats.beta.ppf(1-alpha/2,x+0.5,n-x+0.5) if x != n else 1
        conf_int = (lwr,upr)
    elif method == 'Agre':
        z = -stats.norm.ppf((1-conf)/2)
        n_t = n+z**2
        p_t = (x+z**2/2)/n_t
        lwr = max(0,p_t-z*(p_t*(1-p_t)/n_t)**0.5)
        upr = min(1,p_t+z*(p_t*(1-p_t)/n_t)**0.5)
        #print(stats.norm.interval(conf,loc=p_t,scale=(p_t*(1-p_t)/n_t)**0.5))
        conf_int = (lwr,upr)
        p = p_t
    dictionary = {'est': p, 'lwr':conf_int[0], 'upr':conf_int[1],
                  'level': conf}
    if form == None:
        return dictionary
    string = '{}[{}%"CI:({},{})]'.format(dictionary['est'],
                                         100*dictionary['level'],
                                         dictionary['lwr'],
                                         dictionary['upr'])
    return string
    
prop_est([1,1,1,1,1,1,1,1,1],0.95,'Jeff')


# +
# part c
def ext_conf_int(dict,dec=4):
    """
    Extract the confident interval as a string.
    Parameters
    ----------
    dict: dictionary provided
    dec: number of decimals
    
     Returns
     -------
     string : a confident interval with required decimals

    """    
    lwr = round(dict['lwr'],dec)
    upr = round(dict['upr'],dec)
    string = '({},{})'.format(lwr,upr)
    return string


arr = np.concatenate((np.repeat(1,42),np.repeat(0,48)))
Mean_norm = [ext_conf_int(mean_est(arr,0.90,None)),
             ext_conf_int(mean_est(arr,0.95,None)),
             ext_conf_int(mean_est(arr,0.99,None))]
Prop_norm = [ext_conf_int(prop_est(arr,0.90,'Norm',None)),
             ext_conf_int(prop_est(arr,0.95,'Norm',None)),
             ext_conf_int(prop_est(arr,0.99,'Norm',None))]
Clopper = [ext_conf_int(prop_est(arr,0.90,'Clop',None)),
           ext_conf_int(prop_est(arr,0.95,'Clop',None)),
           ext_conf_int(prop_est(arr,0.99,'Clop',None))]
Jeffrey = [ext_conf_int(prop_est(arr,0.90,'Jeff',None)),
           ext_conf_int(prop_est(arr,0.95,'Jeff',None)),
           ext_conf_int(prop_est(arr,0.99,'Jeff',None))]
Agresti = [ext_conf_int(prop_est(arr,0.90,'Agre',None)),
           ext_conf_int(prop_est(arr,0.95,'Agre',None)),
           ext_conf_int(prop_est(arr,0.99,'Agre',None))]
conf_data = [['Conf_int\Method','Mean_norm','Prop_norm','Clopper',
              'Jeffrey','Agresti'],
             ['90%',Mean_norm[0],Prop_norm[0],Clopper[0],Jeffrey[0],
              Agresti[0]],
             ['95%',Mean_norm[1],Prop_norm[1],Clopper[1],Jeffrey[1],
              Agresti[1]],
             ['99%',Mean_norm[2],Prop_norm[2],Clopper[2],Jeffrey[2],
              Agresti[2]]]
print(tabulate(conf_data, tablefmt="grid"))
# -

# The Agresti-Coull method produces the interval with the smallest width for all 3 confidence levels.
