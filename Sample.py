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