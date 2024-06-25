from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from actions import action
from config import url, userAPI, token
import json, pickle, os, importlib, subprocess, logging

logging.basicConfig(level=logging.CRITICAL)
def install_if_not_exists(package_name):
    try:
        importlib.import_module(package_name) 
        # print(f"{package_name} Sudah Diinstall.")
    except ImportError:
        print(f"{package_name} Tidak Terinstall. Menginstall ... ")
        subprocess.check_call(["pip", "install", package_name]) 

packages = [
    "selenium",
    "webdriver_manager",
]

# Install Package if Not Exists
for package in packages:
    install_if_not_exists(package)

def main():
    print("Loading ... ")
    options = Options()
    # Install Chrome Driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    dir = os.path.dirname(os.path.abspath(__file__))
    driver.get(url)
    print("Sedang Mengambil Cookie ... ")
    # Update website cookies
    cookies = pickle.load(open(f"{dir}/APICache.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    print("Cockie Berhasil Diambil ... ")

    while True:
        requestTypeMessage = '''
0. Tutup
1. Tambah Data User
2. Detail User
3. Edit User
4. Hapus Data User

Tuliskan Angka 0-4 Untuk Melakukan Aksi : '''
        requestType={
            1: "Melakukan Tambah Data User",
            2: "Melakukan Tampil Detail User",
            3: "Melakukan Edit Data User",
            4: "Melakukan Hapus Data User"
        }
        requestTypeInput = input(requestTypeMessage)

        # if else statement for every determining case
        if int(requestTypeInput) == 0:
            break
        elif int(requestTypeInput) in [2, 4]:
            userIdMessage = "Masukkan ID User : "
            userId = input(userIdMessage)
            print(f"{requestType.get(int(requestTypeInput))} Dengan ID {userId} ... ")
        elif int(requestTypeInput) == 1:
            # looping until user input 'y' to confirm
            while True:
                name = input("Masukkan Nama User : ")
                email = input("Masukkan Email User : ")
                gender = input("Masukkan Jenis Kelamin User (male atau female): ")
                confirm = input(f"\n{requestType.get(int(requestTypeInput))} Dengan \nNama : {name}\nEmail : {email}, \nJenis Kelamin : {gender}\nApakah Data Sudah Benar ? (y/n) : ")
                if confirm.lower() == 'y':
                    break
            data = {
                "name": name,
                "gender": gender,
                "email": email,
                "status": "active"
            }
        elif int(requestTypeInput) == 3:
            # looping until user input 'y' to confirm
            while True:
                userId = input("\nMasukkan ID User : ")
                name = input("Ubah Nama User Menjadi : ")
                email = input("Ubah Email User Menjadi : ")
                gender = input("Ubah Jenis Kelamin User Menjadi (male atau female): ")
                confirm = input(f"\n{requestType.get(int(requestTypeInput))} Dengan \nNama : {name}\nEmail : {email}\nJenis Kelamin : {gender}\nApakah Data Sudah Benar ? (y/n) : ")
                if confirm.lower() == 'y':
                    break
            data = {
                "name": name,
                "gender": gender,
                "email": email,
                "status": "active"
            }
        else:
            print(f'Masukkan Jenis Aksi yang Benar')
            break
        
        # List of element ID
        requestTypeId = "rsq_type"
        APIInputId = "rsq_url"
        headerValueId = "rsq_header_value_0"
        requestBodyId = "rsq_body"
        buttonSendId = "rsq_send"
        respondStatusId = "rsp-body-title"
        respondBodyId = "rsp_body"

        APIurlCustom = userAPI if int(requestTypeInput) == 1 else f"{userAPI}/{userId}"
        
        action(driver, requestTypeId, 'select', requestTypeInput, "")
        action(driver, APIInputId, 'text', requestTypeInput, APIurlCustom)
        action(driver, headerValueId, 'text', requestTypeInput, token)
        
        # Running if request need data and convert the data to json format
        if int(requestTypeInput) in [1, 3]:
            action(driver, requestBodyId, 'text', requestTypeInput, json.dumps(data, indent=4))
        action(driver, buttonSendId, 'click', requestTypeInput, "")

        # Get respond status and respond to a vary of case
        respondStatus = action(driver, respondStatusId, 'getStatus', requestTypeInput, "").split(": ")[1]
        if respondStatus == "404":
            print("Terjadi Kesalahan!")
        elif respondStatus == "200":
            print("\nBerikut Detail User : ")
            action(driver, respondBodyId, 'getText', requestTypeInput, "")
        elif respondStatus == "201":
            print("\nData Berhasil Ditambah!")
            action(driver, respondBodyId, 'getText', requestTypeInput, "")
        elif respondStatus == "204":
            print("Data Berhasil Di Hapus!")
        else:
            action(driver, respondBodyId, 'getText', requestTypeInput, "")
        input("Klik Enter Untuk Melanjutkan ... ")

    driver.quit()

if __name__ == "__main__":
    main()
