#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Thu May 24 10:41:42 CEST 2012

from nose.plugins.skip import SkipTest

import bob.pad.base
from bob.bio.base.test.utils import db_available
from bob.bio.base.test.test_database_implementations import check_database


@db_available('verafinger')
def test_verafinger():
    module = bob.bio.base.load_resource('verafinger', 'config',
        preferred_package='bob.pad.vein')
    try:
        check_database(module.database, protocol='full', groups=('dev',
          'eval'))
    except IOError as e:
        raise SkipTest(
            "The database could not queried; probably the db.sql3 file is missing. Here is the error: '%s'" % e)
