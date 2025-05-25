# Rotaract Club of Ambattur - Official Website

## Project Overview

This repository contains the source code for the official website of the Rotaract Club of Ambattur. The website is designed to showcase the club's activities, projects, team members, and provide a platform for communication and engagement with members and the wider community.

**Authored by: Rtr. Prashanth E**

**Date: May 26, 2025**

---

## Key Features Implemented

The website currently includes the following functionalities and pages:

**1. Homepage:**
   - Engaging hero section with a call-to-action.
   - Introductory content about the club.
   - Snippets for "About Us" and "Featured Projects."
   - "LOGIN" button in the navigation bar for direct access to the Django Admin panel.

**2. Informational Pages:**
   - **About Us:** Detailed information about the club's mission, vision, and history.
   - **Our Team:**
     - Displays current club officials in a "playing card" style layout with profile pictures.
     - Clicking on a team card opens a modal popup with detailed information:
       - Name, Position, Bio, Photo
       - Member Joining Year, RI ID, Contact Number, Blood Group.
     - A separate list displaying the names of all club members.
     - Logic to determine and display officials for the current Rotaract year.
   - **Projects:**
     - Dynamic listing of club projects in a card layout.
     - Each project card links to a dedicated detail page.
     - **Project Detail Pages:**
       - Comprehensive information about each project (long description, focus area, status, beneficiary count).
       - Displays a featured image for the project.
       - Includes a gallery for multiple project images, presented as a horizontally scrolling carousel (using SwiperJS).
   - **Contact Us:**
     - Club contact details (email, meeting information placeholders).
     - Links to social media profiles with icons.
     - Functional contact form that captures user input (currently prints to console, email sending to be fully configured).

**3. Dynamic Content Management:**
   - **Projects and Team Members:** Content for these sections is managed dynamically via the Django Admin interface.
     - Includes image uploads for project galleries and team member profile pictures.
   - **Django Admin Customization:** Basic branding applied (site header, title, logo).

**4. User Interface & User Experience (UI/UX):**
   - **Responsive Design:** The website adapts to various screen sizes (desktop, tablet, mobile).
   - **Theme Toggle:**
     - Allows users to switch between Light and Dark mode.
     - User preference is saved in `localStorage` for persistence.
     - Toggle button includes a sun/moon icon transition.
   - **Navigation:**
     - Main navigation bar with links to all key sections.
     - Responsive "hamburger" menu for mobile devices.
   - **Visual Styling:**
     - Modern, clean aesthetic inspired by "Facebook" color schemes.
     - Consistent use of cards, buttons, and typography.
     - Font Awesome icons for social media and other UI elements.
   - **Interactive Elements:**
     - Modals for team member details.
     - Image carousel for project galleries.
     - CSS hover effects and transitions.

**5. Branding:**
   - Rotaract Club of Ambattur logo implemented as a favicon.

---

## Technologies Used

* **Backend:** Python, Django Framework
* **Frontend:** HTML5, CSS3 (with CSS Custom Properties/Variables, Flexbox, Grid), JavaScript (ES6+)
* **Database:** SQLite (default for development)
* **Key Libraries/Frameworks:**
    * SwiperJS (for image carousels)
    * Font Awesome (for icons)
* **Version Control:** Git, GitHub
* **Development Environment:** IntelliJ IDEA (as per user setup)

---

## Setup and Local Development (Basic)

To run this project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sunilprashanthh/rac-ambattur-website.git](https://github.com/sunilprashanthh/rac-ambattur-website.git)
    cd rac-ambattur-website
    ```
2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install Django Pillow
    ```
4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser** (for accessing the Django admin):
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
7.  Open your browser and go to `http://127.0.0.1:8000/`.
    * The admin panel is accessible at `http://127.0.0.1:8000/admin/`.

**Note on Media Files:** Ensure `MEDIA_ROOT` and `MEDIA_URL` are correctly configured in `settings.py` for image uploads to work. The project is set up to serve media files in development mode.

---

## Future Enhancements / To-Do

This project is an ongoing development. Potential future features include:
* Fully operational email sending for the contact form.
* Dynamic "Blog/News" section.
* Dynamic "Events" page.
* "Membership Information" page (possibly with an interest form).
* "Resources" section.
* Advanced SEO features.
* User registration and login for club members (Role-Based Access Control).
* Donation portal.

---
