# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from sys import version

from spack.package import *

class OtsdaqSuite(BundlePackage):
    """The Off-The-Shelf DAQ suite, otsdaq, providing graphical wrappers for artdaq
    """
    
    version("v2_07_00")
    version("v2_06_11")
    version("v2_06_10")
    version("v2_06_09")
    version("v2_06_08")
    
    squals = ("112", "117", "118", "120", "120a", "122", "123", "124", "126")
    variant(
        "s",
        default="0",
        values=("0",) + squals,
        multi=False,
        description="Art suite version to use",
    )
    for squal in squals:
        depends_on(f"art-suite@s{squal}+root", when=f"s={squal}")
    depends_on(f"art-suite+root", when="s=0")

    variant(
        "artdaq",
        default="0",
        values = ("0","31202","31203","31204", "31205", "31207"),
        multi=False,
        description="Artdaq suite version to use",
    )
    depends_on("artdaq-suite@v3_12_07", when="artdaq=31207")
    depends_on("artdaq-suite@v3_12_05", when="artdaq=31205")
    depends_on("artdaq-suite@v3_12_04", when="artdaq=31204")
    depends_on("artdaq-suite@v3_12_03", when="artdaq=31203")
    depends_on("artdaq-suite@v3_12_02", when="artdaq=31202")
    depends_on("artdaq-suite+db+epics~demo~pcp")

    variant("demo", default=False, description="Install otsdaq-demo")
    variant("prep", default=False, description="Install PREP modernization library")
    
    with when("@v2_07_00"):
        depends_on("otsdaq@v2_07_00")
        depends_on("otsdaq-utilities@v2_07_00")
        depends_on("otsdaq-components@v2_07_00")
        depends_on("otsdaq-epics@v2_07_00")
        depends_on("otsdaq-demo@v2_07_00", when="+demo")
        depends_on("otsdaq-prepmodernization@v2_07_00", when="+prep")
    with when("@v2_06_11"):
        depends_on("otsdaq@v2_06_11")
        depends_on("otsdaq-utilities@v2_06_11")
        depends_on("otsdaq-components@v2_06_11")
        depends_on("otsdaq-epics@v2_06_11")
        depends_on("otsdaq-demo@v2_06_11", when="+demo")
        depends_on("otsdaq-prepmodernization@v2_06_11", when="+prep")
    with when("@v2_06_10"):
        depends_on("otsdaq@v2_06_10")
        depends_on("otsdaq-utilities@v2_06_10")
        depends_on("otsdaq-components@v2_06_10")
        depends_on("otsdaq-epics@v2_06_10")
        depends_on("otsdaq-demo@v2_06_10", when="+demo")
        depends_on("otsdaq-prepmodernization@v2_06_10", when="+prep")
    with when("@v2_06_09"):
        depends_on("otsdaq@v2_06_09")
        depends_on("otsdaq-utilities@v2_06_09")
        depends_on("otsdaq-components@v2_06_09")
        depends_on("otsdaq-epics@v2_06_09")
        depends_on("otsdaq-demo@v2_06_09", when="+demo")
        depends_on("otsdaq-prepmodernization@v2_06_09", when="+prep")
    with when("@v2_06_08"):
        depends_on("otsdaq@v2_06_08")
        depends_on("otsdaq-utilities@v2_06_08")
        depends_on("otsdaq-components@v2_06_08")
        depends_on("otsdaq-epics@v2_06_08")
        depends_on("otsdaq-demo@v2_06_08", when="+demo")
        depends_on("otsdaq-prepmodernization@v2_06_08", when="+prep")
