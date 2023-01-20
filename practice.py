login_in_database = "sarylbekovaziret@gmail.com"
password_in_database = "123"

print("Hello")
login = input("Enter login:").strip()
password = input("Enter password:").strip()

login_check = login == login_in_database  # запрашиваем логин
password_check = password == password_in_database
if login_check and password_check:
    print("Correctly")
else:
    print("Invalid password or login")

# проверяем банков. карточку
card_bank = input("Enter bank card:").strip()

if not card_bank.isalpha() and len(card_bank) == 5:
    print("digit")
else:
    print("Non't digit")

# check phone number
phone_num = input("Enter phone number:")

if (phone_num.startswith("996") or phone_num.startswith("0")) and (len(16) or len(10)):
    print("Right number")
else:
    print("Your code invalid")
