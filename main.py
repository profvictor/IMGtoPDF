from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
from PIL import Image
import img2pdf
import os

# from tkinter import *
# Explicit imports to satisfy Flake8


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\vccos\Desktop\IMGtoPDF\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Variáveis globais
window = None
canvas = None
status_text = None
selected_image_path = None  # Nova variável para armazenar o caminho da imagem


def update_status(text, color="#B3B3B3"):
    global status_text
    if status_text:
        canvas.itemconfig(status_text, text=text, fill=color)


def select_image():
    global selected_image_path
    file_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[
            ("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("Todos os arquivos", "*.*")
        ]
    )
    if file_path:
        selected_image_path = file_path  # Armazena o caminho da imagem
        update_status("Imagem selecionada", "#4CAF50")
    return file_path


def convert_to_pdf():
    global selected_image_path
    if not selected_image_path:
        update_status("Selecione uma imagem primeiro!", "#FF0000")
        return

    try:
        # Abre a imagem usando PIL
        image = Image.open(selected_image_path)

        # Define o caminho do PDF de saída
        pdf_path = os.path.splitext(selected_image_path)[0] + ".pdf"

        # Converte a imagem para PDF
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(selected_image_path))

        update_status("PDF gerado com sucesso!", "#4CAF50")
    except Exception as e:
        update_status(f"Erro: {str(e)}", "#FF0000")


def main():
    global window, canvas, status_text

    window = Tk()
    window.title("Conversor de Imagem para PDF")
    try:
        window.iconbitmap("icon.ico")  # Tenta carregar o ícone
    except:
        pass  # Se não encontrar o ícone, continua sem ele
    window.geometry("425x337")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=337,
        width=425,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        425.0,
        337.0,
        fill="#FFFFFF",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=select_image,
        relief="flat"
    )
    button_1.place(
        x=49.0,
        y=99.0,
        width=320.0,
        height=89.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=convert_to_pdf,
        relief="flat"
    )
    button_2.place(
        x=111.0,
        y=249.0,
        width=196.0,
        height=63.0
    )

    canvas.create_text(
        212.0,
        210.0,
        anchor="center",
        text="Status:",
        fill="#3F3F3F",
        font=("Jersey25 Regular", 24 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        212.0,
        37.0,
        image=image_image_1
    )

    status_text = canvas.create_text(
        212.0,
        235.0,
        anchor="center",
        text="Aguardando",
        fill="#B3B3B3",
        font=("Jersey25 Regular", 24 * -1)
    )

    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    main()
