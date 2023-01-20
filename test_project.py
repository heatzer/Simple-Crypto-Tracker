from project import check_date, check_user_coin, get_user_coin_id

def main():
    # test_check_date()
    test_check_user_coin()

# testing date format
def test_check_date():
    assert check_date("11-10-2021") == True
    assert check_date("31-11-2021") == False
    assert check_date("29-02-2020") == True
    assert check_date("01/08/2010") == False
    assert check_date("11th of January, 2022") == False
    assert check_date("23-04-2013") == "no data"

# testing valid cryptocurrencies
def test_check_user_coin():
    assert check_user_coin("bitcoin") == True
    assert check_user_coin("bnb") == True
    assert check_user_coin("BNb") == True
    assert check_user_coin("cardano") == True
    assert check_user_coin("crypt") == False
    assert check_user_coin("%$1") == False

# testing for coin ID field
def test_get_user_coin_id():    
    assert get_user_coin_id("bitcoin") == "bitcoin"
    assert get_user_coin_id("bnb") == "binancecoin"
    assert get_user_coin_id("cardano") == "cardano"
    assert get_user_coin_id("PancakeSwap") == "pancakeswap-token"

if __name__ == "__main__":
    main()