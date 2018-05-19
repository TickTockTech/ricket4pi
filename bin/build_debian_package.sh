#!/bin/bash

package_name=ricket4pi
package_version="0.0.1-1"

original_path=$(pwd)
script_name=$0
script_path=$(dirname "$0")
base_folder="$( cd "$(dirname "$0")/../" ; pwd -P )"
project_folder=ricket4pi

echo "Changing to directory: $(script_path)."
cd $(script_path)

echo "Creating folder structure."
mkdir -p debian_package/opt/$(project_folder)
mkdir -p debian_package/usr/local/share/supervisor/conf.d/

echo "Creating scripts."
cp $(base_folder)/src/*.py debian_package/opt/$(project_folder)/src/
cp -r $(base_folder)/www/*.* debian_package/opt/$(project_folder)/www/
cp ricket.conf debian_package/usr/local/share/supervisor/conf.d/

echo "Building package."
dpkg-deb --build debian_package

mv debian_package.deb $(package_name)_$(package_version)_all.deb

echo "Changing back to directory: $(original_path)."
cd $(original_path)

echo ""
echo "Package name: $(package_name)_$(package_version)_all.deb"
echo "Package available in: $(script_path)"
