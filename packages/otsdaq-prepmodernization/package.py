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



class OtsdaqPrepmodernization(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/otsdaq_prepmodernization/archive/refs/tags/v2_06_08.tar.gz"
    git = "https://github.com/art-daq/otsdaq_prepmodernization.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v2_07_00", sha256="fdd9669d93f63be756a43113f2360497ef5d2ce5a42636fa44d9bdc363a07cc5")
    version("v2_06_11", sha256="b6d5d52b723dacffe292dcd9979c8bb1a77e014f7f8c69b00b5a7d7dcc3ded8f")
    version("v2_06_10", sha256="9f04f751b9161de42fe737d94a84f8b76bbfc66572d13c537d431a5fa860d810")
    version("v2_06_09", sha256="2292d08afa50c6946f722a0a1ece333a889e5b018fcab2c0d28d03fb843dd975")
    version("v2_06_08", sha256="bbb04dee03dc212aa499f7d978492db26f6896e8436d0c14576be4e22d688e59")

    def url_for_version(self, version):
        url = "https://github.com/art-daq/otsdaq_prepmodernization/archive/refs/tags/{0}.tar.gz"
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

    depends_on("otsdaq")
    depends_on("otsdaq-utilities")
    depends_on("otsdaq-components")


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