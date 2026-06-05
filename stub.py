def draw_stub(c, x, y, width, date, payee, amount, memo):
    height = 150
    c.rect(x, y - height, width, height)

    c.setFont("Helvetica-Bold", 10)
    c.drawString(x + 10, y - 20, "PAYMENT STUB")

    c.setFont("Helvetica", 9)
    c.drawString(x + 10, y - 40, "Date:")
    c.drawString(x + 60, y - 40, date)
    c.drawString(x + 10, y - 60, "Payee:")
    c.drawString(x + 60, y - 60, payee)
    c.drawString(x + 10, y - 80, "Amount:")
    c.drawString(x + 60, y - 80, f"${amount:,.2f}")
    c.drawString(x + 10, y - 100, "Memo:")
    c.drawString(x + 60, y - 100, memo)

    c.line(x, y - 115, x + width, y - 115)

    c.setFont("Helvetica-Bold", 9)
    c.drawString(x + 10, y - 130, "Description")
    c.drawRightString(x + width - 10, y - 130, "Amount")

    c.setFont("Helvetica", 9)
    c.drawString(x + 10, y - 145, memo)
    c.drawRightString(x + width - 10, y - 145, f"${amount:,.2f}")
