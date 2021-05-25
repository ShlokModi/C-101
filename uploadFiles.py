import dropbox
import os
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = '-Hh86Q7qstsAAAAAAAAAATCjZXuNf4DP4DQc8SjDmNR4HvKsg4FnNR9iteGRBMzB'
    transferData = TransferData(access_token)

    file_from = input("File to be uploaded: ")
    file_to = input("Full path to upload the file to, including name that you wish the file to be called once uploaded: ")
    transferData.upload_file(file_from, file_to)
    print("File is succesfully uploaded")

main()