// https://www.html5rocks.com/en/tutorials/websockets/basics/
var console_textarea;

function loaded()
{
	var hostaddr = location.hostname,
		ws_addr,
	    connection;

	console_textarea = document.getElementById("console");
	consoleOut("Host: " + hostaddr);

	ws_addr = "ws://" + hostaddr + ":8807";
	consoleOut("Socket Address: " + ws_addr);

	connection = new WebSocket(host=ws_addr);

	// When the connection is open, send some data to the server
	connection.onopen = function () 
	{
		consoleOut("Connected.");
	    connection.send("{'msg':0,'data':{'msg':'Hello Ricket!'}}");
	};

	// Log errors
	connection.onerror = function (error)
	{
	    console.log('WebSocket Error ' + error);
	};

	// Log messages from the server
	connection.onmessage = function (e) 
	{
	    console.log('Server: ' + e.data);
	};
}

function consoleOut(message)
{
	console_textarea.value += "\n" + message;
}

