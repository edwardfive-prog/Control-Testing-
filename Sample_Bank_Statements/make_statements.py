"""Generate clearly-marked SAMPLE bank statements for a fictional bank (Jul-Sep 2026)."""
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer,
                                Table, TableStyle, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

OUT = sys.argv[1]
BANK = "Northwind Sample Bank (Fictional)"
WM = "SAMPLE – NOT A REAL BANK STATEMENT"
HOLDER = ["SAMPLE ACCOUNT HOLDER", "100 EXAMPLE STREET", "ANYTOWN ST 00000"]
PRIMARY = ("Northwind Premier Checking", "XXXX-XXXX-0001")
EVERYDAY = ("Northwind Everyday Checking", "XXXX-XXXX-0002")
SAVINGS = ("Northwind Savings", "XXXX-XXXX-0003")

# Continues the Jan-Jun pattern: primary +5,500/mo, everyday +10,000/mo, savings +13,000/mo.
MONTHS = [
    # name, month num, last day, opening primary, everyday end, savings end, YTD interest
    ("July", 7, 31, 462069.00, 72500.00, 91200.00, 0.84),
    ("August", 8, 31, 467569.00, 82500.00, 104200.00, 0.96),
    ("September", 9, 30, 473069.00, 92500.00, 117200.00, 1.08),
]

ss = getSampleStyleSheet()
body = ParagraphStyle("b", parent=ss["Normal"], fontSize=9, leading=12)
small = ParagraphStyle("s", parent=body, fontSize=7.5, leading=10)
h1 = ParagraphStyle("h1", parent=ss["Heading1"], fontSize=16, textColor=colors.HexColor("#1F3B5C"))
h2 = ParagraphStyle("h2", parent=ss["Heading2"], fontSize=11.5, textColor=colors.HexColor("#1F3B5C"))
NAVY = colors.HexColor("#1F3B5C")


def money(v, sign=False):
    return ("$" if sign else "") + f"{v:,.2f}"


