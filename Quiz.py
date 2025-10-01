def quiz():
    perguntas = [
        {
            "pergunta": "Qual a capital do Brasil?",
            "resposta": "Brasília"
        },
        {
            "pergunta": "Qual é o maior planeta do Sistema Solar?",
            "resposta": "Júpiter"
        },
        {
            "pergunta": "Quem escreveu 'Dom Casmurro'?",
            "resposta": "Machado de Assis"
        }
    ]

    print("=== Quiz Interativo ===")
    pontos = 0

    for i, item in enumerate(perguntas, start=1):
        while True:
            resposta = input(f"Pergunta {i}: {item['pergunta']} ").strip()
            if resposta == "":
                print("Resposta não pode ser vazia. Tente novamente.")
                continue
            else:
                break

        if resposta.lower() == item['resposta'].lower():
            print("Resposta correta!\n")
            pontos += 1
        else:
            print(f"Errado! A resposta correta é: {item['resposta']}\n")

        # Perguntar se quer continuar
        while True:
            continuar = input("Quer continuar? (s/n) ").strip().lower()
            if continuar not in ["s", "n"]:
                print("Digite 's' para sim ou 'n' para não.")
                continue
            elif continuar == "n":
                print("Você optou por sair do quiz.")
                break
            else:
                break
        
        if continuar == "n":
            break

    print(f"\nFim do quiz! Você acertou {pontos} de {i} perguntas.")

if __name__ == "__main__":
    quiz()