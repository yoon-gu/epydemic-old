"""
Example
-------

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil, illo provident temporibus. 
Tenetur ad facere in optio, dignissimos minus necessitatibus nam quidem laboriosam itaque 
inventore doloribus dolor perferendis cupiditate nobis.

* Lorem ipsum dolor.
* Lorem ipsum dolor.
* Lorem ipsum dolor.
* Lorem ipsum dolor.

"""
__author__ = ("Jacob Hwang <jacob@dnry.org>")

__all__ = ["ols", "gls", "sir", "seir"]

from models import sir, seir
from estimations import ols, gls
import epydemic_app