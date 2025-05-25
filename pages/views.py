from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, TeamMember
import datetime

def home_page_view(request):
    return render(request, 'pages/home.html')

def about_us_view(request):
    return render(request, 'pages/about_us.html')

def our_team_view(request):
    return render(request, 'pages/our_team.html')

def projects_view(request):
    # Fetch all Project objects from the database
    # Order them, e.g., by creation date (newest first) or by title
    all_projects = Project.objects.all().order_by('-created_at') # '-created_at' for newest first

    context = {
        'all_projects_list': all_projects, # Pass the list of projects to the template
    }
    return render(request, 'pages/projects.html', context)

def project_detail_view(request, project_slug):
    # Fetch the specific project by its slug. If not found, it will raise a 404 error.
    project = get_object_or_404(Project, slug=project_slug)

    context = {
        'project': project, # Pass the single project object to the template
    }
    return render(request, 'pages/project_detail.html', context)

def contact_us_view(request):
    form_submitted_successfully = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email'] # Email address of the person sending
            subject = form.cleaned_data['subject']
            message_body = form.cleaned_data['message']

            # Construct the full message
            full_message = f"Message from: {name} ({from_email})\n\n"
            full_message += f"Subject: {subject}\n\n"
            full_message += f"Message:\n{message_body}"

            # Print to console (as a backup or for logging)
            print(f"\n--- Contact Form Submission (Preparing to send email) ---")
            print(f"From: {name} <{from_email}>")
            print(f"Subject: {subject}")
            print(f"Message: {message_body}")
            print(f"--------------------------------------------------------\n")

            # Send the email
            try:
                send_mail(
                    f'Contact Form: {subject} - from {name}', # Email subject
                    full_message,                             # Email body
                    from_email,                               # Sender's email (from the form)
                    ['racambattur@gmail.com'], # LIST of recipient email addresses (replace with your club's actual email)
                    fail_silently=False, # If False, it will raise an error if sending fails
                )
                form_submitted_successfully = True
                form = ContactForm() # Show a new empty form
            except Exception as e:
                # Handle email sending errors if necessary (e.g., log them)
                print(f"Error sending email: {e}")
                # You might want to pass an error message to the template here
                # For now, we'll let the form submission appear successful to the user
                # but log the error. Or, set form_submitted_successfully = False
                # and add another flag for email_error.
                # For simplicity, if console backend is used, this error is less likely.
                pass # Continue as if successful for console backend, or handle error

        # If form is not valid, it will re-render with errors by default
        # No need for an else here if just re-rendering the form with errors

    else: # GET request
        form = ContactForm()

    context = {
        'form': form,
        'form_submitted_successfully': form_submitted_successfully,
    }
    return render(request, 'pages/contact_us.html', context)

def our_team_view(request):
    today = datetime.date.today()

    # Determine current Rotaract year (July 1st to June 30th)
    # If current month is July or later, current term started this year.
    # Otherwise, current term started last year.
    if today.month >= 7:
        current_rotaract_term_start_year = today.year
    else:
        current_rotaract_term_start_year = today.year - 1

    # For the page heading (e.g., "Club Officers 2024 - 25")
    heading_year_start = current_rotaract_term_start_year
    heading_year_end_short = str(heading_year_start + 1)[-2:]

    # Fetch current officials for the determined Rotaract year
    current_officials = TeamMember.objects.filter(
        official_term_start_year=current_rotaract_term_start_year
    ).order_by('display_order', 'name')

    # Fetch all team members for the list (you might want to filter out general members
    # if 'Position' is 'Member' and they aren't officials, or list everyone)
    # For simplicity, let's list everyone who has a name.
    all_club_members = TeamMember.objects.all().order_by('name')

    context = {
        'current_officials_list': current_officials,
        'all_club_members_list': all_club_members,
        'current_year_display': heading_year_start,
        'next_year_short_display': heading_year_end_short,
    }
    return render(request, 'pages/our_team.html', context)