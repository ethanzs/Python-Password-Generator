from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox
import random
import string
import pyperclip

# generate random string with lowercase, uppercase, digits, and punctuation
def rand_string(length):
    letters = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
    )
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


# init UI and button
app = QApplication([])
button = QPushButton("Generate Password")

# when button is clicked
def on_button_clicked():
    pw = rand_string(32)
    # copy generated password to clipboard
    pyperclip.copy(pw)
    alert = QMessageBox()
    alert.setText(f"{pw}\nCopied to clipboard.")
    alert.exec_()


button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
