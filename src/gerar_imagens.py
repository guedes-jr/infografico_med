from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Carregar dados
df = pd.read_excel("data/medicamentos.xlsx")

# Cores e fontes
COR_FUNDO = "#F1F5F9"
COR_TITULO = "#0F172A"
COR_TEXTO = "#334155"
COR_ESTRELA = "#FBBF24"

FONTE_TITULO = "src/fonts/Roboto-Italic.ttf"
FONTE_TEXTO = "src/fonts/Roboto.ttf"

def desenhar_estrelas(draw, x, y, n):
    for i in range(5):
        cor = COR_ESTRELA if i < n else "#E2E8F0"
        draw.text((x + i * 40, y), "★", fill=cor, font=ImageFont.truetype(FONTE_TEXTO, 36))

def gerar_infografico(linha, output_path):
    img = Image.new("RGB", (1240, 1754), color=COR_FUNDO)
    draw = ImageDraw.Draw(img)

    # Fontes
    titulo = ImageFont.truetype(FONTE_TITULO, 60)
    texto = ImageFont.truetype(FONTE_TEXTO, 34)

    y = 100
    draw.text((80, y), linha["Nome do Medicamento"], font=titulo, fill=COR_TITULO)
    y += 100

    campos = [
        ("Categoria", linha["Categoria"]),
        ("Principais Indicações", linha["Principais Indicações"]),
        ("Melhor Horário para Uso", linha["Melhor Horário para Uso"]),
        ("Potencializadores", linha["Potencializadores"]),
        ("Inibidores", linha["Inibidores"]),
        ("Efeitos Colaterais", linha["Efeitos Colaterais"]),
        ("Fontes Alimentares", linha.get("Fontes Alimentares", "-")),
        ("Bibliografia", linha["Bibliografia"]),
    ]

    for titulo_secao, conteudo in campos:
        draw.text((80, y), f"{titulo_secao}:", font=texto, fill=COR_TITULO)
        y += 40
        draw.text((100, y), str(conteudo), font=texto, fill=COR_TEXTO)
        y += 80

    # Estrelas
    draw.text((80, y), "Nível de Evidência:", font=texto, fill=COR_TITULO)
    desenhar_estrelas(draw, 400, y - 10, int(linha["Nível de Evidência"]))

    # Salvar imagem
    img.save(output_path)

def gerar_todos():
    os.makedirs("output/img", exist_ok=True)
    for _, linha in df.iterrows():
        nome = linha["Nome do Medicamento"].replace(" ", "_")
        gerar_infografico(linha, f"output/img/{nome}.png")

if __name__ == "__main__":
    gerar_todos()
