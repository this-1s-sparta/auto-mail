import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Φόρτωση των Excel αρχείων
all_df = pd.read_excel("dont_touch.xlsx")  # Αρχείο με αριθμούς και email
grades_df = pd.read_excel("grades.xlsx")  # Αρχείο με αριθμούς και βαθμούς

# Μετατροπή σε λεξικό για γρήγορη αναζήτηση
students = all_df.set_index("Number").to_dict(orient="index")
grades = grades_df.set_index("Number")["Grade"].to_dict()

# Ρύθμιση SMTP για αποστολή email
#todo: for gmail    :  "smtp.gmail.com"
#      for mail.auth:  "mail.auth.gr"
SMTP_SERVER = "mail.auth.gr" #line 17
SMTP_PORT = 587 #no need to change

EMAIL_SENDER = input("Enter your email: ('email@example.com') : ")
EMAIL_PASSWORD = input("password (goto README/report first) :")

# Σύνδεση στο email server
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(EMAIL_SENDER, EMAIL_PASSWORD)

subject = input("ΟΝΟΜΑ ΜΑΘΗΜΑΤΟΣ")
# Αποστολή email σε κάθε φοιτητή
for number, grade in grades.items():
    if number in students:
        recipient_email = students[number]["Mail"]
        student_name = students[number]["Name"]

        #Δημιουργία μηνύματος
        body = f"{student_name},\n\nΒαθμός:{grade}\n"

        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Αποστολή email
        server.sendmail(EMAIL_SENDER, recipient_email, msg.as_string())
        print(f"Sent email to {student_name} ({recipient_email}) with grade {grade}")

# Κλείσιμο σύνδεσης
server.quit()
print("FINISHED")