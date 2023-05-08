# SDEV265Group5Project

SDEV 265 Group 5 Project

!! IMPORTANT !!
This program directory includes a modified version of the tzwhere.py package. tzwhere is not included in the requirements.txt file because of that. It was edited in response to an error: "ValueError: setting an array element with a sequence". The following shows the edits made to the code:

    try:
        import numpy
        WRAP = numpy.asarray
        COLLECTION_TYPE = numpy.ndarray
    except ImportError:
        WRAP = tuple
        COLLECTION_TYPE = tuple

We modified it to match the following:

    # try
    # import numpy
    # WRAP = numpy.asarray
    # COLLECTION_TYPE = numpy.ndarray
    # except ImportError:
    WRAP = tuple
    COLLECTION_TYPE = tuple

Original sky_chart.py file pulled from viyaleta on GitHub, url: https://github.com/viyaleta/Python-Demos/blob/main/Sky%20Map%20Demo.ipynb.