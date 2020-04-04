# Task-Manager

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1ac554483fac462797ffa5a8b9adf2fa?style=flat-square)](https://app.codacy.com/app/kushthedude/Task-Manager?utm_source=github.com&utm_medium=referral&utm_content=kushthedude/Task-Manager&utm_campaign=Badge_Grade_Dashboard)
[![Dependabot Status](https://api.dependabot.com/badges/status?host=github&repo=kushthedude/Task-Manager)](https://dependabot.com)

- A Multi-Project Task Manager created in flask, for an internship assignment.
- Code is well commented and all the css has been acquired from bootstrap.
- Easy to use and well to play around.
- A quick project and yeah its not well decorated .


## Installation
- I personally prefer using virtual env , You may use the global installaitiong to by adding `SUDO` before pip and `-H` after pip .
```py
    mkdir Project-Manager
    cd Project-Manager
    git clone https://github.com/kushthedude/Multiproject-Task-Manager.git
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py
```

- TADA , Your app is ready to be deployed , open `localhost:5000` or `127.0.0.1:5000` on your favourite browser except IE (You know speed matters) to play with this little app.
- You can also use `Gunicorn` to play around with the app just use `gunicorn wsgi:app`.


## Contributors
Made with :heart: by [Kush](github.com/kushthedude)


