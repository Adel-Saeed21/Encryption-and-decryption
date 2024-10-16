from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.geometry("250x200")

ENCRYPTION_MARKER = b'ENCR'  # Marker to identify encrypted files

def encrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END).strip()

        # Open the image file
        with open(file_name, 'rb') as fi:
            image = fi.read()

        # Check if the file is already encrypted by looking for the marker
        if image.startswith(ENCRYPTION_MARKER):
            messagebox.showinfo("Error", "This image is already encrypted.")
            return

        image = bytearray(image)
        for index, value in enumerate(image):
            image[index] = value ^ int(key)  

        encrypted_data = ENCRYPTION_MARKER + image

        # Save the encrypted image back
        with open(file_name, 'wb') as fi1:
            fi1.write(encrypted_data)

        messagebox.showinfo("Success", f"Image {file_name} encrypted successfully.")


def decrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END).strip()

        
        with open(file_name, 'rb') as fi:
            image = fi.read()

       
        if not image.startswith(ENCRYPTION_MARKER):
            messagebox.showinfo("Error", "This image is not encrypted.")
            return

        # Remove the encryption marker
        image = bytearray(image[len(ENCRYPTION_MARKER):])

        # Decrypt the image by applying XOR with the key
        for index, value in enumerate(image):
            image[index] = value ^ int(key)  # XOR with the key for decryption

        # Save the decrypted image back
        with open(file_name, 'wb') as fi1:
            fi1.write(image)

        messagebox.showinfo("Success", f"Image {file_name} decrypted successfully.")


# Create the GUI elements
entry1 = Text(root, height=1, width=10)
entry1.place(x=50, y=50)

b1 = Button(root, text="Encrypt", command=encrypt_image)
b1.place(x=30, y=1)

buttonDecrypt = Button(root, text="Decrypt", command=decrypt_image)
buttonDecrypt.place(x=110, y=1)

root.mainloop()
