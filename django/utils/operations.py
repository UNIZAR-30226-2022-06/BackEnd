import os, PyPDF2
from fpdf import FPDF
from epub2txt import epub2txt
from posixpath import split
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from pydrive2.files import FileNotUploadedError

import convertapi
convertapi.api_secret = 'K7dXPhcugEDqJr28'

directorio_credenciales = 'credentials_module.json'
# ID UNICOS DE LAS CARPETAS DEL DRIVE
main_id_folder = '0AHc558HLxAXpUk9PVA'
file_id_folder = "1FEctPuVXqzFzAnp4hV2zD0cvaw0pi-wE"
imagen_id_folder = "1ozwxIKKXnb0TRRg2jgPm3EfAZGpmXcn_"
# RUTAS DE LAS CARPETAS DONDE SE DESCARGAN LOS ARCHIVOS
local_file_location = './libros_local/'
local_imagen_location = './imagen_local/'

# INICIAR SESION
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = directorio_credenciales
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(directorio_credenciales)
    credenciales = GoogleDrive(gauth)
    return credenciales

# SUBIR UN ARCHIVO CON NOMBRE 'archivo' DESDE 'file_location' A LA CARPETA DE DRIVE CON ID 'id_folder'
def subir_archivo(archivo, id_folder, file_location):
    ruta_archivo = file_location + archivo
    credenciales = login()
    archivo = credenciales.CreateFile({'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    archivo['title'] = ruta_archivo.split("/")[-1]
    archivo.SetContentFile(ruta_archivo)
    archivo.Upload()

# DESCARGAR UN ARCHIVO CON ID 'id_drive' DE DRIVE A 'local_location'
def descargar_archivo_por_id(id_drive, local_location):
    credenciales = login()
    archivo = credenciales.CreateFile({'id': id_drive}) 
    nombre_archivo = archivo['title']
    archivo.GetContentFile(local_location + nombre_archivo)

# DESCARGAR UN ARCHIVO DE DRIVE POR NOMBRE 'nombre_archivo' A 'local_location'
def descargar_archivo_por_nombre(nombre_archivo, local_location):
    credenciales = login()
    lista_archivos = credenciales.ListFile({'q': "title = '" + nombre_archivo + "'"}).GetList()
    if not lista_archivos:
        print('No se encontro el archivo: ' + nombre_archivo)
    archivo = credenciales.CreateFile({'id': lista_archivos[0]['id']}) 
    archivo.GetContentFile(local_location + nombre_archivo)

# BUSCAR ARCHIVOS
def busca(query):
    resultado = []
    credenciales = login()
    # Archivos con el nombre 'mooncode': title = 'mooncode'
    # Archivos que contengan 'mooncode' y 'mooncoders': title contains 'mooncode' and title contains 'mooncoders'
    # Archivos que NO contengan 'mooncode': not title contains 'mooncode'
    # Archivos que contengan 'mooncode' dentro del archivo: fullText contains 'mooncode'
    # Archivos en el basurero: trashed=true
    # Archivos que se llamen 'mooncode' y no esten en el basurero: title = 'mooncode' and trashed = false
    lista_archivos = credenciales.ListFile({'q': query}).GetList()
    for f in lista_archivos:
        # ID Drive
        print('ID Drive:',f['id'])
        # Link de visualizacion embebido (mostrar archivo sin salir de la página)
        print('Link de visualizacion embebido:',f['embedLink'])
        # Link de descarga
        print('Link de descarga:',f['downloadUrl'])
        # Nombre del archivo
        print('Nombre del archivo:',f['title'])
        # Tipo de archivo
        print('Tipo de archivo:',f['mimeType'])
        # Esta en el basurero
        print('Esta en el basurero:',f['labels']['trashed'])
        # Fecha de creacion
        print('Fecha de creacion:',f['createdDate'])
        # Fecha de ultima modificacion
        print('Fecha de ultima modificacion:',f['modifiedDate'])
        # Version
        print('Version:',f['version'])
        # Tamanio
        print('Tamanio:',f['fileSize'])
        resultado.append(f)
    return resultado

# CREAR CARPETA EN LA UNIDAD
def crear_carpeta(nombre_carpeta):
    credenciales = login()
    folder = credenciales.CreateFile({'title': nombre_carpeta, 
                               'mimeType': 'application/vnd.google-apps.folder',
                               'parents': [{"kind": "drive#fileLink",\
                                                    "id": main_id_folder}]})
    folder.Upload()

# Convierte  un archivo .txt a .pdf, con el mismo nombre, que se encuentra en 'local_file_location'
def convert_txt_pdf(archivo):
    if os.path.isfile(local_file_location+archivo):
        pdf = FPDF()   
        pdf.add_page()
        pdf.set_font("Arial", size = 10)
        f = open(local_file_location+archivo, "r")
        # insert the texts in pdf
        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
        # save the pdf with name .pdf
        split_archivo = archivo.split(".", 1)
        pdf_file = split_archivo[0]+".pdf"
        pdf.output(local_file_location+pdf_file)

# Convierte  un archivo .epub a .txt, con el mismo nombre, que se encuentra en 'local_file_location'
def convert_epub_txt(archivo):
    if os.path.isfile(local_file_location+archivo):
        split_archivo = archivo.split(".", 1)
        txt_file=local_file_location+split_archivo[0]+".txt"
        local_file=open(txt_file,'w')
        local_file.write(epub2txt(local_file_location+archivo))

# Devuelve el contenido de la pagina 'numero_pagina' de 'archivo'
def traducir_archivo(archivo, numero_pagina):
    split_archivo = archivo.split(".", 1)
    if not os.path.isfile(local_file_location+archivo):
        descargar_archivo_por_nombre(archivo, local_file_location)
    if (split_archivo[1]=='pdf'):
        local_archivo = open(local_file_location+archivo, 'rb')
        pdfReader = PyPDF2.PdfFileReader(local_archivo) # print(pdfReader.numPages)
        pageObj = pdfReader.getPage(numero_pagina) #print(pageObj.extractText())
        print(pageObj.extractText()) #-------
        return pageObj.extractText() 
    elif (split_archivo[1]=='epub'):
        #convertapi.convert('pdf', {
        #    'File': 'C:/Users/David/Desktop/ProySoft/BackEnd/django/utils/libros_local/libro.epub'
        #}, from_format = 'epub').save_files('C:/Users/David/Desktop/ProySoft/BackEnd/django/utils/libros_local')
        #convert_epub_txt(archivo)
        #convert_txt_pdf(split_archivo[0]+".txt")
        pdf_file =  open(local_file_location+split_archivo[0]+".pdf", 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        print (number_of_pages)
        page = read_pdf.getPage(numero_pagina)
        page_number = read_pdf.getPageNumber(page)
        page_content = page.extractText()
        print (page_content)
        print (page_number)
        print(local_file_location+split_archivo[0]+".pdf")
        local_archivo = open(local_file_location+split_archivo[0]+".pdf", 'rb')
        print(local_file_location+split_archivo[0]+".pdf")
        pdfReader = PyPDF2.PdfFileReader(local_file_location+split_archivo[0]+".pdf") # print(pdfReader.numPages)
        print(local_file_location+split_archivo[0]+".pdf")
        pageObj = pdfReader.getPage(numero_pagina) #print(pageObj.extractText())
        print(pageObj.extractText()) #-------
        #return pageObj.extractText()       
    else:
       print("EXTENSION DIFERENTE")

if __name__ == "__main__":
    traducir_archivo("libro.epub", 7)
    #traducir_archivo("libro.epub", 6)
    #convert_epub_txt("libro.epub")
    #subir_archivo("prueba.pdf",file_id_folder, local_file_location)
    #descargar_libro_por_nombre('1.png')
    #crear_archivo_texto('Hola_mundo', 'Holi')
    #subir_libro('prueba.pdf')
    #busca("title = 'prueba.pdf' and trashed=false")
    #ruta_archivo = '/home/falv/Escritorio/fondo.jpg'
    #id_folder = '0AI_9cD6f9EEZUk9PVA'
    #id_drive = '1LVdc-DUwr30kfrA30cVO3K92RVh56pmw'
    #ruta_descarga = '/home/falv/Descargas/'
    #crear_archivo_texto('HolaDrive.txt','Hey MoonCoders',id_folder)
    #subir_archivo(ruta_archivo,id_folder)
    #bajar_archivo_por_id(id_drive,ruta_descarga)
    #busca("title = 'mooncode.png'")
    #bajar_acrchivo_por_nombre('Logo_1.png',ruta_descarga)
    #borrar_recuperar('1lHBMFjdyKfAYRa4M57biDZCiDwFhAYTy')
    #crear_carpeta('hola_folder',id_folder)
    #mover_archivo('1PmdkaivVUZKkDwFapSWrXNf6n6pO_YK-','1uSMaBaoLOt7F7VJiCZkrO4ckvj6ANecQ')
