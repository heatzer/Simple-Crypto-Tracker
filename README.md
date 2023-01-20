
# Simple Cryptocurrency Portfolio Tracker
#### Video Demo:  <https://youtu.be/X7eNbAXYfNs>
#### Description:
This is a simple Python project to track your Cryptocurrency trades (buy only) using coingecko public API to access historical prices of Cryptocurrency, see how much profit/ loss up to today and save your Cryptocurrency trades as a CSV file.
## Requirements
To run this project you need to install python on your computer and internet to access API, then install python packages below.
- requests
- re
- datetime
- pandas
- csv
## How to setup and run
After installing above packages, run the python.py file in the directory to start the project. Then user will prompt 4 options to select as below.
- Option 01 - Enter a transaction (buy)
- Option 02 - Display your transaction
- Option 03 - Save your transactions as a csv
- Option 04 - Exit

By choosing option 1 you can enter a Cryptocurrency transaction. Using "coin_list.csv" in the project directory, you can find the Cryptocurrency names as this csv contains all the cryptocurrencies listed as of 29-10-2022 in CoinGecko.

After successfully entering coin name, you will be prompt to enter date of transaction in 'dd-mm-yy' format and the amount bought.

You can repeat above step many times and finally you can see your transaction by selecting 2nd option.

If the you want to save your transactions as a csv file, you can select option 3 and it will be save as transactions.csv in project directory.

## Limitations
As a free API, this has a rate limit of 50 calls/minute. You might get error 429 for too many requests.