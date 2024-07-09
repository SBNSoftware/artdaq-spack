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

class ArtdaqDemo(CMakePackage):
    """The toolkit currently provides functionality for data transfer,
    event building, event reconstruction and analysis (using the art analysis
    framework), process management, system and process state behavior, control
    messaging, local message logging (status and error messages), DAQ process
    and art module configuration, and the writing of event data to disk in ROOT
    format."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/artdaq/wiki"
    url = "https://github.com/art-daq/artdaq_demo/archive/refs/tags/v3_12_02.tar.gz"
    git = "https://github.com/art-daq/artdaq_demo.git"

    version("develop", branch="develop", get_full_repo=True)
    version("v3_14_00", commit="2e67f04e7fac6b7ab6d6896c0df0316b3122ab1b")    
    version("v3_13_01", commit="3bb72231d2196be8efd028b6137070e6ca2dcd60") 
    version("v3_13_00", commit="a0255fe443765839448664c915b542b0419c0c7d") 
    version("v3_12_07", sha256="3908cc9678fa92c1b5870a5f67787fcabce2414ccb7d6aa5619b2484e866d43e")
    version("v3_12_05", sha256="0fe69abc89294903ac4c5f98bc2e71b6556e1b7e273c27dce6b4206c2e892510")
    version("v3_12_04", sha256="959a5926951199a3a19d5f29213cb4eae42899fca32e3c4e8f2b17ceea0a8e42")
    version("v3_12_03", sha256="e068ea0cd09e94fc9e4ad6fce067ca716db82fd79480c07c1e16cd2659325ee2")
    version("v3_12_02", sha256="3044f14e28f2c54318d06a64c22685839d4dba1a85a30d92ebaa9fe2e8f86055")

    def url_for_version(self, version):
        url = "https://github.com/art-daq/artdaq_demo/archive/refs/tags/{0}.tar.gz"
        return url.format(version)

    variant(
        "cxxstd",
        default="17",
        values=("14", "17"),
        multi=False,
        sticky=True,
        description="Use the specified C++ standard when building.",
        when="@:v3_12_04"        
    )
    variant(
        "cxxstd",
        default="20",
        values=("17", "20"),
        multi=False,
        sticky=True,
        description="Use the specified C++ standard when building.",
        when="@v3_12_04:"        
    )

    depends_on("cetmodules", type="build")

    depends_on("artdaq")
    depends_on("artdaq-core-demo")

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

