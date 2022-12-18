import numpy as np
import pandas as pd
import yfinance as yf
import datetime
from scipy.stats import norm

def download(stock,start,end):
    data = {}
    ticker = yf.download(stock,start,end)
    data[stock] = ticker['Adj Close']
    df = pd.DataFrame(data)
    print(df)
    return df

def cal_var(position,c,mu,sigma,n):
    v = norm.ppf(1-c)
    vr = position*(mu*n-sigma*np.sqrt(n)*v)
    print(vr)
    return vr


start = datetime.datetime(2010,1,1)
end = datetime.datetime(2022,12,18)
download('TCS.NS',start,end)
stock_data = download('TCS.NS',start,end)
stock_data['returns'] = np.log(stock_data['TCS.NS']/stock_data['TCS.NS'].shift(1))
stock_data = stock_data[1:]
print(stock_data)
S = 100
c = 0.95
mu = np.mean(stock_data['returns'])
sigma = np.std(stock_data['returns'])
cal_var(S,c,mu,sigma,100)

