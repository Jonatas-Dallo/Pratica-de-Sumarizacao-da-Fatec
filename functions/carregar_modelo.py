import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

def carregar_modelo(model_name="unicamp-dl/ptt5-base-portuguese-vocab"):
    print("Carregando modelo e tokenizador...")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Dispositivo em uso: {device}")

    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

    print("Modelo carregado com sucesso!")
    return model, tokenizer, device