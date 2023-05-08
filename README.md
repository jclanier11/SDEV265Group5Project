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

Constellation Image sources/attribution:

Aquarius: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0
https://commons.wikimedia.org/w/index.php?curid=15406063

Aries: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15406068

Cancer: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15406241

Capricornus: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15406245

Gemini: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15407383

Leo: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15407527

Libra: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15407530

Pisces: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15412178

Sagittarius: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15412401

Scorpius: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15412402

Taurus: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15412408

Virgo: By IAU and Sky & Telescope magazine (Roger Sinnott & Rick Fienberg) - CC BY 3.0,
https://commons.wikimedia.org/w/index.php?curid=15412504

Other Information Sources:

    Chartrand, M. R. (1991). National Audubon Society Field Guide to the Night Sky (Ser. National Audubon Society Field Guides). Alfred A. Knopf.
    ISBN: 978-0-679-40852-9

    Howell, C. H. (2017). National Geographic Pocket Guide to the Night Sky of North America (Ser. National Geographic Pocket Guide Series). National Geographic.
    ISBN: 978-1-4262-1785-2
