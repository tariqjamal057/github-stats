function toggleMobileMenu() {
    const mobileMenu = document.getElementById('mobile-menu');
    const menuItems = mobileMenu.querySelectorAll('li', 'a');

    if (mobileMenu.classList.contains('h-0')) {
        mobileMenu.classList.remove('h-0', 'opacity-0');
        mobileMenu.classList.add('h-auto', 'opacity-100', 'py-4');
    } else {
        mobileMenu.classList.add('h-0', 'opacity-0');
        mobileMenu.classList.remove('h-auto', 'opacity-100', 'py-4');
    }
}