# NaviGoCarNaviGoCar

NaviGoCar is a Django-based web application for a car rental service, featuring a modern, responsive interface built with Bootstrap 4. The platform allows users to browse available cars, explore pricing, read blog posts, and submit inquiries via a contact form. Data for cars and blogs is hardcoded, with contact form submissions stored in a database.

Features





Responsive design with Bootstrap 4



Pages for Home, About, Services, Pricing, Cars, Blog, and Contact



Car listings and detailed car views



Blog section with post listings and individual post pages



Functional contact form with database integration



Google Maps integration on the contact page (requires API key)



Django admin interface for managing contact submissions

Installation

Prerequisites





Python 3.8+



Django 3.2+



Git



Google Maps API key (optional)

Setup





Clone the repository:

git clone https://github.com/<your-username>/navigocar.git
cd navigocar



Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install dependencies:

pip install django



Apply database migrations:

python manage.py makemigrations
python manage.py migrate



Collect static files:

python manage.py collectstatic



Create a superuser for admin access:

python manage.py createsuperuser



(Optional) Configure Google Maps API key in rental/templates/rental/contact.html:

<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&sensor=false"></script>



Run the development server:

python manage.py runserver

Access at http://127.0.0.1:8000/.

Usage





Home: / - Service overview



Cars: /cars/ and /car/<id>/ - Browse and view car details



Blog: /blog/ and /blog/<id>/ - Read blog posts



Contact: /contact/ - Submit inquiries



Admin: /admin/ - Manage contact submissions

Contributing

Contributions are welcome! To contribute:





Fork the repository.



Create a feature branch (git checkout -b feature/your-feature).



Commit changes (git commit -m "Add your feature").



Push to the branch (git push origin feature/your-feature).



Open a pull request.

Please follow PEP 8 guidelines and include relevant tests.

License

This project is licensed under the MIT License. The template is based on Colorlib's Carbook, licensed under CC BY 3.0, and requires the footer attribution to remain intact.

Contact

For inquiries, please open an issue on GitHub.