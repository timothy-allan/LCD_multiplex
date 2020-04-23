# LCD_multiplex
Display images over multiple LCD Character displays


We have a 3*4 pixel grid. 

So, the number of pixels = (3*4) = 12 pixels.

We want to have, say, 6 pixels ON.

How can we generate ALL possible configurations of 6 pixels ON in this 12 pixel grid?

We generate an empty list of 12 items - let's call it pixel_configuration.

For each item in that configuration_list we generate a random number  - either  0 - OFF or 1 - ON, and add it to the list.

We get something like this:

pixel_configuration = [ 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1 ]

That's one possible configuration, but we want to find ALL possible configurations.

We need to keep generating different variations of pixel_configuration, to find all possible configurations of pixels that are ON...


For example:

pixel_configuration ONE
[ 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1 ]

pixel_configuration TWO
[ 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0 ]

pixel_configuration THREE
[ 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0 ]

... etc

Let's add each pixel_configuration to another list that contains all these configurations - lets call it LIST_OF_pixel_configurations:

[ 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1 ] ,
[ 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0 ] , 
[ 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0 ]


Because we are generating configurations that are randomly generated, we are going to generate duplicate configurations.

We don't want to add duplicate configurations to our LIST_OF_pixel_configurations, so we need to check if a particular configuration has already been added.


HOWEVER:
This algorithm will loop infinitely:

Once the max amount of configurations of six pixels ON out of twelve pixels has been added to our LIST_OF_pixel_configurations, the program will continue to generate random configurations, check if they are contained in	LIST_OF_pixel_configurations, find they are not, ad infinitum. The program will not halt.

One way to ensure a halt is to generate an arbitrarily large number (n) of configurations and then stop. Increasing (n) will eventually yield a max number of possibilities, but this is not a proof. 

TEST RESULTS
8 pixels TOTAL, 4 ON

NUM_LOOPS: 100 
CONFIGURATIONS: 25

NUM_LOOPS: 1000
CONFIGURATIONS: 66

NUM_LOOPS: 10 000
CONFIGURATIONS: 70

NUM_LOOPS: 100 000
CONFIGURATIONS: 70

NUM_LOOPS: 1000000
CONFIGURATIONS: 70

So, we can make a pretty good guess that there are 70 possible configurations of 8 pixels TOTAL, 4 ON. We can then limit the number of configurations we generate. Rather than generate configurations infinitely, we can stop our program once LIST_OF_pixel_configurations contains 70 configurations.


All of this work takes time. Let's look at the time it took to generate the results above.

NUM_LOOPS: 100
CONFIGURATIONS: 25
Time to complete: 0.0007348060607910156

NUM_LOOPS: 1000
CONFIGURATIONS: 66
Time to complete: 0.00728607177734375

NUM_LOOPS: 10 000
CONFIGURATIONS: 70 
Time to complete: 0.08138489723205566

NUM_LOOPS: 100 000
CONFIGURATIONS: 70
Time to complete: 0.7345280647277832

NUM_LOOPS: 100 000 000
CONFIGURATIONS: 70
Time to complete: 7.315468072891235


If we limit the size of LIST_OF_pixel_configurations to 70, our best guess of the max number of configurations, it takes far less time - we are not wasting time generating configurations that have already been found and added:

while LIST_OF_pixel_configurations < 70
CONFIGURATIONS: 70
Time to complete: 0.008151769638061523


OK, so this is a smallish number of pixels - only eight in our example.  But it took between ten thousand and a million loops to be reasonably sure we'd found the maximum number of configurations.


Lets try a bigger number of total pixels - say 16, and find configurations for 6 pixels ON:

TEST RESULTS
16 pixels TOTAL, 6 ON

NUM_LOOPS: 100 
CONFIGURATIONS: 16
Time to complete: 0.00139

NUM_LOOPS: 1000 
CONFIGURATIONS: 124
Time to complete: 0.01471

NUM_LOOPS: 10 000
CONFIGURATIONS: 1146
Time to complete: 0.15992

NUM_LOOPS: 100 000 
CONFIGURATIONS: 6266
Time to complete: 2.29078

NUM_LOOPS: 10 000 000 
CONFIGURATIONS: 8008
Time to complete: 260.518

NUM_LOOPS: 100 000 000 
CONFIGURATIONS: 8008
Time to complete: 2649.93 - around 45 minutes...


Question ONE:
Is there a way to calculate, in advance, the number of possible configurations of pixel grid of some (width * height) = length (l), with (n) pixels ON? This would allow us to end our program once it had found the total number of configurations before running the exhaustive tests above.

Question TWO:
Is there a way to generate all possible configurations of such a  a pixel grid WITHOUT this brute force method? That is to say - without generating endless random configurations?










