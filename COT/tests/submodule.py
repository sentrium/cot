#!/usr/bin/env python
#
# submodule.py - test cases for the generic COTSubmodule class
#
# January 2015, Glenn F. Matthews
# Copyright (c) 2015 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
# and at https://github.com/glennmatthews/cot/blob/master/COPYRIGHT.txt.
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution and at
# https://github.com/glennmatthews/cot/blob/master/LICENSE.txt. No part
# of COT, including this file, may be copied, modified, propagated, or
# distributed except according to the terms contained in the LICENSE.txt file.

from COT.tests.ut import COT_UT
from COT.ui_shared import UI
from COT.submodule import COTSubmodule
from COT.vm_description import VMInitError


class TestCOTSubmodule(COT_UT):
    """Test cases for COTSubmodule class"""

    def setUp(self):
        """Test case setup function called automatically prior to each test"""
        super(TestCOTSubmodule, self).setUp()
        self.instance = COTSubmodule(UI())
        self.instance.output = self.temp_file

    def test_vmfactory_fail(self):
        self.instance.output = "foo.vmx"
        with self.assertRaises(VMInitError):
            self.instance.package = self.input_ovf

    def test_create_subparser_noop(self):
        label, subparser = self.instance.create_subparser(None)
        self.assertEqual(label, "")
        self.assertEqual(subparser, None)
