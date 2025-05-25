# Conversor de Imagem para PDF

Um aplicativo desktop simples e intuitivo para converter imagens em arquivos PDF. Desenvolvido em Python com interface gráfica usando Tkinter.

## 🚀 Funcionalidades

- Interface gráfica amigável e moderna
- Suporte para múltiplos formatos de imagem (PNG, JPG, JPEG, BMP, GIF)
- Conversão rápida e eficiente
- Feedback visual do status da conversão
- Geração do PDF no mesmo diretório da imagem original

## 📋 Pré-requisitos

- Python 3.x
- Bibliotecas Python necessárias:
  - tkinter
  - PIL (Pillow)
  - img2pdf

## 🔧 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/conversor-img-pdf.git
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🎮 Como usar

1. Execute o arquivo `main.py`:
```bash
python main.py
```

2. Na interface do aplicativo:
   - Clique no botão "Selecionar Imagem" para escolher a imagem que deseja converter
   - Clique em "Converter para PDF" para gerar o arquivo PDF
   - O arquivo PDF será gerado no mesmo diretório da imagem original

## 📦 Estrutura do Projeto

```
conversor-img-pdf/
│
├── main.py              # Código fonte principal
├── requirements.txt     # Dependências do projeto
├── icon.ico            # Ícone do aplicativo
├── assets/             # Recursos gráficos
│   └── frame0/         # Imagens da interface
└── README.md           # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- Python
- Tkinter (Interface gráfica)
- PIL (Pillow) para manipulação de imagens
- img2pdf para conversão de imagens para PDF

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit das suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
