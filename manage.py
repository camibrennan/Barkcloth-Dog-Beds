import utils
import sys

print('Usage:')
print('Rebuild site: python manage.py build')
print('Create new page: python manage.py new')

print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
    print("Build was specified")
    utils.main()
    print('Build complete!')
elif command == "new":
    print("New page was specified")
    utils.create_new_page()
    print('New Page added!')

else:
    print("Please specify 'build' or 'new'")


