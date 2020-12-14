from fpdf import FPDF
pdf = FPDF()

#Add page

pdf.add_page()
pdf.set_font("Arial", size=25)
pdf.cell(200,10,txt="Hello, this is meet", ln=1, align="C")
pdf.output("meettxttopdf.pdf")

