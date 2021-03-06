"""Tests for cmake database generation.

Attributes:
    FlagsFile (TYPE): Description
"""
import imp
from os import path
from unittest import TestCase

from EasyClangComplete.plugin.flags_sources import flags_file
from EasyClangComplete.plugin import tools

imp.reload(flags_file)
imp.reload(tools)

SearchScope = tools.SearchScope
PKG_NAME = tools.PKG_NAME

FlagsFile = flags_file.FlagsFile


class TestFlagsFile(TestCase):
    """Test finding and generatgin flags from .clang_complete file.

    Attributes:
        view (TYPE): Description
    """

    def test_init(self):
        """Initialization test."""
        self.assertEqual(FlagsFile._FILE_NAME, '.clang_complete')

    def test_load_file(self):
        """Test finding and loading existing file."""
        test_file_path = path.join(
            path.dirname(__file__), 'test_files', 'test.cpp')

        flags_file = FlagsFile(['-I', '-isystem'])
        flags = flags_file.get_flags(test_file_path)
        self.assertIn('-std=c++11', flags)

    def test_fail_to_find(self):
        """Test failing to find a .clang_complete file."""
        test_file_path = path.join(
            path.dirname(__file__), 'test_files', 'test.cpp')

        folder = path.dirname(test_file_path)
        flags_file = FlagsFile(['-I', '-isystem'])
        wrong_scope = SearchScope(from_folder=folder, to_folder=folder)
        flags = flags_file.get_flags(test_file_path, wrong_scope)
        self.assertIs(flags, None)
