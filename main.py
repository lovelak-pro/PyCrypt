import secrets
import webview
import pyautogui as py


class APP:
    # Just a warning to user on how to Decrypt !
    def warning(self):
        py.alert('Make sure the ( .txt ) file is in the same folder as this tool !', 'Warning', 'OK')
        py.alert('Just Copy the file name without ( .txt ) and paste it in the textarea !', 'Warning', 'OK')

    # Encryption Process
    def encrypt(self,key_to_encrypt):
        name = secrets.token_hex(3)
        for x in range(len(key_to_encrypt)):
            rann = secrets.token_hex(3)
            safe = key_to_encrypt[x]+ rann
            with open(f"KEY-{name}.txt","a") as f:
                f.write(safe)
            
    # Decryption Process
    def decrypt(self ,key_to_decrypt):

        # Generating a random 4 letter string
        name = secrets.token_hex(2)

        # Cheacking if the file is present or not
        try:
            with open(f"{key_to_decrypt}.txt","r") as f:
                read = f.read()
        except Exception as e:

            # if the file is not present it will show a message to user
            if 'No such file or directory' in str(e):
                py.alert('File Not Found !', 'Error', 'OK')
            return
        
        # if the file is present it will start the decryption process
        for i in range(0, len(read)-1, 7):
            print(read[i])
            with open(f"DECRYPTED-{name}.txt","a") as f:
                f.write(read[i])
            
            
# this is to create the window
if __name__ == "__main__":
    app = APP()
    window = webview.create_window("PyCrypt", "src/index.html",js_api=app, width=400, height=230,resizable=False)
    webview.start()