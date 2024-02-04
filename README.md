# Traffic Fine Checker

This Flask application demonstrates a secure method for querying traffic fines using vehicle plate numbers and TIN numbers. By employing encryption, it aims to enhance the privacy and security of user data during transmission.

## Features

- **Secure Data Transmission**: Utilizes AES encryption and SHA256 hashing to encrypt plate numbers and TIN numbers before sending them over the network.
- **Data Privacy Compliance**: Aligns with best practices for data protection, offering a method that can help in adhering to data privacy laws such as Rwanda's Data Protection Law.


## Installation

Ensure you have Python 3.x installed on your system. Clone this repository, then navigate to the project directory and install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the application:

```bash
python app.py
```

Navigate to `http://localhost:5000/` in your web browser. Enter a plate number and TIN number to check for traffic fines while keeping the data encrypted during transmission.

## How It Works

1. **Encryption**: The application generates a timestamp-based key for AES encryption. It encrypts the combined plate number and TIN number along with the timestamp, ensuring each session's key is unique.
2. **Decryption**: Demonstrates how the encrypted values can be safely decrypted on the server-side, retrieving the original information.
3. **Secure API Call**: Makes a secure request to the `irembo.gov.rw` API endpoint, simulating how encrypted data can be transmitted securely.

## Security Considerations
- Consider implementing additional layers of security depending on the application's context and sensitivity of data being processed.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Disclaimer

This application is for demonstration and educational purposes only. It is important to note that I do not own the platform mentioned (irembo.gov.rw), and the script provided is not intended for production use. The code is meant for research and learning purposes, highlighting the importance of data encryption in protecting personal information. Use of this application should be in compliance with applicable laws and regulations concerning data protection and privacy.
