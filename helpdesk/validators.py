# validators.py
#
# validators for file uploads, etc.

from django.conf import settings

# TODO: can we use the builtin Django validator instead?
# see: https://docs.djangoproject.com/en/4.0/ref/validators/#fileextensionvalidator
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    # TODO: we might improve this with more thorough checks of file types
    # rather than just the extensions.

    # check if VALID_EXTENSIONS is defined in settings.py
    # if not use defaults

    if settings.VALID_EXTENSIONS:
        valid_extensions = settings.VALID_EXTENSIONS
    else:
        valid_extensions = [".txt", ".pdf", ".doc", ".docx", ".odt", ".jpg", ".png"]

    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")
