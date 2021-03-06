##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Flac(AutotoolsPackage):
    """Encoder/decoder for the Free Lossless Audio Codec"""

    homepage = "https://xiph.org/flac/index.html"
    url      = "http://downloads.xiph.org/releases/flac/flac-1.3.2.tar.xz"

    version('1.3.2', '454f1bfa3f93cc708098d7890d0499bd')
    version('1.3.1', 'b9922c9a0378c88d3e901b234f852698')
    version('1.3.0', '13b5c214cee8373464d3d65dee362cdd')

    depends_on('libvorbis')
    depends_on('id3lib')
