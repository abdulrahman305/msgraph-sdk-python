from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource import AccessPackageResource
    from .entity import Entity

from .entity import Entity

@dataclass
class AccessPackageResourceRole(Entity, Parsable):
    # A description for the resource role.
    description: Optional[str] = None
    # The display name of the resource role such as the role defined by the application.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the resource role in the origin system. For a SharePoint Online site, the originId is the sequence number of the role in the site.
    origin_id: Optional[str] = None
    # The type of the resource in the origin system, such as SharePointOnline, AadApplication, or AadGroup.
    origin_system: Optional[str] = None
    # The resource property
    resource: Optional[AccessPackageResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageResourceRole:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceRole
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceRole()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource import AccessPackageResource
        from .entity import Entity

        from .access_package_resource import AccessPackageResource
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "originId": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "originSystem": lambda n : setattr(self, 'origin_system', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(AccessPackageResource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .access_package_resource import AccessPackageResource
        from .entity import Entity

        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
        writer.write_object_value("resource", self.resource)
    

