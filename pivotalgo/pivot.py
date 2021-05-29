
import yfinance as yf
from yahoo_finance import Share
import pandas as pd




def pivot(high, low, close, hugosflag = False):
    '''
    takes t high, low, close, all float

    returns t+1 pivot high, pivot low as tuple 

    '''



    pma = (high+low+close)/3

    differential = (high+low)/2

    pr = pma - differential

    ph = pma + pr 

    pl = differential - pr

    if hugosflag:
        ph, pl = ph +5, pl+5

    return (ph, pl)



if __name__ == '__main__': 

    recent = yf.Ticker('ES=F').history(period = 'max')
    pivots = [[0 for i in range(2)] for j in range(len(recent))]
 
    idx = []

   
    for i in range(len(recent)):
        data = recent.iloc[i]
        c,h,l = data['Close'], data['High'], data['Low']
        pivots[i][0] = pivot(h,l,c, True)[0]
        pivots[i][1] = pivot(h,l,c, True)[1]
        date_str_list = [str(i) for i in str(recent.iloc[i])[-40:] if i.isnumeric()][0:8]
        date_str = ''
        for char in date_str_list:
            date_str += char
        idx.append(pd.to_datetime(date_str))

    
    df = pd.DataFrame(pivots, columns = ['PH', 'PL'], index = idx)
    df.to_csv('pivots.csv')

    


    #print('Pivot High: ' + str(()) +', Pivot Low: ' + str(()))
