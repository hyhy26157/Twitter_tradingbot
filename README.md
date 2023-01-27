# Twitter_tradingbot
To create a twitter trading bot using ML model that gets data from mysql.

A fun little project I create to learn about how to upload and pull data from mysql database using python.

Things required
1) twitter developer account
2) mysql account

yfinance is a Python library that allows developers to easily pull stock market data such as historical prices, financial statements, and news articles.
MySQL is one of the most popular open-source relational database management systems and is widely used in web applications and data analytics projects.

One of the main reasons to use MySQL for storing financial data is its scalability and robustness. 
MySQL is able to handle large amounts of data and can be easily integrated into a variety of programming languages and frameworks. 
Additionally, MySQL offers a variety of built-in security features and can be easily backed up and restored, making it a great choice for mission-critical data.

By storing financial data in a SQL database, we can easily query and analyze the data using SQL commands.
This allows us to make sense of stock market trends and performance by creating custom reports and visualizations.
Additionally, by storing financial data in a SQL database, we can easily integrate it into other applications and tools for further analysis.
The process for getting your financial data from yfinance into a MySQL database will depend on the specifics of your project. 

A simple train_model function uses ARIMA (AutoRegressive Integrated Moving Average) which is particularly well-suited for time series data, 
is used to determine for the trend of the stock. The model will return an string output of 'higher' or 'lower' by comparing its
current day prediction with the previous day result.To further improve the model, we can run a backtest or compare it with other models type.

The output from the ARIMA model will past to python post_tweet function that generate a twitter post to mention if the stock will go higher or 
lower and post it as a tweet.

I used a microsoft task scheduler to execute the script on daily basis, however, this will only work if the computer is not in OFF mode when the scheduler is triggered.
To get past that, we can do a cron job using cloud to schedule the script.

See the result here at https://twitter.com/MoversMomentum
