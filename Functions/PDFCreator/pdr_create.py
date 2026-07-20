from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet


def pdf_creator(analysis: dict, metrics_path: str, output: str = f"output/report.pdf"):
    doc = SimpleDocTemplate(output)
    style = getSampleStyleSheet()
    title_style = style["Heading1"]
    subtitle_style = style["Heading2"]
    normal_style = style["BodyText"]

    content = []

    content.append(
        Paragraph(
            "Relatório Analisado com IA",
            title_style
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"<b>Categoria:</b> {analysis["category"]}",
            normal_style
        )
    )

    content.append(
        Paragraph(
            f"<b>Urgência:</b> {analysis["urgency"]}",
            normal_style
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            "<b>Resumo: </b>",
            subtitle_style
        )
    )

    content.append(
        Paragraph(
            analysis["summary"],
            normal_style
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            "<b>Tópico Principal:</b>",
            subtitle_style
        )
    )

    content.append(
        Paragraph(
            analysis["main_topic"],
            normal_style
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            "Dashbord",
            subtitle_style
        )
    )

    content.append(
        Image(metrics_path, width=420, height=220)
    )

    doc.build(content)