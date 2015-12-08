"""
Epydemic Module
===============

``epydemic`` is a software package written in ``Python`` for mathematical epidemic modeling. There are three submodules.

* ``models`` contains epidemic modeling ordinary differential equation(ODE).
* ``estimations`` performs parameter estimations given real world data.
* ``controls`` solves optimal a control problem.

Example
-------
Examples can be given using either the ``Example`` or ``Examples``
sections. Sections support any reStructuredText formatting, including
literal blocks.

    $ python example_numpy.py


Section breaks are created with two blank lines. Section breaks are also
implicitly created anytime a new section starts. Section bodies *may* be
indented.

Notes
-----
    This is an example of an indented section. It's like any other section,
    but the body is indented to help it stand out from surrounding text.

If a section is indented, then a section break is created simply by
resuming unindented text.

"""
__author__ = ("Jacob Hwang <jacob@dnry.org>")

__all__ = ["models", "estimations", "epydemic_app"]

import models, estimations, epydemic_app