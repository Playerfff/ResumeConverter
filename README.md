# Django Resume Converter

## Introduction

This Django project allows users to upload their resume in PDF format and converts it into HTML format for easy viewing.

## Features

Upload a resume in PDF format.

Extract text from the uploaded PDF.

Display the extracted text in an HTML format.

## Installation and Setup

Follow these steps to set up and run the project on your local machine.


```
git clone <repository_url>
cd ResumeConverter
```


```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate  # Apply Migrations
python manage.py runserver  # Run the Server
```
Open your browser and go to:

http://127.0.0.1:8000/

Upload a PDF resume and see the extracted content displayed as HTML.