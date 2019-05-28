import numpy as np

def moving_average(ts, n):
    ma = [np.nan] * (n - 1)
    for i in range(n, len(ts)):
        ma.append(ts[i-n:i].mean())
    return ma

def linear_weighted_moving_average(ts, n):
    ma = [np.nan] * (n - 1)
    weights = np.arange(n) + 1
    for i in range(n, len(ts)):
        ma.append(np.dot(ts[i-n:i], weights) / weights.sum())
    return ma

def exponential_smoothing(ts, alpha):
    es = []
    p = ts[0]
    for i in ts:
        p = alpha * p + (1 - alpha) * i
        es.append(p)
    return es

def holt_trend(ts):
    return

def holt_winters(ts):
    return