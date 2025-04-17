from PIL import Image
import os

caminho_imagens = "output/img"
caminho_pdf_final = "output/livro_medicamentos.pdf"
caminho_pdfs_individuais = "output/pdf"

os.makedirs(caminho_pdfs_individuais, exist_ok=True)

# Lista de imagens
imagens = []
for nome_arquivo in sorted(os.listdir(caminho_imagens)):
    if nome_arquivo.endswith(".png"):
        caminho_completo = os.path.join(caminho_imagens, nome_arquivo)
        img = Image.open(caminho_completo).convert("RGB")
        
        # Salva PDF individual
        nome_pdf = nome_arquivo.replace(".png", ".pdf")
        img.save(os.path.join(caminho_pdfs_individuais, nome_pdf), "PDF", resolution=300.0)

        imagens.append(img)

# Gerar PDF final com todas as páginas
if imagens:
    imagens[0].save(caminho_pdf_final, save_all=True, append_images=imagens[1:], resolution=300.0)
    print("PDF final gerado com sucesso:", caminho_pdf_final)
else:
    print("Nenhuma imagem encontrada para gerar o PDF.")
