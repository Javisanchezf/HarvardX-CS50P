from fpdf import FPDF


class PDF:
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page(orientation="portrait", format="a4")
        self._pdf.image("./shirtificate.png", 10, 70, 190)
        self._pdf.set_font("Times", size=60)
        self._pdf.cell(
            0, 20, f"CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C"
        )
        self._pdf.set_font("helvetica", size=42)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.cell(0, 242, f"{name} took CS50", align="C")

    def save(self, name):
        self._pdf.output(name)


def main():
    pdf = PDF(input("Name: "))
    pdf.save("shirtificate.pdf")


if __name__ == "__main__":
    main()
