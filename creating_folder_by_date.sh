#!/bin/bash
sourceFolder="volume1/gr030vpl/Дела в обработке/ДЕМО (МСП)/ПТК_НВП_109"
wFolder="ТЕКУЩАЯ ВЫПЛАТА"
YMFolder=`date +%Y.%m`
YMDFolder=`date +%Y.%m.%d`
mkdir -p /"$sourceFolder"/"$wFolder"/"$YMFolder"/"$YMDFolder"

