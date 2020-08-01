from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
	help = 'Create new user'

	def add_arguments(self, parser):
		parser.add_argument('-u', '--username', required=True, help='Login name')
		parser.add_argument('-e', '--email', required=True, help='Email')
		parser.add_argument('-f', '--first_name', required=True, help='First name')
		parser.add_argument('-l', '--last_name', required=True, help='Last name')
		parser.add_argument('-p', '--password', default=None, help='Password, default is no password')
		parser.add_argument('-t', '--token', action='store_true', help='Generate and print auth token for new user')

	def handle(self, *args, **options):
		user = User.objects.create_user(
			username=options['username'],
			email=options['email'],
			first_name=options['first_name'],
			last_name=options['last_name'],
			password=options['password'],
		)
		print('User {} is created'.format(user.username))
		if options['token']:
			token = Token.objects.create(user=user)
			print(token)
