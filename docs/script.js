// --- View Switcher Logic ---
function switchView(viewId) {
    // Hide all views
    const views = document.querySelectorAll('.view');
    views.forEach(view => {
        view.classList.remove('active');
    });

    // Show the target view
    const targetView = document.getElementById(viewId + '-view');
    if (targetView) {
        targetView.classList.add('active');
        // Scroll to top instantly
        window.scrollTo(0, 0);
        
        // Re-trigger scroll animations for the new view
        setTimeout(handleScrollAnimations, 100);
    }
}

// --- Scroll Reveal Animations ---
function handleScrollAnimations() {
    const scrollElements = document.querySelectorAll('.scroll-element');
    
    scrollElements.forEach(el => {
        const elementTop = el.getBoundingClientRect().top;
        const elementBottom = el.getBoundingClientRect().bottom;
        const isVisible = (elementTop < window.innerHeight - 50) && (elementBottom > 0);
        
        if (isVisible) {
            el.classList.add('visible');
        }
    });
}

// Initial check
document.addEventListener('DOMContentLoaded', () => {
    handleScrollAnimations();
});

// Check on scroll
window.addEventListener('scroll', () => {
    requestAnimationFrame(handleScrollAnimations);
});
