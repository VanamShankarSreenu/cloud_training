# Cloud Training Assignment 1

## Summary:
  - Created a container,Container contains 3 Folders.(Folder1,Folder2,Folder3)
  - In each Folder there are some files.
  - Created a VNET with in East US region.
  - Added Tiger VPN
  - Created a VM and configured it with the VNET.
  - Created a flask app.
        - app.py (Gets the folder name from user and displays the folder names).
        - templates (contains html pages)
        - static(empty)
  - Pushed the code to github.
  
## Steps to deploy to VM and run Flask App.
  - Use putty to connect with vm.
  - Enter the fallowing commands in vm CLI.
  - sudo apt-get update.
  - sudo apt-get -y install python3 python3-dev.
  - sudo apt install python3-pip.
  - sudo apt-get -y install nginx.
  - sudo apt-get -y install git.
  - sudo apt install python3-flask.
  - Steps fallowed to deploy in vm.
  - git clone https://github.com/VanamShankarSreenu/cloud_training.
  - cd cloud_training.
  - pip install requirements.txt
  - python3 app.py

## Application running screenshots.
