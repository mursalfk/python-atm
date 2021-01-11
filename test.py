import random
import time as t
import json
import datetime
     
def main():
    if curr_sel == "1" :
        name = input("Please state your name: ")
        password = input("Please input your password: ")
        userid = str(random.randint(10, 1000000))
        status = "Inactive"
        username = (name.replace(" ", "")).lower() + userid
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
       
    #  File Creation
        
        def write_json(data, filename='data.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
        with open('data.json') as json_file: 
            data = json.load(json_file) 
            temp = data['userdata'] 
            userdata_temp = {
                "id" : userid,
                "Username": username, 
                "Name": name,
                "pin" : str(pin),
                "Account Status": status,
                "Password": password,
                "Balance": balance,
                "transactions": {}
            }
            temp.append(userdata_temp)
        write_json(data)       
        
        def write_json1(data, filename='transactions.json'): 
            with open(filename,'w') as f: 
                json.dump(data, f, indent=4) 
        with open('transactions.json') as json1_file: 
            data1 = json.load(json1_file) 
            temp = data1['transactions'] 
            userdata_temp = {
                "id" : userid,
                "signup": str(datetime.datetime.now())
            }
            temp.append(userdata_temp)
        write_json1(data1)
    
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
                current_pin = user['pin']
                current_status = user["Account Status"]
                current_password = user['Password']
                current_balance = user['Balance']
                flag =1
        if flag==0:
            print("No account found")            
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
                    def write_json(data, filename='data.json'): 
                        with open(filename,'w') as f: 
                            json.dump(data, f, indent=4) 
                    with open('data.json') as json_file: 
                        data = json.load(json_file)
                        userid = input("Please enter your Userid Again: ")
                        filtered = list(filter(lambda f: (f["id"] == userid), data["userdata"]))
                        newpass = input("Please enter your new password: ")
                        newpass_confirm = input("Please enter your new password again: ")
                        if newpass == newpass_confirm:
                            print("Password Successfully Updated!")
                            filtered[0]["Password"] = newpass
                        else:
                            input("Your Passswords did not match. Please Start over and try again.")
                    write_json(data) 
                else:
                    print("Please enter the correct password and start over. Thanks")
                    
            elif post_signin == "2":
                confirm_pin = input("Please enter your current Pin: ")
                if confirm_pin == current_pin:
                    def write_json(data, filename='data.json'): 
                        with open(filename,'w') as f: 
                            json.dump(data, f, indent=4) 
                    with open('data.json') as json_file: 
                        data = json.load(json_file)
                        userid = input("Please enter your Userid Again: ")
                        filtered = list(filter(lambda f: (f["id"] == userid), data["userdata"]))
                        newpin = input("Please enter your new Pin: ")
                        newpin_confirm = input("Please enter your new Pin again: ")
                        if newpin == newpin_confirm:
                            print("Pin Successfully Updated!")
                            filtered[0]["pin"] = newpin
                        else:
                            input("Your Entered Pin Codes did not match. Please Start over and try again.")
                    write_json(data) 
                else:
                    print("Please enter the correct pin code and start over. Thanks")
                    
            elif post_signin == "3":
                print("Your Current Balance is %s Rupees." %current_balance ) 
                
            elif post_signin == "4":
                def write_json(data, filename='data.json'): 
                    with open(filename,'w') as f: 
                        json.dump(data, f, indent=4) 
                with open('data.json') as json_file: 
                    data = json.load(json_file)
                    userid = input("Please enter your Userid Again: ")
                    filtered = list(filter(lambda f: (f["id"] == userid), data["userdata"]))
                    add_balance = int(input("How much Balance You want to Add? "))
                    new_balance = int(current_balance) + int(add_balance)
                    print("Balance Successfully Added!")
                    filtered[0]["Balance"] = new_balance
                    my_date = datetime.datetime.now()
                    my_date_formatted = my_date.strftime('%Y-%m-%dT%H:%M:%S')
                    filtered[0]["transactions"][str(my_date_formatted)] = "Added " + str(add_balance)
                write_json(data) 
                
            elif post_signin == "5":
                if current_balance == 0:
                    print("Sorry. Your Current Balance is 0")
                else:
                    def write_json(data, filename='data.json'): 
                        with open(filename,'w') as f: 
                            json.dump(data, f, indent=4) 
                    with open('data.json') as json_file: 
                        data = json.load(json_file)
                        userid = input("Please enter your Userid Again: ")
                        filtered = list(filter(lambda f: (f["id"] == userid), data["userdata"]))
                        balance_wihdrawl = int(input("How much Balance You want to Withdraw? "))
                        if balance_wihdrawl > current_balance:
                            print("You do not have sufficient balance.")
                        else:
                            new_balance = current_balance - balance_wihdrawl
                            print("Withdrawl Successful!")
                            filtered[0]["Balance"] = new_balance
                            my_date = datetime.datetime.now()
                            my_date_formatted = my_date.strftime('%Y-%m-%dT%H:%M:%S')
                            filtered[0]["transactions"][str(my_date_formatted)] = "Withdrawn " + str(balance_wihdrawl)
                    write_json(data) 
    
            elif post_signin == "6":
                for user in data['userdata']:
                    if user['id']==userid_sign:
                        print("Transaction History:")
                        for each in user['transactions']:
                            print(each + " : " + user['transactions'][each])

if __name__ == "__main__":
    print("Hello and Welcome")
    curr_sel = "1"
    while curr_sel!="0":
        curr_sel = input("""
        ***==> M A I N    M E N U <==***
        0 - Exit | 1- Signup | 2 - Signin
        """)
        main()
        
print("Thank you for banking with us!")


# Function => Class => Enhancing => 