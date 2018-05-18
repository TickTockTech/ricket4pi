function Robot()
{
	const STATE_INIT = 0,
		  STATE_PAUSE = 1,
		  STATE_REQUEST_SENSOR_DATA = 2,
		  STATE_IDLE = -2,
		  STATE_NONE = -1;

	var obj = {};

	function delayedStateChange(next_state, time)
	{
		obj.state = STATE_PAUSE;
		obj.next_state = next_state;
		obj.pause_time = time;
	}

	function state_init(dT)
	{
		delayedStateChange(STATE_REQUEST_SENSOR_DATA, 1000);
        consoleOut("Robot: Initialised.");
	}

	function state_pause(dT)
	{
		obj.pause_time -= dT;
		if (obj.pause_time <= 0)
		{
			obj.state = obj.next_state;
			obj.pause_time = 0;
		}
	}

	function state_request_sensor_data(dT)
	{
		obj.state = STATE_IDLE;

		connectionSend('{"msg":3}');
        consoleOut("Robot: Request sensor data.");
	}

	obj.update = function()
	{
		var now = (new Date).getTime(),
			dT = now - obj.last;

		switch (obj.state)
		{
		case STATE_INIT:
			state_init(dT);
			break;

		case STATE_PAUSE:
			state_pause(dT);
			break;

		case STATE_REQUEST_SENSOR_DATA:
			state_request_sensor_data(dT);
			break;
		}

		obj.last = now;
	}

	obj.state = STATE_INIT;
	obj.last = (new Date).getTime();
	obj.timer = setInterval(obj.update, 250);

    consoleOut("Robot: Created.");

	return obj;
}
