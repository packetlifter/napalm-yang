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


class config(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/route-preference/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines route preference configuration.
  """
    __slots__ = (
        "_path_helper",
        "_extmethods",
        "__external_route_preference",
        "__internal_route_preference",
    )

    _yang_name = "config"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__external_route_preference = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..max"]},
            ),
            is_leaf=True,
            yang_name="external-route-preference",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
        )
        self.__internal_route_preference = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..max"]},
            ),
            is_leaf=True,
            yang_name="internal-route-preference",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
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
            return [
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "levels",
                "level",
                "route-preference",
                "config",
            ]

    def _get_external_route_preference(self):
        """
    Getter method for external_route_preference, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/route_preference/config/external_route_preference (uint8)

    YANG Description: Administrative Distance(preference) for external ISIS routes.
    """
        return self.__external_route_preference

    def _set_external_route_preference(self, v, load=False):
        """
    Setter method for external_route_preference, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/route_preference/config/external_route_preference (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_route_preference is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_route_preference() directly.

    YANG Description: Administrative Distance(preference) for external ISIS routes.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=int,
                        restriction_dict={"range": ["0..255"]},
                        int_size=8,
                    ),
                    restriction_dict={"range": ["1..max"]},
                ),
                is_leaf=True,
                yang_name="external-route-preference",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """external_route_preference must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..max']}), is_leaf=True, yang_name="external-route-preference", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)""",
                }
            )

        self.__external_route_preference = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_external_route_preference(self):
        self.__external_route_preference = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..max"]},
            ),
            is_leaf=True,
            yang_name="external-route-preference",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
        )

    def _get_internal_route_preference(self):
        """
    Getter method for internal_route_preference, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/route_preference/config/internal_route_preference (uint8)

    YANG Description: Administrative Distance(preference) for internal ISIS routes.
    """
        return self.__internal_route_preference

    def _set_internal_route_preference(self, v, load=False):
        """
    Setter method for internal_route_preference, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/route_preference/config/internal_route_preference (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_internal_route_preference is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_internal_route_preference() directly.

    YANG Description: Administrative Distance(preference) for internal ISIS routes.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=int,
                        restriction_dict={"range": ["0..255"]},
                        int_size=8,
                    ),
                    restriction_dict={"range": ["1..max"]},
                ),
                is_leaf=True,
                yang_name="internal-route-preference",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """internal_route_preference must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..max']}), is_leaf=True, yang_name="internal-route-preference", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)""",
                }
            )

        self.__internal_route_preference = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_internal_route_preference(self):
        self.__internal_route_preference = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..max"]},
            ),
            is_leaf=True,
            yang_name="internal-route-preference",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
        )

    external_route_preference = __builtin__.property(
        _get_external_route_preference, _set_external_route_preference
    )
    internal_route_preference = __builtin__.property(
        _get_internal_route_preference, _set_internal_route_preference
    )

    _pyangbind_elements = OrderedDict(
        [
            ("external_route_preference", external_route_preference),
            ("internal_route_preference", internal_route_preference),
        ]
    )


class config(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/route-preference/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines route preference configuration.
  """
    __slots__ = (
        "_path_helper",
        "_extmethods",
        "__external_route_preference",
        "__internal_route_preference",
    )

    _yang_name = "config"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__external_route_preference = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..max"]},
            ),
            is_leaf=True,
            yang_name="external-route-preference",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
        )
        self.__internal_route_preference = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..max"]},
            ),
            is_leaf=True,
            yang_name="internal-route-preference",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
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
            return [
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "levels",
                "level",
                "route-preference",
                "config",
            ]

    def _get_external_route_preference(self):
        """
    Getter method for external_route_preference, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/route_preference/config/external_route_preference (uint8)

    YANG Description: Administrative Distance(preference) for external ISIS routes.
    """
        return self.__external_route_preference

    def _set_external_route_preference(self, v, load=False):
        """
    Setter method for external_route_preference, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/route_preference/config/external_route_preference (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_route_preference is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_route_preference() directly.

    YANG Description: Administrative Distance(preference) for external ISIS routes.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=int,
                        restriction_dict={"range": ["0..255"]},
                        int_size=8,
                    ),
                    restriction_dict={"range": ["1..max"]},
                ),
                is_leaf=True,
                yang_name="external-route-preference",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """external_route_preference must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..max']}), is_leaf=True, yang_name="external-route-preference", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)""",
                }
            )

        self.__external_route_preference = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_external_route_preference(self):
        self.__external_route_preference = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..max"]},
            ),
            is_leaf=True,
            yang_name="external-route-preference",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
        )

    def _get_internal_route_preference(self):
        """
    Getter method for internal_route_preference, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/route_preference/config/internal_route_preference (uint8)

    YANG Description: Administrative Distance(preference) for internal ISIS routes.
    """
        return self.__internal_route_preference

    def _set_internal_route_preference(self, v, load=False):
        """
    Setter method for internal_route_preference, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/route_preference/config/internal_route_preference (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_internal_route_preference is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_internal_route_preference() directly.

    YANG Description: Administrative Distance(preference) for internal ISIS routes.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=int,
                        restriction_dict={"range": ["0..255"]},
                        int_size=8,
                    ),
                    restriction_dict={"range": ["1..max"]},
                ),
                is_leaf=True,
                yang_name="internal-route-preference",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """internal_route_preference must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..max']}), is_leaf=True, yang_name="internal-route-preference", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)""",
                }
            )

        self.__internal_route_preference = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_internal_route_preference(self):
        self.__internal_route_preference = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..max"]},
            ),
            is_leaf=True,
            yang_name="internal-route-preference",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
        )

    external_route_preference = __builtin__.property(
        _get_external_route_preference, _set_external_route_preference
    )
    internal_route_preference = __builtin__.property(
        _get_internal_route_preference, _set_internal_route_preference
    )

    _pyangbind_elements = OrderedDict(
        [
            ("external_route_preference", external_route_preference),
            ("internal_route_preference", internal_route_preference),
        ]
    )
