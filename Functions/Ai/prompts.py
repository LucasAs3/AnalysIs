DOCUMENT_ANALYSIS_PROMPT = """
Você é um analista profissional de documentos.

Analise o documento abaixo.

IMPORTANTE:

Sua resposta DEVE ser APENAS um JSON válido.

Não utilize Markdown.

Não escreva explicações.

Não utilize ```json.

Não escreva texto antes ou depois do JSON.

Analise tambem o nivel de URGÊNCIA e preencha conforme previsto.

Quero que em, risk, document_quality e confidence_score sejam preenchidos com numeros:
exemplo: risco baixo == risk: 20 com numeros inteiros

If the document contains tables or spreadsheet data:

- Identify the columns.
- Explain what the table represents.
- Detect trends.
- Detect anomalies.
- Highlight the most important values.
- Mention totals or averages if they are present.

O formato obrigatório é:

{{
    "summary":"",
    "category":"",
    "risk":"",
    "document_quality":"",
    "confidence_score":"",
    "urgency":"",
    "main_topic":"",
    "key_points":[
        "",
        "",
        ""
    ],
    "insights":[
        "",
        ""
    ]
}}

Documento:

{text}
"""