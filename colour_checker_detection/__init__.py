"""
Colour - Checker Detection
==========================

Colour checker detection algorithms for *Python*.

Subpackages
-----------
-   detection : Colour checker detection.
"""

from __future__ import annotations

import contextlib
import cv2
import numpy as np
import os
import subprocess

import colour

from .detection import (
    SETTINGS_SEGMENTATION_COLORCHECKER_CLASSIC,
    SETTINGS_SEGMENTATION_COLORCHECKER_SG,
    colour_checkers_coordinates_segmentation,
    extract_colour_checkers_segmentation,
    detect_colour_checkers_segmentation,
)

__author__ = "Colour Developers"
__copyright__ = "Copyright 2018 Colour Developers"
__license__ = "BSD-3-Clause - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "SETTINGS_SEGMENTATION_COLORCHECKER_CLASSIC",
    "SETTINGS_SEGMENTATION_COLORCHECKER_SG",
    "colour_checkers_coordinates_segmentation",
    "extract_colour_checkers_segmentation",
    "detect_colour_checkers_segmentation",
]

ROOT_RESOURCES: str = os.path.join(os.path.dirname(__file__), "resources")
ROOT_RESOURCES_EXAMPLES: str = os.path.join(
    ROOT_RESOURCES, "colour-checker-detection-examples-datasets"
)
ROOT_RESOURCES_TESTS: str = os.path.join(
    ROOT_RESOURCES, "colour-checker-detection-tests-datasets"
)

__application_name__ = "Colour - Checker Detection"

__major_version__ = "0"
__minor_version__ = "1"
__change_version__ = "5"
__version__ = ".".join(
    (__major_version__, __minor_version__, __change_version__)
)

try:
    _version = (
        subprocess.check_output(
            ["git", "describe"],  # noqa: S603, S607
            cwd=os.path.dirname(__file__),
            stderr=subprocess.STDOUT,
        )
        .strip()
        .decode("utf-8")
    )
except Exception:
    _version = __version__

colour.utilities.ANCILLARY_COLOUR_SCIENCE_PACKAGES[  # pyright: ignore
    "colour-checker-detection"
] = _version
colour.utilities.ANCILLARY_RUNTIME_PACKAGES[  # pyright: ignore
    "opencv"
] = cv2.__version__  # pyright: ignore

del _version

# TODO: Remove legacy printing support when deemed appropriate.
with contextlib.suppress(TypeError):
    np.set_printoptions(legacy="1.13")
