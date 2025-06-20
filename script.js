const chatWindow = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

function appendMessage(text, sender) {
  const message = document.createElement('div');
  message.className = `message ${sender}`;
  message.textContent = text;
  chatWindow.appendChild(message);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

sendBtn.addEventListener('click', () => {
  const text = userInput.value.trim();
  if (text) {
    appendMessage(text, 'user');
    userInput.value = '';
    simulateBotResponse(text);
});

userInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendBtn.click();
});

function simulateBotResponse(input) {
  // This will later be replaced with Copilot integration
  setTimeout(() => {
    appendMessage("🤖 I'm just a placeholder... but I’ll be Copilot soon!", 'bot');
  }, 800);
}

