def gerar_arquivo_modelo(save_path: str):
    with open(save_path, 'w', encoding='latin-1') as file:
        file.write('nota;valor')
