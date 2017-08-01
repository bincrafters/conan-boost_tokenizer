## This repository holds a conan recipe for Boost.Tokenizer.

[Conan.io](https://conan.io) package for [Boost.Tokenizer](https://github.com/Boostorg/Tokenizer) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/conan-public/Boost.Tokenizer%3Abincrafters).

## For Users: Use this package

### Basic setup

    $ conan install Boost.Tokenizer/1.64.0@bincrafters/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Boost.Tokenizer/1.64.0@bincrafters/stable

    [generators]
    txt

Complete the installation of requirements for your project running:</small></span>

    $ mkdir build && cd build && conan install ..
	
Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they shoudl not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This is a header only library, so nothing needs to be built.

## Package 

    $ conan create bincrafters/testing
	
## Add Remote and Associate package with it

	$ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"
	$ conan remote add_ref Boost.Tokenizer/1.64.0@bincrafters/testing bincrafters

## Upload

    $ conan upload Boost.Tokenizer/1.64.0@bincrafters/testing --all

### License
[Boost](LICENSE)
