let ws = new WebSocket('ws://10.100.60.84:8000/ws/chat/1/'); 
 
ws.onopen = () => { 
    setTimeout(() => { 
 
    }, 2000); 
} 
 
ws.onmessage = (event) => { 
    console.log(event.data); 
    const messageData = JSON.parse(event.data); 
     
    const p = document.createElement('p'); 
    p.textContent = messageData.message; 
 
    const messagesContainer = document.getElementById('messages'); 
    messagesContainer.appendChild(p); 
    messagesContainer.scrollTop = messagesContainer.scrollHeight;  
} 
 
const inp = document.querySelector('#inp'); 
const btn = document.querySelector('#btn'); 
 
btn.onclick = (e) => { 
    if (inp.value) { 
        const data = { 
            'message': inp.value 
        } 
 
        ws.send(JSON.stringify(data)); 
        inp.value = '';  
    } 
}