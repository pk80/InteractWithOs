import math


def triangle(base, height):
    """Returns area of a triangle with base and height provided"""
    return base * height / 2


def rectangle(base, height):
    """Returns area of a rectangle with base and height provided"""
    return base * height


def circle(radius):
    """Returns area of a circle with radius provided"""
    return round(math.pi * (radius ** 2), 2)


def donut(outside_radius, inside_radius):
    """Returns area of a donut provided inside and outside radii"""
    return round(circle(outside_radius) - circle(inside_radius), 2)
