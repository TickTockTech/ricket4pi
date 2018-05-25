/** Colour the first 10 cm in shades of red
 */
var _colourReturn = {};  // Save creating a new object every time function called
function distanceColouring(val)
{
    var r = 0,
        g = 0,
        b = 0;

    if (val <= 10)
    {
        r = 255 - (val * 25.4);
    }
    if (val >= 5 && val <= 50)
    {
        g = 255 - ((val - 10) * 5.08);
    }
    if (val >= 25 && val <= 50)
    {
        b = 255 - (val - 50);
    }


    if (r > 255) r = 255
    if (g > 255) g = 255
    if (b > 255) b = 255

    if (r < 0) r = 0
    if (g < 0) g = 0
    if (b < 0) b = 0

    _colourReturn.r = r << 0;
    _colourReturn.g = g << 0;
    _colourReturn.b = b << 0;

    return _colourReturn;
}

// Linear estimated value between two points
function smoothPoint(v1, v2, range, offset)
{
    var dV, os;

    if (v1 > 255)
    {
        v1 = 255;
    }
    else if (v1 < 0)
    {
        v1 = 0;
    }

    if (v2 > 255)
    {
        v2 = 255;
    }
    else if (v2 < 0)
    {
        v2 = 0;
    }

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
        y,
        col;

    for(i = 0; i < imgDataLen / 4; i++){  //iterate over every pixel in the canvas
        x = i % REQUIRED_WIDTH;
        y = (i / REQUIRED_WIDTH) << 0;
        //if (i > 4000) debugger;
//        shade = 255 - dataArray[x][y];
        dist = dataArray[x][y];

        col = distanceColouring(dist);

        imgData.data[4 * i] = col.r;    // RED (0-255)
        imgData.data[4 * i + 1] = col.g;    // GREEN (0-255)
        imgData.data[4 * i + 2] = col.b;    // BLUE (0-255)
        imgData.data[4 * i + 3] = 255;  // APLHA (0-255)
    }

    ctx.putImageData(imgData, 0, 0);
}
