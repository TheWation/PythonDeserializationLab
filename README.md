# Python Insecure Deserialization Lab

This project demonstrates a vulnerable environment that allows you to test Python's insecure deserialization issue. It is built using FastAPI and showcases how Python's `pickle` module can be exploited when handling untrusted data.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Warning](#warning)
4. [License](#license)

## Installation

Follow these steps to set up the project:

### Prerequisites
- Python 3.7 or higher
- `pip` for managing Python packages

### Steps
1. Clone the repository:
```bash
git clone https://github.com/TheWation/PythonDeserializationLab
cd PythonDeserializationLab
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
 ```bash
 uvicorn main:app --reload
 ```

The server will be available at `http://127.0.0.1:8000`.

## Usage

1. Once the server is running, visit the homepage: `http://127.0.0.1:8000`.

2. You will see a list of books with clickable links. Each book's information is serialized using Python's `pickle` module and encoded using `base64`.

3. Clicking on a book title will send the serialized book data to the server, which will then deserialize it using `pickle`. This is where the insecure deserialization vulnerability is demonstrated.

4. The book details will be shown, including the title, author, and year of publication.

## Warning

**This project is intentionally vulnerable and should not be used in production environments.** The code showcases the risk of insecure deserialization using Python's `pickle` module. It is recommended to only run this project in a controlled, isolated environment, specifically for educational or testing purposes. Deserializing untrusted data with `pickle` can allow attackers to execute arbitrary code.

## License

This project is for educational purposes only and is not intended for commercial use. Use at your own risk.