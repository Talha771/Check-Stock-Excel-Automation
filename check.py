from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from num2words import num2words
from stub import draw_stub


def _amount_in_words(amount: float) -> str:
    dollars = int(amount)
    words = num2words(dollars, lang="en").replace(",", "").title()
    return f"{words} Dollars ***"


def render_check(output_path, template_path, date, payee, amount, memo):
    amt_dollar = f"${amount:.2f}"
    amt_in_words = _amount_in_words(amount)

    c = canvas.Canvas(output_path, pagesize=letter)

    c.drawString(520, 738, date)
    c.drawString(80, 703, payee)
    c.drawString(520, 703, amt_dollar)
    c.drawString(80, 683, amt_in_words)
    c.drawString(80, 606, memo)

    draw_stub(c, x=25, y=500, width=560, date=date, payee=payee, amount=amount, memo=memo)
    draw_stub(c, x=25, y=250, width=560, date=date, payee=payee, amount=amount, memo=memo)

    c.save()


def render_check_page(c, date, payee, amount, memo):
    """Draw one check onto an existing canvas and advance to the next page."""
    amt_dollar = f"${amount:.2f}"
    amt_in_words = _amount_in_words(amount)

    c.drawString(520, 738, date)
    c.drawString(80, 703, payee)
    c.drawString(520, 703, amt_dollar)
    c.drawString(80, 683, amt_in_words)
    c.drawString(80, 606, memo)

    draw_stub(c, x=25, y=500, width=560, date=date, payee=payee, amount=amount, memo=memo)
    draw_stub(c, x=25, y=250, width=560, date=date, payee=payee, amount=amount, memo=memo)

    c.showPage()
