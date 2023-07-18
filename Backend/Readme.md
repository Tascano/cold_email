Here are the steps to run the FastAPI email server:

1. Install dependencies

```
pip install fastapi uvicorn[standard] fastapi-mail python-multipart
```

2. Save the code in a file such as `main.py`

3. Update the SMTP configuration with your actual credentials

4. Run the server:

```
uvicorn main:app --reload
```

5. The FastAPI server should now be running on http://127.0.0.1:8000

6. You can test sending an email via POST request:

```
curl --location --request POST 'http://127.0.0.1:8000/send-mail' \
--header 'Content-Type: application/json' \
--data-raw '{
    "recipients": [
        "recipient1@email.com",
        "recipient2@email.com"
    ]
}'
```

7. Check the recipient emails for the test message.

So in summary - install dependencies, update config, run Uvicorn server, make POST request to /send-mail endpoint with list of emails.

The --reload option will restart the server on code changes. Make sure to update the SMTP settings and enable less secure apps for sender email before testing.