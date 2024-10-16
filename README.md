Overview
This is a Python-based tool that allows users to encrypt and decrypt .jpg image files using a custom key. It utilizes a simple XOR-based encryption technique to scramble the image data and provides a Tkinter-based GUI for ease of use.

Key Features
Encrypts Images: Scrambles the content of a .jpg image file using XOR encryption.
Decrypts Images: Restores the original image from its encrypted form using the same XOR key.
Encryption Marker: Ensures files are not encrypted multiple times by marking encrypted files.
Simple GUI: Provides a graphical interface for selecting files, inputting the key, and triggering the encryption or decryption process.
Installation
Prerequisites
Python 3.x
Required Python library:
tkinter (This comes pre-installed with Python on most systems)
Usage
Graphical Interface
Launch the tool: Run the Python script to open the GUI window.
Input the Key: Enter a numeric key in the provided text field (e.g., 1234).
Encrypt an Image:
Click on the "Encrypt" button.
Select a .jpg image file from your system.
The tool will check if the image is already encrypted and, if not, will encrypt it using the provided key.
Decrypt an Image:
Click on the "Decrypt" button.
Select an encrypted .jpg image.
The tool will check if the image contains the encryption marker and, if so, will decrypt it using the provided key.
Notes:
You must use the same key for both encryption and decryption.
If an image is already encrypted, the tool will notify you and prevent further encryption.
