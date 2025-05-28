document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('form');
  const timeInput = document.getElementById('time');
  const nameInput = document.getElementById('name');
  const textInput = document.getElementById('message');
  const messagesList = document.getElementById('messages');

  form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const time = timeInput.value.trim();
    const name = nameInput.value.trim();
    const message = textInput.value.trim();

    if (time && name && message) {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/add_messages', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ name, message })
        });

        if (!response.ok) {
          throw new Error('Ошибка при отправке');
        }

        const message = await response.json();
        console.log(message)
        const li = document.createElement('li');
        li.className = 'list-group-item';
        li.textContent = `${message.name}: ${message.message}`;
        messagesList.prepend(li);

        nameInput.value = '';
        textInput.value = '';
      } catch (error) {
        alert('Не удалось отправить сообщение');
        console.error(error);
      }
    }
  });

  // (опционально) Подгружаем все старые сообщения при загрузке
  async function loadMessages() {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/messages');
      const messages = await response.json();

      messagesList.innerHTML = ''; // очистим
      messages.reverse().forEach((msg) => {
        const li = document.createElement('li');
        li.className = 'list-group-item';
        li.textContent = `${msg.name}: ${msg.message}`;
        messagesList.appendChild(li);
      });
    } catch (error) {
      console.error('Ошибка загрузки сообщений', error);
    }
  }

  loadMessages();
});
