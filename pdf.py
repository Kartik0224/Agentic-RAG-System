from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from faker import Faker
import random

fake = Faker()
styles = getSampleStyleSheet()

doc = SimpleDocTemplate("rag_large_document.pdf")

elements = []

def generate_article():
    title = fake.sentence(nb_words=6)
    elements.append(Paragraph(f"<b>{title}</b>", styles['Heading2']))
    elements.append(Spacer(1, 10))

    for _ in range(20):  # paragraphs per article
        paragraph = " ".join(fake.paragraphs(nb=5))
        elements.append(Paragraph(paragraph, styles['BodyText']))
        elements.append(Spacer(1, 10))

# 🔁 Increase this number to reach ~200MB
for i in range(5000):  
    generate_article()

doc.build(elements)

print("✅ Large RAG-ready PDF generated!")