# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
    import builtins as __builtin__

    long = int
elif six.PY2:
    import __builtin__

from . import server


class servers(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/aaa/server-groups/server-group/servers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container the list of servers
  """
    __slots__ = ("_path_helper", "_extmethods", "__server")

    _yang_name = "servers"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__server = YANGDynClass(
            base=YANGListType(
                "address",
                server.server,
                yang_name="server",
                parent=self,
                is_container="list",
                user_ordered=False,
                path_helper=self._path_helper,
                yang_keys="address",
                extensions=None,
            ),
            is_container="list",
            yang_name="server",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="list",
            is_config=True,
        )

        load = kwargs.pop("load", None)
        if args:
            if len(args) > 1:
                raise TypeError("cannot create a YANG container with >1 argument")
            all_attr = True
            for e in self._pyangbind_elements:
                if not hasattr(args[0], e):
                    all_attr = False
                    break
            if not all_attr:
                raise ValueError("Supplied object did not have the correct attributes")
            for e in self._pyangbind_elements:
                nobj = getattr(args[0], e)
                if nobj._changed() is False:
                    continue
                setmethod = getattr(self, "_set_%s" % e)
                if load is None:
                    setmethod(getattr(args[0], e))
                else:
                    setmethod(getattr(args[0], e), load=load)

    def _path(self):
        if hasattr(self, "_parent"):
            return self._parent._path() + [self._yang_name]
        else:
            return ["system", "aaa", "server-groups", "server-group", "servers"]

    def _get_server(self):
        """
    Getter method for server, mapped from YANG variable /system/aaa/server_groups/server_group/servers/server (list)

    YANG Description: List of AAA servers
    """
        return self.__server

    def _set_server(self, v, load=False):
        """
    Setter method for server, mapped from YANG variable /system/aaa/server_groups/server_group/servers/server (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_server is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_server() directly.

    YANG Description: List of AAA servers
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=YANGListType(
                    "address",
                    server.server,
                    yang_name="server",
                    parent=self,
                    is_container="list",
                    user_ordered=False,
                    path_helper=self._path_helper,
                    yang_keys="address",
                    extensions=None,
                ),
                is_container="list",
                yang_name="server",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/system",
                defining_module="openconfig-system",
                yang_type="list",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """server must be of a type compatible with list""",
                    "defined-type": "list",
                    "generated-type": """YANGDynClass(base=YANGListType("address",server.server, yang_name="server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='address', extensions=None), is_container='list', yang_name="server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='list', is_config=True)""",
                }
            )

        self.__server = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_server(self):
        self.__server = YANGDynClass(
            base=YANGListType(
                "address",
                server.server,
                yang_name="server",
                parent=self,
                is_container="list",
                user_ordered=False,
                path_helper=self._path_helper,
                yang_keys="address",
                extensions=None,
            ),
            is_container="list",
            yang_name="server",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="list",
            is_config=True,
        )

    server = __builtin__.property(_get_server, _set_server)

    _pyangbind_elements = OrderedDict([("server", server)])
