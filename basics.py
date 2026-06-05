from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from num2words import num2words
c = canvas.Canvas("test.pdf", pagesize=letter)

# Background template

date = "06/05/2026"
name = "ABC Supply"
amt = 125133.50
amt_dollar = "$"+str(amt)
amt_in_words = num2words(amt)
memo = "Week Ending in 5-20-2026"
# Overlay fields
c.drawString(520, 720, date)
c.drawString(80, 685, name)
c.drawString(520, 685, amt_dollar)
c.drawString(80, 665, amt_in_words)
c.drawString(80, 665, amt_in_words)
c.drawString(80,590,memo)
def draw_stub(c, x, y, width, date, payee, amount, memo):
    """
    x, y = top-left corner of stub
    width = width of stub area
    """

    height = 150

    # Outer box
    c.rect(x, y - height, width, height)

    # Header
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x + 10, y - 20, "PAYMENT STUB")

    c.setFont("Helvetica", 9)

    # Left column
    c.drawString(x + 10, y - 40, "Date:")
    c.drawString(x + 60, y - 40, date)

    c.drawString(x + 10, y - 60, "Payee:")
    c.drawString(x + 60, y - 60, payee)

    c.drawString(x + 10, y - 80, "Amount:")
    c.drawString(x + 60, y - 80, f"${amount:,.2f}")

    c.drawString(x + 10, y - 100, "Memo:")
    c.drawString(x + 60, y - 100, memo)

    # Detail section
    c.line(x, y - 115, x + width, y - 115)

    c.setFont("Helvetica-Bold", 9)
    c.drawString(x + 10, y - 130, "Description")
    c.drawRightString(x + width - 10, y - 130, "Amount")

    c.setFont("Helvetica", 9)
    c.drawString(x + 10, y - 145, memo)
    c.drawRightString(x + width - 10, y - 145, f"${amount:,.2f}")
draw_stub(
    c,
    x=25,
    y=500,      # top edge of stub
    width=560,
    date=date,
    payee=name,
    amount=amt,
    memo=memo
)
draw_stub(
    c,
    x=25,
    y=250,      # top edge of stub
    width=560,
    date=date,
    payee=name,
    amount=amt,
    memo=memo
)
c.save()





