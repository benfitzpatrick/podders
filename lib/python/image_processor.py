""" Print pixel RGB values to file. """

import sys

import Image

CATEGORIES = {"Science": [0.0, 0.33],
              "Art": [0.33, 0.66],
              "Citizenship": [0.66, 1.0]}
RATINGS = {0: [0.0, 0.166],
           1: [0.166, 0.33],
           2: [0.33, 0.5],
           3: [0.5, 0.66],
           4: [0.66, 0.833],
           5: [0.833, 1.0]}


class ColourProcessor(object):

    """Class to get x and y pixel fractions for given colours."""

    COLOURS = ["pink", "green", "yellow"]

    def __init__(self, pixarray, size_x, size_y):
        self.xfrac = {}
        self.yfrac = {}
        self.size_x = size_x
        self.size_y = size_y
        self.pixarray = pixarray

    def process(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                a = self.pixarray[i, j]
                if (0.9 < float(a[0]) / max([1, float(a[1])]) < 1.1 and
                    0.9 < float(a[1]) / max([1, float(a[2])]) < 1.1 and
                    0.9 < float(a[2]) / max([1, float(a[0])]) < 1.1):
                    continue
                for colour in self.COLOURS:
                    if getattr(self, "is_" + colour)(a[0], a[1], a[2]):
                        self.xfrac.setdefault(colour, [])
                        self.xfrac[colour].append(float(i) / float(self.size_x))
                        self.yfrac.setdefault(colour, [])
                        self.yfrac[colour].append(float(j) / float(self.size_y))
                        break
        return self.xfrac, self.yfrac
        
    def is_pink(self, red, green, blue):
        """Return whether the object is pink or not."""
        return (red > 1.2 * blue and red > 1.2 * green and 
                blue + green < 1.5 * red)

    def is_yellow(self, red, green, blue):
        """Return whether the object is yellow or not."""
        return (red < 1.4 * green and green < 1.4 * red and
                red > 1.9 * blue)

    def is_green(self, red, green, blue):
        """Return whether the object is green or not."""
        return (green > 1.2 * red and green > 1.2 * blue and
                red + blue < 1.5 * green)


def get_colour_fractions(image_filename):
    im = Image.open(image_filename)
    pixload = im.load()
    pixlist = im.getdata()
    colour_processor = ColourProcessor(pixload, im.size[0], im.size[1])
    xfrac_map, yfrac_map = colour_processor.process()
    colour_median_xfrac_map = {}
    colour_median_yfrac_map = {}
    for colour, fractions in xfrac_map.items():
        fractions.sort()
        colour_median_xfrac_map[colour] = fractions[len(fractions)/2]
    for colour, fractions in yfrac_map.items():
        fractions.sort()
        colour_median_yfrac_map[colour] = fractions[len(fractions)/2]
    return colour_median_xfrac_map, colour_median_yfrac_map


def process_colour_fractions(xfrac_map, yfrac_map):
    """Turn colour xfrac and yfrac to ratings, categories."""
    category_rating_map = {}
    for category in CATEGORIES:
        category_rating_map[category] = min(RATINGS.keys())
    for colour in xfrac_map:
        for category, min_max in CATEGORIES.items():
            if min_max[0] < yfrac_map[colour] < min_max[1]:
                break
        for rating, min_max in RATINGS.items():
            if min_max[0] < xfrac_map[colour] < min_max[1]:
                break
        if (category in category_rating_map and
            rating < category_rating_map[category]):
            continue 
        category_rating_map[category] = rating
    return category_rating_map


def main():
    xfrac_map, yfrac_map = get_colour_fractions(sys.argv[1])
    category_rating_map = process_colour_fractions(xfrac_map, yfrac_map)
    f = open("ratings.txt", 'w')
    for category, rating in category_rating_map.items():
        print category, ":", rating
        f.write(str(category) + " : " + str(rating) + "\n")
    f.close()

if __name__ == "__main__":
    main()
