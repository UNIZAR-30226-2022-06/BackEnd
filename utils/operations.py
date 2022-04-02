import dropbox

DROPBOX_TOKEN = 'sl.BE_8E3kyWOFMSG1RzICAYL_sVs_MuCYXIHiM-cKHe6YPHs6G0MwwqfLsoLIOV8NzcDft7IQ5AanaQ2bKZvkfy00wJHdOZ8jN6LCa302K8hmNBo3NNVo-jY7y30NsFi7liuJDvrCpDc2F'
dropbox_file_location = "/libros/"
dropbox_imagen_location = "/imagen/"
local_file_location = './libros_local/'

dbx = dropbox.Dropbox(DROPBOX_TOKEN)
user = dbx.users_get_current_account()

#
# Sube el archivo llamado 'file' a dropbox, 'file' tiene que estar en el directorio ".\libros_local"
#
def upload_file (file):
    with open(local_file_location+file, "rb") as f:
        dbx.files_upload(f.read(), dropbox_file_location+file, mode=dropbox.files.WriteMode.overwrite)

#
# Descarga el 'file de dropbox a local, en el directorio ".\libros_local"
#
def download_file (file):
    with open(local_file_location+file, "w") as f:
        dbx.files_download_to_file(local_file_location+file, dropbox_file_location+file)

#with open(file_from, "rb") as f:
    #dbx.files_upload(f.read(), file_to, mute=True)
#dbx.files_upload(open(file_from,'rb').read(), file_to)
