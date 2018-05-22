// Linear estimated value between two points
function smoothPoint(v1, v2, range, offset)
{
	var dV, os;

	dV = v1 - v2;
	os = offset / range;

	return v1 - (dV * os)
}

// Given a small array array use the smoothing function to fill in the spaces to create a bigger one
function expandData(dataA)
{
	var x = dataA.length - 1,
		y = dataA[0].length - 1,
		REQUIRED_WIDTH = 180,
		REQUIRED_HEIGHT = 120,
		modX = REQUIRED_WIDTH / x,
		modY = REQUIRED_HEIGHT / y,
		iX,
		iY,
		newData = [],
		osX,
		osY,
		tL,
		bL,
		bL,
		bR,
		tV,
		bV,
		v;

    extra_x = REQUIRED_WIDTH / x;
    extra_y = REQUIRED_HEIGHT / y;

    for (iX = 0; iX < REQUIRED_WIDTH; ++iX)
    {
    	newData[iX] = []
    	for (iY = 0; iY < REQUIRED_HEIGHT; ++iY)
	    {
	    	osX = iX % modX;
	    	osY = iY % modY;

	    	tlX = (iX / modX) << 0;
	    	tlY = (iY / modY) << 0;

	    	//console.log("Point: " + tlX + "/" + x + ", " + tlY + "/" + y + ". Coords: " + iX + ", " + iY + ". Mods: " + modX + ", " + modY);
	    	tL = dataA[tlX][tlY];
	    	if (tlX + 1 >= dataA.length) debugger;
	    	if (tlY >= dataA[tlX + 1].length) debugger;
	    	tR = dataA[tlX + 1][tlY];
	    	bL = dataA[tlX][tlY + 1];
	    	bR = dataA[tlX + 1][tlY + 1];

	    	tV = smoothPoint(tL, tR, modX, osX);
	    	bV = smoothPoint(bL, bR, modX, osX);

	    	v = smoothPoint(tV, bV, modY, osY);

	    	newData[iX][iY] = v << 0;
	    }
    }

    return newData;
}

function testContourData()
{
	var test = [
		[0, 0, 0],
		[0, 255, 0],
		[255, 0, 255]
	];

	return expandData(test);
}

function colourCanvas(dataArray)
{
	var REQUIRED_WIDTH = 180,
		REQUIRED_HEIGHT = 120,
		ctx = document.getElementById('contour_canvas').getContext('2d'),
		imgData = ctx.getImageData(0, 0, 180, 120),
		imgDataLen = imgData.data.length,
		shade,
		i,
		x,
		y;

	for(i = 0; i < imgDataLen / 4; i++){  //iterate over every pixel in the canvas
		x = i % REQUIRED_WIDTH;
		y = (i / REQUIRED_WIDTH) << 0;
		//if (i > 4000) debugger;
		shade = dataArray[x][y];


  		imgData.data[4 * i] = shade;    // RED (0-255)
  		imgData.data[4 * i + 1] = shade;    // GREEN (0-255)
  		imgData.data[4 * i + 2] = shade;    // BLUE (0-255)
  		imgData.data[4 * i + 3] = 255;  // APLHA (0-255)
	}

	ctx.putImageData(imgData, 0, 0);
}