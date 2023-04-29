// Get the logo element
const logo = document.getElementById('logo');

// Add a scroll event listener to the window
window.addEventListener('scroll', () => {
  // If the user has scrolled more than 80 pixels, add the "scrolled" class to the logo element
  if (window.scrollY > 80) {
    logo.classList.add('scrolled');
  } else {
    // Otherwise, remove the "scrolled" class from the logo element
    logo.classList.remove('scrolled');
  }
});
