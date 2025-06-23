from functions.carregar_modelo import carregar_modelo
from functions.resumir import resumir
from functions.preprocessamento import preprocessar_texto
import time

if __name__ == "__main__":
    start_time = time.time()
    modelo, tokenizer, device = carregar_modelo()
    end_time = time.time()
    print(f"Tempo de carregamento do modelo: {end_time - start_time:.2f} segundos.\n")

    try:
        with open("texto_original.txt", "r", encoding="utf-8") as f:
            texto_original = f.read()
    except FileNotFoundError:
        print("Erro: Arquivo 'texto_original.txt' não encontrado.")
        print("Crie o arquivo e insira o texto a ser resumido.")
        exit()

    print("Aplicando pré-processamento de limpeza no texto...")
    texto_original_processado = preprocessar_texto(texto_original)
    print("Pré-processamento concluído.\n")

    print("Iniciando o processo de sumarização...")
    start_time = time.time()
    resumo_gerado = resumir(modelo, tokenizer, device, texto_original_processado)
    end_time = time.time()
    print(f"Tempo de sumarização: {end_time - start_time:.2f} segundos.\n")

    palavras_original = len(texto_original_processado.split())
    palavras_resumo = len(resumo_gerado.split())
    
    print("="*20 + " TEXTO ORIGINAL " + "="*20)
    print(texto_original_processado)
    print(f"\n(Contagem de palavras: {palavras_original})\n")
    
    print("="*20 + " RESUMO ABSTRATIVO GERADO " + "="*20)
    print(resumo_gerado)
    print(f"\n(Contagem de palavras: {palavras_resumo})\n")

    print("="*20 + " ANÁLISE " + "="*20)
    reducao = 100 - (palavras_resumo / palavras_original * 100)
    print(f"O resumo é {reducao:.2f}% menor que o texto original.")
    if palavras_resumo <= palavras_original / 2:
        print("Critério da tarefa (resumo <= 50% do original) foi ATENDIDO.")
    else:
        print("Critério da tarefa (resumo <= 50% do original) NÃO foi atendido.")