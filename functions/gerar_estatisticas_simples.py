import re

def gerar_estatisticas_simples(texto_original: str, texto_resumido: str):
    palavras_orig = len(re.findall(r'\b\w+\b', texto_original))
    palavras_resumo = len(re.findall(r'\b\w+\b', texto_resumido))

    if palavras_orig > 0:
        taxa_compressao = (1 - (palavras_resumo / palavras_orig)) * 100
    else:
        taxa_compressao = 0

    print("\n--- ESTATÍSTICAS DE SUMARIZAÇÃO ---")
    print(f"Palavras no texto original: {palavras_orig}")
    print(f"Palavras no resumo: {palavras_resumo}")
    print(f"Taxa de compressão (redução de palavras): {taxa_compressao:.2f}%")