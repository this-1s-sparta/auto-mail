ΤΑ EXCEL ΠΡΕΠΕΙ ΝΑ ΕΙΝΑΙ ΚΛΕΙΣΤΑ

Το αρχείο EXCEL "elearning" υπάρχει έτοιμο στο elearning.
Το αρχείo EXCEL "grades" έχει τις βαθμολογίες.

ΑΠΟ ΤΑ EXCEL ΔΕΝ ΠΡΈΠΕΙ ΝΑ ΑΛΛΑΞΟΥΝ ΟΙ ΠΡΏΤΕΣ ΓΡΑΜΜΕΣ!!!!!

Ο ΦΑΚΕΛΟΣ ΔΕΝ ΠΡΕΠΕΙ ΝΑ ΑΛΛΑΞΕΙ.

--->  ΑΠΟ GMAIL σε csd.auth (πιο ασφαλές):
    βήμα 1: Συμπληρώστε το αρχείο EXCEL "βαθμών"

    βήμα 2: H γραμμη 17 πρέπει να είναι : SMTP_SERVER = "smtp.gmail.com"
            Πρέπει να δημιουργήσετε ή να χρησιμοποιήσετε έναν ήδη υπάρχοντα λογαριασμό Gmail.
            RUN
            1. Input email address.
            Στο gmail ενεργοποιήστε τo 2-step authentication.
            Μεταβείτε στη διεύθυνση https://myaccount.google.com/apppasswords.
            Πληκτρολογήστε "Python Script" και πατήστε δημιουργία.
            2. Ιnput τον κωδικό πρόσβασης 16 χαρακτήρων που εμφανίζεται μετα τη δημιουργία.

    βήμα 3: Input ΟΝΟΜΑ ΜΑΘΗΜΑΤΟΣ

    βήμα 4: Εκτελέστε το πρόγραμμα όταν τελειώσει το πρόγραμμα, θα λάβετε ένα μήνυμα "FINISHED".


--->  ΑΠΟ csd.auth σε csd.auth (πιο απλό) :
    βήμα 1: Η γραμμη 17 πρέπει να είναι :
            SMTP_SERVER = "mail.auth.gr"

    βήμα 2: RUN
            Input mail.auth
            Input κωδικός email
            Input όνομα μαθήματος


Αν δοθεί μια ξεχωρηστή διευθύνση mail για αυτο το σκοπό τοτε μπορεί να χρησιμοποιηθεί
ΜΟΝΟ ΜΙΑ για ολούς όσους θα το χρησιμοποιήσουν.
Σε αυτό το σενάριο ο κώδικας θα έχει πάνω αυτόματα τη διεύθηνση και τον κωδικό
και θα γίνει αλλαγή στη γραμμη 17 όπου "smtp.gmail.com" βάζω "mail.auth.gr".
Ο χρήστης θα αλλάζει μόνο το ΟΝΟΜΑ ΜΑΘΗΜΑΤΟΣ.

Πλεονεκτήματα: ασφάλεια και ταχύτητα
