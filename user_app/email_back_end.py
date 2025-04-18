import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# Initialize logger
logger = logging.getLogger(__name__)

class email_back_end(ModelBackend):
    """
    Custom authentication backend to authenticate users using their email and password.
    """
    def authenticate(self, username=None, password=None):
        """
        Authenticate a user based on email and password.
        """
        logger.info(f"Attempting to authenticate user with email: {username}")
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            logger.warning(f"User with email {username} does not exist.")
            return None
        else:
            if user.check_password(password):               
                return user
        return None
    
    