// https://www.html5rocks.com/en/tutorials/websockets/basics/
var console_textarea,
    console_lines = 0,
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
        connectionSend('{"msg":' + MSG_NULL + ',"data":{"msg":"Hello Ricket!"}}');
    };

    // Log errors
    web_socket_conn.onerror = function (error)
    {
        console.log('WebSocket Error ' + error);
    };

    // Log messages from the server
    web_socket_conn.onmessage = function (msg)
    {
        consoleOut("Serer: <- " + msg.data);
        console.log('Server: <-' + msg.data);

        try
        {
            obj = JSON.parse(msg.data)
            handleMessage(obj.msg, obj.data);
        }
        catch(e)
        {
            console.error("Invalid message: " + e);
            console.error("Message: " + msg)
        }
    };

    window.robot = Robot();
}

function consoleOut(message)
{
    var console_text;
    console_lines++;
    if (console_lines > 90)
    {
        console_text = console_textarea.value;
        console_text = console_text.substring(console_text.indexOf("\n") + 1);
        console_textarea.value = console_text;
        console_lines--;
    }
    console_textarea.value += "\n" + message;
}

function connectionSend(message)
{
    consoleOut("-> " + message);
    web_socket_conn.send(message);
}
