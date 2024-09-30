# Prueba-carpetas
import streamlit as st
import os
import shutil

# Definimos las carpetas de categorías
folders = ['Metodologías de la investigación', 'Metodologias cualitativas', 'Tic y humanidades']
base_dir = 'uploads'

# Creamos las carpetas si no existen
os.makedirs(base_dir, exist_ok=True)
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# Función para subir archivos
def upload_file(file, category):
    if file is not None:
        # Ruta de destino donde se guardará el archivo
        file_path = os.path.join(base_dir, category, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        st.success("Tu archivo ha sido subido exitosamente!")

# Función para listar archivos y permitir la descarga
def list_files(category):
    files = os.listdir(os.path.join(base_dir, category))
    return files

st.title("Comunsam repositorio")

# Subida de archivos
st.header("Sumá tus textos")
uploaded_file = st.file_uploader("Selecciona un texto", type=['txt', 'csv', 'jpg', 'png', 'pdf'])
selected_category = st.selectbox("Selecciona la materia", folders)

if st.button("Selecioná la materia y subí tu texto"):  
    upload_file(uploaded_file, selected_category)

# Descarga de archivos
st.header("Descargar archivo")
category_to_download = st.selectbox("Selecciona la categoría para descargar", folders)

if st.button("Ver textos"):
    files = list_files(category_to_download)
    if files:
        selected_file = st.selectbox("Selecciona el archivo para descargar", files)
        if st.button("Descargar"):
            file_path = os.path.join(base_dir, category_to_download, selected_file)
            with open(file_path, 'rb') as f:
                st.download_button("Descargar " + selected_file, f, file_name=selected_file)
    else:
        st.warning("No hay archivos en esta categoría.")
