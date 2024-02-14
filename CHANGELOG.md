## 0.4.1 (2024-02-14)

### Fix

- dependencies versions
- moved commitizen in the dev dependencies
- updated dependencies
- updated django-naomi version

## 0.4.0 (2024-02-13)

### Feat

- Updated templates, using django-filters instead of the previous ones.
- Updated the demo project to work with poetry.

### Fix

- bumpversion to 0.3.6
- changed dependency for django-naomi to >= 0.7
- changed dependency for django-naomi to >= 0.7
- updated the version for django-celery-beat

## 0.3.3 (2022-03-19)

### Fix

- **kb**: no db
- **kb**: no db
- **kb**: no db

## 0.3.2 (2021-11-21)

## 0.3.1 (2021-11-19)

## 0.3.0 (2021-10-18)

### Feat

- **emails**: Do not auto-reply on auto-replies and add auto-reply header for auto-replies and fix headers propagation for our email messages
- **forms**: Ability to provide custom public ticket form

### Fix

- strip extraneous whitespace characters that are returned in the Message-ID and In-Reply-To fields from some email providers
- **emails**: Avoid 'value too long for type character varying(200) ' error when incoming message has too long subject
- **email**: Add ability to attach full first email text to avoid losing forwards, and to save .eml files for any incoming mesages, plus fix tests and some minor bugs
- prepend file attachments with 'part-%i_' to prevent name collisions when an email has attachments with the same filename

## 0.3.0b3 (2021-01-04)

### Fix

- **tests**: Run tests without the socks components and document their usage

## 0.3.0b1 (2020-11-12)

### Fix

- **migrations**: Rename the migration back due to InconsistentMigrationHistory otherwise
- **migrations**: Fix the 0034 migration for Postgres

## 0.2.22 (2020-07-30)

### Fix

- **public**: Fix the public ticket creation by passing user or None to the form.save() method
- **demo**: Update demo's INSTALLED_APPS to avoid it crashing after pinax-team library was introduced #820
- **makefile**: Avoid --user flag usage if previous PIP run has failed - which makes no difference for virtualenv anyway

## 0.2.21 (2020-04-15)

## 0.2.20 (2020-04-15)

## 0.2.19 (2019-12-24)

## 0.2.18 (2019-12-17)

## 0.2.17 (2019-08-27)

## 0.2.16 (2019-05-25)

## 0.2.15 (2019-03-09)

## 0.2.14 (2019-02-15)

## 0.2.13 (2019-01-17)

## 0.2.12 (2019-01-02)

## 0.2.11 (2018-12-31)

## 0.2.10 (2018-09-01)

## 0.2.9 (2018-07-18)

## 0.2.8 (2018-07-03)

## 0.2.7 (2018-03-04)

## 0.2.6 (2017-12-28)

## 0.2.5 (2017-12-28)

## 0.2.4 (2017-12-18)

## 0.2.3 (2017-12-09)

## 0.2.1 (2017-09-14)

## 0.2.0 (2017-09-14)

## 0.1.18 (2016-10-28)

## 0.1.17 (2015-12-22)

## 0.1.16 (2015-02-19)

## 0.1.15 (2015-01-15)
