from django.db.utils import IntegrityError
from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from django.utils.crypto import get_random_string
import getpass


class Command(createsuperuser.Command):
    help = 'Create a superuser with additional fields'
    def handle(self, *args, **options):
        email = input("Email: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        employee_code = input("Employee Code: ")

        # Validate the provided fields
        if not email:
            raise CommandError('Email is required')
        if not first_name:
            raise CommandError('First Name is required')
        if not last_name:
            raise CommandError('Last Name is required')
        if not employee_code:
            raise CommandError('Employee Code is required')

        password = None
        while not password:
            password = getpass.getpass("Password: ")
            password_confirmation = getpass.getpass("Password (again): ")
            if password != password_confirmation:
                self.stderr.write(self.style.ERROR("Passwords do not match. Please try again."))
                password = None

        try:
            user_data = {
                'email': email,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
                'employee_code': employee_code,
            }
            self.UserModel._default_manager.db_manager().create_superuser(**user_data)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        except IntegrityError as e:
            raise CommandError('Superuser creation failed: {}'.format(str(e)))
