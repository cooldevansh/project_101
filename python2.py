import dropbox

class TransferData:
    def __init__(self, access):
        self.access = access
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access)


        file_upload = open(file_from, 'rb')
        dbx.files_upload(file_upload.read(), file_to)
def main():
    access = "sl.BdVUDo1wVJZypw3JcLo0L2RHd5gjJH4h6FOm9q3lT3f4mvWzK0lLH5MqejUXg6xkjdQmtmorS73x7g7CkRwiI1_aZHk3K3BfvfLqo8eSia-IBWfEqVpF6kjKORgX9dJaS5pCsrEUv74"
    transferData = TransferData(access)
    file_from="dropboxtest.txt"
    file_to = "/test_dropbox/test.txt"
    transferData.upload_file(file_from, file_to)
    print("File has been moved to dropbox.")
main()