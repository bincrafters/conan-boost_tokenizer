#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostTokenizerConan(base.BoostBaseConan):
    name = "boost_tokenizer"
    url = "https://github.com/bincrafters/conan-boost_tokenizer"
    lib_short_names = ["tokenizer"]
    header_only_libs = ["tokenizer"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_iterator",
        "boost_mpl",
        "boost_throw_exception"
    ]
