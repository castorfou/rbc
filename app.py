# AUTOGENERATED! DO NOT EDIT! File to edit: main.ipynb.

# %% auto 0
__all__ = ['analyse_fichier']

# %% main.ipynb 1
import gradio as gr
import pandas as pd
import tempfile
from pathlib import Path
from rbc import add_classements


def analyse_fichier(file):
    fichier = file[0]
    fichier_save = Path(fichier.name).stem
    df_adherents = pd.read_excel(fichier)
    df_classements = add_classements(df_adherents)
    
    with tempfile.NamedTemporaryFile(prefix=fichier_save+'_', suffix=".xlsx", delete=False) as temp:
        df_classements.to_excel(temp.name)
        return temp.name

with gr.Blocks() as classement_converter:
    file = gr.File(label="Adhérents", file_count=1)
    greet_btn = gr.Button("Ajoute Classements")
    outputs = gr.File(label="Adhérents avec classement", file_count=1, visible=True)
    greet_btn.click(fn=analyse_fichier, inputs=file, outputs=outputs)

classement_converter.launch()
