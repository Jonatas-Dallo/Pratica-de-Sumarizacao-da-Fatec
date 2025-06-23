from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch

def carregar_modelo():
    print("Iniciando o carregamento do modelo mBART-large-50...")
    print("Isso pode levar alguns minutos e consumir >2GB de RAM.")
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Usando dispositivo: {device}")

    modelo = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt").to(device)
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    
    tokenizer.src_lang = "pt_XX"
    tokenizer.tgt_lang = "pt_XX"
    
    print("Modelo carregado com sucesso!")
    return modelo, tokenizer, device