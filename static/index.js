const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");

function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.className = `message ${sender}`;

  if (sender === "bot") {
    msg.innerHTML = marked.parse(text);  // ✅ render Markdown
  } else {
    msg.innerText = text;
  }

  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage(customMessage = null) {
  const message = customMessage || userInput.value.trim();
  if (!message) return;

  addMessage(message, "user");
  userInput.value = "";

  // Loader message
  const loader = document.createElement("div");
  loader.className = "message bot loader";
  loader.innerText = "Typing...";
  chatBox.appendChild(loader);
  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    chatBox.removeChild(loader);
    addMessage(data.reply, "bot");

  } catch (err) {
    console.error("Fetch error:", err);
    chatBox.removeChild(loader);
    addMessage("⚠️ Failed to get response from the server.", "bot");
  }
}

userInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});
