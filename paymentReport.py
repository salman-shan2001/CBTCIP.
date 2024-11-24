import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


# Function to generate the receipt
def generate_receipt(receipt_number, customer_name, customer_email, items, payment_method, store_name, store_address,
                     filename):
    # Create the PDF canvas object
    c = canvas.Canvas(filename, pagesize=letter)

    # Title of the receipt
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, 750, f"{store_name} Payment Receipt")

    # Store address
    c.setFont("Helvetica", 10)
    c.drawString(50, 730, f"Address: {store_address}")

    # Receipt number and date
    c.setFont("Helvetica", 12)
    c.drawString(400, 730, f"Receipt No: {receipt_number}")
    c.drawString(400, 715, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Customer information
    c.drawString(50, 680, f"Customer Name: {customer_name}")
    c.drawString(50, 665, f"Customer Email: {customer_email}")

    # Draw the line separator
    c.line(50, 650, 550, 650)

    # Table headers
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 630, "Item")
    c.drawString(200, 630, "Quantity")
    c.drawString(300, 630, "Price")
    c.drawString(400, 630, "Total")

    # Draw the item list
    c.setFont("Helvetica", 10)
    y_position = 615
    total_amount = 0
    for item in items:
        item_name, item_quantity, item_price = item
        item_total = item_quantity * item_price
        c.drawString(50, y_position, item_name)
        c.drawString(200, y_position, str(item_quantity))
        c.drawString(300, y_position, f"${item_price:.2f}")
        c.drawString(400, y_position, f"${item_total:.2f}")

        total_amount += item_total
        y_position -= 15

    # Draw the total amount
    c.setFont("Helvetica-Bold", 12)
    c.drawString(300, y_position - 10, "Total Amount:")
    c.drawString(400, y_position - 10, f"${total_amount:.2f}")

    # Payment method
    c.setFont("Helvetica", 10)
    c.drawString(50, y_position - 30, f"Payment Method: {payment_method}")

    # Footer with Thank You message
    c.setFont("Helvetica", 12)
    c.drawString(50, y_position - 50, "Thank you for your purchase!")

    # Save the PDF
    c.save()


# Main function to interact with the user
def main():
    # Store details (updated as per your request)
    store_name = "CollegeStore"
    store_address = "Shanti Nagar, Kerala 679322"

    # Automatically generate a random receipt number
    receipt_number = random.randint(10000, 99999)  # Generates a random number between 10000 and 99999
    print(f"Receipt Number: {receipt_number}")

    # Getting customer details
    customer_name = input("Enter the customer's name: ")
    customer_email = input("Enter the customer's email: ")

    # Getting item details
    items = []
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        item_quantity = int(input(f"Enter quantity for {item_name}: "))
        item_price = float(input(f"Enter price for {item_name}: "))
        items.append((item_name, item_quantity, item_price))

    # Getting payment method
    payment_method = input("Enter the payment method (e.g., Cash, Credit Card, etc.): ")

    # Generate the receipt
    filename = f"receipt_{receipt_number}.pdf"
    generate_receipt(receipt_number, customer_name, customer_email, items, payment_method, store_name, store_address,
                     filename)
    print(f"Receipt generated successfully! The file is saved as {filename}")


# Run the program
if __name__ == "__main__":
    main()
