# Converts JSON text to use translate with resource files instead of hardcoded text
# Author: Georg Begerow @gbegerow gbegerow@gmail.com
# Repository: https://github.com/gbegerow/ConvertTextToTranslate.git
# License: The MIT License (MIT)

# based on the great works from @TexelElf, @ABrightmoore, @SethBling and others

from pymclevel import TAG_Byte, TAG_Int, TAG_Compound, TAG_String
import mcplatform

sorts = {"Y, X, Z":(1,0,2), "Y, Z, X":(1,2,0),"X, Y, Z":(0,1,2), "Z, Y, X":(2,1,0), "X, Z, Y":(0,2,1), "Z, X, Y":(2,0,1)}
blockTypes = {"Command Block", "Sign", "Book"}


inputs = (
    ("Converts JSON text to use translate with resource files instead of hardcoded text", "label"),

	("Operation:",("Show Statistic","Append to Export")),
    ("Command Blocks:", True),
    ("Signs:", True),
    ("Books:",True),
	("File path:",("string","value=None")),
	("Sort output by:",tuple(sorted(sorts.keys()))),

    ("Georg Begerow @gbegerow")
	)

displayName = "Convert Text to Translate"


def perform(level, box, options):
    op = options["Operation:"]
    order = sorts[options["Sort output by:"]]
    filepath = options["File path:"]

    print '%s: Started at %s' % (displayName, time.ctime())

    print("No implementation yet")    
    
    
    print '%s: Started at %s' % (displayName, time.ctime())
