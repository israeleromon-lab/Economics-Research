// --- Scroll Reveal Animations ---
function handleScrollAnimations() {
    const scrollElements = document.querySelectorAll('.scroll-element');
    
    scrollElements.forEach(el => {
        const elementTop = el.getBoundingClientRect().top;
        const elementBottom = el.getBoundingClientRect().bottom;
        // Triggers slightly earlier to make it feel smoother
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

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            // Account for fixed navbar
            const headerOffset = 100;
            const elementPosition = targetElement.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.scrollY - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: "smooth"
            });
        }
    });
});
