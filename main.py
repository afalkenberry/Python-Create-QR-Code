#install qr code
!pip install qrcode[pil]

import os
import pandas as pd
import qrcode

# Store excel in dataframe
df = pd.read_excel('SN_Data_Test.xlsx', header = None)
SN = df.values.tolist()

def get_SerialNumbers():
  serial_string = []
  all_serial_numbers = []


  snRangeLength = len(SN[1:])
  PartNumber = "".join(SN[0])
  prefix = ("[)>{RS}" + str(snRangeLength) + "{GS}" + PartNumber + "{GS}")
  suffix = ("{RS}" + "{Eot}")

  for serial_row in SN[1:]:

    serial_number = serial_row[0]
    serial_string = (str(serial_number)+"{GS}")
    all_serial_numbers.append(serial_string)

  #all_serial_numbers.append(serial_string)

  delimited_serials = ''.join(all_serial_numbers)

  QRString = prefix + delimited_serials + suffix

  print(QRString)

  QRString

  # Create a QR code object
  qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
    box_size=2,  # controls how many pixels each “box” of the QR code is
    border=4,  # controls how many boxes thick the border should be
  )

# Add data to the QR code
  qr.add_data(QRString)
  qr.make(fit=True)

# Create an image from the QR Code instance
  img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
  img.save("qrcode.png")

  output_file = os.path.join('qrcode.png')
  from google.colab import files
  files.download('qrcode.png')

get_SerialNumbers()
