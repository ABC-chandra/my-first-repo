#!/bin/bash
echo "#########################################################################"
echo "#########################################################################"
echo "STANDBY  BACKUP"
echo "#########################################################################"

email_list='chandrasekhar@venusgeo.com'
export BACKUP_PATH="/IMEIDB_BACKUP/backup/"
date1=$(date +"%d%m%Y")
date=$(date +"%d%m%Y01")
echo "###############"backup validation ###########"
backupFilename="imeidb_$date.bak"
ls -lrt $BACKUP_PATH
if [ ! -e  $BACKUP_PATH$backupFilename ]
then
su - enterprisedb << EOF
pwd
whoami
cd bin
export PGPASSWORD="edbpass123"
nohup ./pg_dump -Fc IMEIDB > $BACKUP_PATH$backupFilename &
echo -e "Hi Team,\n\n IMEIDB database daily back successfully on $date1 \n\nRegards,\nDBA Team.\n" | mail -s "ALARM:IMEIDB database daily backup " -- $email_list
EOF
fi
