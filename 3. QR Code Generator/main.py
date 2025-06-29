import qrcode

WELCOME_TEXT = r'''
╔════════════════════════════════════════════════════════╗
║                                                        ║
║   ██████╗ ██████╗     ██████╗  ██████╗  ██████╗         ║
║  ██╔════╝██╔═══██╗   ██╔════╝ ██╔═══██╗██╔════╝         ║
║  ██║     ██║   ██║   ██║  ███╗██║   ██║██║  ███╗        ║
║  ██║     ██║   ██║   ██║   ██║██║   ██║██║   ██║        ║
║  ╚██████╗╚██████╔╝██╗╚██████╔╝╚██████╔╝╚██████╔╝        ║
║   ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝         ║
║                                                        ║
║   💸 UPI QR CODE GENERATOR for GPay / PhonePe / Paytm  ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
'''

GOODBYE_TEXT = r'''
╔════════════════════════════════════════════════════╗
║                                                    ║
║   ██████╗   ██████╗   ██████╗  ██████╗ ██╗   ██╗    ║
║  ██╔═══██╗ ██╔════╝  ██╔════╝ ██╔═══██╗╚██╗ ██╔╝    ║
║  ██║   ██║ ██║  ███╗ ██║  ███╗██║   ██║ ╚████╔╝     ║
║  ██║   ██║ ██║   ██║ ██║   ██║██║   ██║  ╚██╔╝      ║
║  ╚██████╔╝ ╚██████╔╝ ╚██████╔╝╚██████╔╝   ██║       ║
║   ╚═════╝   ╚═════╝   ╚═════╝  ╚═════╝    ╚═╝       ║
║                                                    ║
║     👋 Thank you for using UPI QR Code Generator!   ║
║         Stay safe. Scan. Pay. Done. 💸             ║
║                                                    ║
╚════════════════════════════════════════════════════╝
'''


print(WELCOME_TEXT)

def generate_upi_qr(UPI_ID):
    UPI_URL = f'upi://pay?pa={UPI_ID}&pn=Recipient%20Name&mc=1234'
    
    UPI_QR = qrcode.make(UPI_URL)

    
    UPI_QR.save('upi_qr.png')
    
    print("QR Code Generated Successfully!")
    
    UPI_QR.show()


while True:
    UPI_ID = input("Enter the UPI ID: ")

    PAYEE_NAME = input("Enter the Payee Name: ")

    generate_upi_qr(UPI_ID)

    GENERATE_AGAIN = input("Do you want to generate QR again? (yes/no): ").lower()
    
    if GENERATE_AGAIN != "yes":
        print("Thanks for using QR Code Generator!")
        break
    
print(GOODBYE_TEXT)