def build(name, m, last, opening, everyday, savings, ytd):
    date_str = f"{name} {last}, 2026"
    txns = [
        (5, "Payroll Dir Dep - Sample Employer Inc", 5067.31, None),
        (10, "Customer Deposit - Sample Client LLC", 17500.00, None),
        (15, "Payroll Dir Dep - Sample Employer Inc", 5067.31, None),
        (18, "Mobile Check Deposit", 865.26, None),
        (20, f"Online Transfer to Everyday Checking {EVERYDAY[1][-4:]}", None, 10000.00),
        (22, f"Online Transfer to Savings {SAVINGS[1][-4:]}", None, 13000.00),
        (last, "Interest Payment", 0.12, None),
    ]
    rows, bal = [], opening
    for d, desc, dep, wd in txns:
        bal = round(bal + (dep or 0) - (wd or 0), 2)
        rows.append([f"{m}/{d}", Paragraph(desc, body), money(dep) if dep else "",
                     money(wd) if wd else "", money(bal)])
    deposits = sum(t[2] or 0 for t in txns)
    withdrawals = sum(t[3] or 0 for t in txns)
    closing = round(opening + deposits - withdrawals, 2)
    assert closing == bal
    total = closing + everyday + savings
    total_pages = 4

    def decorate(c, doc):
        c.saveState()
        w, h = letter
        c.setFillColor(NAVY)
        c.rect(0, h - 0.55 * inch, w, 0.55 * inch, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(0.6 * inch, h - 0.36 * inch, BANK)
        c.setFont("Helvetica", 9)
        c.drawRightString(w - 0.6 * inch, h - 0.30 * inch, date_str)
        c.drawRightString(w - 0.6 * inch, h - 0.44 * inch, f"Page {doc.page} of {total_pages}")
        # watermark
        c.setFillColor(colors.Color(0.85, 0.1, 0.1, alpha=0.16))
        c.setFont("Helvetica-Bold", 28)
        c.translate(w / 2, h / 2)
        c.rotate(35)
        c.drawCentredString(0, 0, WM)
        c.restoreState()
        c.saveState()
        c.setFillColor(colors.HexColor("#B00020"))
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(w / 2, 0.45 * inch, WM + " – FOR TESTING / TRAINING USE ONLY")
        c.restoreState()

    doc = BaseDocTemplate(OUT_PATH(name), pagesize=letter, leftMargin=0.6 * inch,
                          rightMargin=0.6 * inch, topMargin=0.85 * inch, bottomMargin=0.8 * inch,
                          title=f"SAMPLE Statement - {name} 2026 - {BANK}", author="Sample data")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=decorate)])

    tbl = lambda data, widths, extra=(): Table(data, colWidths=widths, style=TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 9), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        *extra]))

    s = []
    # Page 1 - summary
    s.append(Paragraph(PRIMARY[0], h1))
    contact = Paragraph("<b>Questions? Contact us (fictional):</b><br/>Available 24 hours a day, 7 days a week<br/>"
                        "Phone: 1-555-0100<br/>Online: northwind-sample.example<br/>"
                        "Write: Northwind Sample Bank, P.O. Box 0000, Anytown, ST 00000", body)
    s.append(tbl([[Paragraph("<br/>".join(HOLDER), body), contact]], [3.4 * inch, 3.9 * inch],
                 [("VALIGN", (0, 0), (-1, -1), "TOP")]))
    s.append(Spacer(1, 18))
    s.append(Paragraph(f"Accounts linked to your {PRIMARY[0]} account:", h2))
    s.append(Paragraph("Bank Deposit Account(s)", body))
    s.append(Spacer(1, 6))
    data = [["Account (Account Number)", "$ Balance"],
            [f"{PRIMARY[0]} ({PRIMARY[1]}) - Your primary account", money(closing)],
            [f"{EVERYDAY[0]} ({EVERYDAY[1]})", money(everyday)],
            [f"{SAVINGS[0]} ({SAVINGS[1]})", money(savings)],
            ["Your Qualification Balance this month:", money(total, True)]]
    s.append(tbl(data, [5.3 * inch, 2.0 * inch], [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("ALIGN", (1, 0), (1, -1), "RIGHT"), ("LINEBELOW", (0, 0), (-1, -2), 0.4, colors.grey),
        ("LINEABOVE", (0, -1), (-1, -1), 1, NAVY), ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    s.append(Spacer(1, 8))
    s.append(Paragraph("Accounts linked in Summary will be provided a separate statement.", small))
    s.append(PageBreak())

    # Page 2 - account activity + interest
    s.append(Paragraph(f"{PRIMARY[0]} – Statement period activity", h2))
    s.append(Paragraph(f"Account number: {PRIMARY[1]} (primary account) &nbsp;&nbsp; {HOLDER[0]}", body))
    s.append(Spacer(1, 8))
    s.append(tbl([[f"Balance on {m}/1", money(opening, True)],
                  ["Deposits/Additions", money(deposits, True)],
                  ["Withdrawals/Subtractions", "- " + money(withdrawals, True)],
                  [f"Balance on {m}/{last}", money(closing, True)]],
                 [3.0 * inch, 1.8 * inch], [
        ("ALIGN", (1, 0), (1, -1), "RIGHT"), ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("LINEABOVE", (0, -1), (-1, -1), 1, NAVY)]))
    s.append(Spacer(1, 14))
    s.append(Paragraph("Interest summary", h2))
    s.append(tbl([["Interest paid this statement", "$0.12"],
                  ["Interest earned this statement period", "$0.12"],
                  ["Average collected balance", money(opening + 2750, True)],
                  ["Annual percentage yield earned", "0.01%"],
                  ["Interest paid this year", money(ytd, True)]],
                 [3.0 * inch, 1.8 * inch], [("ALIGN", (1, 0), (1, -1), "RIGHT"),
                                            ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.lightgrey)]))
    s.append(Spacer(1, 14))
    s.append(Paragraph("Important Account Information (sample text)", h2))
    s.append(Paragraph("If your Premier Checking account is closed or converted to another checking product, "
                       "linked accounts are delinked and relationship benefits no longer apply. Balances in the linked "
                       "accounts summary may differ from separate statements of record due to differences in statement "
                       "periods. This is placeholder disclosure text for a fictional institution.", body))
    s.append(PageBreak())

    # Page 3 - transaction history
    s.append(Paragraph("Transaction history", h2))
    data = [["Date", "Description", "Deposits/\nAdditions", "Withdrawals/\nSubtractions", "Ending Daily\nBalance"]]
    data += rows
    data.append(["Totals", "", money(deposits, True), money(withdrawals, True), ""])
    s.append(tbl(data, [0.6 * inch, 3.2 * inch, 1.15 * inch, 1.2 * inch, 1.15 * inch], [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, 0), 8),
        ("ALIGN", (2, 0), (-1, -1), "RIGHT"), ("FONTNAME", (0, -1), (-1, -1), "Helvetica-Bold"),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, colors.lightgrey), ("LINEABOVE", (0, -1), (-1, -1), 1, NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, colors.HexColor("#F2F5F9")]),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    s.append(Spacer(1, 8))
    s.append(Paragraph("The Ending Daily Balance does not reflect any pending withdrawals or holds on deposited "
                       "funds that may have been outstanding when your transactions posted.", small))
    s.append(Spacer(1, 12))
    s.append(Paragraph("Monthly service fee summary", h2))
    s.append(Paragraph("The Premier Checking account has a $25 monthly service fee which can be avoided each fee "
                       "period with $20,000 or more in statement-ending qualifying linked balances. "
                       f"Qualifying balance this period: {money(total, True)} – fee waived.", body))
    s.append(PageBreak())

    # Page 4 - disclosures
    s.append(Paragraph("Important Information You Should Know (sample text)", h2))
    for p in [
        "<b>In case of errors or questions about your electronic transfers:</b> Contact us at the number on the front "
        "of this statement as soon as you can if you think your statement or receipt is wrong. We must hear from you "
        "no later than 60 days after we sent the FIRST statement on which the error appeared.",
        "1. Tell us your name and account number (if any).<br/>2. Describe the error or the transfer you are unsure "
        "about.<br/>3. Tell us the dollar amount of the suspected error.",
        "We will investigate your complaint and correct any error promptly. If we take more than 10 business days, "
        "we will credit your account for the amount you think is in error while we complete our investigation.",
        "<b>If your account has a negative balance:</b> an overdraft not resolved within 60 days may result in "
        "closure of the account.",
        "Promptly review your account statement within 30 days after it was made available to you, and notify us "
        "of any errors.",
        f"<b>{WM}.</b> {BANK} does not exist. All names, addresses, account numbers and amounts in this document are "
        "fictitious and provided solely for control testing, QA and training purposes.",
    ]:
        s.append(Paragraph(p, body))
        s.append(Spacer(1, 8))
    doc.build(s)
    print(name, opening, deposits, withdrawals, closing, everyday, savings, total)


OUT_PATH = lambda name: f"{OUT}/SAMPLE_NorthwindBank_{name}2026.pdf"
for args in MONTHS:
    build(*args)
