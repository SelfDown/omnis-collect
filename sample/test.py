# -*- coding: utf-8 -*-

from ldap3 import HASHED_SALTED_SHA
from ldap3.utils.hashed import hashed
hashed_password = hashed(HASHED_SALTED_SHA, str("123456"))
print hashed_password
