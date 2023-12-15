# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


class OtsdaqEpics(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/otsdaq_epics/archive/refs/tags/v2_06_08.tar.gz"
    git = "https://github.com/art-daq/otsdaq_epics.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v2_07_00", sha256="60bf90b0572ef0f20df9b7728f3274b38be46e2a49b0dbe2e1ab17b4c146d6b0")
    version("v2_06_11", sha256="7bf9253b421846992fbf23bbb9a749f80ff2c0073954803951d3f8df1dda9925")
    version("v2_06_10", sha256="106321637bf47facd7ea59d21575c91fa8efaddd0afb6067de209231ecbe7a6d")
    version("v2_06_09", sha256="96c5e5b9a88fd0f18a6682d210bde83dbad7a25b9c8ca5ce4acf072cf02702a8")
    version("v2_06_08", sha256="5f24df325f4e27dfbd5a30892a80ba75a3eef642d60a759d1580f846f2e22813")

    def url_for_version(self, version):
        url = "https://github.com/art-daq/otsdaq_epics/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", conditional("20",when="@v2_06_10:")),
        multi=False,
        sticky=True,
        description="Use the specified C++ standard when building.",
    )

    depends_on("cetmodules", type="build")
    depends_on("epics-base")
    depends_on("libpqxx")

    depends_on("otsdaq")
    depends_on("otsdaq-utilities")


