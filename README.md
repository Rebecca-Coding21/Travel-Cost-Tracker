# Travel Cost Tracker

![Logo_small](https://github.com/Rebecca-Coding21/Travel-Cost-Tracker/assets/94243632/e89d5023-d599-4102-a2f3-a93ebcd86c04)

#### Video Demo: https://www.youtube.com/watch?v=GD9rrEy3XZk

#### Description:
The Travel Cost Tracker is a console application to track travel costs in any currency and automatically convert the costs into euro (EUR). This is very useful to track all costs while traveling and directly know their value in your home currency.
The user can input a name of the expense he wants to track and the cost and currency whereby USD is the default currency. The users can add as many expenses, one after another, as they want. When the user is finished with cost tracking, the sum of all expenses is shown in euro. The user also has the possibility to create a pdf file with all expenses. All expenses are saved in a csv-file. When starting the application, the user can specify if he wants to add expenses to the existing costs from the last session or if he wants to start freshly.

#### Tech Stack:
The application uses python in combination with several packages such as pandas, requests and fpdf2. The file "project.py" contains the backend of the app itself. The requirements.txt file contains all used packages. All expenses the user adds are written into a csv-file called "expenses.csv". The conversion of the costs into euro is done via the currency-exchange API by RapidAPI which returns the current conversion rate from the user specified currency into euro. The file "test_project.py" contains several unit tests to test three functions of project.py.
With help of the fpdf2-library a pdf-file called "travel_costs.pdf" can be created from the added expenses.

#### Design Choices:
The design of the pdf-file that can be created is kept simple and clear. The unique app logo gives it a individual touch. Through the clearness of the table, all costs can be quickly overviewed.

![image](https://github.com/Rebecca-Coding21/Travel-Cost-Tracker/assets/94243632/1768f605-0ab2-4dda-b7de-ddc763625605)

#### Important Information:
To use the application you need to generate your own API key on rapid API and exchange it with the current API key.
