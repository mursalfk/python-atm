#Importing Important libraries
import random
import time as t
import json
import datetime

def write_json_func(data, filename):
    """Function for writing data back in the JSON File"""
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4)  

def user_create(userid, username, name, pin, status, password, balance): 
    """Function for creating the user in JSON File"""
    with open('data.json') as json_file: 
        data = json.load(json_file) 
        temp = data['userdata'] 
        userdata_temp = {
            "id" : userid,
            "Username": username, 
            "Name": name,
            "Pin" : str(pin),
            "Account Status": status,
            "Password": password,
            "Balance": balance,
            "transactions": {}
        }
        temp.append(userdata_temp)
    write_json_func(data, filename='data.json')

def change_pwd_n_pin(post_signin, userid):
    """Updating the Password at Runtime"""   
    
    if post_signin == "1":
        key_word = "Password"
    elif post_signin == "2":
        key_word = "pin"            
            
    with open('data.json') as json_file: 
        data = json.load(json_file)
        filtered = list(filter(lambda f: (f["id"] == userid), data["userdata"]))

        new = input("Please enter your new %s: " %key_word)
        new_confirm = input("Please enter your new %s again: " %key_word)
        if new == new_confirm:
            print("%s Successfully Updated!" %key_word)
            filtered[0]["%s" %key_word] = new
        else:
            input("Your %s did not match. Please Start over and try again." %key_word)
    write_json_func(data, filename='data.json') 

def current_balance_func(current_id, current_password):
    """Function for Retrieving Live Current Balance of User"""
    with open('data.json') as json_file: 
        data = json.load(json_file) 
    for user in data['userdata']:
        if user['id']==current_id and user['Password'] == current_password:
            current_balance = user['Balance']
    return current_balance
    
def balance_inquiry(current_id, current_password):
    """Check Balance (Need Updatation)"""
    
    print("Your Current Balance is %s Rupeese." %current_balance_func(current_id, current_password) )

def add_balance(current_id, current_password):
    """Function to Add Balance"""
    with open('data.json') as json_file: 
        data = json.load(json_file)
        filtered = list(filter(lambda f: (f["id"] == current_id), data["userdata"]))
        add_balance = int(input("How much Balance You want to Add? "))
        new_balance = int(current_balance_func(current_id, current_password)) + int(add_balance)
        print("Balance Successfully Added!")
        filtered[0]["Balance"] = new_balance
        my_date = datetime.datetime.now()
        my_date_formatted = my_date.strftime('%Y-%m-%dT%H:%M:%S')
        filtered[0]["transactions"][str(my_date_formatted)] = "Added " + str(add_balance)    
    write_json_func(data, filename='data.json')

def withdrawal(current_id, current_password):
    """Function for withdrawal"""
    if current_balance_func(current_id, current_password) == 0:
        print("Sorry. Your Current Balance is 0")
    else: 
        with open('data.json') as json_file: 
            data = json.load(json_file)
            filtered = list(filter(lambda f: (f["id"] == current_id), data["userdata"]))
            balance_wihdrawl = int(input("How much Balance You want to Withdraw? "))
            if balance_wihdrawl > current_balance_func(current_id, current_password):
                print("You do not have sufficient balance.")
            else:
                new_balance = current_balance_func(current_id, current_password) - balance_wihdrawl
                print("Withdrawl Successful!")
                filtered[0]["Balance"] = new_balance
                my_date = datetime.datetime.now()
                my_date_formatted = my_date.strftime('%Y-%m-%dT%H:%M:%S')
                filtered[0]["transactions"][str(my_date_formatted)] = "Withdrawn " + str(balance_wihdrawl)
        write_json_func(data, filename='data.json') 

def print_history(data, userid_sign, current_password):
    """Function to print Transaction History"""
    with open('data.json') as json_file: 
        data = json.load(json_file) 
    for user in data['userdata']:
        if user['id']==userid_sign and user['Password'] == current_password:
            print("  < == == Transaction History == == >")
            for each in user['transactions']:
                print(each + " : " + user['transactions'][each])   

