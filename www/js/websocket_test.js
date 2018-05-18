// https://www.html5rocks.com/en/tutorials/websockets/basics/
var console_textarea,
    web_socket_conn;

function loaded()
{
    var hostaddr = location.hostname,
        ws_addr;

    console_textarea = document.getElementById("console");
    consoleOut("Host: " + hostaddr);

    ws_addr = "ws://" + hostaddr + ":8807";
    consoleOut("Socket Address: " + ws_addr);

    web_socket_conn = new WebSocket(host=ws_addr);

    // When the connection is open, send some data to the server
    web_socket_conn.onopen = function ()
    {
        consoleOut("Connected.");
        connectionSend("{'msg':0,'data':{'msg':'Hello Ricket!'}}");
    };

    // Log errors
    web_socket_conn.onerror = function (error)
    {
        console.log('WebSocket Error ' + error);
    };

    // Log messages from the server
    web_socket_conn.onmessage = function (e) 
    {
        console.log('Server: ' + e.data);
    };
}

function consoleOut(message)
{
    console_textarea.value += "\n" + message;
}

function connectionSend(message)
{
//    var leng = new Uint8Array(2);
//    leng[1] = 0;
//    leng[0] = message.length;
//    web_socket_conn.send(leng.buffer)
    web_socket_conn.send(message);
}
