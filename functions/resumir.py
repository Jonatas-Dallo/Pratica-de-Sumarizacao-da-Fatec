import time

def resumir(modelo, tokenizer, device, texto: str, max_length: int = 400, min_length: int = 50, num_beams: int = 5):
    inputs = tokenizer(texto, return_tensors="pt", max_length=2048, truncation=True).to(device)
    
    summary_ids = modelo.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        num_beams=num_beams,
        max_length=max_length,
        min_length=min_length,
        forced_bos_token_id=tokenizer.lang_code_to_id["pt_XX"],
        early_stopping=True
    )
    
    resumo = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=True)[0]
    return resumo