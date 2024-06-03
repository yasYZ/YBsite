
    document.addEventListener('DOMContentLoaded', function() {
        const carouselRow = document.querySelector('.carousel-row');
        const carouselCols = document.querySelectorAll('.carousel-col');
        let currentIndex = 0;

        function updateCarousel() {
            const totalCols = carouselCols.length;
            const halfCols = Math.floor(totalCols / 2);

            carouselCols.forEach((col, index) => {
                col.classList.remove('center');
                col.style.transform = '';
                col.style.opacity = '';
                col.style.zIndex = '';

                if (index === currentIndex) {
                    col.classList.add('center');
                    col.style.zIndex = 2;
                    col.style.opacity = 100;
                    col.style.transform = 'translateX(0)';
                } else {
                    const onset = (index - currentIndex + totalCols) % halfCols;
                    const offset = (index - currentIndex + totalCols) % totalCols;
                    const direction = offset > halfCols ? -1 : 1;
                    col.style.transform = `translateX(${direction * 250 * onset}px)`;
                    col.style.zIndex = 1;
                    col.style.opacity = 0.5;
                }
            });
        }

        function moveNext() {
            currentIndex = (currentIndex + 1) % carouselCols.length;
            updateCarousel();
        }

        updateCarousel(); // Initialize carousel

        // Automatic carousel movement
        setInterval(moveNext, 3000);
    });