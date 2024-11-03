import random
import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client

# Twilio configuration
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
USER_PHONE_NUMBER = 'recipient_phone_number'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Function to generate a random OTP
def generate_otp():
    return random.randint(100000, 999999)

# Function to send OTP via SMS
def send_otp():
    global otp
    otp = generate_otp()
    message = client.messages.create(
        body=f'Your OTP is {otp}',
        from_=TWILIO_PHONE_NUMBER,
        to=USER_PHONE_NUMBER
    )
    print(f'OTP sent: {otp}')  # For debugging purposes

# Function to verify the OTP entered by the user
def verify_otp():
    entered_otp = otp_entry.get()
    if entered_otp.isdigit() and int(entered_otp) == otp:
        messagebox.showinfo("Success", "OTP Verified Successfully!")
    else:
        messagebox.showerror("Error", "Invalid OTP. Please try again.")

# Setting up the Tkinter window
root = tk.Tk()
root.title("OTP Verification")

tk.Label(root, text="Enter OTP:").pack(pady=10)
otp_entry = tk.Entry(root, width=10)
otp_entry.pack(pady=5)

tk.Button(root, text="Send OTP", command=send_otp).pack(pady=10)
tk.Button(root, text="Verify OTP", command=verify_otp).pack(pady=5)

root.mainloop()
