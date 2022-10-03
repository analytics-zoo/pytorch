# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Optional

from torch.onnx._internal.diagnostics.infra.sarif import (
    _property_bag,
    _tool_component_reference,
)


@dataclasses.dataclass
class ReportingDescriptorReference(object):
    """Information about how to locate a relevant reporting descriptor."""

    guid: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "guid"}
    )
    id: Optional[str] = dataclasses.field(
        default=None, metadata={"schema_property_name": "id"}
    )
    index: int = dataclasses.field(
        default=-1, metadata={"schema_property_name": "index"}
    )
    properties: Optional[_property_bag.PropertyBag] = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )
    tool_component: Optional[
        _tool_component_reference.ToolComponentReference
    ] = dataclasses.field(
        default=None, metadata={"schema_property_name": "toolComponent"}
    )


# flake8: noqa