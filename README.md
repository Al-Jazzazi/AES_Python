# AES File Encryption and Decryption

This project provides a Python script to encrypt and decrypt files using AES encryption in EAX mode. 

## Prerequisites

Before running the script, ensure you have Python installed on your system. You will also need to install the required library:

```bash
pip install pycryptodome
```

## How to Use

1. **Prepare the Demo File**:  
   A demo file, `demofile.txt`, is included for testing. Make sure it is in the same directory as the script.

2. **Run the Script**:  
   Use the following command to encrypt and decrypt the demo file:
   ```bash
   python3 script.py demofile.txt
   ```
   If you want to use your own file: 
   ```bash
   python3 script.py PATH_TO_FILE
   ```

3. **Expected Output**:  
   The script will:
   - Generate a random AES encryption key.
   - Encrypt the contents of `demofile.txt`.
   - Print the ciphertext and decrypted data.

## Notes

- The script is configured to handle binary files, so you can test it with text or any binary content.
- The decrypted data will match the original file's contents exactly unless the file is modified or the encryption key is incorrect.
```

