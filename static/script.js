document.getElementById('chat-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const inputField = document.getElementById('user-input');
  const userText = inputField.value.trim();
  if (!userText) return;

  appendMessage('user', userText);
  inputField.value = '';

  appendMessage('bot', '⏳ Typing...');

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: userText })
    });

    const data = await response.json();
    removeLastBotMessage(); // remove "Typing..."
    appendMessage('bot', data.response || '⚠️ No response.');
  } catch (error) {
    removeLastBotMessage();
    appendMessage('bot', '⚠️ Sorry, the server is not responding.');
  }
});

function appendMessage(sender, text) {
  const msgDiv = document.createElement('div');
  msgDiv.classList.add('message', sender);
  msgDiv.textContent = text;
  document.getElementById('chat-box').appendChild(msgDiv);
  msgDiv.scrollIntoView({ behavior: 'smooth' });
}

function removeLastBotMessage() {
  const messages = document.querySelectorAll('.message.bot');
  if (messages.length > 0) {
    messages[messages.length - 1].remove();
  }
}
