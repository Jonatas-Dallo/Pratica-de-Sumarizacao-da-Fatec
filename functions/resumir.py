from functions.preprocessamento import preprocessar_texto

def resumir(texto: str, model, tokenizer, device, max_length=400, min_length=40, num_beams=4):
    prefixo_tarefa = "sumarize: "
    entrada = prefixo_tarefa + preprocessar_texto(texto)

    inputs = tokenizer(
        entrada,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    ).to(device)

    summary_ids = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=max_length,
        min_length=min_length,
        num_beams=num_beams,
        early_stopping=True
    )

    resumo = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return resumo