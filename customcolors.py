#!/usr/bin/python
# Filename: customcolors.py


def deloitte_html():
    """
    Arguments: None
    Returns: Dictionary for Deloitte's color palette in HTML format

    Description of the palette:    
    The color palette revolves around the green. Additional colors are
    neutral grays and complementary greens and blues that allow the
    Deloitte Green to stand out. This creates a color scheme that is
    distinctively Deloitte.
    Throughout the identity system, color is used as a highlight
    rather than in large areas. It makes information clear,
    breaks up documents or spaces and provides focal points.
    The pie chart shows the proportion of colors that should
    be used when creating a Deloitte document.
    All colors should be used with white space to add pace.
    Deloitte Green should be used sparingly to protect its
    visual impact. Colors from the palette help to focus on
    specific information and to punctuate.
    Always make sure that white is the predominant color
    across the whole piece to maintain clarity, the overriding
    guideline with using the secondary colors is to keep it
    simple. In charts and diagrams, mix the colors up so
    that there is maximum differentiation between
    adjacent elements.

    Usage
    - Primary palette can be used in pullout quotes, charts
    and diagrams, icons, divider pages and slides
    - A solid page color can be used to provide separation
    and contrast in a document, although panels of color
    may not be used
    - Secondary palette can be used in complex charts and
    diagrams
    """
    return {
        # primary:
        "White": "#ffffff",
        "Black": "#000000",
        "Deloitte Green": "#86BC25",
        "Green 2": "#C4D600",
        "Green 4": "#43B02A",
        "Green 6": "#046A38",
        "Green 7 ": "#2C5234",
        "Teal 5": "#0097A9",
        "Blue 2": "#62B5E5",
        "Blue 3": "#00A3E0",
        "Blue 4": "#0076A8",
        "Blue 6": "#012169",
        "Cool Gray 2": "#D0D0CE",
        "Cool Gray 4": "#BBBCBC",
        "Cool Gray 7": "#97999B",
        "Cool Gray 9": "#75787B",
        "Cool Gray 11": "#53565A",
        # secondary:
        "Green 1": "#E3E48D",
        "Green 5": "#009A44",
        "Teal 1": "#DDEFE8",
        "Teal 2": "#9DD4CF",
        "Teal 3": "#6FC2B4",
        "Teal 4": "#00ABAB",
        "Teal 6": "#007680",
        "Teal 7": "#004F59",
        "Blue 1": "#A0DCFF",
        "Blue 5": "#005587",
        "Blue 7": "#041E42",
        "Cool Gray 6": "#A7A8AA",
        "Cool Gray 10": "#63666A",
        # additional functional colors:
        "Red": "#DA291C",
        "Orange": "#ED8B00",
        "Yellow": "#FFCD00"
    }


def deloitte_rgb():
    """
    Arguments: None
    Returns: Dictionary for Deloitte's color palette in RGB format

    Description of the palette:    
    The color palette revolves around the green. Additional colors are
    neutral grays and complementary greens and blues that allow the
    Deloitte Green to stand out. This creates a color scheme that is
    distinctively Deloitte.
    Throughout the identity system, color is used as a highlight
    rather than in large areas. It makes information clear,
    breaks up documents or spaces and provides focal points.
    The pie chart shows the proportion of colors that should
    be used when creating a Deloitte document.
    All colors should be used with white space to add pace.
    Deloitte Green should be used sparingly to protect its
    visual impact. Colors from the palette help to focus on
    specific information and to punctuate.
    Always make sure that white is the predominant color
    across the whole piece to maintain clarity, the overriding
    guideline with using the secondary colors is to keep it
    simple. In charts and diagrams, mix the colors up so
    that there is maximum differentiation between
    adjacent elements.

    Usage
    - Primary palette can be used in pullout quotes, charts
    and diagrams, icons, divider pages and slides
    - A solid page color can be used to provide separation
    and contrast in a document, although panels of color
    may not be used
    - Secondary palette can be used in complex charts and
    diagrams
    """
    return {
        "White": {"r": 255, "g": 255, "b": 255},
        "Black": {"r": 0, "g": 0, "b": 0},
        "Deloitte Green": {"r": 134, "g": 188, "b": 37},
        "Green 2": {"r": 196, "g": 214, "b": 0},
        "Green 4": {"r": 67, "g": 176, "b": 42}
    }
