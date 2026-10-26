"""Generate fictional sample bank statements for control-testing exercises.

All names, account numbers, addresses and amounts are fictional. Every page
carries a "SAMPLE - NOT A REAL STATEMENT" watermark. Balances roll forward:
each month's opening balance equals the prior month's closing balance.
"""
import calendar
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

OUT_DIR = Path(__file__).parent
BANK = "Harborview Demo Bank (Fictional)"
HOLDER = ["JORDAN SAMPLE", "100 EXAMPLE AVE", "TESTVILLE ZZ 00000"]
ACCOUNTS = {
    "checking": ("Demo Premier Checking", "XXXXXX0001"),
    "everyday": ("Demo Everyday Checking", "XXXXXX0002"),
    "savings": ("Demo Savings", "XXXXXX0003"),
}
YEAR = 2026
OPENING = {"checking": 100_000.00, "everyday": 5_000.00, "savings": 10_000.00}

# Same monthly pattern as the other months: two payroll deposits, one other
# deposit, a mobile deposit, transfers to the linked accounts, and interest.
PATTERN = [
    (5, "Example Employer Inc Dir Dep", 4_250.00, None),
    (10, "Customer Deposit", 6_000.00, None),
    (15, "Example Employer Inc Dir Dep", 4_250.00, None),
    (18, "Mobile Check Deposit", 500.00, None),
    (20, "Online Transfer to Everyday Checking XXXXXX0002", None, 3_000.00),
    (22, "Online Transfer to Savings XXXXXX0003", None, 4_000.00),
]
MONTHS = [7, 8, 9]
INTEREST_RATE = 0.0001  # 0.01% APY, simple monthly approximation


def money(x):
    return f"${x:,.2f}"


def watermark(c):
    c.saveState()
    c.setFillColor(colors.Color(0.85, 0.1, 0.1, alpha=0.18))
    c.setFont("Helvetica-Bold", 36)
    c.translate(306, 396)
    c.rotate(40)
    c.drawCentredString(0, 0, "SAMPLE - NOT A REAL STATEMENT")
    c.restoreState()
    c.setFont("Helvetica-Oblique", 7)
    c.setFillColor(colors.red)
    c.drawCentredString(306, 20, "Fictional test data for control-testing purposes only. "
                        "Not issued by any financial institution.")
    c.setFillColor(colors.black)


def header(c, stmt_date, page, pages):
    c.setFont("Helvetica", 9)
    c.drawRightString(580, 760, stmt_date)
    c.drawRightString(580, 748, f"Page {page} of {pages}")


def compute_month(month, bal):
    """Return the statement figures for one month, rolling forward from bal."""
    last = calendar.monthrange(YEAR, month)[1]
    name = calendar.month_name[month]
    opening = bal["checking"]

    rows, running = [], opening
    daily = []
    for day, desc, dep, wd in PATTERN:
        running += (dep or 0) - (wd or 0)
        rows.append((f"{month}/{day}", desc, dep, wd, running))
        daily.append(running)
    interest = round(sum(daily) / len(daily) * INTEREST_RATE / 12, 2)
    running = round(running + interest, 2)
    rows.append((f"{month}/{last}", "Interest Payment", interest, None, running))

    deposits = sum(r[2] or 0 for r in rows)
    withdrawals = sum(r[3] or 0 for r in rows)
    closing = running
    assert round(opening + deposits - withdrawals, 2) == closing

    new_bal = {
        "checking": closing,
        "everyday": bal["everyday"] + 3_000.00,
        "savings": bal["savings"] + 4_000.00,
    }
    return {
        "month": month, "last": last, "name": name,
        "stmt_date": f"{name} {last}, {YEAR}",
        "opening": opening, "closing": closing, "interest": interest,
        "deposits": deposits, "withdrawals": withdrawals, "rows": rows,
        "balances": new_bal, "total": sum(new_bal.values()),
    }


def build(month, bal):
    m = compute_month(month, bal)
    last, name, stmt_date = m["last"], m["name"], m["stmt_date"]
    opening, closing, interest = m["opening"], m["closing"], m["interest"]
    deposits, withdrawals, rows = m["deposits"], m["withdrawals"], m["rows"]
    new_bal, total = m["balances"], m["total"]

    path = OUT_DIR / f"SAMPLE_Statement_{name}{YEAR}.pdf"
    c = canvas.Canvas(str(path), pagesize=letter)
    c.setTitle(f"SAMPLE statement {name} {YEAR} - fictional test data")

    # Page 1: summary
    header(c, stmt_date, 1, 2)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, 720, BANK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, 700, ACCOUNTS["checking"][0])
    c.setFont("Helvetica", 10)
    for i, line in enumerate(HOLDER):
        c.drawString(40, 670 - i * 13, line)
    c.drawString(330, 670, "Questions? 1-000-000-0000 (fictional)")
    c.drawString(330, 657, "Online: example.invalid")
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, 600, "Accounts linked to your primary account")
    c.setFont("Helvetica", 10)
    c.drawString(40, 580, "Account (Account Number)")
    c.drawRightString(570, 580, "$ Balance")
    c.line(40, 575, 570, 575)
    y = 558
    for key in ("checking", "everyday", "savings"):
        label, num = ACCOUNTS[key]
        suffix = " - primary account" if key == "checking" else ""
        c.drawString(40, y, f"{label} ({num}){suffix}")
        c.drawRightString(570, y, f"{new_bal[key]:,.2f}")
        y -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(40, y - 5, "Qualification balance this month:")
    c.drawRightString(570, y - 5, money(total))
    watermark(c)
    c.showPage()

    # Page 2: activity
    header(c, stmt_date, 2, 2)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, 720, f"{ACCOUNTS['checking'][0]}  -  {ACCOUNTS['checking'][1]}")
    c.setFont("Helvetica", 10)
    summary = [
        (f"Balance on {month}/1", money(opening)),
        ("Deposits/Additions", money(deposits)),
        ("Withdrawals/Subtractions", f"- {money(withdrawals)}"),
        (f"Balance on {month}/{last}", money(closing)),
        ("Interest paid this statement", money(interest)),
    ]
    y = 695
    for k, v in summary:
        c.drawString(40, y, k)
        c.drawRightString(300, y, v)
        y -= 15
    y -= 15
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "Transaction history")
    y -= 18
    c.setFont("Helvetica-Bold", 9)
    for x, t in ((40, "Date"), (80, "Description")):
        c.drawString(x, y, t)
    c.drawRightString(410, y, "Deposits/Additions")
    c.drawRightString(495, y, "Withdrawals")
    c.drawRightString(575, y, "Ending Balance")
    c.line(40, y - 4, 575, y - 4)
    c.setFont("Helvetica", 9)
    y -= 18
    for date, desc, dep, wd, run in rows:
        c.drawString(40, y, date)
        c.drawString(80, y, desc)
        if dep:
            c.drawRightString(410, y, f"{dep:,.2f}")
        if wd:
            c.drawRightString(495, y, f"{wd:,.2f}")
        c.drawRightString(575, y, f"{run:,.2f}")
        y -= 16
    c.line(40, y + 10, 575, y + 10)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(40, y - 4, "Totals")
    c.drawRightString(410, y - 4, money(deposits))
    c.drawRightString(495, y - 4, money(withdrawals))
    watermark(c)
    c.showPage()
    c.save()
    print(f"{path.name}: open {money(opening)} +{money(deposits)} -{money(withdrawals)} "
          f"= close {money(closing)}; linked total {money(total)}")
    return new_bal


if __name__ == "__main__":
    bal = dict(OPENING)
    for m in MONTHS:
        bal = build(m, bal)
