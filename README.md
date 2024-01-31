# Mini Social Media CRUD App

## Overview

This is a simple mini social media app built using htmx, Flask, and Bootstrap. It allows users to share posts. The project is designed to be lightweight and easy to understand, making it a great starting point for those learning web development with these technologies.

## Features

- **Post Creation:** Users can create and share posts with text and images.
- **Interaction:** Users can like and comment on posts.
- **Responsive Design:** Bootstrap is used to ensure a mobile-friendly and responsive user interface.

## Technologies Used

- [htmx](https://htmx.org/): For seamless and fast interactions between the server and the client.
- [Flask](https://flask.palletsprojects.com/): A lightweight web application framework for Python.
- [Bootstrap](https://getbootstrap.com/): A front-end framework for designing responsive and mobile-first websites.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python
- Flask (`pip install Flask`)
- htmx

### Installation

1. Clone the repository:

```bash
git clone https://github.com/MrMDrX/mini-social-media-htmx-flask-app.git
cd mini-social-media-htmx-flask-app
```

2. Create and Activate a Virtual Environment (Optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
flask --app server run --port 3000
```

Visit [http://localhost:3000](http://localhost:3000) in your browser to see the app in action.

## Folder Structure

- **`templates/`**: Contains HTML templates.
- **`static/`**: Stores static assets like CSS and JavaScript.
- **`server.py`**: The main Flask application file.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the creators of htmx, Flask, and Bootstrap for providing excellent tools for web development.
