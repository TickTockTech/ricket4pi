function sensor_data(data)
{
    var td_irL = document.getElementById("irL"),
        td_irR = document.getElementById("irR"),
        td_lineL = document.getElementById("lineL"),
        td_lineR = document.getElementById("lineR"),
        td_dist = document.getElementById("dist"),
        td_cmpCal = document.getElementById("compassCalibrated"),
        td_cmpHead = document.getElementById("compassHeading");

    td_irL.bgColor = data.irL ? "#00FF00" : "#FF0000";
    td_irR.bgColor = data.irR ? "#00FF00" : "#FF0000";
    td_lineL.bgColor = data.lineL ? "#00FF00" : "#FF0000";
    td_lineR.bgColor = data.lineR ? "#00FF00" : "#FF0000";
    td_dist.innerHTML = (data.dist << 0) + "&nbsp;cm";
    td_cmpCal.bgColor = data.cmpCal ? "#00FF00" : "#FF0000";
}

function click_data(data)
{
    var td_clicks = document.getElementById("clicks");

    td_clicks.innerHTML = data.clicks;
}

function handleMessage(msg, data)
{
    var expand;

    console.log("In: " + msg + ", Data: " + JSON.stringify(data));

    switch(msg)
    {
        case MSG_SENSOR_DATA:
            sensor_data(data);
            break;
        case MSG_CLICK_DATA:
            click_data(data);
            break;
        case MSG_SONAR_SCAN_DATA:
            expand = expandData(data.dist);
            rotated = rotateArray(expand);
//            colourCanvas( highlightNear(rotated) );
            colourCanvas( rotated );
            break;
        default:
            console.log("[WARNING] " + msg + " not handled.")
	}

    if (window.robot)
    {
        robot.incomingMessage(msg, data);
    }
}
