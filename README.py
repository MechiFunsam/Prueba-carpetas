# Prueba-carpas
importar streamlit como st
importar sistema operativo
Importar shutil

# Definimos las carpetas de categorías
carpetas = ['Metodologías de la investigación', 'Metodologías cualitativas', 'Tic y humanidades']
base_dir = 'subidas'

# Creamos las carpetas si no existen
os.makedirs(directorio_base, exist_ok=Verdadero)
Para carpeta en carpetas:
    os.makedirs(os.path.join(directorio_base, carpeta), exist_ok=Verdadero)

# Función para subir archivos
def upload_file(archivo, categoría):
    Si el archivo no es Ninguno:
        # Ruta de destino donde se guardará el archivo
        ruta_archivo = os.path.join(directorio_base, categoría, nombre_archivo)
        con open(file_path, "wb") como f:
            f.write(archivo.getbuffer())
        st.success("Tu archivo ha sido subido exitosamente!")

# Función para listar archivos y permitir la descarga
def list_files(categoría):
    archivos = os.listdir(os.path.join(base_dir, categoría))
    devolver archivos

st.title("Repositorio común")

# Subida de archivos
st.header("Suma tus textos")
uploaded_file = st.file_uploader("Selecciona un texto", type=['txt', 'csv', 'jpg', 'png', 'pdf'])
selected_category = st.selectbox("Selecciona el material", folders)
# Descarga de archivos
st.header("Descargar archivo")
categoria_to_download = st.selectbox("Selecciona una materia para descargar", carpetas)

si st.button("Ver textos"):
    archivos = lista_archivos(categoría_a_descargar)
    si archivos:
        selected_file = st.selectbox("Selecciona el archivo para descargar", files)
        si st.button("Descargar"):
            ruta_archivo = os.path.join(directorio_base, categoría_a_descargar, archivo_seleccionado)
            con open(file_path, 'rb') como f:
                st.download_button("Descargar " + archivo_seleccionado, f, nombre_archivo=archivo_seleccionado)
    demás:
        st.warning("No hay archivos en esta categoría.")
