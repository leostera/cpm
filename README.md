#cpm
####A Package Manager for C/C++

## Draft
So don't expect too much too soon, I'm trying to get something really simple working because I'm just fed up with manual dependency handling and having to upload tons of 3rd party headers and stuff to a projects repo.

## Proposed workflow
Create a `package.toml` [TOML](https://github.com/mojombo/toml) file with the following syntax: 

```toml
title="Tome"
description="A dynamic tile-based file-driven RPG Engine"

[author]
name="Leandro Ostera"
email="leostera@gmail.com"

[dependencies]
  [yaml-cpp]
  version="~1.x"
  source="hg+https://code.google.com/p/yaml-cpp/"
  build_script="cmake" # mkdir build; cd build; cmake ..; make -j

  [boost-headers]
  source="git+https://github.com/leostera/boost-headers.git"

  [sdl]
  source="http://www.libsdl.org/release/SDL-1.2.15.tar.gz"
  build_script="autotools" # ./configure && make -j
```

Upon calling `cpm install` It will create a `cpm_modules` folder at the same level of your `package.toml` file and inside it it will create a structure like the following:

```
package.toml
cpm_modules
  + sdl
    + 1.2.15
      + lib  # compiled libraries ready to be linked
      + bin  # compiled binaries if resulting from the build process
      + include  # the includes
      + ...  # other files and folders from the source
  + boost-headers
    + 1.52.0
      + include  # the includes
  + yaml-cpp
    + 1.5
      + lib  # compiled libraries
      + bin  # compiled binaries
      + include  # the includes
      + ...  # other files and folders from the source
```

For each dependency it will try to detect the building tool being used (autotools, cmake, plain-old Makefile, xcodebuild, etc) unless the dependency package.toml file defines one or more build processes for the same or different platforms. In that case, `cpm` will try to find the build tools until it finds one of the listed or output an error message asking the user to install at least one of them.

To handle recursive dependency management inside a given dependency folder (say yaml-cpp/1.5) a `cpm_modules` folder will be created if and only if the required dependency is not already in the top-level `cpm_modules` folder. E.g. `yaml-cpp` depends on `boost-headers` and the latter is not included in the dependencies list of your project. Then the generated folder structure will be:

```
package.toml
cpm_modules
  + yaml-cpp
    + 1.5
      + lib
      + bin
      + include 
      + ...  # other files and folders from the source
      + cpm_modules
        + boost-headers
          + 1.52.0
            + include  # finally, the boost headers
```

Otherwise the `boost-headers` folder we just saw would be a symlink to the top level `cpm_modules/boost-headers` folder. 

In any case, each `lib`, `bin` and `include` folder from each dependency will be symlinked into a top level `lib`, `bin` and `include` folder (thou configurable from the `package.toml` file) to assure compatibility with current build processes.

## License
MIT Licensed, check the LICENSE file for details.