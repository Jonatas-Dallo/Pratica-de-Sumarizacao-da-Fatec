import re

def preprocessar_texto(texto: str) -> str:
    texto = texto.replace('\t', ' ')
    texto = re.sub(r'\n+', '\n', texto)
    texto = texto.replace('‑', '-')
    texto = texto.replace(' ', ' ')
    texto = re.sub(r'\s{2,}', ' ', texto)
    texto = re.sub(r'https?://\S+|www\.\S+', '', texto)
    texto = re.sub(r'<.*?>', '', texto)
    return texto.strip()
