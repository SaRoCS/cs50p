from fpdf import FPDF


name = input("Name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 64)
pdf.ln(10)
pdf.cell(5)
pdf.cell(40, 10, "CS50 Shirtificate")
pdf.image("shirtificate.png", 5, 60, 200)
pdf.set_font("helvetica", "", 32)
pdf.set_text_color(255, 255, 255)
pdf.set_y(125)
pdf.cell(210, 20, f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")