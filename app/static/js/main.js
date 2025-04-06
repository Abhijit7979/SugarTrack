// Main SugarTrack JavaScript

document.addEventListener("DOMContentLoaded", function () {
  // Initialize tooltips
  const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  if (tooltips.length > 0) {
    tooltips.forEach((tooltip) => {
      new bootstrap.Tooltip(tooltip);
    });
  }

  // Flash messages auto-close
  const alerts = document.querySelectorAll(".alert-dismissible");
  if (alerts.length > 0) {
    alerts.forEach((alert) => {
      setTimeout(() => {
        const bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
      }, 5000);
    });
  }

  // Sticky notifications
  setupNotifications();

  // Character counter for summary textarea
  const summaryTextarea = document.getElementById("summary");
  if (summaryTextarea) {
    const charCounter = document.createElement("div");
    charCounter.classList.add("form-text", "text-end");
    charCounter.innerHTML = "0/100 characters (minimum)";
    summaryTextarea.parentNode.appendChild(charCounter);

    summaryTextarea.addEventListener("input", function () {
      const currentLength = this.value.length;
      charCounter.innerHTML = `${currentLength}/100 characters (minimum)`;

      if (currentLength >= 100) {
        charCounter.classList.add("text-success");
        charCounter.classList.remove("text-danger");
      } else {
        charCounter.classList.add("text-danger");
        charCounter.classList.remove("text-success");
      }
    });
  }
});

// Notifications system
function setupNotifications() {
  // Mock notifications - in a real app these would come from the server
  const notificationMessages = [
    "You're on a 5-day streak! Keep it up!",
    "Don't forget to submit today's summary!",
    "You're just 15 coins away from the Hackathon Pass!",
  ];

  // Only setup notifications if we're on the dashboard
  const dashboardContainer = document.querySelector(".dashboard-container");
  if (!dashboardContainer) return;

  // Create notification toast container if it doesn't exist
  let toastContainer = document.querySelector(".toast-container");
  if (!toastContainer) {
    toastContainer = document.createElement("div");
    toastContainer.className =
      "toast-container position-fixed bottom-0 end-0 p-3";
    document.body.appendChild(toastContainer);
  }

  // Show a random notification every 30 seconds
  setInterval(() => {
    const randomIndex = Math.floor(Math.random() * notificationMessages.length);
    const message = notificationMessages[randomIndex];

    showNotification(message, toastContainer);
  }, 30000);

  // Show initial notification
  setTimeout(() => {
    showNotification("Welcome to SugarTrack! Ready to learn?", toastContainer);
  }, 3000);
}

function showNotification(message, container) {
  const toastId = "toast-" + Date.now();
  const toastHtml = `
        <div id="${toastId}" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="toast-header">
                <i class="bi bi-bell-fill me-2 text-primary"></i>
                <strong class="me-auto">SugarTrack</strong>
                <small>Just now</small>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
                ${message}
            </div>
        </div>
    `;

  container.insertAdjacentHTML("beforeend", toastHtml);
  const toastElement = document.getElementById(toastId);
  const toast = new bootstrap.Toast(toastElement, {
    autohide: true,
    delay: 8000,
  });
  toast.show();

  // Remove toast from DOM after it's hidden
  toastElement.addEventListener("hidden.bs.toast", function () {
    this.remove();
  });
}
