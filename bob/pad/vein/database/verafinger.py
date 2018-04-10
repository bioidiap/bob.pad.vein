#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bob.pad.base.database import PadFile, PadDatabase


class File(PadFile):
  """A high level implementation of the File class for the Verafinger
  database.
  """

  def __init__(self, f):
    self.f = f
    super(File, self).__init__(client_id=f.finger.unique_name,
        path=f.path, attack_type=None if f.source == 'bf' else 'attack',
        file_id=f.id)


class Database(PadDatabase):
  """A high level implementation of the Database class for the Verafinger
  database.
  """

  def __init__(self, **kwargs):
    """
    Parameters
    ----------

    kwargs
        The arguments of the :py:class:`bob.bio.base.database.BioDatabase`
        base class constructor.
    """

    from bob.db.verafinger import PADDatabase as LowLevelDatabase
    self.db = LowLevelDatabase()
    super(Database, self).__init__(name='verafinger', **kwargs)


  def objects(self, groups=None, protocol=None, purposes=None, model_ids=None,
      **kwargs):
      """
      This function returns lists of ReplayPadFile objects, which fulfill the
      given restrictions.

      Parameters
      ----------
      groups : :obj:`str` or [:obj:`str`]
          The groups of which the clients should be returned.
          Usually, groups are one or more elements of
          ('train', 'dev', 'eval')

      protocol : str
          The protocol for which the clients should be retrieved.
          The protocol is dependent on your database.
          If you do not have protocols defined, just ignore this field.

      purposes : :obj:`str` or [:obj:`str`]
          The purposes for which File objects should be retrieved.
          Usually it is either 'real' or 'attack'.

      model_ids
          This parameter is not supported in PAD databases yet
      **kwargs

      Returns
      -------
      files : [File]
          A list of File objects.
      """

      files = self.db.objects(protocol=protocol, groups=groups,
          purposes=purposes, **kwargs)
      return [File(f) for f in files]
