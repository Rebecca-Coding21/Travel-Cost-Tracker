from project import check_exit, split_cost, calculate_expense_sum, get_exchange_rate
import pytest

def test_check_exit():
    assert check_exit("n") == True
    assert check_exit("N") == True
    assert check_exit("a") == False

def test_split_cost():
    cost_string, currency = split_cost("15 USD")
    assert cost_string == "15"
    assert currency == "USD"

    cost_string, currency = split_cost("15")
    assert cost_string == "15"
    assert currency == "USD"

def test_get_exchange_rate():
    try:
        get_exchange_rate(15, "USD")
    except:
        pytest.fail("API connection problem")


