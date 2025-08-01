// Simple UX: disable button and show status on submit
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('prompt-form');
  const button = document.getElementById('submit-button');
  const status = document.getElementById('status');

  form.addEventListener('submit', () => {
    button.disabled = true;
    status.textContent = "Generating image, please wait...";
  });
});

    
  