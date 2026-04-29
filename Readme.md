<p align="center">
  <img src="https://img.shields.io/badge/Backend-Django%206.0-092E20?style=flat&logo=django&logoColor=white" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Serverless_DB-Neon-00E599?style=flat&logo=neon&logoColor=black" />
  <img src="https://img.shields.io/badge/Container-Docker-2496ED?style=flat&logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Hosting-Railway-131313?style=flat&logo=railway&logoColor=white" />
  <img src="https://img.shields.io/badge/API%20Docs-Swagger-85EA2D?style=flat&logo=swagger&logoColor=black" />
</p>

<h1 align="center">Blog API</h1>

<p align="center"><strong>🚀 A robust, production-ready REST API for modern blogging platforms 🚀</strong></p>


<div align="center">
  <h3>
    <a href="https://blog-api-production.up.railway.app/swagger/">
      🖥️ Live Demo
    </a>
     | 
    <a href="https://github.com/umitarat-dev/blog-api">
      📂 Repository
    </a>
  </h3>
</div>

<p align="center">
  <a href="https://blog-api-production.up.railway.app/swagger/">
    <img src="./assets/swagger.gif" alt="Interactive Swagger Documentation" width="700"/>
  </a>
</p>

## 📖 Overview
The **Blog API** is a comprehensive backend solution featuring user authentication, role-based access control, and a hierarchical data model for posts, comments, and likes. Designed with a cloud-native mindset, it leverages **Docker** for orchestration and **Railway/Neon** for seamless production delivery.

## 📚 Navigation
- [🚀 Live API Documentation](#-live-api-documentation)
- [📦 Key Features](#-key-features)
- [🛠️ Built With](#️-built-with)
- [⚙️ Setup & Installation](#️-setup--installation)
- [🧪 API Testing](#-api-testing)
- [📬 Contact Information](#-contact-information)


## 🚀 Live API Documentation
The API is fully documented and interactive. You can test all endpoints (Auth, Blog, Comments, Likes) directly through:
* **Swagger UI:** [https://blog-api-production.up.railway.app/swagger/](https://blog-api-production.up.railway.app/swagger/)
* **ReDoc:** [https://blog-api-production.up.railway.app/redoc/](https://blog-api-production.up.railway.app/redoc/)

## 📦 Key Features
* **Hierarchical Content:** Advanced nested routing for comments and interactions using `drf-nested-routers`.
* **Smart Analytics:** Automatic tracking of post view counts and real-time like/comment tallies.
* **Environment Orchestration:** Multi-tier settings (Dev/Prod) for secure and scalable deployment.
* [cite_start]**Production Hardened:** Integrated with **WhiteNoise** for efficient static file serving and **Gunicorn** as a production-grade WSGI server. 

## 🛠️ Built With
* [cite_start]**Core:** [Django 6.0](https://www.djangoproject.com/) & [Django REST Framework](https://www.django-rest-framework.org/) 
* [cite_start]**Auth:** [dj-rest-auth](https://dj-rest-auth.readthedocs.io/) with Token Authentication 
* **Infrastructure:** [Docker](https://www.docker.com/)
* [cite_start]**Database:** [Neon PostgreSQL](https://neon.tech/) 
* **Hosting:** [Railway](https://railway.app/)


## ⚙️ Setup & Installation

### Local Development
1. **Clone the repository:**
```bash
git clone [https://github.com/umitarat-dev/blog-api.git](https://github.com/umitarat-dev/blog-api.git)
cd blog-app-api
```


2. **Environment Setup:**
  - Create a virtual environment: python -m venv env   
  - Activate it: source env/bin/activate (Mac/Linux) or env\Scripts\activate (Win)
  - Install dependencies: pip install -r requirements.txt   

3. **Configuration:**
  - Create a .env file in the root directory:

```js
SECRET_KEY=your_secret_key
ENV_NAME=dev
DEBUG=True
```

4. **Database & Run:**

```Bash
python manage.py migrate
python manage.py runserver
```

## 🧪 API Testing
While Swagger is the preferred interactive method, a dedicated **Postman Collection** is also provided for automated integration testing and detailed request analysis.

### 📥 How to Use the Collection
1. **Download:** Navigate to the [postman/](./postman/blog-api-postman_collection.json) directory and download the JSON collection file.
2. **Import:** Open Postman, click the **Import** button, and drag-and-drop the downloaded file.
3. **Environment:** Set your `base_url` variable in Postman to:
   * **Local:** `http://127.0.0.1:8000`
   * **Production:** `https://blog-api-production.up.railway.app`
4. **Authenticate:** Use the `Login` request to get your token, and apply it to subsequent requests.

## 📬 Contact Information

I am always open to discussing new projects, creative ideas, or opportunities to be part of your visions.

* **LinkedIn:** [linkedin.com/in/umit-arat](https://www.linkedin.com/in/umit-arat/)
* **Email:** [umitarat8098@gmail.com](mailto:umitarat8098@gmail.com)
* **GitHub:** [github.com/umitarat-dev](https://github.com/umitarat-dev) (Current Workspace)
