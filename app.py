from flask import Flask,redirect, url_for, request,render_template
import os
from azure.storage.blob import ContainerClient
  

app = Flask(__name__)


#Get request
@app.route('/success/<name>')
def AccessBlobStorage(name):
    #  stores file names
    filenames = []
    # accessing connection  string.
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    # connecting to vm blob container.
    blob_service_client = ContainerClient.from_connection_string(connect_str,container_name="codecontainer")
    #listing the folders and files present in container.
    blob_list = blob_service_client.list_blobs()
    #search for the filename provided .
    for blob in blob_list:
        temp = str(blob.name)
        folder,file = temp.split('/')
        if folder  ==  name:
            filenames.append(file)
    # if file is not found sends msg "file dosen't exsist" as context.
    if filenames == []:
        return render_template('listfoldernames.html',filenames=["File name dosen't match with existing files"])
    return render_template('listfoldernames.html',filenames=filenames)


# Home page of application
@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        Folder_name = request.form['name']
        return redirect(url_for('AccessBlobStorage', name=Folder_name))
    return render_template('home.html')
 

#app run
if __name__ == '__main__':
    app.run(debug=True)