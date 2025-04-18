import logging
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from user_app.models import CustomUser
from user_app.email_back_end import email_back_end

# Initialize logger
logger = logging.getLogger(__name__)

User = get_user_model()

# Constant for pagination items per page
ITEMS_PER_PAGE = 2

def base(request):
    """
    Render the base template.
    """
    try:
        return render(request, 'base.html')
    except Exception as e:
        logger.error(f"Error rendering base template: {e}")
        return JsonResponse({'status': 'error', 'message': 'An error occurred while rendering the base template.'}, status=500)

def custom_login(request):
    """
    Render the login page.
    """
    try:
        return render(request, 'login.html')
    except Exception as e:
        logger.error(f"Error rendering login page: {e}")
        return JsonResponse({'status': 'error', 'message': 'An error occurred while rendering the login page.'}, status=500)

def do_login(request):
    """
    Authenticate user using email_back_end with email and password POSTed.
    On success, log the user in and redirect to manage_users.
    On failure, redirect back to login with error message.
    """
    if request.method == 'POST':
        try:
            user = email_back_end.authenticate(
                request,
                username=request.POST.get('email'),
                password=request.POST.get('password')
            )
            if user is not None:
                login(request, user)
                logger.info(f"User {user.username} logged in successfully.")
                messages.success(request, 'Login successful!')
                return redirect('manage_users')
            else:
                messages.error(request, 'Email or Password is not valid')
                return redirect('login')
        except Exception as e:
            logger.error(f"Error during login: {e}")
            messages.error(request, 'An error occurred during login.')
            return redirect('login')
    else:
        logger.warning("Invalid request method for login.")
        messages.error(request, 'Invalid request method.')
        return redirect('login')

def do_logout(request):
    """
    Log out the current user and redirect to the login page.
    """
    try:
        username = request.user.username
        logout(request)
        logger.info(f"User {username} logged out successfully.")
        return redirect('login')
    except Exception as e:
        logger.error(f"Error during logout: {e}")
        return JsonResponse({'status': 'error', 'message': 'An error occurred during logout.'}, status=500)

@login_required(login_url='/')
def manage_users(request):
    """
    Display the logged-in user's profile details with pagination.
    Filters users by the email of the currently logged-in user.
    """
    if request.method == 'GET':
        try:
            # Fetch user details filtered by the logged-in user's email, ordered by newest first
            users_detail = CustomUser.objects.filter(email=request.user.email).values().order_by('-date_joined')

            # Pagination: ITEMS_PER_PAGE users per page
            page = request.GET.get('page', 1)
            paginator = Paginator(users_detail, ITEMS_PER_PAGE)

            try:
                users_page = paginator.page(page)
            except Exception as e:
                logger.warning(f"Invalid page number: {e}")
                users_page = paginator.page(1)

            context = {
                'users_detail': users_page,
                'page_obj': users_page,  # Useful for Django's pagination template tags
            }
            response = render(request, 'user_profile.html', context)
            response.status_code = 200
            return response
        except Exception as e:
            logger.error(f"Error in manage_users view: {e}")
            return JsonResponse({'status': 'error', 'message': 'An error occurred while fetching user details.'}, status=500)
    else:
        logger.warning("Invalid request method for manage_users.")
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)

def edit_user_profile(request, id):
    """
    Handle POST request to update a user's profile fields.
    Returns JSON response indicating success or failure.
    """
    if request.method == "POST":
        try:
            user = CustomUser.objects.get(id=id)
            # Update fields only if new data is provided, else keep existing
            user.username = request.POST.get('username') or user.username
            user.email = request.POST.get('email') or user.email
            user.first_name = request.POST.get('first_name') or user.first_name
            user.last_name = request.POST.get('last_name') or user.last_name
            user.phone_number = request.POST.get('phone_number') or user.phone_number
            user.home_address = request.POST.get('home_address') or user.home_address
            user.location = request.POST.get('location') or user.location
            user.save()
            logger.info(f"User profile updated successfully for {user.username}.")
            messages.success(request, 'User profile updated successfully!')
            return JsonResponse({'status': 'success', 'message': 'User profile updated successfully!'}, status=200)
        except CustomUser.DoesNotExist:
            logger.error(f"User with id {id} does not exist.")
            return JsonResponse({'status': 'error', 'message': 'User not found!'}, status=404)
        except Exception as e:
            logger.error(f"Error updating user profile: {e}")
            return JsonResponse({'status': 'error', 'message': 'An error occurred while updating the user profile.'}, status=500)
    else:
        logger.warning("Invalid request method for edit_user_profile.")
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=400)
