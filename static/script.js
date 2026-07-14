const chat = document.getElementById('chat');
  const input = document.getElementById('msg-input');
  const sendBtn = document.getElementById('send-btn');
  const suggestions = document.getElementById('suggestions');

  function autoGrow(el){
    el.style.height = 'auto';
    el.style.height = Math.min(el.scrollHeight, 120) + 'px';
  }

  function handleKeydown(e){
    if(e.key === 'Enter' && !e.shiftKey){
      e.preventDefault();
      sendMessage();
    }
  }

  function useSuggestion(el){
    input.value = el.textContent;
    input.focus();
  }

  function timeNow(){
    return new Date().toLocaleTimeString([], {hour:'numeric', minute:'2-digit'});
  }

  function scrollToBottom(){
    chat.scrollTop = chat.scrollHeight;
  }

  function appendUserMessage(text){
    const row = document.createElement('div');
    row.className = 'row user';
    row.innerHTML = `
      <div class="avatar">Y</div>
      <div class="bubble-wrap">
        <div class="bubble"><p></p></div>
        <span class="timestamp">${timeNow()}</span>
      </div>`;
    row.querySelector('p').textContent = text;
    chat.appendChild(row);
    scrollToBottom();
  }

  function appendTypingIndicator(){
    const row = document.createElement('div');
    row.className = 'row bot';
    row.id = 'typing-row';
    row.innerHTML = `
      <div class="avatar">M</div>
      <div class="bubble-wrap">
        <div class="bubble typing"><span></span><span></span><span></span></div>
      </div>`;
    chat.appendChild(row);
    scrollToBottom();
  }

  function removeTypingIndicator(){
    const row = document.getElementById('typing-row');
    if(row) row.remove();
  }

  function appendBotMessage(text, sources){
    const row = document.createElement('div');
    row.className = 'row bot';
    let sourcesHtml = '';
    if(sources && sources.length){
      sourcesHtml = `<div class="sources">${
        sources.map((s,i) => `<div class="source-chip"><span class="idx">${i+1}</span> ${s}</div>`).join('')
      }</div>`;
    }
    row.innerHTML = `
      <div class="avatar">M</div>
      <div class="bubble-wrap">
        <div class="bubble"><p></p></div>
        ${sourcesHtml}
        <span class="timestamp">${timeNow()}</span>
      </div>`;
    row.querySelector('p').textContent = text;
    chat.appendChild(row);
    scrollToBottom();
  }

  async function sendMessage(){
    const text = input.value.trim();
    if(!text) return;

    if(suggestions) suggestions.remove();

    appendUserMessage(text);
    input.value = '';
    input.style.height = 'auto';
    sendBtn.disabled = true;
    appendTypingIndicator();

    try{
      // Matches the common Flask RAG-chatbot pattern: POST to /get with form field "msg"
      const res = await fetch('/get', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ msg: text })
      });

      const raw = await res.text();
      removeTypingIndicator();

      // Backend may return plain text OR JSON like {"answer": "...", "sources": ["Gale Encyclopedia — p. 12", ...]}
      let answer = raw;
      let sources = null;
      try{
        const parsed = JSON.parse(raw);
        if(parsed && typeof parsed === 'object'){
          answer = parsed.answer ?? raw;
          sources = parsed.sources ?? null;
        }
      }catch(_e){ /* plain text response, use as-is */ }

      appendBotMessage(answer, sources);
    }catch(err){
      removeTypingIndicator();
      appendBotMessage("I couldn't reach the server. Please check your connection and try again.");
      console.error(err);
    }finally{
      sendBtn.disabled = false;
      input.focus();
    }
  }