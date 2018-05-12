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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/timers/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS interface timers.
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__csnp_interval", "__lsp_pacing_interval"
    )

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__csnp_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
            ),
            is_leaf=True,
            yang_name="csnp-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint16",
            is_config=False,
        )
        self.__lsp_pacing_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="lsp-pacing-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
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
            return [
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "interfaces",
                "interface",
                "timers",
                "state",
            ]

    def _get_csnp_interval(self):
        """
    Getter method for csnp_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/timers/state/csnp_interval (uint16)

    YANG Description: The interval, specified in seconds, at which periodic CSNP packets
should be transmitted by the local IS.
    """
        return self.__csnp_interval

    def _set_csnp_interval(self, v, load=False):
        """
    Setter method for csnp_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/timers/state/csnp_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_csnp_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_csnp_interval() directly.

    YANG Description: The interval, specified in seconds, at which periodic CSNP packets
should be transmitted by the local IS.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
                ),
                is_leaf=True,
                yang_name="csnp-interval",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint16",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """csnp_interval must be of a type compatible with uint16""",
                    "defined-type": "uint16",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="csnp-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
                }
            )

        self.__csnp_interval = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_csnp_interval(self):
        self.__csnp_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
            ),
            is_leaf=True,
            yang_name="csnp-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint16",
            is_config=False,
        )

    def _get_lsp_pacing_interval(self):
        """
    Getter method for lsp_pacing_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/timers/state/lsp_pacing_interval (uint64)

    YANG Description: The interval interval in milliseconds between the
detection of topology change and when the SPF algorithm runs.
    """
        return self.__lsp_pacing_interval

    def _set_lsp_pacing_interval(self, v, load=False):
        """
    Setter method for lsp_pacing_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/timers/state/lsp_pacing_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_pacing_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_pacing_interval() directly.

    YANG Description: The interval interval in milliseconds between the
detection of topology change and when the SPF algorithm runs.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..18446744073709551615"]},
                    int_size=64,
                ),
                is_leaf=True,
                yang_name="lsp-pacing-interval",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint64",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """lsp_pacing_interval must be of a type compatible with uint64""",
                    "defined-type": "uint64",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="lsp-pacing-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
                }
            )

        self.__lsp_pacing_interval = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_lsp_pacing_interval(self):
        self.__lsp_pacing_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="lsp-pacing-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
            is_config=False,
        )

    csnp_interval = __builtin__.property(_get_csnp_interval)
    lsp_pacing_interval = __builtin__.property(_get_lsp_pacing_interval)

    _pyangbind_elements = OrderedDict(
        [("csnp_interval", csnp_interval), ("lsp_pacing_interval", lsp_pacing_interval)]
    )


class state(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/timers/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines state information for ISIS interface timers.
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__csnp_interval", "__lsp_pacing_interval"
    )

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__csnp_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
            ),
            is_leaf=True,
            yang_name="csnp-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint16",
            is_config=False,
        )
        self.__lsp_pacing_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="lsp-pacing-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
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
            return [
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "interfaces",
                "interface",
                "timers",
                "state",
            ]

    def _get_csnp_interval(self):
        """
    Getter method for csnp_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/timers/state/csnp_interval (uint16)

    YANG Description: The interval, specified in seconds, at which periodic CSNP packets
should be transmitted by the local IS.
    """
        return self.__csnp_interval

    def _set_csnp_interval(self, v, load=False):
        """
    Setter method for csnp_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/timers/state/csnp_interval (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_csnp_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_csnp_interval() directly.

    YANG Description: The interval, specified in seconds, at which periodic CSNP packets
should be transmitted by the local IS.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
                ),
                is_leaf=True,
                yang_name="csnp-interval",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint16",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """csnp_interval must be of a type compatible with uint16""",
                    "defined-type": "uint16",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="csnp-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint16', is_config=False)""",
                }
            )

        self.__csnp_interval = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_csnp_interval(self):
        self.__csnp_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..65535"]}, int_size=16
            ),
            is_leaf=True,
            yang_name="csnp-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint16",
            is_config=False,
        )

    def _get_lsp_pacing_interval(self):
        """
    Getter method for lsp_pacing_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/timers/state/lsp_pacing_interval (uint64)

    YANG Description: The interval interval in milliseconds between the
detection of topology change and when the SPF algorithm runs.
    """
        return self.__lsp_pacing_interval

    def _set_lsp_pacing_interval(self, v, load=False):
        """
    Setter method for lsp_pacing_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/timers/state/lsp_pacing_interval (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_pacing_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_pacing_interval() directly.

    YANG Description: The interval interval in milliseconds between the
detection of topology change and when the SPF algorithm runs.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..18446744073709551615"]},
                    int_size=64,
                ),
                is_leaf=True,
                yang_name="lsp-pacing-interval",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint64",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """lsp_pacing_interval must be of a type compatible with uint64""",
                    "defined-type": "uint64",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="lsp-pacing-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
                }
            )

        self.__lsp_pacing_interval = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_lsp_pacing_interval(self):
        self.__lsp_pacing_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="lsp-pacing-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
            is_config=False,
        )

    csnp_interval = __builtin__.property(_get_csnp_interval)
    lsp_pacing_interval = __builtin__.property(_get_lsp_pacing_interval)

    _pyangbind_elements = OrderedDict(
        [("csnp_interval", csnp_interval), ("lsp_pacing_interval", lsp_pacing_interval)]
    )
