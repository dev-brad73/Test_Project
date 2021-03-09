"""
The NL Chocolate Company needs a program to process salesperson travel claims when they return from a business trip.
As employees return from business trips they record all required information on a Travel Claim Form,
and return the form, with all invoices, to the main office.
The program will process the travel claims returned to the office.
Initialize a constant for Claim number (34) and the HST rate (15%).
Start by prompting the user to enter information from the Travel Claim Form including the employee number, name,
location of the trip, start date, end date, the number of days
(BONUS: rather than input the number of days use the start and end dates to calculate this value),
a value to indicate if they used their own car, or if a car was rented (O or R), and the total kilometers traveled.
Only enter the total kilometers if the employee used their own car. NOTE: No validations are required at this time.
Calculate the per diem amount by multiplying the total days by a daily rate of 85.00 for claims of 3 days or less,
or by a daily rate of $100.00 for claims of 4 or more days.
The mileage amount is calculated using a rate of .10 per kilometer if the salesperson used their car,
or a rate of $56.00 per day is the salesperson rented a car.
The Claim Amount is calculated as the Per Diem amount and the Mileage amount.
The HST is calculated on the per diem amount only.
The Claim Total is the Claim Amount plus the HST.
The program will display all input and calculated values to the screen as results.
Only display the mileage amount if it is calculated.
Just do a basic printout with headings and values.
Write all the input values and the calculated values to a file called Claims.dat – you can write one value per line
or create a comma separated file (CSV file).
Display a message for the user indicating that the claim information has been saved, and update the invoice
number by adding 1 to it.
Repeat the program until the user enters the word END for the employee number.
"""

# By:           Brad Rice
# Date:         March 8, 2021
# Project Name: Week10_Lesson1_NLChocolateCompany


import datetime
cur_date = datetime.datetime.now()


def save_data():
    outfile = open("Claims.dat", "a")

    outfile.write("Claim Number: " + str(CLAIM_NUM) + "\n")
    outfile.write("Employee Number: " + emp_num + "\n")
    outfile.write("Employee Name: " + emp_name + "\n")
    outfile.write("Trip Location: " + trip_loc + "\n")
    outfile.write("Date Start: " + date_startStr + "\n")
    outfile.write("Date End: " + date_endStr + "\n")
    outfile.write("Number of Days: " + str(days_num) + "\n")
    outfile.write("KM Traveled: " + str(km_trav) + "\n")
    outfile.write("Car Used (O for Own, R for Rental): " + car_used + "\n")
    outfile.write("Per Diem: " + per_diemPad + "\n")
    outfile.write("Mileage Paid: " + mile_amtPad + "\n")
    outfile.write("Claim amount: " + claim_amtPad + "\n")
    outfile.write("HST: " + hstPad + "\n")
    outfile.write("Claim Total: " + claim_totPad + "\n")
    outfile.write("\n")

    outfile.close()


# Constants:
HST = 0.15
CLAIM_NUM = 34

while True:

    # Inputs:

    emp_num = input("Employee number: ")
    if emp_num.upper() == "END":
        exit(0)
    emp_name = input("Employee name: ")
    trip_loc = input("Location of trip: ")
    date_startStr = input("Start date (YYYY-MM-DD): ")
    date_endStr = input("End date (YYYY-MM-DD): ")

    # Asking user whether they used their own car or a rental and only allowing them to answer with O or o for own
    # and R or r for rental
    car_used = input("Enter O for own car or R for rental: ")
    if car_used.upper() != "O" and car_used.upper() != "R":
        print("You must enter O or R")
        car_used = input("Enter O for own car or R for rental: ")

    km_trav = int(input("Kilometers traveled: "))

    # Processes:

    # Calculating number of days:
    date_start = datetime.datetime.strptime(date_startStr, "%Y-%m-%d")
    date_end = datetime.datetime.strptime(date_endStr, "%Y-%m-%d")
    days_num = (date_end - date_start).days

    # Calculating per diem amount:
    per_diem = 0
    if days_num <= 3:
        per_diem = 85 * days_num
    else:
        (per_diem) = 100 * days_num

    # Calculating mileage amount:
    mile_amt = 0
    if (car_used == "O") or (car_used == "o"):
        mile_amt = 0.1 * km_trav
    elif (car_used == "R") or (car_used == "r"):
        mile_amt = 56 * days_num

    # Calculating claim amount:
    claim_amt = per_diem + mile_amt

    # Calculating HST:
    hst = HST * per_diem

    # Calculating claim total:
    claim_tot = claim_amt + hst

    # Formatting:

    per_diemStr = "${:,.2f}".format(per_diem)
    per_diemPad = "{:>10}".format(per_diemStr)

    mile_amtStr = "${:,.2f}".format(mile_amt)
    mile_amtPad = "{:>10}".format(mile_amtStr)

    claim_amtStr = "${:,.2f}".format(claim_amt)
    claim_amtPad = "{:>10}".format(claim_amtStr)

    hstStr = "${:,.2f}".format(hst)
    hstPad = "{:>10}".format(hstStr)

    claim_totStr = "${:,.2f}".format(claim_tot)
    claim_totPad = "{:>10}".format(claim_totStr)

    # Outputs:

    print(" " * 28 + "NL Chocolate Company")
    print(" " * 30 + "Travel Claim Form")
    print()
    print()
    print("Employee Number:   {:<}".format(emp_num))
    print("Employee Name:     {:<}".format(emp_name))
    print()
    print("Trip Location:     {:<}".format(trip_loc))
    print("Start Date:        {:<}".format(date_startStr))
    print("End Date:          {:<}".format(date_endStr))
    print("Number of Days:    {:<}".format(days_num))
    print()
    if (car_used == "O") or (car_used == "o"):
        print("{:<} = Own car used".format(car_used))
    elif (car_used == "R") or (car_used == "r"):
        print("{:<} = Rental car used".format(car_used))
    print("Vehicle amount ={}".format(mile_amtPad))
    print()
    print()
    print(" " * 32 + "Per Diem Amount:           {}".format(per_diemPad))
    if car_used.upper() == "O":
        print(" " * 32 + "Mileage Amount:            {}".format(mile_amtPad))
    print(" " * 32 + "                         ------------")
    print(" " * 32 + "Subtotal:                  {}".format(claim_amtPad))
    print(" " * 32 + "HST @15%:                  {}".format(hstPad))
    print(" " * 32 + "                         ------------")
    print(" " * 32 + "Total Amount:              {}".format(claim_totPad))
    print()
    print()
    save_data()
    print("Claim information has been saved to the Claims.dat file.")
    CLAIM_NUM += 1
    print()
    print()
    Cont = input("Process another Claim (Y/N): ")
    if Cont.upper() == "Y":
        continue
    else:
        break
