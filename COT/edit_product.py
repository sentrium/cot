#!/usr/bin/env python
#
# edit_product.py - Implements "edit-product" sub-command
#
# August 2013, Glenn F. Matthews
# Copyright (c) 2013-2015 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
# and at https://github.com/glennmatthews/cot/blob/master/COPYRIGHT.txt.
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution and at
# https://github.com/glennmatthews/cot/blob/master/LICENSE.txt. No part
# of COT, including this file, may be copied, modified, propagated, or
# distributed except according to the terms contained in the LICENSE.txt file.

import logging

from .submodule import COTSubmodule

logger = logging.getLogger(__name__)


class COTEditProduct(COTSubmodule):
    """Edit product information (short version, long version)"""

    def __init__(self, UI):
        super(COTEditProduct, self).__init__(UI)
        self.version = None
        self.full_version = None

    def ready_to_run(self):
        """Are we ready to go?
        Returns the tuple (ready, reason)"""

        ready, reason = super(COTEditProduct, self).ready_to_run()
        if not ready:
            return ready, reason

        work_to_do = False
        if self.version is not None:
            work_to_do = True
        elif self.full_version is not None:
            work_to_do = True

        if not work_to_do:
            return False, ("Neither version nor full version was specified "
                           "- nothing to do!")
        return ready, reason

    def run(self):
        super(COTEditProduct, self).run()

        if self.version is not None:
            self.vm.set_short_version(self.version)
        if self.full_version is not None:
            self.vm.set_long_version(self.full_version)

    def create_subparser(self, parent):
        p = parent.add_parser(
            'edit-product',
            help="""Edit product info in an OVF""",
            usage=self.UI.fill_usage("edit-product", [
                "PACKAGE [-o OUTPUT] [-v SHORT_VERSION] [-V FULL_VERSION]",
            ]),
            description="""
Edit product information attributes of the given OVF or OVA""")

        p.add_argument('-o', '--output',
                       help="""Name/path of new OVF/OVA package to create """
                       """instead of updating the existing OVF""")
        p.add_argument('-v', '--version', metavar="SHORT_VERSION",
                       help="""Software short version string, such as """
                       """"15.3(4)S" or "5.2.0.01I" """)
        p.add_argument('-V', '--full-version',
                       help="""Software long version string, such as """
                       """"Cisco IOS-XE Software, Version 15.3(4)S" """)
        p.add_argument('PACKAGE',
                       help="""OVF descriptor or OVA file to edit""")
        p.set_defaults(instance=self)

        return 'edit-product', p
