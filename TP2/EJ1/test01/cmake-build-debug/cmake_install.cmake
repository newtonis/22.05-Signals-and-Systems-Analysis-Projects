<<<<<<< HEAD
# Install script for directory: C:/Users/newtonis/Documents/GitHub/INFORMES_ASSD/TP2/EJ1/test01
=======
# Install script for directory: C:/Users/newto/INFORMES_ASSD/TP2/EJ1/test01
>>>>>>> de3a750c4a435e36ffce5a905e64b97a6fae6068

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "C:/Program Files (x86)/test01")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
<<<<<<< HEAD
file(WRITE "C:/Users/newtonis/Documents/GitHub/INFORMES_ASSD/TP2/EJ1/test01/cmake-build-debug/${CMAKE_INSTALL_MANIFEST}"
=======
file(WRITE "C:/Users/newto/INFORMES_ASSD/TP2/EJ1/test01/cmake-build-debug/${CMAKE_INSTALL_MANIFEST}"
>>>>>>> de3a750c4a435e36ffce5a905e64b97a6fae6068
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
