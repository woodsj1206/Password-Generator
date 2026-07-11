# Password-Generator
This project generates a password containing uppercase characters, lowercase characters, special characters, and digits.

## Usage
Follow the steps below to set up and run the program:

### 1. Clone the Repository
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/woodsj1206/Password-Generator.git
cd Password-Generator
```

### 2. Run the Script
Execute the main script:
```bash
python main.py --num_upper_chars 2 --num_lower_chars 3 --num_digits 2 --num_special_chars 1
```

> [!NOTE]
> The program accepts the following command-line arguments:
> ```
> OPTIONAL:
> --num_upper_chars NUM_UPPER_CHARS
>     The number of uppercase letters (A-Z) that will appear in the password.
>     Default is 2.
> 
> --num_lower_chars NUM_LOWER_CHARS
>     The number of lowercase letters (a-z) that will appear in the password.
>     Default is 3.
> 
> --num_digits NUM_DIGITS
>     The number of digits (0-9) that will appear in the password.
>     Default is 2.
>
> --num_special_chars NUM_SPECIAL_CHARS
>     The number of special characters that will appear in the password.
>     Default is 1.
> ```

## Project Structure
The following shows the main file structure of the project with brief descriptions:
```
├── main.py                    # Run the project
```

## Development Environment
Tools and technologies used in the development of the project:
- Microsoft Visual Studio Code
- Python 3.13.7
