from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_resource import EducationResource

from .education_resource import EducationResource

@dataclass
class EducationLinkResource(EducationResource):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationLinkResource"
    # URL to the resource.
    link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationLinkResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationLinkResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationLinkResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_resource import EducationResource

        from .education_resource import EducationResource

        fields: Dict[str, Callable[[Any], None]] = {
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("link", self.link)
    

