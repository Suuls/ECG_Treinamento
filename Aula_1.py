def calcular_media(notas):

    return sum(notas) / len(notas)

def obter_status(media):
    
    if media >= 6:
        return "Aprovado"
    elif 4 <= media < 6:
        return "Em Recuperação"
    else:
        return "Reprovado"
    
dados_alunos = {
    "Pedro": {
        "Controle e Automação": [9.0, 8.5, 9.5],
        "Programação Orientada a Objetos": [9.5, 8.5, 9.0]
    },
    "Maria": {
        "Controle e Automação": [7.0, 8.0, 9.0],
        "Programação Orientada a Objetos": [7.5, 8.0, 9.5]
    },
    "João": {
        "Controle e Automação": [8.5, 9.0, 7.5],
        "Programação Orientada a Objetos": [8.0, 9.0, 7.0]
    }
}

print("--- Boletim Final dos Alunos ---")
for nome_aluno, disciplinas in dados_alunos.items():
    print(f"\n----------------------------------")
    print(f"ALUNO: {nome_aluno}")
    print(f"----------------------------------")

    for nome_disciplina, notas in disciplinas.items():

        media_disciplina = calcular_media(notas)
        
        status_disciplina = obter_status(media_disciplina)

        print(f"  - Disciplina: {nome_disciplina}")
        print(f"    Notas: {notas}")
        print(f"    Média: {media_disciplina:.2f} | Status: {status_disciplina}")
        
print("\n--- Fim do Relatório ---")

