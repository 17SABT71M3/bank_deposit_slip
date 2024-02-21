from pydone import create_field_data_dict
from pydone import fill_pdf
import shlex
from datetime import datetime
import os


# NUMBERS TO WORDS CONVERSION IN PYTHON (INDIAN NUMBER SYSTEM)

def words(n):
    units = ['Zero', 'One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Ninteen']
    tens = ['Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
    if n>=0 and n<=9:
        return units[n]
    elif n>=10 and n<=19:
        return teens[n-10]
    elif n>=20 and n<=99:
        return tens[(n//10)-2] + " " + (units[n%10] if n%10!=0 else "")
    elif n>=100 and n<=999:
        return units[n//100] + " Hundred " + (words(n%100) if n%100!=0 else "")
    elif n>=1000 and n<=99999:
        return words(n//1000) + " Thousand " + (words(n%1000) if n%1000!=0 else "")
    elif n>=100000 and n<=9999999:
        return words(n//100000) + " Lakh "+(words(n%100000) if n%100000!=0 else "") 
    elif n>=10000000 and n<=99999999999:
        return words(n//10000000) + " Crore " + (words(n%10000000) if n%10000000!=0 else "")
    else:
        return 'Provide a valid number from one digit to eleven digits.'
    

# Sample field_names_data dictionary
cheque_names_data = {
    'Cheque Number for Line 1': ['Cheque No', 'Cheque No 8'],
    'Cheque Number for Line 2': ['Cheque No 2', 'Cheque No 9'],
    'Cheque Number for Line 3': ['Cheque No 3', 'Cheque No 10'],
    'Cheque Number for Line 4': ['Cheque No 4', 'Cheque No 11'],
    'Cheque Number for Line 5': ['Cheque No 5', 'Cheque No 12'],
    'Cheque Number for Line 6': ['Cheque No 6', 'Cheque No 13'],
    'Cheque Number for Line 7': ['Cheque No 7', 'Cheque No 14'],
}

cheque_details_data = {
    'Details Line 1': ['Cash/Cheque details', 'Bank & Branch'],
    'Details Line 2': ['Cash/Cheque details 2', 'Bank & Branch 2'],
    'Details Line 3': ['Cash/Cheque details 3', 'Bank & Branch 3'],
    'Details Line 4': ['Cash/Cheque details 4', 'Bank & Branch 4'],
    'Details Line 5': ['Cash/Cheque details 5', 'Bank & Branch 5'],
    'Details Line 6': ['Cash/Cheque details 6', 'Bank & Branch 6'],
    'Details Line 7': ['Cash/Cheque details 7', 'Bank & Branch 7'],
}

name_data = {
    'Payee name': ['Name', 'Name 2']
}

phone_number_data = {
    'Contact No': ['Contact No']
}
account_number1 = {
    'Account No': ['Account No', 'Account No 4'],
    'Account No 4': ['Account No 2', 'Account No 5'],

}
account_number2 = {
    'Account No 2': ['Account No', 'Account No 4'],
    'Account No 5': ['Account No 2', 'Account No 5'],

}
account_number3 = {
    'Account No 3': ['Account No', 'Account No 4'],
    'Account No 6': ['Account No 2', 'Account No 5'],

}
loan_account_number = {
    'Loan Account No': ['Account No', 'Account No 4'],
    'Loan Account No 2': ['Account No 2', 'Account No 5'],

}
rupees_data = {
    'Rupees Line 1': ['Rupees', 'Text49'],
    'Rupees Line 2': ['Rupees 2', 'Text51'],
    'Rupees Line 3': ['Rupees 3', 'Text53'],
    'Rupees Line 4': ['Rupees 4', 'Text55'],
    'Rupees Line 5': ['Rupees 5', 'Text57'],
    'Rupees Line 6': ['Rupees 6', 'Text59'],
    'Rupees Line 7': ['Rupees 7', 'Text61'],
    'Rupees Line 8': ['Rupees 7', 'Text63']
}
denomination_data = {
    'Denomination 2000x': ['Text48'],
    'Denomination 500x': ['Text50'],
    'Denomination 200x': ['Text52'],
    'Denomination 100x': ['Text54'],
    'Denomination 50x': ['Text56'],
    'Denomination 20x': ['Text58'],
    'Denomination 10x': ['Text60'],
    'Denomination Others': ['Text62']
}
total_in_words_data = {
    'Rupees In Words': ['Rupees in words 2', 'Rupees in words']
}
day_data = {
    'Day': ['Day', 'Day 1']
}
month_data = {
    'Month': ['Month', 'Month 2']
}
year_data = {
    'Year': ['Year', 'Year 2']
}
total_data = {
    'Total Amt': ['Total', 'Text64']
}
depositor_name_data = {
    'Depositor Name': ['Depositor Name', 'Name 4']
}
city_data = {

    'City': [ 'City' ],
    'City 2': [ 'City 2' ],
    'City 3': [ 'City 3' ],
    'City 4': [ 'City 4' ],
    'City 5': [ 'City 5' ],
    'City 6': [ 'City 6' ],
    'City 7': [ 'City 7' ],

}


if __name__ == "__main__":
    

    # Initialize an empty string
    result_string = ""

    current_datetime = datetime.now()

    # Extract day, month, and year
    current_day = current_datetime.day
    current_month = current_datetime.month
    current_year = current_datetime.year

    while True:
        loan_account = input("Loan Account no: ")

        # Check if the input is empty
        if loan_account == '':
            break  # Exit the loop if the input is empty

        # Try to convert the input to a float
        try:
            numeric_value = int(loan_account)
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    loan_account_number['Loan Account No'][0] = loan_account
    loan_account_number['Loan Account No 2'][0] = loan_account
    for key, values in loan_account_number.items():
        result_string += f'"{key}" "{values[0]}" '
    # Loop through each cheque in the dictionary
    field_names_data_list = [ name_data, rupees_data ]
    while True:
        input_account = input("Account no: ")

        # Check if the input is empty
        if input_account == '':
            break  # Exit the loop if the input is empty

        # Try to convert the input to a float
        try:
            numeric_value = int(input_account)
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    input_account = str(input_account)
    input_acc1 = input_account[:4]
    input_acc2 = input_account[4:7]
    input_acc3 = input_account[7:14]
    account_number1['Account No'][0] = input_acc1
    account_number1['Account No 4'][0] = input_acc1
    account_number2['Account No 2'][0] = input_acc2
    account_number2['Account No 5'][0] = input_acc2
    account_number3['Account No 3'][0] = input_acc3
    account_number3['Account No 6'][0] = input_acc3

    for key, values in account_number1.items():
        result_string += f'"{key}" "{values[0]}" '
    for key, values in account_number2.items():
        result_string += f'"{key}" "{values[0]}" '
    for key, values in account_number3.items():
        result_string += f'"{key}" "{values[0]}" '
    while True:
        input_total = input("Total: ")

        # Check if the input is empty
        if input_total == '':
            break  # Exit the loop if the input is empty

        # Try to convert the input to a float
        try:
            numeric_value = float(input_total)
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    total_data['Total Amt'][0] = input_total 
    total_data['Total Amt'][1] = input_total  
    result_string += f'"Total" "{input_total}" "Text64" "{input_total}" '
    more_field_names_list = [ cheque_names_data ]
    some_more_field_data = [ cheque_details_data ]
    depositor_info_list = [ phone_number_data, depositor_name_data ]
    cheque_more_field_data = [ city_data ]
    year_data['Year'] = [current_year, current_year]
    
    for key, values in year_data.items():
        result_string += f'"{key}" "{values[0]}" "{key} 2" "{values[1]}" '
        
    month_data['Month'] = [current_month, current_month]
    for key, values in month_data.items():
        result_string += f'"{key}" "{values[0]}" "{key} 2" "{values[1]}" '
        
    day_data['Day'] = [current_day, current_day]
    for key, values in day_data.items():
        result_string += f'"{key}" "{values[0]}" "{key} 1" "{values[1]}" '

    
    for data_dict in field_names_data_list:
        for key, values in data_dict.items():
            # Ask the user to enter a number for the current key
            user_input = input(f"{key}: ")

            # Append elements to the result_string based on user input
            if len(values) > 0:
                result_string += f'"{values[0]}" "{user_input}" '
                data_dict[key][0] = user_input
            if len(values) > 1:
                result_string += f'"{values[1]}" "{user_input}" '
                data_dict[key][1] = user_input



    
    os.system('cls')
    print("Enter Cheque Numbers :")
    input("_________________________________")
    for data_dict in more_field_names_list:
        for key, values in data_dict.items():
            # Ask the user to enter a number for the current key
            user_input = input(f"{key}: ")

            # Append elements to the result_string based on user input
            if len(values) > 0:
                result_string += f'"{values[0]}" "{user_input}" '
                data_dict[key][0] = user_input
            if len(values) > 1:
                result_string += f'"{values[1]}" "{user_input}" '
                data_dict[key][1] = user_input
    os.system('cls')
    print("Enter Cheque Details :")
    input("_________________________________")
    for data_dict in some_more_field_data:
        for key, values in data_dict.items():
            # Ask the user to enter a number for the current key
            user_input = input(f"{key}: ")

            # Append elements to the result_string based on user input
            if len(values) > 0:
                result_string += f'"{values[0]}" "{user_input.upper()}" '
                data_dict[key][0] = user_input
            if len(values) > 1:
                result_string += f'"{values[1]}" "{user_input.upper()}" '
                data_dict[key][1] = user_input
    os.system('cls')
    input("")
    for data_dict in cheque_more_field_data:
        for key, values in data_dict.items():
            # Ask the user to enter a number for the current key
            user_input = input(f"{key}: ")
            # Append elements to the result_string based on user input
            if len(values) > 0:
                result_string += f'"{values[0]}" "{user_input.upper()}" '
                data_dict[key][0] = user_input
            if len(values) > 1:
                result_string += f'"{values[1]}" "{user_input.upper()}" '
                data_dict[key][1] = user_input
    os.system('cls')
    print("Enter Depositor Details:")
    input("_________________________________")
    for data_dict in depositor_info_list:
        for key, values in data_dict.items():
            # Ask the user to enter a number for the current key
            user_input = input(f"{key}: ")

            # Append elements to the result_string based on user input
            if len(values) > 0:
                result_string += f'"{values[0]}" "{user_input.upper()}" '
                data_dict[key][0] = user_input
            if len(values) > 1:
                result_string += f'"{values[1]}" "{user_input.upper()}" '
                data_dict[key][1] = user_input


  
    if 'Total Amt' in total_data:
        # Code to execute when the key exists
        total_amt_value = total_data['Total Amt'][0]
        if total_amt_value != '':
            total_amt_value = int(total_amt_value)

            result = words(total_amt_value)
            result_string += f'"{total_in_words_data["Rupees In Words"][0]}" "{result} only" '
            result_string += f'"{total_in_words_data["Rupees In Words"][1]}" "{result} only" '

    field_data_dict = create_field_data_dict(result_string)
    # Print the final result_string
    print("result stored in output_hdfc_bank_slip39012.pdf")
    fill_pdf('example.pdf','output_hdfc_bank_slip39012.pdf',field_data_dict)
