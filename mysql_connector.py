import mysql.connector
from keys import mysql_password
from get_data import get_data
import pprint
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Connect to the MySQL server
cnx = mysql.connector.connect(user='root', password=mysql_password,
                              host='34.124.218.228',
                              database='spysql')

# Create a cursor object
cursor = cnx.cursor()


def check_last_five():

    # Execute a query
    cursor.execute('SELECT * FROM spysql.stock_prices ORDER BY Date DESC limit 5;')

    # Fetch all the results
    results = cursor.fetchall()
    pprint.pprint(results)

    # Close the cursor and connection
    cursor.close()
    cnx.close()

@get_data()
def insert_data(get_data):
    try:
        #insert data
        data_to_insert = get_data()
        cursor.execute("INSERT INTO stock_prices (Date, Open, High, Low, Close, Adj_Close, Volume) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                       (data_to_insert[0],int(data_to_insert[1]),int(data_to_insert[2]),
                        int(data_to_insert[3]),int(data_to_insert[4]),int(data_to_insert[5]),int(data_to_insert[6])))
    except:
        print('Error, check if the date inserted is duplicated')

    cnx.commit()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

def train_model():

    cursor.execute('SELECT * FROM spysql.stock_prices ORDER BY Date DESC limit 300;')
    data = cursor.fetchall()
    columns = [col[0] for col in cursor.description]

    cursor.close()
    cnx.close()

    #data prepping
    train = pd.DataFrame(data, columns=columns)
    train = train.sort_values(by='Date', ascending=True)
    train.index = train.Date
    train = train.drop('Date', axis=1)

    # transform into stationary data
    ts_diff = train['Close'] - train['Close'].shift(-1)
    ts_diff = ts_diff.fillna(0.0)

    # Fit the model
    model = ARIMA(ts_diff, order=([50, 20, 7], 1, 3), missing='drop')
    model_fit = model.fit()

    # Make predictions
    future_forecast = model_fit.forecast(steps=1, signal_only=False)
    value = str(future_forecast).split()[1]

    if float(value) > 0:
        return 'higher'
    else:
        return 'lower'
