// https://www.html5rocks.com/en/tutorials/websockets/basics/

var connection = new WebSocket('ws://127.0.0.1:8807');

// When the connection is open, send some data to the server
connection.onopen = function () {
  connection.send('Hello Ricket!'); // Send the message 'Ping' to the server
};

// Log errors
connection.onerror = function (error) {
  console.log('WebSocket Error ' + error);
};

// Log messages from the server
connection.onmessage = function (e) {
  console.log('Server: ' + e.data);
};

