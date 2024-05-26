function openModal(imageSrc) {
    var modal = document.getElementById('myModal');
    var modalImage = document.getElementById('modalImage');

    modal.style.display = 'block';
    modalImage.src = imageSrc;
}

function closeModal() {
    var modal = document.getElementById('myModal');
    modal.style.display = 'none';
}

window.onclick = function(event) {
    var modal = document.getElementById('myModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
function toggleMenu() {
    var menuUl = document.querySelector(".nav ul");
    menuUl.classList.toggle("show");
    var close = document.querySelector('.close-btn');
    close.style.display = 'block';
}

document.querySelector(".menu-btn").addEventListener("click", function () {
    // Toggle the mobile menu
    toggleMenu();
});

document.querySelectorAll(".nav ul li a").forEach(function (menuItem) {
    menuItem.addEventListener("click", function () {
        // Hide the mobile menu
        toggleMenu();
    });
});
function CloseNav() {
    var menuUl = document.querySelector(".nav .show");
    var closeBTN = document.querySelector(".close-btn");
    menuUl.classList.remove("show");
    closeBTN.style.display = "none";
}

document.querySelector(".close-btn").addEventListener("click", function () {
    // Toggle the mobile menu
    CloseNav();
});

document.querySelectorAll(".nav .close-btn").forEach(function (menuItem) {
    menuItem.addEventListener("click", function () {
        // Hide the mobile menu
        CloseNav();
    });
});
document.addEventListener("DOMContentLoaded", function () {
    var scrollBtn = document.getElementById("scrollBtn");

    window.addEventListener("scroll", function () {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            scrollBtn.classList.add("show");
        } else {
            scrollBtn.classList.remove("show");
        }
    });

    scrollBtn.addEventListener("click", function () {
        scrollToTop(1000); // Scroll to top with animation in 1000 milliseconds (1 second)
    });

    function scrollToTop(duration) {
        var start = document.documentElement.scrollTop || document.body.scrollTop;
        var startTime = Date.now();

        function scroll() {
            var currentTime = Date.now();
            var timeElapsed = currentTime - startTime;
            document.documentElement.scrollTop = document.body.scrollTop = easeInOutQuad(timeElapsed, start, -start, duration);

            if (timeElapsed < duration) {
                requestAnimationFrame(scroll);
            } else {
                document.documentElement.scrollTop = document.body.scrollTop = 0;
            }
        }

        function easeInOutQuad(t, b, c, d) {
            t /= d / 2;
            if (t < 1) return c / 2 * t * t + b;
            t--;
            return -c / 2 * (t * (t - 2) - 1) + b;
        }

        requestAnimationFrame(scroll);
    }
});
var alert = document.getElementById('alert');
var myButton = document.getElementById('close-alert');

function addNewClass() {
    alert.classList.add('alert-close');
}

myButton.addEventListener('click', addNewClass);
