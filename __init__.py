# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WorldView
                                 A QGIS plugin
 Provides a button in the QGIS interface to toggle the drawing of world borders above all other layers

                             -------------------
        begin                : 2015-07-14
        copyright            : (C) 2015 by Ian Edwards
        email                : ian@myacorn.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load WorldView class from file WorldView.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .worldview import WorldView
    return WorldView(iface)