def signed_in(current_id, current_username, userid_sign, current_name, current_password, current_pin, current_balance, data):
    """When the user is signed in, now it decides what it has to do (it = user)"""
    current_username = userid_sign
    print("Hello Mr/Ms. " + current_name)
    post_signin = "1"
    while post_signin != "0":
        post_signin = input("""What would you like to do?
        1. Change Password
        2. Change Pin
        3. Balance Inquiry
        4. Add Balance
        5. Withdrawl
        6. Transaction History
        0. Signout
        """)
        if post_signin == "1":
            confirm_password = input("Please enter your current Password: ")
            if confirm_password == current_password:
                change_pwd_n_pin(post_signin, current_id)
            else:
                print("Please enter the correct password and start over. Thanks")
        
        elif post_signin == "2":
            confirm_pin = input("Please enter your current Pin: ")
            if confirm_pin == current_pin:
                change_pwd_n_pin(post_signin, current_id)
            else:
                print("Please enter the correct pin and start over. Thanks")

        elif post_signin == "3":
            balance_inquiry(current_id, current_password)

        elif post_signin == "4":
            add_balance(current_id, current_password)

        elif post_signin == "5":
            withdrawal(current_id, current_password)

        elif post_signin == "6":
            print_history(data, userid_sign, current_password)
        else:
            print("Please select a valid number")
    
def main():
    """The main function. i.e. The function when the user selects is s/he wants to sign-up/in untill he exits"""
    if curr_sel == "1" :
        name = input("Please state your name: ")
        password = input("Please input your password: ")
        userid = str(random.randint(10, 1000000))
        status = "Inactive"
        username = (name.replace(" ", "")).lower() + userid
        filename = 'user' + userid + '.txt'
        balance = 0
        print("[Creating Your Account...]")
        t.sleep(2.4)
        print("""Created.
        Your Account ID is """ + str(userid) + """. Please keep it safe. It will be used to sign.
        Thank You for creating your accouting with us. Here are your account details with us till now""")
        print("User ID : %s" %userid)
        print("Name : %s" %name)
        print("Username: %s" %username)
        print("Pin : " + "Not Created")
        print("Status: %s" %status)
        print("Password: %s" %password)
        print("Balance: %s" %balance)

        pin = int(input("Please input your 4 digit secret PIN Number: "))
        while pin < 1000 or pin > 9999:
            pin = int(input("Invalid Pin. Please Re-enter: "))
        else:
            status = "Active"
        print("Your account is now Activated!")
        userdata = {
            "id" : userid,
            "Name": name,
            "Username": username, 
            "pin" : pin,
            "Account Status": status,
            "Password": password,
            "Balance": balance,
            "transactions": {}
        }
       
        """User Creation"""
        user_create(userid, username, name, pin, status, password, balance)
    
    elif curr_sel == "2":
        userid_sign = input("Please enter your Userid: ")
        password_sign = input("Please enter your Password: ")
        print("Checking your credentials...")
        t.sleep(2.4)
        with open('data.json') as json_file: 
            data = json.load(json_file) 
        flag = 0
        for user in data['userdata']:
            if user['id']==userid_sign and user['Password'] == password_sign:
                print("Signedin")
                current_id = user['id']
                current_username = user['Username']
                current_name = user['Name']
                current_pin = user['Pin']
                current_status = user["Account Status"]
                current_password = user['Password']
                current_balance = user['Balance']
                flag =1
           
        if flag==0:
            print("No account found")
        elif flag == 1:
            signed_in(current_id, current_username, userid_sign, current_name, current_password, current_pin, current_balance, data)
            
    else:
        print("Please select a valid number")
        
if __name__ == "__main__":
    """Code starts execution from here."""
    print("Hello and Welcome")
    curr_sel = "1"
    while curr_sel!="0":
        curr_sel = input("""
        ***==> M A I N    M E N U <==***
        0 - Exit | 1- Signup | 2 - Signin
        """)
        main()
        
print("Thank you for banking with us!")
