import csv
import pandas as pd
import requests
from fpdf import FPDF
import os

class Expense():
    def __init__(self, name, cost, currency):
        self.name = name
        self.cost = cost
        self.currency = currency

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "BU", 28)
        self.image("Logo.png",95, 20, 20)
        self.ln(15)
        #Title centered
        self.cell(0,60,"Travel Costs", border=0, align="C")
        #line break
        self.ln(45)

def main():
    print("Welcome to Travel Cost Tracker! You can use this application to track your travel costs.")
    exit_key = False
    check_csv_status()

    # check if user wants to continue to add expenses
    while exit_key == False:
        expense_name, cost, currency = get_user_input()
        currency = currency.upper()

        if currency == "EUR":
            converted_cost = cost
        else:
            conversion_rate = get_exchange_rate(cost, currency)
            converted_cost = round(conversion_rate * cost, 2)

        expense = Expense(expense_name, converted_cost, currency)
        add_expense(expense)

        exit_key = check_exit(input("Do you want to continue (y/n): "))

    total_expenses = calculate_expense_sum()

    print(f"Total Expenses: {total_expenses} EUR")
    pdf_answer = input("Do you want to create a PDF-file of your travel costs (y/n): ")

    # Create pdf-file if user answers with "y"
    if pdf_answer.lower() == "y":
        create_pdf(total_expenses)

def get_user_input():
    """
        Get user input for expense name and cost.
    """

    expense_name = input("Expense Name: ")
    print("You can enter the cost in any currency, specified by its abbreviation (USD, EUR, etc.)-> Default = USD")
    expense_string = input("Expense: ")
    cost_string, currency = split_cost(expense_string)

    try:
        cost = float(cost_string)
    except:
        print("Please input float number + currency for cost!")
        get_user_input()

    return expense_name, cost, currency

def check_exit(answer):
    """
        Check user input to add more expenses or exit the application.
    """

    if answer.lower() == "n":
        return True
    else:
        return False

def split_cost(expense_string):
    """
        Split string into two parts (Cost, Currency).
    """

    cost_string = ""
    currency = ""

    try:
        cost_string, currency = expense_string.split(" ")
    except:
        cost_string = expense_string
        currency = "USD"

    return cost_string, currency

def get_exchange_rate(cost, currency):
    """
        Call RapidAPI to get the current exchange rate from the user-specified currency into euro.
    """

    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from":currency,"to":"EUR","q":cost}

    headers = {
	"X-RapidAPI-Key": "d2f8bbb60cmshcce60aa176e5229p16278bjsnf4d636896200",
	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        raise Exception("API connection failed!")

    conversion_rate = response.json()

    return conversion_rate

def add_expense(expense):
     """
        Add expenses to the csv-file.
     """

     with open("expenses.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["expense_name", "cost"])
        writer.writerow({"expense_name": expense.name, "cost": expense.cost})


def check_csv_status():
    """
        Check if the csv-file is empty. If not the user can specify if he wants to continue with that file, else the existing csv-file is erased and a new empty file with header is created.
    """

    try:
        csv_file = pd.read_csv("expenses.csv")
    except:
        with open("expenses.csv", "w") as csv_file:
            csv_file.write("Expense Name, Cost [EUR]\r\n")

        csv_file = pd.read_csv("expenses.csv")

    if csv_file.empty == False:
        existing_csv = input(("Do you want to resume the existing expense list (y) or overwrite it (n): "))

        if existing_csv.lower() == "n":
            # delete existing csv-file
            os.remove("expenses.csv")
            with open("expenses.csv", "w") as csv_file:
                csv_file.write("Expense Name, Cost [EUR]\r\n")

def calculate_expense_sum():
    """
        Calculate the sum of all expenses.
    """

    expense_sum = 0
    with open("expenses.csv", "r") as csv_file:
        next(csv_file)

        for line in csv_file:
            name, cost = line.rstrip().split(",")
            expense_sum += float(cost)

    expense_sum = round(expense_sum, 2)

    return expense_sum


def create_pdf(total_expenses):
    """
        Create a pdf-file from all expenses in the csv-file.
    """

    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("Helvetica", size=12)
    pdf.set_text_color(0,0,0)
    col_width = 80
    num_cols = 2
    total_table_width = col_width * num_cols
    margin_left = (pdf.w - total_table_width) / 2  # Centering the table
    line_height = pdf.font_size * 2.5

    with open("expenses.csv", "r") as csv_file:
        for line in csv_file:
            row = line.rstrip().split(",")
            pdf.set_x(margin_left)
            for entry in row:
                pdf.multi_cell(col_width,line_height,entry,border=1,new_x="RIGHT", new_y="TOP", align="C")
            pdf.ln(line_height)
    pdf.set_font("Helvetica","BU", size=12)
    pdf.cell(0,20, f"Total Travel Costs: {total_expenses} EUR", align="R")

    pdf.output("travel_costs.pdf")

if __name__ == "__main__":
    main()
