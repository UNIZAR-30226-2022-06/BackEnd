import dropbox

DROPBOX_TOKEN = 'sl.BEx7ek2xTjmymKprCLfHQCyquB-TuDE_YZpO07X8fGf3rbv8359Pa0oYrxVH2DZ-mPq7MMUenM8TPhpx9ZBvJqzyilxDpee0msZqlfbpbJ98OsD6Db6tPczJqPSLqrOIIEzhNW_Xcq9X'
file_from = '1.png'
file_to = '/libros/2.png'

dbx = dropbox.Dropbox(DROPBOX_TOKEN)
user = dbx.users_get_current_account()
#print(user)

with open(file_from, "rb") as f:
    dbx.files_upload(f.read(), file_to, mute=True)
#dbx.files_upload(open(file_from,'rb').read(), file_to)