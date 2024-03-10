# Music - Let's Talk About Kendrick Lamar

This is a 3 part project. A home page with information about Kendrick. An accounts section to register/login users. A articles section for users to post their thoughts.

## Installation

Clone the repository through cmd by running:

```bash
git clone https://github.com/3l-jay/school-django-project.git
```
Use the following command to install required dependencies:

To set up your own `SECRET_KEY` for this Django project, follow these steps:

1. Open a terminal window.
2. Navigate to your Django project directory.
3. Run the following command to generate a new secret key:

    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

4. Copy the generated secret key.
5. Open your Django project's settings file (`settings.py`) in a text editor.
6. Find the line that defines the `SECRET_KEY` variable.
7. Replace the existing value of `SECRET_KEY` with the newly generated secret key.
8. Save the changes to `settings.py`.

## Usage

### Activate Virtual Environment:

### on Windows:
```bash
myenv\Scripts\activate
```
### on Unix or MacOS:
```bash
source myenv/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Set Up Database
```bash
python manage.py migrate
```
### Start Development Server
```bash
python manage.py runserver
```
Run this project on local server as it is not yet live. 
The project is dependent on port 8000, to run efficiently.

### Using Docker

Run Docker Conatainer
```bash
docker run -d -p 80:80 school-django-project
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

This project is not licensed and all rights are reserved. It is intended for educational purposes as part of a school project. Unauthorized use, distribution, or modification of this project is prohibited without explicit permission from the project owner.
