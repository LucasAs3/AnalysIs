def print_analyze(analyze: dict):
    
    print("Categoria | Urgência:")
    
    print( analyze["category"]  + ' | ' + analyze["urgency"])
    
    print()

    print("=" * 60)

    print("Resumo:")
    print(analyze["summary"])

    print()

    print("Tema Principal:")
    print(analyze["main_topic"])

    print()

    print("Principais Informações:")

    for item in analyze["key_points"]:
        print(f" • {item}")

    print()

    print("Insights:")

    for item in analyze["insights"]:
        print(f" • {item}")

    print()

    print("Risco:")
    print(analyze["risk"])

    print()

    print("Qualidade do Documento:")
    print(analyze["document_quality"])

    print()

    print("Conferencia:")
    print(analyze["confidence_score"])