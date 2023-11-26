# Travel Cost Tracker
#### Video Demo:
#### Description:
The Travel Cost Checker is a console applicationto track travel costs in any currency and automatically convert the cost into euro (EUR). This is very useful to track all costs while traveling and directly know their value in your home currency.
The user can input a name of the expense he wants to track and the cost and currency whereby USD is the default currency. The users can add as many expenses one after another as they want. When the user is finished with cost tracking, the sum of all expenses in euro is shown. The users also have the possibility to create a pdf file with all expenses. All expenses are saved in a csv-file. When starting the application, the users can specify if they want to add expenses to the existing costs from the last session or if they want to start freshly.

#### Tech Stack:
The application uses python in combination with several packages such as pandas, requests and fpdf2. The file "project.py" contains the backend of the app itself. The requirements.txt file contains all used packages. All expenses the user adds are written into a csv-file called "expenses.csv". The conversion of the costs into euro is done via the currency-exchange API by RapidAPI which returns the conversion rate from the user specified currency into euro. to The file "test_project.py" contains several tests to test three methods of project.py.
With help of the fpdf2-library a pdf-file called "travel_costs.pdf" can be created from the csv-file.

#### Design Choices:
The design of the pdf-file that can be created is kept simple and clear. The unique app logo gives it a unique touch. Through the clearness of the table, all costs can be quickly overviewed.
