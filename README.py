# Prueba-carpetas  
import streamlit as st  
import os  
import shutil  

# Definimos las carpetas de categorías  
carpetas = ['Metodologías de la investigación', 'Metodologías cualitativas', 'TIC y humanidades']  
base_dir = 'subidas'  

# Creamos las carpetas si no existen  
os.makedirs(base_dir, exist_ok=True)  
for carpeta in carpetas:  
    os.makedirs(os.path.join(base_dir, carpeta), exist_ok=True)  

# Función para subir archivos  
def upload_file(uploaded_file, selected_category):  
    if uploaded_file is not None:  
        # Ruta de destino donde se guardará el archivo  
        file_name = uploaded_file.name  # Obtenemos el nombre del archivo  
        file_path = os.path.join(base_dir, selected_category, file_name)  
        with open(file_path, "wb") as f:  
            f.write(uploaded_file.getbuffer())  
        st.success("Tu archivo ha sido subido exitosamente!")  

# Función para listar archivos y permitir la descarga  
def list_files(selected_category):  
    files = os.listdir(os.path.join(base_dir, selected_category))  
    return files  

st.title("Repositorio ComUnsam")  

# Subida de archivos  
st.header("Suma tus textos")  
uploaded_file = st.file_uploader("Selecciona un texto", type=['txt', 'csv', 'jpg', 'png', 'pdf'])  
selected_category = st.selectbox("Selecciona el material", carpetas)  

# Descarga de archivos  
st.header("Descargar archivo")  
categoria_a_descargar = st.selectbox("Selecciona una materia para descargar", carpetas)  

if st.button("Ver textos"):  
    archivos = list_files(categoria_a_descargar)  
    if archivos:  
        selected_file = st.selectbox("Selecciona el archivo para descargar", archivos)  
        if st.button("Descargar"):  
            file_path = os.path.join(base_dir, categoria_a_descargar, selected_file)  
            with open(file_path, 'rb') as f:  
                st.download_button("Descargar " + selected_file, f, file_name=selected_file)  
    else:  
        st.warning("No hay archivos en esta categoría.")
