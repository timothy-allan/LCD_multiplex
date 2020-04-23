// Arduino, LCD, customChars, multiplex

// We are concerned with drawing images using Processing (not yet to Arduino)

// CONSTRAINT - -  only eight custom characters are available in memory of LCD displays
// CONSTRAINT - -  each character consists of a 5x8 grid of pixels.

// DRAW IMAGE using LCD customChars as pixels. 8 devices wide by 12 devices high

// We have defined a set of eight custom characters to act as 'halftone' pixels


// We will:
// Load an image (or a sequence of images)

// Get each pixel's greyscale value (0 - 255)

// Create array to hold eight custom characters of 5 * 8 pixels

// We only have 8 customChars, so - customChar = map(greyscaleValue, 0, 255, 0, 8)

// Draw image using customChars








int numFrames = 1;  // The number of frames in the animation
int currentFrame = 0;
PImage[] images = new PImage[numFrames];

color pixelColor;

int greyVal;
int randNum;

int greyMapped;
int brightnessMapped;





int numLCDsWide = 4;
int numLCDsHigh = 8;

int LCD_numCharsWide = 20;
int LCD_numCharsHigh = 4;

int LCD_numPixelsWide = 5;
int LCD_numPixelsHigh = 8;

int LCD_pixelSize = 8;
int LCD_pixelGap = 2;
int LCD_charGap = 4;

int LCD_fullGapHorizontal = 40;
int LCD_fullGVertical = 120;


int LCD_charWidth = (LCD_numPixelsWide * LCD_pixelSize + LCD_charGap) + (LCD_numPixelsWide* LCD_pixelGap);
int LCD_charHeight = (LCD_numPixelsHigh * LCD_pixelSize + LCD_charGap) + (LCD_numPixelsHigh * LCD_pixelGap);

int LCD_fullWidth = LCD_numCharsWide * LCD_charWidth + LCD_fullGapHorizontal;
int LCD_fullHeight = LCD_numCharsHigh * LCD_charHeight + LCD_fullGVertical;

color blueWhite = #EAF6FE;
color midBlue = #007FC6;
color darkBlue = #304697;


void setup() {

  size(5120, 2880);
  background(midBlue);
  //pixelDensity(2);
  frameRate(24);
  noStroke();

  fill(255);
  rect(200, 200, 1, 1);



  
  // LOAD SEQUENTIAL IMAGES (or a single image)
  // If you don't want to load each image separately
  // and you know how many frames you have, you
  // can create the filenames as the program runs.
  // The nf() command does number formatting, which will
  // ensure that the number is (in this case) 5 digits.
  for (int i = 0; i < numFrames; i++) {
    String imageName = "random_10x10_" + nf(i, 5) + ".png";
    images[i] = loadImage(imageName);
    //images[i].filter(GRAY);
  }
} 


void draw() {
  //drawPixels();
  //drawSingleCharacter(LCD_charWidth, LCD_charHeight);
  drawMultipleLCDs();

}




///// ****************** draw pixels to screen ********************* /////

void  drawMultipleLCDs() {
  for (int x = 0; x < numLCDsWide; x++) {
    for (int y = 0; y < numLCDsHigh; y++) {
      pushMatrix();          
      translate(x * LCD_fullWidth, y * LCD_fullHeight);
      drawMultipleCharacters();
      popMatrix();
    }
  }
}

void drawMultipleCharacters() {
  for (int x = 0; x < LCD_numCharsWide; x++) {
    for (int y = 0; y < LCD_numCharsHigh; y++) {

      int charXpos = (x * LCD_charWidth);
      int charYpos = (y * LCD_charHeight);

      drawSingleCharacter(charXpos, charYpos);
    }
  }
}


void drawSingleCharacter(int Xoffset, int Yoffset) {

  for (int x = 0; x < LCD_numPixelsWide; x++) {
    for (int y = 0; y < LCD_numPixelsHigh; y++) {

      // decide if particular pixel is ON (black) or OFF (white)
      int fillNum = int(random(10));                 // returns 0 or 1
      int fillVal = (fillNum > 1)  ? darkBlue : blueWhite;      // ternary operator
      fill(fillVal);

      int xPos = (x * LCD_pixelSize + Xoffset) + (x * LCD_pixelGap);
      int yPos = (y * LCD_pixelSize + Yoffset) + (y * LCD_pixelGap);

      rect(xPos, yPos, LCD_pixelSize, LCD_pixelSize);
    }
  }
}



///// ****************** get greyscale values per pixel from images ********************* /////

// capture greyscale or brightnesss values from loadImage();
void drawImagePixels() {

  int charWidth = 50;
  int charHeight = 80;


  currentFrame = (currentFrame+1) % numFrames;  // Use % modulo to cycle through frames

  for (int x = 0; x < images[currentFrame].width; x++) {
    for (int y = 0; y < images[currentFrame].height; y++) {

      pixelColor = int((images[(currentFrame)]).get(x, y));

      // draw enlarged pixel grid
      fill(getGreyScaleVals());
      rect(x * charWidth, y * charHeight, charWidth, charHeight);
    }
  }
}


int getGreyScaleVals() {

  // get greyscale values
  // https://processing.org/discourse/beta/num_1159135995.html
  int r = (pixelColor & 0x00FF0000) >> 16;     // red part
  int g = (pixelColor & 0x0000FF00) >> 8;      // green part
  int b = (pixelColor & 0x000000FF);           // blue part
  int grey = (r + b + g) / 3;
  int brightness = max(r, g, b);               // different method for grabbing values


  // map values to a range: 0 - 8
  greyMapped = int(map(grey, 0, 255, 0, 8));
  brightnessMapped = int(map(brightness, 0, 255, 0, 8));

  return grey;
}
