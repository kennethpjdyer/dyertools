############
DyerTools
############

Collection of tools for professional writers on Linux.  It is open source under a BSD license and runs on Python 3.


*************
Installation
*************

To install DyerTools, run ``setup.py``:

   $ python3 setup.py install 

********
Usage
********

The main utility for DyerTools is called ``dyer``.  


Notifications
================

The ``notify`` command is used to feed information into the notification daemon through the ``notify-send`` utility.  It requires that you install the ``libnotify`` library.

The purpose of notification subcommands is to provide a convenient interface for the crontab.  Users are expected to add cronjobs for the information they want to see at the specific intervals in which they would like the notifications to occur.

Tasks
-------

The ``tasks`` notifications subcommand retrieves project-level counts from Task Warrior then reports the pending tasks to the notification daemon.  This subcommand is useful if you are a user of Task Warrior and would like periodic reminders of pending tasks.



