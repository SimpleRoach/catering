document.addEventListener("DOMContentLoaded", function() {
    const categories = document.querySelectorAll('.category');

    categories.forEach(category => {
        category.style.opacity = 0;
        category.style.transition = "opacity 1s";
    });

    window.addEventListener('scroll', () => {
        categories.forEach(category => {
            const rect = category.getBoundingClientRect();
            if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
                category.style.opacity = 1;
            }
        });
    });
});
