# serverless-workshop

This is a repo I created running through the Queer Code Workshop on AWS Serverless, using AWS Lambda backed by DynamoDB.

You can use these instructions to follow along yourself.

First you should create a directory named `contact-api` and then change to it.

```bash
mkdir contact-api
cd contact-api
```

## Project set up
The following commands were run:

To install the serverless command line utility (`sls`):
```bash
npm install -g serverless
```

Then “link” serverless with this project:

```bash
npm init -f
npm install serverless-wsgi serverless-python-requirements
```

Instruct Python to install dependencies locally, not globally:

```bash
python3 -m venv env
source env/bin/activate
```

Then install Python dependencies:

```bash
pip install flask boto3 werkzeug
```

Output those dependencies to a file to be checked in:

```bash
Pip freeze > requirements.txt
```

## The code

All the code is in three files:

| File | Description |
| ---- | ----------- |
| `app.py` | Definition of the routes |
| `test.py` | Tests to help describe what our routes would do |
| `serverless.yml` | Describes how AWS services should be provisioned (lambda and database instances) |

In the workshop we started by writing the first test in `test.py` (`test_hello_world`) and then making that pass by defining the first route in `app.py`. Then we repeated that process for the next two tests, `test_contact_submission` and `test_missing_params`.

*Note*: I have commented out the calls to DynamoDB in `app.py` because I don’t have AWS set up on my machine 😱. This caused tests to fail. We discussed the solutions to this in the workshop, which is either to get AWS configured (see below) or to use a Python package named [moto](https://github.com/spulec/moto).

## Running tests

On my Mac I can run tests with `python3 test.py`.

## Deploying to AWS

You’ll need an AWS account for this. Be careful as you may get charged!

If you haven’t already configured AWS in your environment:

```bash
aws configure
```

```bash
sls deploy --stage=dev
```
