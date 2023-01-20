import requests
import re
from datetime import datetime
import pandas as pd
import csv

# create empty list to store data
CRYPTO = []
DATE = []
PRICE = []
AMOUNT = []
PROFIT_LOSS = []

def main():
    option = -1
    # run loop while user enter 0 as option
    while option != 0:    
        print("Welcome to Cryptocurrency portfolio tracker")
        print("1. Enter a transaction (buy)")
        print("2. Display your transactions")
        print("3. Save your transactions as a csv")
        print("0. Exit")
        try:
            option = int(input("Please choose an option: "))
            if option == 1:
                while True:
                    # prompt user to enter a cryptocurrency name
                    user_coin_name = input("Enter coin name: ").strip()                   
                    # checking for valid cryptocurrency
                    if check_user_coin(user_coin_name) == False:
                        print("Invalid cryptocurrency, Please re enter")
                        continue
                    else:
                        break
                # assigning coin id as in Coingecko API
                id = get_user_coin_id(user_coin_name)
                while True:
                    # prompt user to enter date in 'dd-mm-yyyy' foramt
                    date = input("Enter the date in format 'dd-mm-yyyy': ")
                    # check user enters date in correct format
                    if check_date(date) == False:
                        print("Invalid date! Please re-enter date in the correct format 'dd-mm-yyyy':")
                        continue
                    # check whether user enters date on or above 28-04-2013
                    elif check_date(date) == "no data":
                        print("Please enter a date on or above 28-04-2013")
                        continue
                    break

                try:
                    # assigning amount user enters
                    amount = float(input("Enter amount: "))
                    # calculating the transaction price
                    price = get_price(id, date, amount)
                    # assigning today in dd-mm-yyyy format
                    TODAY = change_today_format()
                    # calculating transaction is profit/ loss
                    profit_or_loss = get_price(id, TODAY, amount) - price
                    # assiging each data to lists
                    add_expense(date, user_coin_name, amount, price, profit_or_loss)
                    # create a data frame 
                    df = pd.DataFrame()
                    df["Cyrpto"] = CRYPTO
                    df["Date"] = DATE
                    df["Amount"] = AMOUNT
                    df["Price (USD)"] = PRICE
                    df["P&L (USD)"] = PROFIT_LOSS
                    print()
                except:
                    # if user enters a date with no data on that date in Coingecko
                    print(f"{user_coin_name} doesn't have data on {date} \n")
                    continue
            elif option == 2:
                try:
                    # print user's transactions
                    print(df)
                    print()
                except:
                    # incase user did not enter any transactions
                    print("Please enter some transactions to diplay \n")
            elif option == 3:
                try:
                    # saving transactions as a csv
                    df.to_csv('transactions.csv')
                except:
                    # incase user did not enter any transactions
                    print("Please enter some transactions befor saving \n")
            elif option == 0:
                # exiting program
                print("Thank You...")
                break
            else:
                # if user enters an invalid option
                print("Invalid option. Please enter 1, 2, 3 or 0 options: \n")
                continue
        except:
            continue

# checking user entered coin is valid from coin_list.csv
def check_user_coin(user_coin):
    # opening coin_list.csv which contains coins listed in coingecko as of 29-10-2022
    with open('coin_list.csv', encoding='utf8') as file:
        reader = csv.DictReader(file)
        # read each row of csv file
        for coin in reader:
            # check if user enterd coin is present in name column in coin_list.csv
            if re.search(rf"^{user_coin}$", coin["name"], re.IGNORECASE):
                return True
    return False

# getting user entered coin id for coingecko API
def get_user_coin_id(user_coin):
    with open('coin_list.csv', encoding='utf8') as file:
        reader = csv.DictReader(file)
        for coin in reader:
            if re.search(rf"^{user_coin}$", coin["name"], re.IGNORECASE):
                # assigning coin ID of user entered coin
                coin_id = coin["id"]
                return coin_id

def check_date(input_date):
    try:
        fdate = datetime.strptime(input_date, "%d-%m-%Y")
        present_day = datetime.today()
        # first date of historical data cointains in coingecko
        first_day = datetime.strptime("28-04-2013", "%d-%m-%Y")
        # chek if user enters a date before today and after 28-04-2013
        if fdate.date() <= present_day.date() and first_day.date() <= fdate.date():
            return True
        elif first_day.date() >= fdate.date():
            return "no data"

    except ValueError:
        # when user doesn't enter a valid date
        return False

    return False

def change_today_format():
    today = datetime.today()
    today_year = today.strftime("%Y")
    today_month = today.strftime("%m")
    today_date = today.strftime("%d")
    return f"{today_date}-{today_month}-{today_year}"

def get_price(coin_id, date, amount):
    # url from Coingecko API to obtain historical data of a cryptocurrency
    url_history_data = f"https://api.coingecko.com/api/v3/coins/{coin_id}/history?date={date}"
    new_response = requests.get(url_history_data)
    # create a json object
    new_o = new_response.json()
    # get the price in a specific date
    price = new_o["market_data"]["current_price"]["usd"]
    return price*amount

# appending date, cyrpto_name, amount, price, profit_or_loss to global lists created
def add_expense(date, cyrpto_name, amount, price, profit_or_loss):
    DATE.append(date)
    CRYPTO.append(cyrpto_name)
    PRICE.append(price)
    AMOUNT.append(amount)
    PROFIT_LOSS.append(profit_or_loss)

if __name__ == "__main__":
    main()
   