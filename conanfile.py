from conans import ConanFile, tools


class BoostTokenizerConan(ConanFile):
    name = "Boost.Tokenizer"
    version = "1.65.1"

    requires = \
        "Boost.Generator/1.65.1@bincrafters/testing", \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Iterator/1.65.1@bincrafters/testing", \
        "Boost.Mpl/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing"

    lib_short_names = ["tokenizer"]
    is_header_only = True

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-tokenizer"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    def package_id(self):
        self.info.header_only()

    # END
