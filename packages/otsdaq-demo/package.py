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


class OtsdaqDemo(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/otsdaq_demo/archive/refs/tags/v2_06_08.tar.gz"
    git = "https://github.com/art-daq/otsdaq_demo.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v2_09_00", commit="fa35f2c0c00cc84b82c0f567c88fb2405d53ea9c")
    version("v2_08_02", commit="4c4af9009475e00cacdd4fb8c700588f42366bab")
    version("v2_08_01", commit="0ea738a6f21c8678cc6c9d8f41ca1163ccb2cd18")
    version("v2_08_00", commit="677f1844f351c0ac5a481f484c54b8d0ea877191")
    version("v2_07_00", sha256="55d4379bce188b85c9a65989aa61064cd936dc897ba65a4caea23ad3a085cc00")
    version("v2_06_11", sha256="5efa1736f3553f5f6d837597e650a9434ad564baaf78033e80b3d2c45e0db228")
    version("v2_06_10", sha256="174160f6c9206ba50f29bc39797fbc390d5f705bd525e46513e552176cd28468")
    version("v2_06_09", sha256="8685c2800c05b75695dd9f55c0816069f306de187060cf981d8db5c8831f9616")
    version("v2_06_08", sha256="8402dbd195ad95ad5960ede16bdb56a780b248501c9486405e1a72c7993a7a70")

    def url_for_version(self, version):
        url = "https://github.com/art-daq/otsdaq_demo/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17"),
        multi=False,
        sticky=True,
        description="Use the specified C++ standard when building.",
        when="@:v2_06_10"        
    )
    variant(
        "cxxstd",
        default="20",
        values=("17", "20"),
        multi=False,
        sticky=True,
        description="Use the specified C++ standard when building.",
        when="@v2_06_10:"        
    )

    depends_on("cetmodules", type="build")

    depends_on("otsdaq")
    depends_on("otsdaq-utilities")
    depends_on("otsdaq-components")

    def cmake_args(self):
        args = [
            self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd"),
        ]
        if os.path.exists("CMakePresets.cmake"):
            args.extend(["--preset", "default"])
        else:
            self.define("artdaq_core_OLD_STYLE_CONFIG_VARS", True)
        return args


    def setup_run_environment(self, env):
        prefix = self.prefix
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", prefix.lib)
        # Ensure we can find fhicl files
        env.prepend_path("FHICL_FILE_PATH", prefix + "/fcl")
        # Ensure we can find libraries
        env.set("OTSDAQ_DEMO_LIB", prefix.lib)
        # Cleaup.
        sanitize_environments(env, "CET_PLUGIN_PATH", "FHICL_FILE_PATH")

    def setup_dependent_run_environment(self, env, dependent_spec):
        prefix = self.prefix
        # Ensure we can find plugin libraries.
        env.prepend_path("CET_PLUGIN_PATH", prefix.lib)
        # Ensure we can find fhicl files
        env.prepend_path("FHICL_FILE_PATH", prefix + "/fcl")
        # Ensure we can find libraries
        env.set("OTSDAQ_DEMO_LIB", prefix.lib)
        # Cleaup.
        sanitize_environments(env, "CET_PLUGIN_PATH", "FHICL_FILE_PATH")
