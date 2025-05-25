// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed. Initializing scripts...");

    // --- Section 1: Project Details Toggle Logic (if still used anywhere) ---
    const detailToggleButtons = document.querySelectorAll('.toggle-details-btn');
    if (detailToggleButtons.length > 0) {
        console.log(detailToggleButtons.length + " project detail toggle button(s) found.");
        detailToggleButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                const projectCard = this.closest('.project-card'); // Assumes button is inside a .project-card
                if (projectCard) {
                    const detailsDiv = projectCard.querySelector('.project-details');
                    if (detailsDiv) {
                        if (detailsDiv.style.display === 'none' || detailsDiv.style.display === '') {
                            detailsDiv.style.display = 'block';
                            this.textContent = 'Hide Details';
                        } else {
                            detailsDiv.style.display = 'none';
                            this.textContent = 'Show Details';
                        }
                    } else {
                        console.warn("'.project-details' div not found within the project card of the clicked button.");
                    }
                } else {
                    console.warn("'.project-card' parent not found for the clicked button.");
                }
            });
        });
    } else {
        console.log("No project detail toggle buttons found (this is okay if you replaced them with links).");
    }

    // --- Section 2: Hamburger Menu Logic ---
    const hamburgerButton = document.getElementById('hamburger-icon');
    const navMenu = document.getElementById('nav-menu');

    if (hamburgerButton && navMenu) {
        console.log("Hamburger menu elements found. Adding listener.");
        hamburgerButton.addEventListener('click', function() {
            navMenu.classList.toggle('nav-active');
            hamburgerButton.classList.toggle('active'); // For "X" animation

            // Accessibility: Update aria-expanded attribute
            const isExpanded = navMenu.classList.contains('nav-active');
            hamburgerButton.setAttribute('aria-expanded', isExpanded);
            console.log("Hamburger clicked. Nav active: " + isExpanded);
        });
    } else {
        console.warn("Hamburger button or nav menu element not found. Hamburger functionality will not work.");
        if (!hamburgerButton) console.log("Reason: #hamburger-icon not found.");
        if (!navMenu) console.log("Reason: #nav-menu not found.");
    }

    // --- Section 3: Team Member Modal Logic ---
    const teamModal = document.getElementById('team-member-modal');
    const closeModalBtn = document.getElementById('modal-close-btn');
    const teamCardsTriggers = document.querySelectorAll('.team-member-card.modal-trigger');

    const modalPhoto = document.getElementById('modal-photo');
    const modalName = document.getElementById('modal-name');
    const modalPosition = document.getElementById('modal-position');
    const modalBio = document.getElementById('modal-bio');
    const modalJoiningYear = document.getElementById('modal-joining-year');
    const modalRiId = document.getElementById('modal-ri-id');
    const modalContactNumber = document.getElementById('modal-contact-number');
    const modalBloodGroup = document.getElementById('modal-blood-group');

    function openModalWithData(card) {
        if (!teamModal || !card) {
            console.error("Modal or card element missing for openModalWithData.");
            return;
        }

        if (modalPhoto) modalPhoto.src = card.dataset.photoUrl || '#';
        if (modalPhoto) modalPhoto.alt = card.dataset.name ? `${card.dataset.name}'s photo` : 'Profile photo';

        if (modalName) modalName.textContent = card.dataset.name || 'N/A';
        if (modalPosition) modalPosition.textContent = card.dataset.position || 'N/A';

        if (modalBio) modalBio.innerHTML = card.dataset.bio || 'No bio available.';

        if (modalJoiningYear) modalJoiningYear.textContent = card.dataset.joiningYear || 'N/A';
        if (modalRiId) modalRiId.textContent = card.dataset.riId || 'N/A';
        if (modalContactNumber) modalContactNumber.textContent = card.dataset.contactNumber || 'N/A';
        if (modalBloodGroup) modalBloodGroup.textContent = card.dataset.bloodGroup || 'N/A';

        teamModal.style.display = 'flex';
        teamModal.classList.add('modal-open');
        document.body.style.overflow = 'hidden';
        console.log("Team member modal opened for: " + card.dataset.name);
    }

    function closeModal() {
        if (!teamModal) {
            console.error("Modal element missing for closeModal.");
            return;
        }
        teamModal.style.display = 'none';
        teamModal.classList.remove('modal-open');
        document.body.style.overflow = 'auto';
        console.log("Team member modal closed.");
    }

    if (teamCardsTriggers.length > 0 && teamModal) {
        console.log(teamCardsTriggers.length + " team card modal trigger(s) found. Adding listeners.");
        teamCardsTriggers.forEach(function(card) {
            card.addEventListener('click', function() {
                openModalWithData(this);
            });
            card.addEventListener('keydown', function(event) {
                if (event.key === 'Enter' || event.key === ' ') {
                    event.preventDefault();
                    openModalWithData(this);
                }
            });
        });
    } else {
        console.warn("No team card modal triggers or modal element not found. Modal functionality might not work.");
        if (teamCardsTriggers.length === 0) console.log("Reason: No elements with '.team-member-card.modal-trigger' found.");
        if (!teamModal) console.log("Reason: #team-member-modal not found.");
    }

    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', closeModal);
    } else if (teamModal) {
        console.warn("Modal close button (#modal-close-btn) not found.");
    }

    if (teamModal) {
        teamModal.addEventListener('click', function(event) {
            if (event.target === teamModal) {
                closeModal();
            }
        });
    }

    // --- Section 4: Theme Toggle (Light/Dark Mode) ---
    const themeToggleButton = document.getElementById('theme-toggle-btn');
    const bodyElement = document.body;
    const themeToggleIcon = themeToggleButton ? themeToggleButton.querySelector('i') : null;
    const M_THEME_KEY = 'rotaract_ambattur_theme'; // Unique key for localStorage

    function applyTheme(theme) {
        if (theme === 'dark') {
            bodyElement.classList.add('dark-mode');
            if (themeToggleIcon) {
                themeToggleIcon.classList.remove('fa-sun');
                themeToggleIcon.classList.add('fa-moon');
            }
            localStorage.setItem(M_THEME_KEY, 'dark');
            if (themeToggleButton) themeToggleButton.setAttribute('aria-label', 'Switch to light theme');
            console.log("Theme applied: Dark");
        } else { // Default to light
            bodyElement.classList.remove('dark-mode');
            if (themeToggleIcon) {
                themeToggleIcon.classList.remove('fa-moon');
                themeToggleIcon.classList.add('fa-sun');
            }
            localStorage.setItem(M_THEME_KEY, 'light');
            if (themeToggleButton) themeToggleButton.setAttribute('aria-label', 'Switch to dark theme');
            console.log("Theme applied: Light");
        }
    }

    if (themeToggleButton && themeToggleIcon) {
        console.log("Theme toggle button and icon found. Adding listener and setting initial theme.");
        themeToggleButton.addEventListener('click', function() {
            if (bodyElement.classList.contains('dark-mode')) {
                applyTheme('light');
            } else {
                applyTheme('dark');
            }
        });

        // Set initial theme
        const savedTheme = localStorage.getItem(M_THEME_KEY);
        const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

        if (savedTheme) {
            applyTheme(savedTheme);
        } else if (systemPrefersDark) {
            applyTheme('dark');
        } else {
            applyTheme('light'); // Default
        }
    } else {
        console.warn("Theme toggle button or its icon not found. Theme toggle functionality will not work.");
        if (!themeToggleButton) console.log("Reason: #theme-toggle-btn not found.");
        if (themeToggleButton && !themeToggleIcon) console.log("Reason: Icon (<i> tag) inside #theme-toggle-btn not found.");
    }

    // Close modal with Escape key - This should be a general listener
    window.addEventListener('keydown', function(event) {
        const isTeamModalOpen = teamModal && (teamModal.classList.contains('modal-open') || teamModal.style.display === 'flex');
        if (event.key === 'Escape') {
            if (isTeamModalOpen) {
                closeModal(); // Specifically close the team modal
            }
            // If you have other modals in the future, you might need more specific logic here
            // or ensure each modal handles its own Escape key closure.
        }
    });

});