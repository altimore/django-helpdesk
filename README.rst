django-helpdesk - A Django powered ticket tracker for small businesses.
=======================================================================

.. image:: https://travis-ci.org/django-helpdesk/django-helpdesk.png?branch=develop
    :target: https://travis-ci.org/django-helpdesk/django-helpdesk

.. image:: https://codecov.io/gh/django-helpdesk/django-helpdesk/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/django-helpdesk/django-helpdesk

Copyright 2009-2021 Ross Poulton and django-helpdesk contributors. All Rights Reserved.
See LICENSE for details.

django-helpdesk was formerly known as Jutda Helpdesk, named after the
company which originally created it. As of January 2011 the name has been
changed to reflect what it really is: a Django-powered ticket tracker with
contributors reaching far beyond Jutda.

Complete documentation is available in the docs/ directory,
or online at http://django-helpdesk.readthedocs.org/.

You can see a demo installation at http://django-helpdesk-demo.herokuapp.com/,
or run a demo locally in just a couple steps!

Demo Quickstart
---------------

`django-helpdesk` includes a basic demo Django project so that you may easily
get started with testing or developing `django-helpdesk`. The demo project
resides in the `demo_helpdesk/` top-level folder.
``
    git clone https://github.com/altimore/django-helpdesk.git
    cd django-helpdesk
    poetry run demo_helpdesk/manage.py migrate
    poetry run demo_helpdesk/manage.py createsuperuser
    poetry run demo_helpdesk/manage.py runserver
``
then pointing your web browser at `localhost:8080`.

**NOTE REGARDING SQLITE AND SEARCHING:**
The demo project uses `sqlite` as its database. Sqlite does not allow
case-insensitive searches and so the search function may not work as
effectively as it would on other database such as PostgreSQL or MySQL
that does support case-insensitive searches.
For more information, see this note_ in the Django documentation.

When you try to do a keyword search using `sqlite`, a message will be displayed
to alert you to this shortcoming. There is no way around it, sorry.

Installation
------------

    poetry add git+https://github.com/altimore/django-helpdesk.git#stable

Testing
-------
``
    git clone https://github.com/altimore/django-helpdesk.git
    cd django-helpdesk
    poetry run demo_helpdesk/manage.py test
``
Contributing
------------

We're happy to include any type of contribution! This can be:

* back-end python/django code development
* front-end web development (HTML/Javascript, especially jQuery)
* language translations
* writing improved documentation and demos

For more information on contributing, please see the `CONTRIBUTING.rst` file.


Licensing
---------

django-helpdesk is licensed under terms of the BSD 3-clause license.
See the `LICENSE` file for full licensing terms.

Note that django-helpdesk is distributed with 3rd party products which
have their own licenses. See LICENSE.3RDPARTY for license terms for
included packages.

.. _note: http://docs.djangoproject.com/en/dev/ref/databases/#sqlite-string-matching
