# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:17:20 2013

@author: yves
"""

from __future__ import division,print_function,unicode_literals,absolute_import

from traits.has_traits import HasTraits
from traits.trait_types import Int,Tuple
from traitsui.item import Item
from traitsui.view import View

from traitsui.tests._tools import *


class TupleEditor(HasTraits):
    """Dialog containing a Tuple of two Int's.
    """

    tup = Tuple(Int,Int)

    traits_view = View(
        Item(label="Enter 4 and 6, then press OK"),
        Item('tup'),
        buttons = ['OK']
    )




@skip_if_not_qt4
def test_qt_tuple_editor():
    # Behavior: when editing the text part of a spin control box, pressing
    # the OK button updates the value of the HasTraits class

    from pyface import qt

    with store_exceptions_on_all_threads():
        val = TupleEditor()
        ui = val.edit_traits()

        # text element inside the spin control
        lineedits = ui.control.findChildren(qt.QtGui.QLineEdit)
        lineedits[0].setFocus()
        lineedits[0].setText('4')
        lineedits[1].setFocus()
        lineedits[1].setText('6')

        # press the OK button and close the dialog
        press_ok_button(ui)

    # if all went well, the number traits has been updated and its value is 4
    assert val.tup == (4,6)
    


if __name__ == '__main__':
    # Executing the file opens the dialog for manual testing
    val = TupleEditor()
    val.configure_traits()
    print(val.tup)
