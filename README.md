# SDEV265Group5Project

SDEV 265 Group 5 Project

!! IMPORTANT !!
After installing tzwhere, you will need to go and modify the tzwhere.py file.
When running the program and hitting the "ValueError: setting an array element with a sequence", open the file listed (should end in a file called tzwhere.py) and scroll to the top and find the following:

    try:
        import numpy
        WRAP = numpy.asarray
        COLLECTION_TYPE = numpy.ndarray
    except ImportError:
        WRAP = tuple
        COLLECTION_TYPE = tuple

modify to match the following:

    # try
    # import numpy
    # WRAP = numpy.asarray
    # COLLECTION_TYPE = numpy.ndarray
    # except ImportError:
    WRAP = tuple
    COLLECTION_TYPE = tuple
