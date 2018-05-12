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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/peer-groups/peer-group/route-reflector/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to route reflection for the
BGPgroup
  """
    __slots__ = (
        "_path_helper",
        "_extmethods",
        "__route_reflector_cluster_id",
        "__route_reflector_client",
    )

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__route_reflector_cluster_id = YANGDynClass(
            base=[
                RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                ),
                RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
                    },
                ),
            ],
            is_leaf=True,
            yang_name="route-reflector-cluster-id",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-bgp-types:rr-cluster-id-type",
            is_config=False,
        )
        self.__route_reflector_client = YANGDynClass(
            base=YANGBool,
            default=YANGBool("false"),
            is_leaf=True,
            yang_name="route-reflector-client",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="boolean",
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
                "bgp",
                "peer-groups",
                "peer-group",
                "route-reflector",
                "state",
            ]

    def _get_route_reflector_cluster_id(self):
        """
    Getter method for route_reflector_cluster_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/route_reflector/state/route_reflector_cluster_id (oc-bgp-types:rr-cluster-id-type)

    YANG Description: route-reflector cluster id to use when local router is
configured as a route reflector.  Commonly set at the group
level, but allows a different cluster
id to be set for each neighbor.
    """
        return self.__route_reflector_cluster_id

    def _set_route_reflector_cluster_id(self, v, load=False):
        """
    Setter method for route_reflector_cluster_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/route_reflector/state/route_reflector_cluster_id (oc-bgp-types:rr-cluster-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_reflector_cluster_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_reflector_cluster_id() directly.

    YANG Description: route-reflector cluster id to use when local router is
configured as a route reflector.  Commonly set at the group
level, but allows a different cluster
id to be set for each neighbor.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=[
                    RestrictedClassType(
                        base_type=long,
                        restriction_dict={"range": ["0..4294967295"]},
                        int_size=32,
                    ),
                    RestrictedClassType(
                        base_type=six.text_type,
                        restriction_dict={
                            "pattern": "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
                        },
                    ),
                ],
                is_leaf=True,
                yang_name="route-reflector-cluster-id",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="oc-bgp-types:rr-cluster-id-type",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """route_reflector_cluster_id must be of a type compatible with oc-bgp-types:rr-cluster-id-type""",
                    "defined-type": "oc-bgp-types:rr-cluster-id-type",
                    "generated-type": """YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}),], is_leaf=True, yang_name="route-reflector-cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgp-types:rr-cluster-id-type', is_config=False)""",
                }
            )

        self.__route_reflector_cluster_id = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_route_reflector_cluster_id(self):
        self.__route_reflector_cluster_id = YANGDynClass(
            base=[
                RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                ),
                RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
                    },
                ),
            ],
            is_leaf=True,
            yang_name="route-reflector-cluster-id",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-bgp-types:rr-cluster-id-type",
            is_config=False,
        )

    def _get_route_reflector_client(self):
        """
    Getter method for route_reflector_client, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/route_reflector/state/route_reflector_client (boolean)

    YANG Description: Configure the neighbor as a route reflector client.
    """
        return self.__route_reflector_client

    def _set_route_reflector_client(self, v, load=False):
        """
    Setter method for route_reflector_client, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/route_reflector/state/route_reflector_client (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_reflector_client is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_reflector_client() directly.

    YANG Description: Configure the neighbor as a route reflector client.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=YANGBool,
                default=YANGBool("false"),
                is_leaf=True,
                yang_name="route-reflector-client",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="boolean",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """route_reflector_client must be of a type compatible with boolean""",
                    "defined-type": "boolean",
                    "generated-type": """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
                }
            )

        self.__route_reflector_client = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_route_reflector_client(self):
        self.__route_reflector_client = YANGDynClass(
            base=YANGBool,
            default=YANGBool("false"),
            is_leaf=True,
            yang_name="route-reflector-client",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="boolean",
            is_config=False,
        )

    route_reflector_cluster_id = __builtin__.property(_get_route_reflector_cluster_id)
    route_reflector_client = __builtin__.property(_get_route_reflector_client)

    _pyangbind_elements = OrderedDict(
        [
            ("route_reflector_cluster_id", route_reflector_cluster_id),
            ("route_reflector_client", route_reflector_client),
        ]
    )


