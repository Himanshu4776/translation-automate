# Translation Automate

It shows how you can automate Translations of your text, json data, text files and many more using aws bedrock.

```markdown
# Translations Using Python and AWS Bedrock

This Python project demonstrates how to use the AWS Bedrock service to convert text, json, API responses and text files from one language to another using the AWS SDK and requests library.

## Prerequisites

Before running these script, make sure you have the following prerequisites in place:

1. AWS Access Key and Secret Key: You need valid AWS credentials with permissions to access the Bedrock service.

2. Python: Ensure you have Python installed on your system.

3. Required Libraries: Install the necessary Python libraries using pip:

   ```bash
   pip install boto3 requests
   ```

## Usage

1. Replace `access_key` and `secret_key` with your AWS Access Key ID and Secret Access Key.

2. Set the `user_input` variable to the text you want to convert.

3. Set the `language` variable to the target language for conversion.

4. Run the scripts using Python:

   ```bash
   python script_file_name.py
   ```

5. The script will send a request to the Bedrock service and display the converted text.

## Configuration

You can customize the script by modifying the following parameters in the code:

- `access_key`: Your AWS Access Key ID.
- `secret_key`: Your AWS Secret Access Key.
- `service`: The AWS service name (Bedrock in this case).
- `url`: The Bedrock service endpoint URL.
- `user_input`: The input text you want to convert.
- `language`: The target language for conversion.

## Text Translation Example

Here's an example of how to use the text_translate script:

```python
Please enter the text to convert: Hello, world!
Please enter in which language you want to convert: French
Converted result response:
Bonjour, le monde !
```

## JSON Translation Example

Here's an example of how to use the json_translate script:

```python
Please enter the JSON to convert:
{
  "headline": "Business Management System",
  "user_initial": "G",
  "name": "Himanshu"
}
Please enter in which language you want to convert: French
Converted result response:
{
  "headline": "Système de gestion des affaires",
  "user_initial": "G",
  "name": "Himanshu"
}
```

## Text File Translation Example

Here's an example of how to use the script:

1. Create a text file `test.txt` with the following content:

   ```
   Hello, world! This is a test.
   ```

2. Run the script and enter the target language when prompted (e.g., French).

3. The script will display the converted text:

   ```
   Bonjour, le monde ! Ceci est un test.
   ```

# NOTE

This project is just to showcase the working and how anyone can utilise the amazon bedrock to automate the stuffs. The is just for knowledge purpose and not intended to show accuracy or any model.
