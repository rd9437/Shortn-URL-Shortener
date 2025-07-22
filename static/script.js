// Floating link icons for index.html
const iconContainer = document.getElementById("floating-icons");

if (iconContainer) {
  for (let i = 0; i < 30; i++) {
    const icon = document.createElement("div");
    icon.className = "floating-icon";
    icon.innerText = "🔗";
    icon.style.left = `${Math.random() * 100}%`;
    icon.style.top = `${Math.random() * 100}%`;
    icon.style.fontSize = `${16 + Math.random() * 16}px`;
    icon.style.animationDuration = `${20 + Math.random() * 20}s`;
    icon.style.animationDelay = `${Math.random() * 10}s`;
    iconContainer.appendChild(icon);
  }
}

// Confetti celebration for shorten.html
function celebrate() {
  if (typeof confetti === "function") {
    confetti({
      particleCount: 150,
      spread: 70,
      origin: { y: 0.6 }
    });
  }
}
