from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

pdf_path = "Resume.pdf"

doc = SimpleDocTemplate(pdf_path, pagesize=LETTER,
                        rightMargin=36, leftMargin=36, topMargin=8, bottomMargin=10)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Heading1Colored', parent=styles['Heading1'], textColor=colors.HexColor("#ff66c4")))
styles.add(ParagraphStyle(name='SubTitle', parent=styles['Normal'], textColor=colors.HexColor("#666666"), fontSize=10))
styles.add(ParagraphStyle(name='BodyTextBold', parent=styles['BodyText'], fontName="Helvetica-Bold"))
styles.add(ParagraphStyle(
    name='CenteredNormal',
    parent=styles['Normal'],
    alignment=TA_CENTER
))

styles.add(ParagraphStyle(
    name='SignatureLineCentered',
    parent=styles['Normal'],
    fontSize=12,
    textColor=colors.HexColor("#ff66c4"),
    alignment=TA_CENTER,
    fontName="Helvetica-Oblique"
))

content = []
content.append(Paragraph("<b>Your Name Here</b>", styles['Heading1Colored']))
content.append(Paragraph("Your Title Here", styles['Normal']))

content.append(Spacer(1, 5))
header_with_background = Table([[content]], colWidths=[doc.width])
header_with_background.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#ffe6f0")),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#ff66c4")),
    ('INNERPADDING', (0, 0), (-1, -1), 12),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
]))
flowables = []

flowables.append(Paragraph("<b>Work Experience</b>", styles['Heading1Colored']))
flowables.append(Spacer(1, -8))

flowables_block = []

flowables_block.append(Paragraph("<u><b>Job Title</b></u><br/>Company (Location) | Date Started – Present", styles['BodyText']))
flowables_block.append(Paragraph("• Describe a key responsibility or accomplishment here.", styles['Normal']))
flowables_block.append(Paragraph("• List another bullet point showing your impact or tools used.", styles['Normal']))
flowables_block.append(Spacer(1, 3))

flowables_block.append(Paragraph("<u><b>Job Title</b></u><br/>Company (Location) | Date Started – Present", styles['BodyText']))
flowables_block.append(Paragraph("• Describe a key responsibility or accomplishment here.", styles['Normal']))
flowables_block.append(Paragraph("• List another bullet point showing your impact or tools used.", styles['Normal']))
flowables_block.append(Spacer(1, 3))

flowables_block.append(Paragraph("<u><b>Job Title</b></u><br/>Company (Location) | Date Started – Present", styles['BodyText']))
flowables_block.append(Paragraph("• Describe a key responsibility or accomplishment here.", styles['Normal']))
flowables_block.append(Paragraph("• List another bullet point showing your impact or tools used.", styles['Normal']))
flowables_block.append(Spacer(1, 3))

flowables_block_section = Table([[flowables_block]], colWidths=[doc.width])
flowables_block_section.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#ffe6f0")),
    ('BOX', (0, 0), (1, 1), 0.5, colors.HexColor("#ff66c4")),
    ('INNERPADDING', (0, 0), (-1, -1), 12),
    ('VALIGN', (0, 0), (-1, -1), 'TOP')
]))

left_column = []

right_column = []

left_column.append(Paragraph("<u><b>Education & Certifications</b></u>", styles['Heading1Colored']))
left_column.append(Paragraph("• Degree Pursuing – Area of Study<br/>School or Organization (Year to be Completed)", styles['Normal']))
left_column.append(Paragraph("• Certificate<br/> Organization (Year of Completion)", styles['Normal']))
left_column.append(Spacer(1, 2))

left_column.append(Paragraph("<u><b>Projects</b></u>", styles['Heading1Colored']))
left_column.append(Paragraph("• Name of Project – Tools & Languages Used", styles['Normal']))
left_column.append(Paragraph("• Name of Project – Tools & Languages Used", styles['Normal']))
left_column.append(Paragraph("• Name of Project – Tools & Languages Used", styles['Normal']))
left_column.append(Paragraph("• Name of Project – Tools & Languages Used", styles['Normal']))
left_column.append(Paragraph("• Name of Project – Tools & Languages Used", styles['Normal']))
left_column.append(Spacer(1, 8))

right_column.append(Paragraph("<u><b>Key Skills & Technologies</b></u>", styles['Heading1Colored']))
right_column.append(Paragraph("• AI & ML Example: Data Annotation, AI Evaluation, Prompt Engineering, Model Optimization, NLP Analysis, Conversational AI, LLM Testing, AI Training Data", styles['Normal']))
right_column.append(Paragraph("• Programming Languages Example: Python, JavaScript, SQL, HTML, CSS, TypeScript, Bash", styles['Normal']))
right_column.append(Paragraph("• Frameworks & Libraries Example: React, Node.js, Express, Cypress, Flask, Tailwind CSS, API's", styles['Normal']))
right_column.append(Paragraph("• Dev Tools & Platforms Example: Git, GitHub, PostgreSQL, Yarn, NPM, Jest, ESLint, Visual Studio Code", styles['Normal']))
right_column.append(Paragraph("• Systems & Support Tools Example: Zendesk, Oracle Cloud, Synkros, Okta Admin, Yardi, CRM Platforms", styles['Normal']))
right_column.append(Paragraph("• Data Formats & Protocols Example: JSON, XML, YAML, INI, HTTP, SSH", styles['Normal']))

column_block = Table(
    [[left_column, right_column]],
    colWidths=[doc.width / 2.0] * 2
)
column_block.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#ffe6f0")),
    ('BOX', (0, 0), (1, 1), 0.5, colors.HexColor("#ff66c4")),
    ('INNERPADDING', (0, 0), (-1, -1), 12),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LINEBEFORE', (1, 0), (1, 0), 1, colors.HexColor("#ff66c4")),  # optional divider
]))

# Then your contact info block comes AFTER everything
contact = []

contact.append(Paragraph("The resume’s smart, the person behind it? Smarter, shall we connect?", styles['SignatureLineCentered']))
contact.append(Paragraph(
    '<i><a href="https://github.com/(Your GitHub Username)" color="blue">github.com/(Your GitHub Username)</a></i>&nbsp;•&nbsp;'
    '<i><a href="https://linkedin.com/in/(Your LinkedIn Username)" color="blue">linkedin.com/in/(Your LinkedIn Username)</a></i>',
    styles['CenteredNormal']
))
contact.append(Paragraph(
    '<i><a href="mailto:(Your Email Address)" color="blue">(Your Email Address)</a></i>&nbsp;•&nbsp; (Your Phone Number)',
    styles['CenteredNormal']
))

flowables = [header_with_background] + flowables + [flowables_block_section]

flowables.append(KeepTogether(column_block))

 # Adjust to push to bottom
flowables.extend(contact)

doc.build(flowables)

