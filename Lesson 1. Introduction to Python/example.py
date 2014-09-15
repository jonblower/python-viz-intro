# A simple Python script that illustrates some of the concepts of
#  variable assignment, loops, conditionals, functions and testing
# Load into SciTE and run by pressing F5
# Or rwith "python example.py"


# Variable assignment
temperature = 5.0  # a floating-point (decimal) number
numberOfLegs = 2   # an integer (whole number)
name = "Jon"       # a string


# Conditionals
if temperature < 0.0:
    print "It's freezing!"
elif temperature > 30.0:
    print "It's hot! (If you're British)"
else:
    print "Not too hot, not too cold"
# Note: there is no "end if"


# Loops
print "Here are the numbers from 0 to 9:"
for i in range(10):
    print i

print "Here's another (longer) way to print the same thing"
i = 0
while i < 10:
    print i
    i = i + 1

# Define a function that constrains a value of longitude (in degrees) to be in the range
# [-180:180]
def lon180(lon):
    lon = lon % 360
    if lon > 180:
        return lon - 360
    else:
        return lon

# Here's a function that tests the above routine.  It calls lon180 and checks
# the answer is as expected
def testLon180(lon, expected):
    actual = lon180(lon)
    # str(number) converts a number to a string
    print "lon180(" + str(lon) + ") = " + str(actual) + ". Expected = " + str(expected)
    # Here's another way to print the same information, using something like C's
    # C's printf statement
    #print "lon180(%f) = %f. Expected = %f" % (lon, actual, expected)

# Now test the function.  You can probably think of lots more tests
testLon180(-180, 180)
testLon180(360, 0)
testLon180(-190, 170)

