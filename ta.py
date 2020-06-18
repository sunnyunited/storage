import pandas as pd
import numpy as np
#import talib

def STOCH(h,l,c,**kwargs):

    fastkperiod = kwargs.pop('fastk_period',14)
    slowkperiod = kwargs.pop('slowk_period',3)
    slowdperiod = kwargs.pop('slowd_period',3)

    # currently only SMA available, always 0. No need to pass into function
    kmatype = kwargs.pop('slowk_matype', 0)
    dmatype = kwargs.pop('slowd_matype',0)

    # create datafram for calculation
    fastk = ((c.astype(float) - l.rolling(fastkperiod).min().astype(float)) / (h.rolling(fastkperiod).max().astype(float) - l.rolling(fastkperiod).min().astype(float))) * 100
    #slowk =fastk.rolling(slowkperiod).mean()
    #slowd = slowk.rolling(slowdperiod).mean()

    return fastk

def MACD(c,**kwargs):
    fastperiod = kwargs.pop('fastperiod',12)
    slowperiod = kwargs.pop('slowperiod',26)
    sigperiod = kwargs.pop('signalperiod',9)
    macd = c.ewm(span=fastperiod).mean().astype(float)-c.ewm(span=slowperiod).mean().astype(float)
    signal = macd.ewm(span=sigperiod).mean().astype(float)
    hist = macd-signal

    return macd, hist



def main():
    print('hello world')

if __name__ == '__main__':
    main()
