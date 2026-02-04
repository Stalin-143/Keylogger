"""
Basic tests for the keylogger-educational project.
These tests verify the basic project structure and configuration.
"""

import os
import pytest


@pytest.fixture
def project_root():
    """Return the project root directory path."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def test_project_structure(project_root):
    """Test that the project has expected structure."""
    # Check essential files exist
    assert os.path.exists(os.path.join(project_root, 'pyproject.toml'))
    assert os.path.exists(os.path.join(project_root, 'README.md'))
    assert os.path.exists(os.path.join(project_root, 'src'))


def test_src_package_structure(project_root):
    """Test that the src package has expected files."""
    src_dir = os.path.join(project_root, 'src')
    
    assert os.path.exists(os.path.join(src_dir, '__init__.py'))
    assert os.path.exists(os.path.join(src_dir, 'keylogger.py'))
    assert os.path.exists(os.path.join(src_dir, 'server.py'))


def test_config_directory_exists(project_root):
    """Test that the config directory exists."""
    assert os.path.exists(os.path.join(project_root, 'config'))


def test_version_file_exists(project_root):
    """Test that VERSION file exists and contains valid version."""
    version_file = os.path.join(project_root, 'VERSION')
    
    assert os.path.exists(version_file)
    
    with open(version_file, 'r') as f:
        version = f.read().strip()
    
    # Check version is not empty
    assert len(version) > 0
