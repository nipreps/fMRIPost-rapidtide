# SPDX-FileCopyrightText: 2023-present Chris Markiewicz <effigies@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import sys

if __name__ == '__main__':
    from .cli import fmripost_rapidtide

    sys.exit(fmripost_rapidtide())
