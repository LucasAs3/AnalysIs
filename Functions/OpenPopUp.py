from tkinter import Tk, filedialog

def open_pop_up():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo desejado",
        filetypes=[
            ("PDF", "*.pdf"),
            ("Excel", "*.xlsx"),
            ("CSV", "*.csv"),
            ("All Files", "*.*")
        ]
    )

    root.destroy()

    return file_path
