#!/usr/bin/env python
""" A file automatically created in each Django project. """
import os
import sys
from django.core.management import  execute_from_command_line



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'doctor_project.settings')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
