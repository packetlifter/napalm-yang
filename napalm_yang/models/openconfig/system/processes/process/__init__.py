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

from . import state


class process(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/processes/process. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of monitored processes
  """
    __slots__ = ("_path_helper", "_extmethods", "__pid", "__state")

    _yang_name = "process"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__pid = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="pid",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            is_keyval=True,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="leafref",
            is_config=False,
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
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="container",
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
            return ["system", "processes", "process"]

    def _get_pid(self):
        """
    Getter method for pid, mapped from YANG variable /system/processes/process/pid (leafref)

    YANG Description: Reference to the process pid key
    """
        return self.__pid

    def _set_pid(self, v, load=False):
        """
    Setter method for pid, mapped from YANG variable /system/processes/process/pid (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pid() directly.

    YANG Description: Reference to the process pid key
    """
        parent = getattr(self, "_parent", None)
        if parent is not None and load is False:
            raise AttributeError(
                "Cannot set keys directly when" + " within an instantiated list"
            )

        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=six.text_type,
                is_leaf=True,
                yang_name="pid",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                is_keyval=True,
                namespace="http://openconfig.net/yang/system",
                defining_module="openconfig-system",
                yang_type="leafref",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """pid must be of a type compatible with leafref""",
                    "defined-type": "leafref",
                    "generated-type": """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="pid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=False)""",
                }
            )

        self.__pid = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_pid(self):
        self.__pid = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="pid",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            is_keyval=True,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="leafref",
            is_config=False,
        )

    def _get_state(self):
        """
    Getter method for state, mapped from YANG variable /system/processes/process/state (container)

    YANG Description: State parameters related to monitored processes
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /system/processes/process/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters related to monitored processes
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
                namespace="http://openconfig.net/yang/system",
                defining_module="openconfig-system",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """state must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=False)""",
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
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="container",
            is_config=False,
        )

    pid = __builtin__.property(_get_pid)
    state = __builtin__.property(_get_state)

    _pyangbind_elements = OrderedDict([("pid", pid), ("state", state)])
