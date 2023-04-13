import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BRZaAOYMWoL6oNdaW_r7SA3fahx9J88K2TJRKi-6mvY3HR9AERvcqin4jeQ7p71zRL202Nm8IMjSxl8cInC-jVZFjC1QmZsrDYBQBfEnRJEMFi7626tvNdQkgdety1_pMT2xJm4'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '\C:\Users\amogh_0nme2wu\Dropbox\Test\test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()