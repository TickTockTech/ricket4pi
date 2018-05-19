#!/bin/bash

PACKAGE_NAME=ricket4pi
PACKAGE_VERSION="0.0.1-1"

ORIGINAL_PATH=$(pwd -P)
SCRIPT_NAME=$0
SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"
BASE_FOLDER="$( cd "$(dirname "$0")/../" ; pwd -P )"
PROJECT_NAME=ricket4pi

echo "Changing to directory: $SCRIPT_PATH."
cd $SCRIPT_PATH

echo "Creating folder structure."
mkdir -p debian_package/opt/$PROJECT_NAME/www
mkdir -p debian_package/opt/$PROJECT_NAME/src
mkdir -p debian_package/etc/supervisor/conf.d
mkdir -p debian_package/DEBIAN/

echo "Creating scripts."
cp $BASE_FOLDER/src/*.py debian_package/opt/$PROJECT_NAME/src/
cp -r $BASE_FOLDER/www/*.* debian_package/opt/$PROJECT_NAME/www/
cp $BASE_FOLDER/scripts/ricket.conf debian_package/etc/supervisor/conf.d/
cp $BASE_FOLDER/scripts/debian_control debian_package/DEBIAN/control
cp $BASE_FOLDER/scripts/postinst debian_package/DEBIAN/
cp $BASE_FOLDER/scripts/postrm debian_package/DEBIAN/

echo "Fixing permissions."
chmod 755 debian_package/DEBIAN/postinst
chmod 755 debian_package/DEBIAN/postrm

echo "Building package."
dpkg-deb --build debian_package

echo "Renaming to ${PACKAGE_NAME}_${PACKAGE_VERSION}_all.deb"
mv debian_package.deb ${PACKAGE_NAME}_${PACKAGE_VERSION}_all.deb

echo "Changing back to directory: $ORIGINAL_PATH."
cd $ORIGINAL_PATH

echo "Tidying up"
rm -rf $BASE_FOLDER/bin/debian_package

echo ""
echo "Package name: ${PACKAGE_NAME}_${PACKAGE_VERSION}_all.deb"
echo "Package available in: $SCRIPT_PATH"
echo ""
echo "To install > sudo dpkg -i ${PACKAGE_NAME}_${PACKAGE_VERSION}_all.deb"
echo ""
