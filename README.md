# E-Commerce Template using Django

![123GIF](https://github.com/user-attachments/assets/d077c3b1-fe28-49c8-967f-d67a4ebb32a3)

# Clone the repository
git clone https://github.com/yourusername/django-ecommerce.git
cd django-ecommerce

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Tailwind CSS
tailwindcss init
npm install

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the server
python manage.py runserver

