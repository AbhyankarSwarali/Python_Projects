# 🔐 Password Manager

This project is a lightweight **Password Manager** built in Python using
the **cryptography** library.\
It allows you to **securely store and retrieve encrypted passwords**
using the **Fernet symmetric encryption** algorithm.



## 📌 About Fernet

[Fernet](https://cryptography.io/en/latest/fernet/) is a symmetric
encryption method provided by the `cryptography` library in Python. It
guarantees:\
- **Confidentiality** -- All passwords are encrypted before being
stored.\
- **Integrity** -- Any tampering with the encrypted data will make
decryption fail.\
- **Simplicity** -- Encryption and decryption are handled with just a
few lines of code.

Fernet uses:\
- AES in CBC mode with a 128-bit key for encryption\
- HMAC with SHA256 for authentication\
- Base64 encoding for safe storage

This ensures your stored passwords remain **safe and secure**.

------------------------------------------------------------------------

## ⚙️ Setup

1.  Install dependencies:

    ``` bash
    pip install cryptography
    ```

2.  Generate a key (only once):

    ``` python
    from cryptography.fernet import Fernet

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    ```

3.  Save the key file (`key.key`) safely. Losing it will make decryption
    impossible.

------------------------------------------------------------------------

## ▶️ Usage

Run the program:

``` bash
python password_manager.py
```

You'll be prompted to either:\
- **Add** → Save a new encrypted password\
- **View** → Decrypt and show saved passwords\
- **Quit** → Exit the program

### Example Run

``` text
Do you want to add a new password or view the existing passwords? (add/view). Press 'q' to quit: add
Account name: GitHub
Password: mysecret123

Do you want to add a new password or view the existing passwords? (add/view). Press 'q' to quit: view
Username:  GitHub
Password:  mysecret123
```

------------------------------------------------------------------------

> ⚠️ **Note:** The `key.key` file in this repository is included only
> for **educational/demo purposes**.\
> Do not use it in production for storing real passwords. Always keep
> your encryption keys private.

## 🛡️ Security Notes

-   Keep the `key.key` file **private and safe**.\
-   Without the key, you cannot decrypt stored passwords.\
-   Don't share your `Passwords.txt` file with anyone unless you trust
    them and have securely shared the key.
