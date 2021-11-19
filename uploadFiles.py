import dropbox
import os

from dropbox.files import WriteMode

class TransferData(object):
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def UploadFile(self,fileFrom,fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        local_path = 'C:/Users/C/OneDrive/Desktop/Coding/python/Cloud Storage'
        
        for root,dirs,files in os.walk(fileFrom):
            relativePath = os.path.relpath(local_path, fileFrom)
            dropboxPath = os.path.join(fileTo,relativePath)

        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(),dropboxPath, mode=WriteMode("overwrite"))

def main():
    accessToken = 'sl.A8ORdvi0PqTqC0B2weMZ8Rc6LKpReRKTMUZ1Kqep3q-0bdBByS4aHOfwGPcW6KmNlMOtcA8sVJLY6cMy1zd2u86nmy1pRKZOKpAMMFjGToMqMmfCghxj0lhlTltxhMPz_OaanCI'
    transferdata = TransferData(accessToken)

    fileFrom = 'C:/Users/C/OneDrive/Desktop/Coding/python/Cloud Storage/key.txt'
    fileTo = '/PRO-C101/key.txt'

    transferdata.UploadFile(fileFrom,fileTo)

main()