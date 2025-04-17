# Infográfico de Medicamentos

Este projeto gera infográficos e PDFs sobre medicamentos com base em dados fornecidos em uma planilha Excel.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:
```
infografico_med/
├── data/                
│   └── medicamentos.xlsx    # Planilha Excel contendo os dados dos medicamentos
├── scripts/             
│   ├── main.py              # Script principal para processar os dados e gerar os infográficos
│   ├── utils.py             # Funções auxiliares para manipulação de dados e geração de gráficos
│   └── config.py            # Configurações e constantes utilizadas no projeto
├── templates/           
│   ├── infografico.html     # Modelo HTML para a criação dos infográficos
│   └── pdf_template.html    # Modelo HTML para a criação dos PDFs
├── output/              
│   ├── infograficos/        # Diretório contendo os infográficos gerados
│   └── pdfs/                # Diretório contendo os PDFs gerados
├── requirements.txt         # Lista de dependências do projeto, incluindo bibliotecas necessárias
└── readme.md                # Documentação do projeto com instruções de uso e contribuição
```

## Como Usar

1. Certifique-se de que todas as dependências estão instaladas:
    ```bash
    pip install -r requirements.txt
    ```

2. Coloque a planilha Excel com os dados dos medicamentos na pasta `data/`.

3. Execute o script principal para gerar os infográficos e PDFs:
    ```bash
    python scripts/main.py
    ```

4. Os arquivos gerados estarão disponíveis na pasta `output/`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).