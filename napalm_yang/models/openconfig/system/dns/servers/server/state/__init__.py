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


class state(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/dns/servers/server/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for each DNS resolver
  """
    __slots__ = ("_path_helper", "_extmethods", "__address", "__port")

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__address = YANGDynClass(
            base=[
                RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?"
                    },
                ),
                RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?"
                    },
                ),
            ],
            is_leaf=True,
            yang_name="address",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="inet:ip-address",
            is_config=False,
        )
        self.__port = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
                ),
                restriction_dict={"range": ["0..65535"]},
            ),
            default=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
            )(
                53
            ),
            is_leaf=True,
            yang_name="port",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="inet:port-number",
            is_config=False,
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
            return ["system", "dns", "servers", "server", "state"]

    def _get_address(self):
        """
    Getter method for address, mapped from YANG variable /system/dns/servers/server/state/address (inet:ip-address)

    YANG Description: [adapted from IETF system model RFC 7317]

The address of the DNS server, can be either IPv4
or IPv6.
    """
        return self.__address

    def _set_address(self, v, load=False):
        """
    Setter method for address, mapped from YANG variable /system/dns/servers/server/state/address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: [adapted from IETF system model RFC 7317]

The address of the DNS server, can be either IPv4
or IPv6.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=[
                    RestrictedClassType(
                        base_type=six.text_type,
                        restriction_dict={
                            "pattern": "(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?"
                        },
                    ),
                    RestrictedClassType(
                        base_type=six.text_type,
                        restriction_dict={
                            "pattern": "((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?"
                        },
                    ),
                ],
                is_leaf=True,
                yang_name="address",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/system",
                defining_module="openconfig-system",
                yang_type="inet:ip-address",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """address must be of a type compatible with inet:ip-address""",
                    "defined-type": "inet:ip-address",
                    "generated-type": """YANGDynClass(base=[RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='inet:ip-address', is_config=False)""",
                }
            )

        self.__address = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_address(self):
        self.__address = YANGDynClass(
            base=[
                RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?"
                    },
                ),
                RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?"
                    },
                ),
            ],
            is_leaf=True,
            yang_name="address",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="inet:ip-address",
            is_config=False,
        )

    def _get_port(self):
        """
    Getter method for port, mapped from YANG variable /system/dns/servers/server/state/port (inet:port-number)

    YANG Description: [adapted from IETF system model RFC 7317]

The port number of the DNS server.
    """
        return self.__port

    def _set_port(self, v, load=False):
        """
    Setter method for port, mapped from YANG variable /system/dns/servers/server/state/port (inet:port-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.

    YANG Description: [adapted from IETF system model RFC 7317]

The port number of the DNS server.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=int,
                        restriction_dict={"range": ["0..65535"]},
                        int_size=16,
                    ),
                    restriction_dict={"range": ["0..65535"]},
                ),
                default=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
                )(
                    53
                ),
                is_leaf=True,
                yang_name="port",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/system",
                defining_module="openconfig-system",
                yang_type="inet:port-number",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """port must be of a type compatible with inet:port-number""",
                    "defined-type": "inet:port-number",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': ['0..65535']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(53), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='inet:port-number', is_config=False)""",
                }
            )

        self.__port = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_port(self):
        self.__port = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
                ),
                restriction_dict={"range": ["0..65535"]},
            ),
            default=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
            )(
                53
            ),
            is_leaf=True,
            yang_name="port",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="inet:port-number",
            is_config=False,
        )

    address = __builtin__.property(_get_address)
    port = __builtin__.property(_get_port)

    _pyangbind_elements = OrderedDict([("address", address), ("port", port)])
