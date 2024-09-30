# Prueba-carpetas
import streamlit as st
import os
import shutil

# Definimos las carpetas de categorías
folders = ['Categoría1', 'Categoría2', 'Categoría3', 'Categoría4']
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
        st.success("Archivo subido exitosamente!")

# Función para listar archivos y permitir la descarga
def list_files(category):
    files = os.listdir(os.path.join(base_dir, category))
    return files

st.title("Aplicación de Gestión de Archivos")

# Subida de archivos
st.header("Subir archivo")
uploaded_file = st.file_uploader("Selecciona un archivo", type=['txt', 'csv', 'jpg', 'png', 'pdf'])
selected_category = st.selectbox("Selecciona la categoría", folders)

if st.button("Subir Archivo"):
    upload_file(uploaded_file, selected_category)

# Descarga de archivos
st.header("Descargar archivo")
category_to_download = st.selectbox("Selecciona la categoría para descargar", folders)

if st.button("Listar Archivos"):
    files = list_files(category_to_download)
    if files:
        selected_file = st.selectbox("Selecciona el archivo para descargar", files)
        if st.button("Descargar"):
            file_path = os.path.join(base_dir, category_to_download, selected_file)
            with open(file_path, 'rb') as f:
                st.download_button("Descargar " + selected_file, f, file_name=selected_file)
    else:
        st.warning("No hay archivos en esta categoría.")
