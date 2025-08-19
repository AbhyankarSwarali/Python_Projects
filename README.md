# 🔑 Random Password Generator

This is a simple Python script to generate strong random passwords.\
It allows you to specify: - Minimum password length\
- Whether to include numbers\
- Whether to include special characters

The script ensures the generated password meets the chosen criteria.

------------------------------------------------------------------------

## 📌 Features

-   Random password generation with customizable length\
-   Optionally include numbers\
-   Optionally include special characters\
-   Guarantees at least one number and/or special character if selected

------------------------------------------------------------------------

## 🚀 How to Use

1.  Clone this repository or copy the script.\

2.  Run the Python file:

    ``` bash
    python password_generator.py
    ```

3.  Enter the minimum length, and whether you want numbers and/or
    special characters.

------------------------------------------------------------------------

## 📝 Example Run

``` bash
Enter the minimum length: 12  
Do you want to have numbers (y/n) y  
Do you want to have special characters (y/n) y  
The generated password is: J9a!kD7#Lm2z
```

------------------------------------------------------------------------

## 📷 Code Snapshot

Here's the core function from the project:

``` python
def generate_password(min_length, numbers=True, special_characters=True): 
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers: 
        characters += digits
    if special_characters: 
        characters += special

    pswd = ''
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pswd) < min_length: 
        new_char = random.choice(characters)
        pswd += new_char

        if new_char in digits: 
            has_number = True
        elif new_char in special: 
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
        
    return pswd
```

------------------------------------------------------------------------

✅ That's it! Run the script and generate secure random passwords.
