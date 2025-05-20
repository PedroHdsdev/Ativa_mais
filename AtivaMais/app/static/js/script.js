document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.querySelector(".btn_menu");
    const sidebar = document.getElementById("sidebar");
    const menuItems = document.querySelectorAll(".menu-item");

    menuButton.addEventListener("click", function () {
        sidebar.classList.toggle("hidden");
        sidebar.classList.toggle("visible");
    });
});
