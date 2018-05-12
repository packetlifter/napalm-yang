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

from . import config
from . import state
from . import ebgp
from . import ibgp


class use_multiple_paths(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/use-multiple-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters related to the use of multiple paths for the
same NLRI
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__config", "__state", "__ebgp", "__ibgp"
    )

    _yang_name = "use-multiple-paths"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__config = YANGDynClass(
            base=config.config,
            is_container="container",
            yang_name="config",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__ebgp = YANGDynClass(
            base=ebgp.ebgp,
            is_container="container",
            yang_name="ebgp",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__ibgp = YANGDynClass(
            base=ibgp.ibgp,
            is_container="container",
            yang_name="ibgp",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
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
                "bgp",
                "global",
                "use-multiple-paths",
            ]

    def _get_config(self):
        """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/config (container)

    YANG Description: Configuration parameters relating to multipath
    """
        return self.__config

    def _set_config(self, v, load=False):
        """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters relating to multipath
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=config.config,
                is_container="container",
                yang_name="config",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """config must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__config = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_config(self):
        self.__config = YANGDynClass(
            base=config.config,
            is_container="container",
            yang_name="config",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_state(self):
        """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/state (container)

    YANG Description: State parameters relating to multipath
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters relating to multipath
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=state.state,
                is_container="container",
                yang_name="state",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """state must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__state = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_state(self):
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_ebgp(self):
        """
    Getter method for ebgp, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp (container)

    YANG Description: Multipath parameters for eBGP
    """
        return self.__ebgp

    def _set_ebgp(self, v, load=False):
        """
    Setter method for ebgp, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ebgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ebgp() directly.

    YANG Description: Multipath parameters for eBGP
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=ebgp.ebgp,
                is_container="container",
                yang_name="ebgp",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """ebgp must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=ebgp.ebgp, is_container='container', yang_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__ebgp = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_ebgp(self):
        self.__ebgp = YANGDynClass(
            base=ebgp.ebgp,
            is_container="container",
            yang_name="ebgp",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_ibgp(self):
        """
    Getter method for ibgp, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ibgp (container)

    YANG Description: Multipath parameters for iBGP
    """
        return self.__ibgp

    def _set_ibgp(self, v, load=False):
        """
    Setter method for ibgp, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ibgp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ibgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ibgp() directly.

    YANG Description: Multipath parameters for iBGP
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=ibgp.ibgp,
                is_container="container",
                yang_name="ibgp",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """ibgp must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=ibgp.ibgp, is_container='container', yang_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__ibgp = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_ibgp(self):
        self.__ibgp = YANGDynClass(
            base=ibgp.ibgp,
            is_container="container",
            yang_name="ibgp",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    config = __builtin__.property(_get_config, _set_config)
    state = __builtin__.property(_get_state, _set_state)
    ebgp = __builtin__.property(_get_ebgp, _set_ebgp)
    ibgp = __builtin__.property(_get_ibgp, _set_ibgp)

    _pyangbind_elements = OrderedDict(
        [("config", config), ("state", state), ("ebgp", ebgp), ("ibgp", ibgp)]
    )


from . import config
from . import state
from . import ebgp
from . import ibgp


class use_multiple_paths(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/global/use-multiple-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Parameters related to the use of multiple paths for the
same NLRI
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__config", "__state", "__ebgp", "__ibgp"
    )

    _yang_name = "use-multiple-paths"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__config = YANGDynClass(
            base=config.config,
            is_container="container",
            yang_name="config",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__ebgp = YANGDynClass(
            base=ebgp.ebgp,
            is_container="container",
            yang_name="ebgp",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__ibgp = YANGDynClass(
            base=ibgp.ibgp,
            is_container="container",
            yang_name="ibgp",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
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
                "bgp",
                "global",
                "use-multiple-paths",
            ]

    def _get_config(self):
        """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/config (container)

    YANG Description: Configuration parameters relating to multipath
    """
        return self.__config

    def _set_config(self, v, load=False):
        """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters relating to multipath
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=config.config,
                is_container="container",
                yang_name="config",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """config must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__config = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_config(self):
        self.__config = YANGDynClass(
            base=config.config,
            is_container="container",
            yang_name="config",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_state(self):
        """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/state (container)

    YANG Description: State parameters relating to multipath
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters relating to multipath
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=state.state,
                is_container="container",
                yang_name="state",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """state must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__state = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_state(self):
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_ebgp(self):
        """
    Getter method for ebgp, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp (container)

    YANG Description: Multipath parameters for eBGP
    """
        return self.__ebgp

    def _set_ebgp(self, v, load=False):
        """
    Setter method for ebgp, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ebgp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ebgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ebgp() directly.

    YANG Description: Multipath parameters for eBGP
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=ebgp.ebgp,
                is_container="container",
                yang_name="ebgp",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """ebgp must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=ebgp.ebgp, is_container='container', yang_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__ebgp = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_ebgp(self):
        self.__ebgp = YANGDynClass(
            base=ebgp.ebgp,
            is_container="container",
            yang_name="ebgp",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_ibgp(self):
        """
    Getter method for ibgp, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ibgp (container)

    YANG Description: Multipath parameters for iBGP
    """
        return self.__ibgp

    def _set_ibgp(self, v, load=False):
        """
    Setter method for ibgp, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/global/use_multiple_paths/ibgp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ibgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ibgp() directly.

    YANG Description: Multipath parameters for iBGP
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=ibgp.ibgp,
                is_container="container",
                yang_name="ibgp",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """ibgp must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=ibgp.ibgp, is_container='container', yang_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__ibgp = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_ibgp(self):
        self.__ibgp = YANGDynClass(
            base=ibgp.ibgp,
            is_container="container",
            yang_name="ibgp",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    config = __builtin__.property(_get_config, _set_config)
    state = __builtin__.property(_get_state, _set_state)
    ebgp = __builtin__.property(_get_ebgp, _set_ebgp)
    ibgp = __builtin__.property(_get_ibgp, _set_ibgp)

    _pyangbind_elements = OrderedDict(
        [("config", config), ("state", state), ("ebgp", ebgp), ("ibgp", ibgp)]
    )
