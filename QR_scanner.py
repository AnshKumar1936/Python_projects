import qrcode

# take upi id
upi_id = input("Enter your UPI ID =")


phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#creating qr code
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)


#saving qr image
# phonepe_qr.save('Phonepe_qr.png')
# paytm_qr.save('Paytm_qr.png')
# google_pay_qr.save('Google_pay_qr.png')

#display the qr codes using pillow library
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()