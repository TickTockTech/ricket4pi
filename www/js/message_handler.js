function sensor_data(data)
{
	var td_irL = document.getElementById("irL"),
	    td_irR = document.getElementById("irL"),
	    td_lineL = document.getElementById("irL"),
	    td_lineR = document.getElementById("irL"),
	    td_dist = document.getElementById("dist");

	debugger
}

function handleMessage(msg, data)
{
	console.log("In: " + msg + ", Data: " + JSON.stringify(data));

	switch(msg)
	{
		case MSG_SENSOR_DATA:
			sensor_data(data);
			break;
	}
}