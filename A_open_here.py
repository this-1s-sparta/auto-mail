import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Φόρτωση των Excel αρχείων
all_df = pd.read_excel("elearning.xlsx")  # Αρχείο με αριθμούς και email
grades_df = pd.read_excel("grades.xlsx")  # Αρχείο με αριθμούς και βαθμούς

all_df["Dep/Student ID"] = all_df["Dep/Student ID"].str.split("/").str[1].astype(str)
students = all_df.set_index("Dep/Student ID").to_dict(orient="index")
grades = grades_df.set_index("Student ID")["Grade"].to_dict()

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

subject = input("ΟΝΟΜΑ ΜΑΘΗΜΑΤΟΣ: ")

# Αποστολή email σε κάθε φοιτητή
for number, grade in grades.items():
    if str(number) in students:
        recipient_email = students[str(number)]["Email address"]
        student_name = students[str(number)]["First name"]

        # Δημιουργία μηνύματος
        body = f"{student_name},\n\nΒαθμός: {grade}\n"
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