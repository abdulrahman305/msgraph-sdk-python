from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_hash import FileHash

@dataclass
class FileSecurityState(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Complex type containing file hashes (cryptographic and location-sensitive).
    file_hash: Optional[FileHash] = None
    # File name (without path).
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Full file path of the file/imageFile.
    path: Optional[str] = None
    # Provider generated/calculated risk score of the alert file. Recommended value range of 0-1, which equates to a percentage.
    risk_score: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileSecurityState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileSecurityState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_hash import FileHash

        from .file_hash import FileHash

        fields: Dict[str, Callable[[Any], None]] = {
            "fileHash": lambda n : setattr(self, 'file_hash', n.get_object_value(FileHash)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .file_hash import FileHash

        writer.write_object_value("fileHash", self.file_hash)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("path", self.path)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_additional_data_value(self.additional_data)
    

