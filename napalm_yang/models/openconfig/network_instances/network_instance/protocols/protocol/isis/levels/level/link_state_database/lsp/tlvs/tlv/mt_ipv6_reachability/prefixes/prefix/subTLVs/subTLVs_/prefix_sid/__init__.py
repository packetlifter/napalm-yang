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

from . import sid


class prefix_sid(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv6-reachability/prefixes/prefix/subTLVs/subTLVs/prefix-sid. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines segment routing extensions for prefixes.
  """
    __slots__ = ("_path_helper", "_extmethods", "__sid")

    _yang_name = "prefix-sid"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__sid = YANGDynClass(
            base=YANGListType(
                False,
                sid.sid,
                yang_name="sid",
                parent=self,
                is_container="list",
                user_ordered=False,
                path_helper=self._path_helper,
                yang_keys="False",
                extensions=None,
            ),
            is_container="list",
            yang_name="sid",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="list",
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
                "levels",
                "level",
                "link-state-database",
                "lsp",
                "tlvs",
                "tlv",
                "mt-ipv6-reachability",
                "prefixes",
                "prefix",
                "subTLVs",
                "subTLVs",
                "prefix-sid",
            ]

    def _get_sid(self):
        """
    Getter method for sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv6_reachability/prefixes/prefix/subTLVs/subTLVs/prefix_sid/sid (list)

    YANG Description: Prefix Segment-ID list. IGP-Prefix Segment is an IGP segment attached
to an IGP prefix. An IGP-Prefix Segment is global (unless explicitly
advertised otherwise) within the SR/IGP domain.
    """
        return self.__sid

    def _set_sid(self, v, load=False):
        """
    Setter method for sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv6_reachability/prefixes/prefix/subTLVs/subTLVs/prefix_sid/sid (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid() directly.

    YANG Description: Prefix Segment-ID list. IGP-Prefix Segment is an IGP segment attached
to an IGP prefix. An IGP-Prefix Segment is global (unless explicitly
advertised otherwise) within the SR/IGP domain.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=YANGListType(
                    False,
                    sid.sid,
                    yang_name="sid",
                    parent=self,
                    is_container="list",
                    user_ordered=False,
                    path_helper=self._path_helper,
                    yang_keys="False",
                    extensions=None,
                ),
                is_container="list",
                yang_name="sid",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="list",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """sid must be of a type compatible with list""",
                    "defined-type": "list",
                    "generated-type": """YANGDynClass(base=YANGListType(False,sid.sid, yang_name="sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
                }
            )

        self.__sid = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_sid(self):
        self.__sid = YANGDynClass(
            base=YANGListType(
                False,
                sid.sid,
                yang_name="sid",
                parent=self,
                is_container="list",
                user_ordered=False,
                path_helper=self._path_helper,
                yang_keys="False",
                extensions=None,
            ),
            is_container="list",
            yang_name="sid",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="list",
            is_config=False,
        )

    sid = __builtin__.property(_get_sid)

    _pyangbind_elements = OrderedDict([("sid", sid)])


from . import sid


class prefix_sid(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv6-reachability/prefixes/prefix/subTLVs/subTLVs/prefix-sid. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines segment routing extensions for prefixes.
  """
    __slots__ = ("_path_helper", "_extmethods", "__sid")

    _yang_name = "prefix-sid"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__sid = YANGDynClass(
            base=YANGListType(
                False,
                sid.sid,
                yang_name="sid",
                parent=self,
                is_container="list",
                user_ordered=False,
                path_helper=self._path_helper,
                yang_keys="False",
                extensions=None,
            ),
            is_container="list",
            yang_name="sid",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="list",
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
                "levels",
                "level",
                "link-state-database",
                "lsp",
                "tlvs",
                "tlv",
                "mt-ipv6-reachability",
                "prefixes",
                "prefix",
                "subTLVs",
                "subTLVs",
                "prefix-sid",
            ]

    def _get_sid(self):
        """
    Getter method for sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv6_reachability/prefixes/prefix/subTLVs/subTLVs/prefix_sid/sid (list)

    YANG Description: Prefix Segment-ID list. IGP-Prefix Segment is an IGP segment attached
to an IGP prefix. An IGP-Prefix Segment is global (unless explicitly
advertised otherwise) within the SR/IGP domain.
    """
        return self.__sid

    def _set_sid(self, v, load=False):
        """
    Setter method for sid, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv6_reachability/prefixes/prefix/subTLVs/subTLVs/prefix_sid/sid (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid() directly.

    YANG Description: Prefix Segment-ID list. IGP-Prefix Segment is an IGP segment attached
to an IGP prefix. An IGP-Prefix Segment is global (unless explicitly
advertised otherwise) within the SR/IGP domain.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=YANGListType(
                    False,
                    sid.sid,
                    yang_name="sid",
                    parent=self,
                    is_container="list",
                    user_ordered=False,
                    path_helper=self._path_helper,
                    yang_keys="False",
                    extensions=None,
                ),
                is_container="list",
                yang_name="sid",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="list",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """sid must be of a type compatible with list""",
                    "defined-type": "list",
                    "generated-type": """YANGDynClass(base=YANGListType(False,sid.sid, yang_name="sid", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="sid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='list', is_config=False)""",
                }
            )

        self.__sid = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_sid(self):
        self.__sid = YANGDynClass(
            base=YANGListType(
                False,
                sid.sid,
                yang_name="sid",
                parent=self,
                is_container="list",
                user_ordered=False,
                path_helper=self._path_helper,
                yang_keys="False",
                extensions=None,
            ),
            is_container="list",
            yang_name="sid",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="list",
            is_config=False,
        )

    sid = __builtin__.property(_get_sid)

    _pyangbind_elements = OrderedDict([("sid", sid)])
