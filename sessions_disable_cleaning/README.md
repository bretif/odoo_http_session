# Disable sessions cleaning

Purpose of this script is to disable sessions cleaning performed by Odoo.
By default Odoo list all sessions files in `data_dir/sessions` and delete all files older than 1 week

## When use this module?

If you store your session on NFS filesystem you should use this module as listing a directory on NFS is really slow and you will experience perfoamnce issues.

## WARNING

However when this module is installed **you must manage session cleaning by yourself**, for instance by cleaning session dir directly in your OS
