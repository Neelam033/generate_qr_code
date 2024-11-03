import qrcode

# Data to be encoded in the QR code
data = "https://youtu.be/H1rTepnXyVQ?si=-2gvBkOVqgL_QU2w"

# Create an instance of the QRCode class
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="pink", back_color="green")

# Save the image
img.save('qrcode.png')
































