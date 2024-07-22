# Encryption Documentation
Documentation of a basic fernet encryption script.

## Downloading
To download this project, you can run `pip install -i https://test.pypi.org/simple/ EncryptDocumentationBarrett`. This will download the project and its subsequent folders such as `build` and `source`. The project also contains .toml files to display required dependencies, as well as a PDF outlining how the documentation was built.

## Usage

### Documentation Usage
To view documentation you can navigate to your file explorer and open `secret_util.py` which is under the `build` folder. Open this in your preferred browser, Google Chrome is recommended. Alternatively, you can install Sphinx (`pip install Sphinx`), navigate to the `build` folder, and run the command `start secret_util.html` in the terminal.

### Script Usage
To utilize the encryption script, navigate to the `source` folder and run the command `start secret_util.html <filename>`. It will prompt you to enter a secret which will be encrypted in the file. After the secrent is entered, the file with the key and encrypted secret will be saved to your home directory with the name `<filename.enc>`.


## Poetry Installation Instructions
Run `poetry install` to install the env.  
Run `poetry run pre-commit install` to initialize the git hooks.  
Run `poetry run pre-commit run --all-files` if there are file that were committed before adding the git hooks.  
Activate the shell with: `poetry shell`.