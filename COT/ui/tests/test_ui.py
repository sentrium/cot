# test_ui.py - Unit test cases for generic UI class
#
# January 2015, Glenn F. Matthews
# Copyright (c) 2015-2017 the COT project developers.
# See the COPYRIGHT.txt file at the top-level directory of this distribution
# and at https://github.com/glennmatthews/cot/blob/master/COPYRIGHT.txt.
#
# This file is part of the Common OVF Tool (COT) project.
# It is subject to the license terms in the LICENSE.txt file found in the
# top-level directory of this distribution and at
# https://github.com/glennmatthews/cot/blob/master/LICENSE.txt. No part
# of COT, including this file, may be copied, modified, propagated, or
# distributed except according to the terms contained in the LICENSE.txt file.

"""Unit test cases for COT.ui.UI class."""

from COT.ui import UI
from COT.tests import COTTestCase


class TestUI(COTTestCase):
    """Test cases for the COT.ui.UI class."""

    def test_apis_without_force(self):
        """Test confirm(), confirm_or_die(), etc. without --force."""
        ins = UI()

        self.assertTrue(ins.confirm("prompt"))
        ins.confirm_or_die("prompt")

        ins.default_confirm_response = False
        self.assertFalse(ins.confirm("prompt"))
        self.assertRaises(SystemExit, ins.confirm_or_die, "prompt")

        self.assertEqual("hello", ins.get_input("Prompt:", "hello"))

    def test_apis_with_force(self):
        """Test confirm(), confirm_or_die(), etc. with --force."""
        ins = UI(force=True)

        self.assertTrue(ins.confirm("prompt"))
        self.assertLogged(levelname="WARNING", msg="Automatically agreeing")

        ins.confirm_or_die("prompt")
        self.assertLogged(levelname="WARNING", msg="Automatically agreeing")

        ins.default_confirm_response = False
        # With --force, the default_confirm_response doesn't apply
        self.assertTrue(ins.confirm("prompt"))
        self.assertLogged(levelname="WARNING", msg="Automatically agreeing")

        ins.confirm_or_die("prompt")
        self.assertLogged(levelname="WARNING", msg="Automatically agreeing")

        self.assertEqual("hello", ins.get_input("Prompt:", "hello"))
        self.assertLogged(levelname="WARNING", msg="Automatically entering",
                          args=('hello', 'Prompt:'))

    def test_stub_apis(self):
        """Test stub APIs that subclasses should override."""
        ins = UI()
        self.assertEqual("subcommand --foo\nsubcommand --bar",
                         ins.fill_usage("subcommand", ["--foo", "--bar"]))

        self.assertRaises(NotImplementedError,
                          ins.fill_examples,
                          [("foo", "bar"), ("baz", "bat")])

        self.assertRaises(NotImplementedError,
                          ins.get_password, "user", "host")
