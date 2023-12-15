# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys

from spack import *


def sanitize_environments(env, *vars):
    for var in vars:
        env.prune_duplicate_paths(var)
        env.deprioritize_system_paths(var)

class ArtdaqUtilities(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/artdaq_utilities/archive/refs/tags/v1_08_02.tar.gz"
    git = "https://github.com/art-daq/artdaq_utilities.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v1_08_06", sha256="76aff946eae802cc2a8ac285e92403a4c65af82de99f188869e6c43228f315e4")
    version("v1_08_04", sha256="66a3ccbf975c0171c8f2f377a17aa646d22f2aa190763939c270d5a8bf52d3f2")
    version("v1_08_03", sha256="761ce48cfdfb447fa0536df68719ada0d5ae5a426ca76f627792cac894caf475")
    version("v1_08_02", sha256="019a09d1f55d269066e0e5049bad6b0999883c6f6c455c178001bbd9d3b68722")

    def url_for_version(self, version):
        url = "https://github.com/art-daq/artdaq_utilities/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17", conditional("20",when="@v1_08_04:")),
        multi=False,
        sticky=True,
        description="Use the specified C++ standard when building.",
    )

    depends_on("cetmodules", type="build")
    depends_on("messagefacility")

    depends_on("trace+mf")

    def setup_run_environment(self, env):
        prefix = self.prefix
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", prefix.lib)
        # Ensure we can find fhicl files
        env.prepend_path("FHICL_FILE_PATH", prefix + "/fcl")
        # Cleaup.
        sanitize_environments(env, "CET_PLUGIN_PATH", "FHICL_FILE_PATH")

    def setup_dependent_run_environment(self, env, dependent_spec):
        prefix = self.prefix
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", prefix.lib)
        # Ensure we can find fhicl files
        env.prepend_path("FHICL_FILE_PATH", prefix + "/fcl")
        # Cleaup.
        sanitize_environments(env, "CET_PLUGIN_PATH", "FHICL_FILE_PATH")

