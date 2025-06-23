from functions.carregar_modelo import carregar_modelo
from functions.resumir import resumir
from functions.gerar_estatisticas_simples import gerar_estatisticas_simples

if __name__ == "__main__":
    try:
        with open("texto_original.txt", "r", encoding="utf-8") as f:
            texto_original = f.read()
    except FileNotFoundError:
        print("Erro: Arquivo 'texto_original.txt' não encontrado.")
        print("Crie o arquivo e insira o texto a ser resumido.")
        exit()

    
    model, tokenizer, device = carregar_modelo()
    resumo = resumir(texto_original, model, tokenizer, device)
    print("\n--- RESUMO GERADO ---")
    print(resumo)
    gerar_estatisticas_simples(texto_original, resumo)