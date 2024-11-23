from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .azure_resource_evidence import AzureResourceEvidence

from .alert_evidence import AlertEvidence

@dataclass
class BlobContainerEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.blobContainerEvidence"
    # The name of the blob container.
    name: Optional[str] = None
    # The storage which the blob container belongs to.
    storage_resource: Optional[AzureResourceEvidence] = None
    # The full URL representation of the blob container.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BlobContainerEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BlobContainerEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BlobContainerEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .azure_resource_evidence import AzureResourceEvidence

        from .alert_evidence import AlertEvidence
        from .azure_resource_evidence import AzureResourceEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "storageResource": lambda n : setattr(self, 'storage_resource', n.get_object_value(AzureResourceEvidence)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        from .alert_evidence import AlertEvidence
        from .azure_resource_evidence import AzureResourceEvidence

        writer.write_str_value("name", self.name)
        writer.write_object_value("storageResource", self.storage_resource)
        writer.write_str_value("url", self.url)
    