class state(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/peer-groups/peer-group/route-reflector/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information relating to route reflection for the
BGPgroup
  """
    __slots__ = (
        "_path_helper",
        "_extmethods",
        "__route_reflector_cluster_id",
        "__route_reflector_client",
    )

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__route_reflector_cluster_id = YANGDynClass(
            base=[
                RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                ),
                RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
                    },
                ),
            ],
            is_leaf=True,
            yang_name="route-reflector-cluster-id",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-bgp-types:rr-cluster-id-type",
            is_config=False,
        )
        self.__route_reflector_client = YANGDynClass(
            base=YANGBool,
            default=YANGBool("false"),
            is_leaf=True,
            yang_name="route-reflector-client",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="boolean",
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
                "bgp",
                "peer-groups",
                "peer-group",
                "route-reflector",
                "state",
            ]

    def _get_route_reflector_cluster_id(self):
        """
    Getter method for route_reflector_cluster_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/route_reflector/state/route_reflector_cluster_id (oc-bgp-types:rr-cluster-id-type)

    YANG Description: route-reflector cluster id to use when local router is
configured as a route reflector.  Commonly set at the group
level, but allows a different cluster
id to be set for each neighbor.
    """
        return self.__route_reflector_cluster_id

    def _set_route_reflector_cluster_id(self, v, load=False):
        """
    Setter method for route_reflector_cluster_id, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/route_reflector/state/route_reflector_cluster_id (oc-bgp-types:rr-cluster-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_reflector_cluster_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_reflector_cluster_id() directly.

    YANG Description: route-reflector cluster id to use when local router is
configured as a route reflector.  Commonly set at the group
level, but allows a different cluster
id to be set for each neighbor.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=[
                    RestrictedClassType(
                        base_type=long,
                        restriction_dict={"range": ["0..4294967295"]},
                        int_size=32,
                    ),
                    RestrictedClassType(
                        base_type=six.text_type,
                        restriction_dict={
                            "pattern": "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
                        },
                    ),
                ],
                is_leaf=True,
                yang_name="route-reflector-cluster-id",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="oc-bgp-types:rr-cluster-id-type",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """route_reflector_cluster_id must be of a type compatible with oc-bgp-types:rr-cluster-id-type""",
                    "defined-type": "oc-bgp-types:rr-cluster-id-type",
                    "generated-type": """YANGDynClass(base=[RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'}),], is_leaf=True, yang_name="route-reflector-cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-bgp-types:rr-cluster-id-type', is_config=False)""",
                }
            )

        self.__route_reflector_cluster_id = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_route_reflector_cluster_id(self):
        self.__route_reflector_cluster_id = YANGDynClass(
            base=[
                RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                ),
                RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
                    },
                ),
            ],
            is_leaf=True,
            yang_name="route-reflector-cluster-id",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-bgp-types:rr-cluster-id-type",
            is_config=False,
        )

    def _get_route_reflector_client(self):
        """
    Getter method for route_reflector_client, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/route_reflector/state/route_reflector_client (boolean)

    YANG Description: Configure the neighbor as a route reflector client.
    """
        return self.__route_reflector_client

    def _set_route_reflector_client(self, v, load=False):
        """
    Setter method for route_reflector_client, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/peer_groups/peer_group/route_reflector/state/route_reflector_client (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_reflector_client is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_reflector_client() directly.

    YANG Description: Configure the neighbor as a route reflector client.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=YANGBool,
                default=YANGBool("false"),
                is_leaf=True,
                yang_name="route-reflector-client",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="boolean",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """route_reflector_client must be of a type compatible with boolean""",
                    "defined-type": "boolean",
                    "generated-type": """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=False)""",
                }
            )

        self.__route_reflector_client = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_route_reflector_client(self):
        self.__route_reflector_client = YANGDynClass(
            base=YANGBool,
            default=YANGBool("false"),
            is_leaf=True,
            yang_name="route-reflector-client",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="boolean",
            is_config=False,
        )

    route_reflector_cluster_id = __builtin__.property(_get_route_reflector_cluster_id)
    route_reflector_client = __builtin__.property(_get_route_reflector_client)

    _pyangbind_elements = OrderedDict(
        [
            ("route_reflector_cluster_id", route_reflector_cluster_id),
            ("route_reflector_client", route_reflector_client),
        ]
    )
