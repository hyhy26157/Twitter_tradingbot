from datetime import date,timedelta
import yfinance as yf
import pandas as pd

# "2023-01-11", 392.20, 395.6, 391.38, 395.5, 395.5, 68881100.0
def get_data(days = 1):
    #get data from yfinance
    data = yf.download("SPY",
                       start=date.today()- timedelta(days),
                        end=date.today(),
                       )

    data = pd.DataFrame(data)

    return str(data.index)[16:26],round(data.Open,2)[0],round(data.High,2)[0],round(data.Low,2)[0],round(data.Close,2)[0],round(data['Adj Close'],2)[0],round(data.Volume,2)[0]
